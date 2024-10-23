import wallaroo.k8
import wallaroo.sdk

"""Conductor client serves as a common basis/collection of the various parts of the SDK."""

import datetime
import json
import logging
import time
from typing import Any, List, Optional, Union

import gql  # type: ignore
import psycopg2  # type: ignore
import requests
from gql.transport.requests import RequestsHTTPTransport  # type: ignore
from pypika import Order, Table  # type: ignore
from pypika.functions import Cast  # type: ignore
from pypika.terms import JSON  # type: ignore

from . import auth, deployment, model, model_config, pipeline
from . import validation as v
from .client import Client


class Instance:
    """This part of the SDK serves as a common basis/collection of the various other parts.

    Parameters:
      auth_type: string, can be one of:
                 * "none" - for use with unauthenticated platform installs
                 * "sso" - for interactive third-party SSO login
                 * "user_password" - for headless/automated users
    """

    def __init__(
        self,
        rest_api_host="http://rest-api:3030",
        graphql_api_host="http://api-lb:8080",
        auth_host="http://keycloak:8080",
        timeout=1,
        auth_type="none",
    ):
        """Create an instance of the client. Optinally provide a url for the rest api host or graphql api host
            or a timeout for requests in seconds.

        :param str rest_api_host: Host/port of the platform REST API endpoint
        :param str graphql_api_host: Host/port of the platform GraphQL API endpoint
        :param str auth_host: Host/port of the platform Keycloak instance
        :param int timeout: Max timeout of web requests
        :param str auth_type: Authentication type to use. Can be one of: "none", "sso", "user_password".
        """

        assert v.is_url(rest_api_host), "The rest_api_host must be a valid URL."
        assert v.is_url(graphql_api_host), "The graphql_api_host must be a valid URL."
        assert v.is_number(timeout), "Timeout must be a number."

        logging.info(f"Using rest_api_host: {rest_api_host}")
        logging.info(f"Using graphql_api_host: {graphql_api_host}")

        self.auth = auth.create(auth_host, auth_type)
        transport = RequestsHTTPTransport(
            url=graphql_api_host + "/v1/graphql", auth=self.auth
        )
        gql_client = gql.Client(transport=transport, fetch_schema_from_transport=True)

        self.model = model.Model(rest_api_host, gql_client, self.auth)
        self.model_config = model_config.ModelConfig(gql_client)
        self.deployment = deployment.Deployment(gql_client)
        self.pipeline = pipeline.Pipeline(gql_client)

        self.timeout = timeout
        self.retry_interval = 2

    def upload_model(
        self,
        model_name: str,
        model_variant: str,
        model_path: str,
        model_type="onnx",
    ) -> dict:
        """Upload a model and return a newly created model config. Model name and variant
        can contain only lowercase letters, numbers and dashes. Model type must be 'onnx' or 'tensorflow'.
        """

        assert v.is_valid_name(
            model_name
        ), "Model name must contain only lowercase letters, numbers or dashes."

        assert v.is_valid_name(
            model_variant
        ), "Model variant must contain only lowercase letters, numbers or dashes."

        assert v.is_valid_model_type(model_type), "Model type is not valid."

        assert not self.model.get_model(
            model_name, model_variant
        ), "A model with that name and variant already exists."

        model = self.model.upload_model(model_name, model_variant, model_path)
        if model is None:
            raise Exception("Could not upload model")

        model_config = self.model_config.create_model_config(
            model["id"], model_type=model_type
        )
        return model_config

    def deploy_model(
        self,
        deployment_name: str,
        model_name: str,
        model_variant: str,
        model_path: str,
        model_type: str = "onnx",
        deployed: bool = True,
        config: Optional[deployment.DeploymentConfig] = None,
    ) -> dict:
        """One step function to upload and deploy a model. Uploads the model, creates
        the configuration and deploys it. Model and deployment names can contain only
        lowercase letters, numbers and dashes. Model type must be 'onnx' or 'tensorflow'.
        Deployment resource options (CPU, memory, replicas) can be specified in the
        optional deployment config object.

        NOTE: This function returns immediately but the operation may take several
        minutes to complete.
        """

        assert v.is_valid_name(
            deployment_name
        ), "Deployment name must contain only lowercase letters, numbers or dashes."

        model_config = self.upload_model(
            model_name, model_variant, model_path, model_type
        )

        deployment = self.deployment.create_deployment(
            deployment_name, model_config["id"], deployed, config
        )
        endpoint = f"http://engine-svc.{deployment_name}:29502/models/{model_name}"
        deployment["url"] = endpoint

        return deployment

    def replace_model(
        self, deployment: dict, model_name: str, model_variant: str, filepath: str
    ):
        assert type(deployment) == dict, "A valid deployment must be provided."
        assert "id" in deployment, "A valid deployment must be provided."

        new_model = self.upload_model(model_name, model_variant, filepath)
        self.deployment.create_deployment_model_config(
            deployment["id"], new_model["id"]
        )

    def deploy_pipeline(
        self,
        deployment_name: str,
        pipeline_name: str,
        pipeline_variant: str,
        pipeline_config: pipeline.PipelineConfig,
        deployed: bool = True,
        config: Optional[deployment.DeploymentConfig] = None,
    ):
        """Deploy a pipeline.  Pipeline and deployment names and versoin can contain only
        lowercase letters, numbers and dashes. Deployment resource options (CPU, memory,
        replicas) can be specified in the optional deployment config object.

        NOTE: This function returns immediately but the operation may take several
        minutes to complete.
        """
        assert v.is_valid_name(
            deployment_name
        ), "Deployment name must contain only lowercase letters, numbers or dashes."

        assert v.is_valid_name(
            pipeline_name
        ), "Pipeline name must contain only lowercase letters, numbers or dashes."

        assert (
            self.deployment.get_deployment(deployment_name) is None
        ), "A deployment with that name already exists."

        model_config_ids = [m["id"] for m in pipeline_config.model_configs]
        pipeline = self.pipeline.create_pipeline(
            pipeline_name, pipeline_variant, pipeline_config
        )
        pipeline_variant_id = pipeline["pipeline_variants"][0]["id"]
        deployment = self.deployment.create_pipeline_deployment(
            deployment_name, pipeline_variant_id, model_config_ids, deployed, config
        )
        return deployment

    def _make_request(self, url: str, data: Union[dict, list]) -> dict:
        """Keep trying the request while the engines are coming up. Only return on success."""

        failed = False

        # Return only on success as per design.
        while True:
            try:
                resp = requests.post(
                    url, json=data, timeout=self.timeout, auth=self.auth
                )

                if resp.status_code == 200:
                    return resp.json()
                # The lb is up but the engines are not
                raise Exception("Invalid return code")
            except Exception:
                # The lb is not up (timeout) or ready to serve.
                if not failed:
                    print(
                        "Waiting for model to become ready - this may take a few seconds.",
                        end="",
                    )
                    failed = True
                else:
                    print(".", end="")
                time.sleep(self.retry_interval)

    def inference_tensor(self, deployment: dict, data: dict) -> Optional[dict]:
        """Submit tensor for inference to the models endpoint and return the result as a dict.
        The data should be in the form `{"tensor" : [1.0, 2.0]}` with any
        additional metadata if necessary or desired."""

        deployment_name = deployment["deployment_name"]
        model_name = deployment["deployment_model_configs"][0]["model_config"]["model"][
            "model_name"
        ]

        url = f"http://engine-lb.{deployment_name}:29502/models/{model_name}"

        return self._make_request(url, data)

    def inference_file(self, deployment: dict, data_path: str) -> Optional[dict]:
        """Convenience function to submit the json contents of a file to the models
        endpoint for inference."""

        with open(data_path, "rb") as data_filehandle:
            data = json.load(data_filehandle)
        return self.inference_tensor(deployment, data)

    def pipeline_inference_tensor(self, deployment: dict, data: dict) -> Optional[dict]:
        """Submit tensor for inference to the pipeline endpoint and return the result as a dict.
        The data should be in the form `{"tensor" : [1.0, 2.0]}` with any
        additional metadata if necessary or desired."""

        deployment_name = deployment["deployment_name"]
        pipeline_name = deployment["deployment_pipeline_variants"][0][
            "pipeline_variant"
        ]["pipeline"]["pipeline_name"]

        url = f"http://engine-lb.{deployment_name}:29502/pipelines/{pipeline_name}"

        return self._make_request(url, data)

    def pipeline_inference_file(
        self, deployment: dict, data_path: str
    ) -> Optional[dict]:
        """Convenience function to submit the json contents of a file to
        the pipeline endpoint for inference."""

        with open(data_path, "rb") as data_filehandle:
            data = json.load(data_filehandle)

        return self.pipeline_inference_tensor(deployment, data)

    def logs(
        self,
        model_name: str = None,
        pipeline_name: str = None,
        start_time: datetime.datetime = None,
        end_time: datetime.datetime = None,
        limit: int = 1000,
    ):
        """
        Get all audit logs for all engines. Can be scoped down via various
        optional parameters.

        For large volumes of records, we recommend implementing pagination via
        time, and using a reasonable `limit`.

        :param start_time:      fetch all logs after this time, inclusive
        :param end_time:        fetch all logs before this time, exclusive
        :param model_name:        only fetch logs tagged with this model id
        :param pipeline_id:     only fetch logs tagged with this pipeline id
        :param limit:           hard cap on number of records to fetch
        """
        #                       Table "public.fluentbit"
        # Column |            Type             | Collation | Nullable | Default
        # --------+-----------------------------+-----------+----------+---------
        # tag    | character varying           |           |          |
        # time   | timestamp without time zone |           |          |
        # data   | jsonb                       |           |          |

        logs = Table("fluentbit")
        log_data = Cast(logs.data.get_text_value("log"), "json")
        audit_data = JSON.get_json_value(log_data, "audit_data")
        log_model_id = JSON.get_text_value(audit_data, "model_id")
        log_pipeline_id = JSON.get_text_value(audit_data, "pipeline_id")

        q = (
            logs.select(log_data)
            .orderby(logs.time, order=Order.desc)
            .where(audit_data.notnull())
            .limit(limit)
        )
        if start_time is not None:
            q = q.where(logs.time >= start_time)
        if end_time is not None:
            q = q.where(logs.time < end_time)
        if model_name is not None:
            q = q.where(log_model_id == model_name)
        if pipeline_name is not None:
            q = q.where(log_pipeline_id == pipeline_name)

        query_str = q.get_sql()
        args: List = []
        conn = psycopg2.connect(
            "dbname=postgres user=postgres password=password host=postgres port=5432"
        )
        cur = conn.cursor()
        cur.execute(query_str, args)
        res = cur.fetchall()
        cur.close()
        conn.close()

        return res

import logging
from abc import ABC, abstractmethod
from functools import lru_cache, partial
from importlib.metadata import version

from amazon_sagemaker_jupyter_ai_q_developer.clients.base_client import BaseClient
from amazon_sagemaker_jupyter_ai_q_developer.utils import getQTelemetryInteractionType
from botocore import UNSIGNED
from sagemaker_jupyterlab_extension_common.util.environment import Environment

TELEMETRY_PROD_ENDPOINT = "https://codewhisperer.us-east-1.amazonaws.com"
logging.basicConfig(format="%(levelname)s: %(message)s")


@lru_cache(maxsize=1)
def get_extension_version():
    try:
        return version("amazon_sagemaker_jupyter_ai_q_developer")
    except Exception as e:
        logging.error(f"Error getting extension version: {e}")
        return "Unknown"


class TelemetryClient(ABC, BaseClient):
    def __init__(self, opt_out):
        self._client = None
        self._opt_out = opt_out

    @abstractmethod
    def send_telemetry_event(
        self,
        telemetry_event_type,
        request_id,
        conversation_id,
        ide_category,
        telemetry_enabled,
        q_dev_profile_arn,
        metrics,
        telemetry_event=None,
    ):
        raise NotImplementedError("send_telemetry_event method must be implemented")


class QDevTelemetryClient(TelemetryClient):
    def __init__(self, opt_out):
        super().__init__(opt_out)
        client = QDevTelemetryClient.get_client(
            service_name="bearer",
            endpoint_url=TELEMETRY_PROD_ENDPOINT,
            api_version="2022-11-11",
            region_name=TELEMETRY_PROD_ENDPOINT.split(".")[1],
            signature_version=UNSIGNED,
        )
        partial_add_header = partial(QDevTelemetryClient.add_header, opt_out=opt_out)
        client.meta.events.register("before-sign.*.*", partial_add_header)
        self._client = client

    def send_telemetry_event(
        self,
        telemetry_event_type,
        request_id,
        conversation_id,
        ide_category,
        telemetry_enabled,
        q_dev_profile_arn,
        metrics,
        telemetry_event=None,
    ):
        t_event = {
            telemetry_event_type: {
                "conversationId": conversation_id,
                "messageId": request_id,
            },
        }

        if telemetry_event_type == "chatInteractWithMessageEvent" and telemetry_event:
            interactionType = getQTelemetryInteractionType(telemetry_event["type"])
            t_event[telemetry_event_type]["interactionType"] = interactionType
            metrics.put_dimensions({"InteractionType": interactionType})

            code = telemetry_event.get("code", {})
            charCount = code.get("charCount", None)
            if charCount is not None:
                t_event[telemetry_event_type]["acceptedCharacterCount"] = charCount
                metrics.put_metric("CharCount", int(charCount))

            lineCount = code.get("lineCount", None)
            if lineCount is not None:
                t_event[telemetry_event_type]["acceptedLineCount"] = lineCount
                metrics.put_metric("LineCount", int(lineCount))

        metrics.set_property("QDevProfileArn", q_dev_profile_arn)
        user_context = {
            "ideCategory": ide_category,
            "operatingSystem": "LINUX",
            "product": "QChat",
        }
        self._client.send_telemetry_event(
            telemetryEvent=t_event,
            # Based on Q team, we need to always send_telemetry_event and pass along
            # OPTIN when telemetry is enabled otherwise, we pass OPTOUT.
            optOutPreference="OPTIN" if telemetry_enabled else "OPTOUT",
            userContext=user_context,
            profileArn=q_dev_profile_arn,
        )


class ToolkitTelemetryClient(TelemetryClient):
    def send_telemetry_event(
        self,
        telemetry_event_type,
        request_id,
        conversation_id,
        ide_category,
        telemetry_enabled,
        q_dev_profile_arn,
        metrics,
        telemetry_event=None,
    ):
        pass


class TelemetryClientFactory:
    _clients = {
        Environment.MD_IDC: QDevTelemetryClient,
        Environment.MD_IAM: ToolkitTelemetryClient,
        Environment.STUDIO_SSO: QDevTelemetryClient,
        Environment.STUDIO_IAM: ToolkitTelemetryClient,
    }

    @classmethod
    def get_client(cls, environment, opt_out) -> TelemetryClient:
        logging.info(f"Getting client creator for ${environment}")
        creator = cls._clients.get(environment)
        if not creator:
            raise ValueError(environment)
        return creator(opt_out=opt_out)

import time
import typing
from ..sessions.client import SessionsClient, AsyncSessionsClient
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sessions_response import SessionsResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.not_found_error import NotFoundError
from ..types.error_envelope import ErrorEnvelope
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..errors.internal_server_error import InternalServerError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.session_config_v1 import SessionConfigV1
from ..types.session_response import SessionResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.jsonable_encoder import jsonable_encoder


# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)

RUNNINNG_STATUS = "running"

class ExtendedSessionConfigV1(SessionConfigV1):
    """
    Extended session configuration with additional properties.
    """
    skipWaitSessionReady: bool = False  # Default value

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Ensure base class is initialized

# ... existing code ...
class AirtopSessions(SessionsClient):
    """
    AirtopSessions client functionality.
    """

    def create(
            self,
            *,
            configuration: typing.Optional[SessionConfigV1] = None, 
            request_options: typing.Optional[RequestOptions] = None,
        ) -> SessionResponse:
            extended_config = configuration if isinstance(configuration, ExtendedSessionConfigV1) else None
            
            session_config_v1 = SessionConfigV1(**{k: v for k, v in extended_config.__dict__.items() if k in SessionConfigV1.__fields__}) if extended_config else None
            session_data = super().create(configuration=session_config_v1, request_options=request_options)
            if extended_config is None or not extended_config.skipWaitSessionReady:
                self.wait_for_session_ready(session_data.data.id)
            return session_data

    def wait_for_session_ready(self, session_id: str, timeout_seconds: int = 60):
        initial_status = ""
        desired_status = RUNNINNG_STATUS
        status = initial_status
        start_time = time.time()

        while status != desired_status:
            print(f"waiting for session {session_id} to be ready")
            status = self.getinfo(id=session_id).data.status
            if status == desired_status:
                break

            elapsed_time = time.time() - start_time
            if timeout_seconds and elapsed_time > timeout_seconds:
                break

            time.sleep(1)
        return status



class AsyncAirtopSessions(AsyncSessionsClient):
    """
    AsyncAirtopSessions client functionality.
    """

    async def create(
        self,
        *,
        configuration: typing.Optional[SessionConfigV1] = None, 
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionResponse:
        """
        Parameters
        ----------
        configuration : typing.Optional[SessionConfigV1]
            Session configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionResponse
            Created

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sessions.create()


        asyncio.run(main())
        """
        extended_config = configuration if isinstance(configuration, ExtendedSessionConfigV1) else None
        session_config_v1 = SessionConfigV1(**{k: v for k, v in extended_config.__dict__.items() if k in SessionConfigV1.__fields__}) if extended_config else None


        session_data = await super().create(configuration=session_config_v1, request_options=request_options)
        if extended_config is None or not extended_config.skipWaitSessionReady:
            await self.wait_for_session_ready(session_data.data.id)
        return session_data

    async def wait_for_session_ready(self, session_id: str, timeout_seconds: int = 60):
        initial_status = "UNINITIALIZED"
        desired_status = RUNNINNG_STATUS
        status = initial_status
        start_time = time.time()

        while status != desired_status:
            status = (await self.getinfo(id=session_id)).data.status
            if status == desired_status:
                break

            elapsed_time = time.time() - start_time
            if timeout_seconds and elapsed_time > timeout_seconds:
                break

            time.sleep(1)
        return status



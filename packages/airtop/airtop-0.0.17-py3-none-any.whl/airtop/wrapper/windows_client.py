import typing
import requests
from ..windows.client import WindowsClient, AsyncWindowsClient
from ..core.request_options import RequestOptions
from ..types import ExternalSessionWithConnectionInfo

# ... existing code ...
class AirtopWindows(WindowsClient):
    """
    AirtopWindows client that extends the WindowsClient functionality.
    """

    def _get_playwright_target_id(self, playwright_page):
        cdp_session = playwright_page.context.new_cdp_session(playwright_page)
        target_info = cdp_session.send("Target.getTargetInfo")
        return target_info["targetInfo"]["targetId"]

    def _get_selenium_target_id(self, selenium_driver, session: ExternalSessionWithConnectionInfo):
        airtop_api_key = self._client_wrapper._api_key
        chromedriver_session_url = f"{session.chromedriver_url}/session/{selenium_driver.session_id}/chromium/send_command_and_get_result"
        response = requests.post(
            chromedriver_session_url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {airtop_api_key}'
            },
            json={
                'cmd': 'Target.getTargetInfo',
                'params': {}
            }
        )
        return response.json().get('value', {}).get('targetInfo', {}).get('targetId', None)

    def get_window_info_for_playwright_page(
        self,
        session: ExternalSessionWithConnectionInfo,
        playwright_page,
        *,
        include_navigation_bar: typing.Optional[bool] = None,
        disable_resize: typing.Optional[bool] = None,
        screen_resolution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        target_id = self._get_playwright_target_id(playwright_page)
        return self.get_window_info(
            session_id=session.id,
            window_id=target_id,
            include_navigation_bar=include_navigation_bar,
            disable_resize=disable_resize,
            screen_resolution=screen_resolution,
            request_options=request_options
        )

    def get_window_info_for_selenium_driver(
        self,
        session: ExternalSessionWithConnectionInfo,
        selenium_driver,
        *,
        include_navigation_bar: typing.Optional[bool] = None,
        disable_resize: typing.Optional[bool] = None,
        screen_resolution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        target_id = self._get_selenium_target_id(selenium_driver, session)
        return self.get_window_info(
            session_id=session.id,
            window_id=target_id,
            include_navigation_bar=include_navigation_bar,
            disable_resize=disable_resize,
            screen_resolution=screen_resolution,
            request_options=request_options
        )





class AsyncAirtopWindows(AsyncWindowsClient):
    """
    AsyncAirtopWindows client that extends the AsyncWindowsClient functionality.
    """

    async def _get_playwright_target_id(self, playwright_page):
        cdp_session = await playwright_page.context.new_cdp_session(playwright_page)
        target_info = await cdp_session.send("Target.getTargetInfo")
        return target_info["targetInfo"]["targetId"]

    async def _get_selenium_target_id(self, selenium_driver, session: ExternalSessionWithConnectionInfo):
        airtop_api_key = self._client_wrapper._api_key
        chromedriver_session_url = f"{session.chromedriver_url}/session/{selenium_driver.session_id}/chromium/send_command_and_get_result"
        response = requests.post(
            chromedriver_session_url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {airtop_api_key}'
            },
            json={
                'cmd': 'Target.getTargetInfo',
                'params': {}
            }
        )
        return response.json().get('value', {}).get('targetInfo', {}).get('targetId', None)

    async def get_window_info_for_playwright_page(
        self,
        session: ExternalSessionWithConnectionInfo,
        playwright_page,
        *,
        include_navigation_bar: typing.Optional[bool] = None,
        disable_resize: typing.Optional[bool] = None,
        screen_resolution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        target_id = await self._get_playwright_target_id(playwright_page)
        return await self.get_window_info(
            session_id=session.id,
            window_id=target_id,
            include_navigation_bar=include_navigation_bar,
            disable_resize=disable_resize,
            screen_resolution=screen_resolution,
            request_options=request_options
        )

    async def get_window_info_for_selenium_driver(
        self,
        session: ExternalSessionWithConnectionInfo,
        selenium_driver,
        *,
        include_navigation_bar: typing.Optional[bool] = None,
        disable_resize: typing.Optional[bool] = None,
        screen_resolution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        target_id = await self._get_selenium_target_id(selenium_driver, session)
        return await self.get_window_info(
            session_id=session.id,
            window_id=target_id,
            include_navigation_bar=include_navigation_bar,
            disable_resize=disable_resize,
            screen_resolution=screen_resolution,
            request_options=request_options
        )

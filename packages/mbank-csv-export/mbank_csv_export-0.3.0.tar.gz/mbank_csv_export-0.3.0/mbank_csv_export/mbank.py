import datetime
import sys
from logging import basicConfig, getLogger
from pathlib import Path
from tempfile import TemporaryDirectory

from playwright.sync_api import Page, TimeoutError, sync_playwright

logger = getLogger(__name__)

MBANK_HOSTNAME = "online.mbank.pl"
MBANK_LOGIN_URL = f"https://{MBANK_HOSTNAME}/login"
MBANK_DASHBOARD_URL = f"https://{MBANK_HOSTNAME}/dashboard"
MBANK_HISTORY_URL = f"https://{MBANK_HOSTNAME}/history"
MBANK_AUTHORIZATION_URL = f"https://{MBANK_HOSTNAME}/authorization"


class MBank:
    """Manages the browser instance, provides simple API for interacting with mBank.

    The browser uses persistent storage to skip mobile authentication.
    Update `state_dir` parameter in `__init__` to change it's location.
    """

    def __init__(
        self,
        headless: bool = True,
        log_level: str = "INFO",
        state_dir: Path = Path.home() / ".local" / "state" / "mbank-csv-exporter",
    ) -> None:
        basicConfig(
            stream=sys.stderr,
            format="[{asctime}][{levelname:.1s}:{name}] {message}",
            style="{",
            level=log_level,
        )
        self.playwright = sync_playwright().start()
        state_dir.mkdir(parents=True, exist_ok=True)
        self.context = self.playwright.firefox.launch_persistent_context(
            user_data_dir=state_dir, headless=headless, accept_downloads=True
        )
        if len(pages := self.context.pages) > 0:
            self.page = pages[0]
        else:
            self.page = self.context.new_page()

    def __del__(self) -> None:
        self.page.close()
        self.context.close()
        self.playwright.stop()

    def login(self, username: str, password: str) -> None:
        """Logs into mbank."""
        page = self.page
        page.goto(MBANK_LOGIN_URL)
        page.fill("#userID", username)
        page.fill("#pass", password)
        page.click("#submitButton", force=True)

        try:
            page.wait_for_url(MBANK_DASHBOARD_URL, timeout=20_000)
        except TimeoutError:
            pass

        current_url = page.url
        if MBANK_AUTHORIZATION_URL in current_url:
            self._handle_unknown_device(page)
            success = True
        else:
            logger.error(f"Unexpected URL: {current_url}")
            success = False

        return success

    def _handle_unknown_device(self, page: Page) -> None:
        """Requests adding a new device, requires the user to authenticate with a mobile device."""
        add_new_device_button = "#module-root button:nth-of-type(1)"
        confirm_new_device_checkbox = "#checkboxInput3"
        submit_new_device_button = "#module-root button"
        redirect_to_dashboard_button = (
            'button[data-test-id="SCA:Status:goToNextModuleButton"]'
        )
        page.click(selector=add_new_device_button, force=True)
        page.click(selector=confirm_new_device_checkbox, force=True)
        page.click(selector=submit_new_device_button, force=True)
        logger.info("Complete the authentication using you mobile device.")
        page.wait_for_selector(
            selector=redirect_to_dashboard_button, timeout=5 * 60 * 1000
        ).click()
        page.wait_for_url(MBANK_DASHBOARD_URL, timeout=120000)

    def export_operations_csv(
        self, date_from: datetime.date, date_to: datetime.date
    ) -> str:
        """Exports the bank operations, returns csv file content as a string."""
        page = self.page
        page.goto(MBANK_HISTORY_URL)
        page.wait_for_load_state("networkidle")

        selectors = page.query_selector_all("input.DateInput_input")
        selectors[0].fill(date_from.strftime("%d.%m.%Y"), force=True)
        selectors[1].fill(date_to.strftime("%d.%m.%Y"), force=True)

        page.click(
            'button[data-test-id="history:exportHistoryMenuTrigger"]', force=True
        )
        page.wait_for_load_state("networkidle")
        with TemporaryDirectory() as temporary_dir:
            with page.expect_download() as download_info:
                page.click(
                    'div[data-test-id="Menu:Container"] li:nth-of-type(3)', force=True
                )
                download = download_info.value
                download_path = Path(temporary_dir) / download.suggested_filename
                download.save_as(download_path)

            content = download_path.read_text(encoding="utf-8")
        return content

import json
import logging
import os
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from playwright.sync_api import sync_playwright, Page

from silverriver import Crux
from silverriver.utils.auth import read_silverriver_key

logger = logging.getLogger(__name__)

_STORAGE_FILE = "storage.json"
_PW_TRACE_FILE = "pw_trace.zip"
_USER_TRACE_FILE = "user_trace.json"
_TRACE_BUCKET_PREFIX = "traces"
_JS_SCRIPT = Path(__file__).parent / "javascript" / "record_interactions.js"


def _track_interaction(interactions: list[dict[str, Any]], interaction_type: str, details: dict[str, Any]):
    interactions.append({
        "type": interaction_type,
        "details": details,
        "timestamp": datetime.now(tz=timezone.utc).timestamp()
    })
    logger.debug(f"Tracked interaction: {interaction_type}")


def _make_handler(interactions: list[dict[str, Any]]):
    def handle_interaction(interaction_type: str, details_json: str):
        _track_interaction(interactions, interaction_type, json.loads(details_json))

    return handle_interaction


def _inject_tracking_js(page: Page, interactions: list[dict[str, Any]]):
    js_code = _JS_SCRIPT.read_text(encoding="utf-8")
    page.expose_function("registerInteraction", _make_handler(interactions))
    page.add_init_script(js_code)


def _dump_recorded_data_and_archive(src_path: Path, output_file: str, recorded_data: dict[str, Any]) -> str:
    logger.info("Saving user interactions")
    user_trace_path = src_path / _USER_TRACE_FILE
    user_trace_path.write_text(json.dumps(recorded_data, indent=2))

    logger.info(f"Creating trace archive at {output_file}.zip")
    return shutil.make_archive(
        base_name=output_file,
        format='zip',
        root_dir=src_path.parent,
        base_dir=src_path.name
    )


def _register_close_handler(page: Page, output_path: Path):
    def flush_pw_trace_and_storage(page_: Page):
        page_.context.storage_state(path=output_path / _STORAGE_FILE)
        page_.context.tracing.stop(path=output_path / _PW_TRACE_FILE)

    page.on("close", flush_pw_trace_and_storage)


def _track_interactions(start_url: str, output_path: Path) -> list[dict[str, Any]]:
    interactions = []
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--start-maximized"], headless=False)
        page = browser.new_context(no_viewport=True).new_page()
        page.context.tracing.start(title="User trace", screenshots=True, snapshots=True, sources=True)
        _inject_tracking_js(page, interactions)
        _register_close_handler(page, output_path)
        logger.info(f"Navigating to {start_url}")
        page.goto(start_url)
        logger.info("Tracking user interactions. Close the browser to stop")
        page.wait_for_event('close', timeout=0)
        logger.info("Tracking stopped")
    return interactions


def record_trace(start_url: str, output_zip_file: str) -> str:
    """
    Tracks user interactions starting at the given URL and saves the trace as a ZIP file.

    This function launches a browser, tracks user interactions beginning from the specified URL,
    and saves the interaction trace as a ZIP file. If the user interrupts the tracing process,
    no trace will be saved.

    Args:
        start_url (str): The URL where the tracking of user interactions will begin.
        output_zip_file (str): The filename to use when saving the interaction trace as a ZIP file.

    Returns:
        str: The path to the saved ZIP file containing the interaction trace.
             Returns an empty string if the tracing was interrupted by the user.

    Raises:
        Any exceptions raised by the _track_interactions or _dump_recorded_data_and_archive functions.
    """

    logger.info("Launching browser")
    with tempfile.TemporaryDirectory(prefix=f"{output_zip_file}_") as output_path:
        output_path = Path(output_path)
        try:
            interactions = _track_interactions(start_url, output_path)
        except KeyboardInterrupt:
            logger.info("User interrupted tracing, no trace saved")
            return ""
        zipped_file = _dump_recorded_data_and_archive(
            src_path=output_path,
            output_file=output_zip_file,
            recorded_data={
                "interactions": interactions,
                "start_url": start_url,
                "task_name": output_zip_file
            })
        logger.info("Browser closed")
        logger.info(f"Trace saved to {zipped_file}")
        return zipped_file


def upload_trace(filename: str):
    """
     Uploads a trace file to Crux using the provided API token.

     This function authenticates with Crux using a token, verifies the existence of the specified file,
     and then uploads the trace file to Crux.

     Args:
         filename (str): The path to the trace file that should be uploaded.

     Raises:
         AssertionError: If the specified file does not exist.
         Any exceptions raised by the Crux client during authentication or upload.
     """
    key = read_silverriver_key()
    assert filename and os.path.exists(filename), f"File not found: {filename}"
    client = Crux(api_key=key)
    response = client.upload_trace(prefix=_TRACE_BUCKET_PREFIX, filename=filename)
    logger.info(f"Trace upload result: {response}")

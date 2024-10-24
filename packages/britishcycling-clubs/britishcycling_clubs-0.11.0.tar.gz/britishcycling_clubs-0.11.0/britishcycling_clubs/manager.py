"""Functions to get info from a club's Club Manager pages."""

from __future__ import annotations

import logging
import time
from pprint import pformat
from typing import NamedTuple

from playwright.sync_api import sync_playwright

_MANAGER_VIA_LOGIN_BASE_URL = "https://www.britishcycling.org.uk/uac/connect?success_url=/dashboard/club/membership?club_id="


class ManagerMemberCounts(NamedTuple):
    """Returned by `get_manager_member_counts()` function."""

    active: int
    """Value from 'Active Club Members' tab."""
    expired: int
    """Value from 'Expired Club Members' tab."""
    new: int
    """Value from 'New Club Subscriptions' tab."""


def get_manager_member_counts(
    club_id: str,
    username: str,
    password: str,
    manager_page_load_delay: int = 5,
) -> ManagerMemberCounts:
    """Get number of active, new, expired members from the Club Manager page.

    This is a slow operation (circa 10s), so get them all in one go.

    Parameters
    ----------
    club_id :
        From the URL used to access club pages.

    username :
        Username

    password :
        Password

    manager_page_load_delay :
        Time (s) allowed for club manager page to load. Defaults to 5.
        Consider increasing if 'Active member count was zero' exceptions occur.

    Returns
    -------
    `ManagerMemberCounts`

    Raises
    ------
    ValueError :
        if zero 'active members' would be returned, as it's assumed this indicates
        an issue with data collection.
    """
    logger = logging.getLogger(__name__)
    start_time = time.time()
    _log_info(logger, "Started timer for Playwright operations", start_time)

    with sync_playwright() as p:
        _log_info(logger, "Launching browser...", start_time)
        browser = p.chromium.launch()
        page = browser.new_page()

        # login page
        page.goto(manager_url_via_login(club_id))
        page.locator("id=username2").fill(username)
        page.locator("id=password2").fill(password)
        page.locator("id=login_button").click()
        _log_info(logger, "Got club manager page; logging in", start_time)

        # allow time for club manager page to load fully,
        # as page.wait_for_load_state() is ineffective
        _log_info(
            logger,
            f"Waiting extra {manager_page_load_delay} s for page load",
            start_time,
        )
        time.sleep(manager_page_load_delay)

        raw_member_counts = {
            "active": page.locator("id=members-active-count").inner_text(),
            "expired": page.locator("id=members-expired-count").inner_text(),
            "new": page.locator("id=members-new-count").inner_text(),
        }

        _log_info(logger, "Raw data retrieved", start_time)
        browser.close()
        _log_info(logger, "Closed browser", start_time)

    return _process_manager_member_counts(raw_member_counts)


def manager_url_via_login(club_id: str) -> str:
    """Return URL of club's Club Manager page.

    Parameters
    ----------
    club_id :
        From the URL used to access club pages.

    Returns
    -------
    str :
        URL

    """
    return f"{_MANAGER_VIA_LOGIN_BASE_URL}{club_id}/"


def _process_manager_member_counts(
    counts: dict[str, str],
) -> ManagerMemberCounts:
    """Process raw values.

    Values are blank if there aren't any members (although they appear as zeros
    during page load); convert these to 0 and ensure all are ints.

    Raise exception if zero 'active members' value.
    """
    processed_counts = {
        key: int(value) if value else 0 for key, value in counts.items()
    }
    # Assume an error if zero 'active' value.
    # 'active' appears to be the slowest value to populate.
    # 'new' will often be genuinely zero; 'expired' could be genuinely zero
    if processed_counts["active"] == 0:
        error_message = (
            "Active member count was zero; assuming issue with data collection. "
            f"{pformat(processed_counts)}. "
            "Consider increasing `manager_page_load_delay`."
        )
        raise ValueError(error_message)

    return ManagerMemberCounts(
        active=processed_counts["active"],
        expired=processed_counts["expired"],
        new=processed_counts["new"],
    )


def _log_info(logger: logging.Logger, message: str, start_time: float) -> None:
    """Add log entry, with elapsed time since `start_time`."""
    elapsed_time = time.time() - start_time
    log_message = f"Elapsed: {elapsed_time:.1f} s. {message}"
    logger.info(log_message)

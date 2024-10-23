#!/usr/bin/env python3
"""Wikidata test."""

import datetime
import logging
import time
import urllib.error
from email.utils import parsedate_to_datetime

from SPARQLWrapper import SPARQLWrapper, JSON

from .version import VERSION


LOGGER = logging.getLogger(__name__)


def parse_retry_after_header(value):
    """
    Parse a Retry-After HTTP header and return the number of seconds to wait
    before the request is tried again.
    """
    try:
        wait = int(value)
    except ValueError:
        # datetime.UTC was only added in Python 3.11
        utc = datetime.timezone.utc
        dtime = parsedate_to_datetime(value)
        if dtime.tzinfo is None:
            dtime = dtime.replace(tzinfo=datetime.timezone.utc)
        now = datetime.datetime.now(tz=utc)
        wait = (dtime - now).total_seconds()
    return max(wait, 0)


def construct_user_agent_string(name, email, version="0.0", url=None):
    """
    Construct a user-agent string.

    Args:
        name:
            The name of the application.

        version:
            The version of the application.

        email:
            A contact address that Wikidata may use to contact the user. This is
            required by Wikimedia's User-Agent policy.

        url:
            The URL of the application. If None, use "https://example.com/<name>".
    """
    lib_name = __name__
    if url is None:
        url = f"https://example.com/{name}"
    return f"{name}/{version} ({url}; {email}) {lib_name}/{VERSION}"


class WikidataSPARQLWrapperError(Exception):
    """Custom exception raised by WikidataSPARQLWrapper."""


class WikidataSPARQLWrapper:
    """
    Wrapper around a Wikidata SPARQLWrapper that handles HTTP 429 Too Many
    Requests errors.

    * https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual
    * https://www.wikidata.org/wiki/Wikidata:Data_access
    * https://foundation.wikimedia.org/wiki/Policy:User-Agent_policy
    """

    def __init__(self, user_agent, endpoint=None):
        """
        Args:
            user_agent:
                The user-agent string to use for queries. It should respect
                Wikimedia's User-Agent policy.

            endpoint:
                The Wikidata SPARQL endpoint. If not given, the default is used.
        """
        if endpoint is None:
            endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
        self.wrapper = SPARQLWrapper(endpoint=endpoint, agent=user_agent)
        self.wrapper.setReturnFormat(JSON)

    def query(self, query):
        """
        Send a query to the endpoint.

        Args:
            query:
                The SPARQL query to send.

        Returns:
            The SPARQLWrapper query result.
        """
        self.wrapper.setQuery(query)
        while True:
            try:
                LOGGER.info("Sending query to %s.", self.wrapper.endpoint)
                return self.wrapper.query()
            except urllib.error.HTTPError as http_err:
                if http_err.code == 429:
                    error_name = "429 Too Many Requests"
                    LOGGER.info(
                        "%s replied with an HTTP %s error.",
                        error_name,
                        self.wrapper.endpoint,
                    )
                    try:
                        retry_after = http_err.headers()["Retry-After"]
                        wait = parse_retry_after_header(retry_after)
                        if wait > 0:
                            LOGGER.info(
                                "Waiting %s second%s to retry query.",
                                wait,
                                "" if wait == 1 else "s",
                            )
                            time.sleep(wait)
                    except KeyError as key_err:
                        raise WikidataSPARQLWrapperError(
                            f"HTTP {error_name} error did not include a Retry-After header."
                        ) from key_err
                    except ValueError as val_err:
                        raise WikidataSPARQLWrapperError(val_err) from val_err
                else:
                    raise WikidataSPARQLWrapperError(http_err) from http_err

    def query_bindings(self, query):
        """
        Wrapper around query() that returns the bindings of a successful result.

        Args:
            query:
                The SPARQL query to send.

        Returns:
            The result's bindings.
        """
        return self.query(query).convert()["results"]["bindings"]

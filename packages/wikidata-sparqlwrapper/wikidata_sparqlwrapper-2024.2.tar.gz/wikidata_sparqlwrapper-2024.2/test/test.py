#!/usr/bin/env python3
"""
This is just a very simple test to check that the wrapper works. It does not
generate HTTP 429 errors and is not a unit test.
"""

import sys

from wikidata_sparqlwrapper import (
    WikidataSPARQLWrapper,
    WikidataSPARQLWrapperError,
    construct_user_agent_string,
)


def test():
    """
    Test.
    """
    agent = construct_user_agent_string(name="TestAgent", email="test@example.com")
    print("User-agent:", agent)
    wrapper = WikidataSPARQLWrapper(user_agent=agent)
    query = """\
    SELECT ?item ?itemLabel
    WHERE
    {
        ?item wdt:P31 wd:Q146.
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    """
    bindings = wrapper.query_bindings(query)
    n_bindings = len(bindings)
    ending = "" if n_bindings == 1 else "s"
    print(f"Retrieved {n_bindings} result{ending}.")
    for i, binding in enumerate(bindings, start=1):
        if i >= 9:
            print("...")
            break
        print(i, binding["itemLabel"]["value"])


if __name__ == "__main__":
    try:
        test()
    except KeyboardInterrupt:
        pass
    except WikidataSPARQLWrapperError as err:
        sys.exit(err)

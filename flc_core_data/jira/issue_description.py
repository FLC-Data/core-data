"""Get Jira Issue Description by id"""
import json
import sys
from urllib.parse import urljoin

import requests
from requests.auth import HTTPBasicAuth


jira_domain = 'https://flcdata.atlassian.net'


def get_task_description(issue_id: str, api_token: str) -> str:
    """
    Extracts the issue description on the jira board.

    Args:
        issue_id: str: Jira Issue Id.
        api_token: str: Jira Auth Token API.

    Returns:
        A string describing the task on the jira board.
    """

    url = urljoin(jira_domain, f"/rest/api/2/issue/{issue_id}")
    auth = HTTPBasicAuth("fabio.caffarello@gmail.com", api_token)

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )

    r_json = json.loads(response.text)

    return print(r_json['fields']['description'])
# print(json.dumps(r_json, sort_keys=True, indent=4, separators=(",", ": ")))


def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    return get_task_description(*args)


# if __name__ == '__main__':
#     issue_id = '10004'
#     api_token = '1W9LqCcRcISmv0sTaKgT76E9'
#     get_task_description(issue_id, api_token)

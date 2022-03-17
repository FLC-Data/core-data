"""Send greetings."""
import sys
import requests
from requests.auth import HTTPBasicAuth
import json
from urllib.parse import urljoin


jira_domain = 'https://flcdata.atlassian.net'


def get_task_description(task_id, api_token):

    url = urljoin(jira_domain, f"/rest/api/2/issue/{task_id}")
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

    return r_json['fields']['description']


def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    return get_task_description(*args)

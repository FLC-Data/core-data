"""Send greetings."""
import sys


def greet(tz, token):
    """Greet a location."""
    return f"Hello, {tz}! your token is {token}"


def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]
    issue = args[0]
    token = args[1]
    print(greet(issue, token))

# # This code sample uses the 'requests' library:
# # http://docs.python-requests.org
# import requests
# from requests.auth import HTTPBasicAuth
# import json
# from urllib.parse import urljoin

# def get_tasks():
#     jira_domain = 'https://flcdata.atlassian.net'
#     api_token = 'O0HMdDoAmHNu28PUzMEgB6F9'
#     taskId = '10006'

#     url = f"https://flcdata.atlassian.net/rest/api/2/issue/10004"
#     # url = f"/rest/api/3/task/{taskId}"
#     # url = urljoin(jira_domain, "/rest/api/2/search")

#     auth = HTTPBasicAuth("fabio.caffarello@gmail.com", api_token)

#     headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json"
#     }


#     response = requests.request(
#         "GET",
#         url,
#         headers=headers,
#         auth=auth
#     )

#     r_json = json.loads(response.text)
#     return  print(r_json['fields']['description'])

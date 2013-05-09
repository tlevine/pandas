import json

import requests

from pandas import DataFrame

def _flatten_issue(issue):
    '''issue : dict
    One issue from the list of issues, containing such things as a body and labels
    '''
    return {
        u'assignee': issue[u'assignee'],
        u'body': issue[u'body'],
        u'closed_at': issue[u'closed_at'],
        u'created_at': issue[u'created_at'],
        u'comments': issue[u'comments'],
        u'id': issue[u'id'],
#       u'labels',
#       u'milestone',
        u'number': issue[u'number'],
#       u'pull_request',
        u'state': issue[u'state'],
        u'title': issue[u'title'],
        u'updated_at': issue[u'updated_at'],
        u'url': issue[u'url'],
        u'user': issue[u'user'][u'html_url'].split('/')[-1],
    }


def issues(owner, repo, state = u'open', labels = []):
    '''
    owner: str/unicode
        The owner' name

    repo: str/unicode
        The repository name

    state: "open" or "closed"
        Return the open issues or the closed ones?

    labels: list of str/unicode
        If this is not empty, return only the accordingly labeled repositories.

    Read more here.
    http://developer.github.com/v3/issues/#list-issues-for-a-repository
    '''

    url = u'https://api.github.com/repos/%s/%s/issues' % (owner, repo)
    params = {u'state': state}
    if len(labels) > 0:
        params[u'labels'] = u','.join(labels)

    r = requests.get(url, params = params)
    if r.status_code != 200:
        raise Exception('%d\n%s' % (r.status_code, r.text))

    issues = json.loads(r.text)
    return DataFrame([_flatten_issue(issue) for issue in issues])

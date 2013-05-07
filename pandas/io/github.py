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


def issues(owner, repo):
#              label = None, not_label = None,
#              has_milestone = None, not_milestone = None):
    url = u'https://api.github.com/repos/%s/%s/issues' % (owner, repo)
    params = {u'state': 'closed'}
    r = requests.get(url, params = params)
    issues = json.loads(r.text)
    return DataFrame([_flatten_issue(issue) for issue in issues])

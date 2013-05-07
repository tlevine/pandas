import nose

import pandas
from pandas.util.testing import network
from pandas.util.testing import assert_frame_equal
from numpy.testing.decorators import slow

from pandas.io.github import issues

@slow
@network
def test_issues():
    expected = {u'assignee': {0: None},
         u'body': {0: u''},
         u'closed_at': {0: u'2012-03-21T04:53:08Z'},
         u'comments': {0: 1},
         u'created_at': {0: u'2012-03-19T16:46:59Z'},
         u'id': {0: 3713483},
         u'number': {0: 1},
         u'state': {0: u'closed'},
         u'title': {0: u'Add NumPy intro.'},
         u'updated_at': {0: u'2012-03-21T04:53:08Z'},
         u'url': {0: u'https://api.github.com/repos/pydata/pydata2012/issues/1'},
         u'user': {0: u'stefanv'}}
    observed = issues('pydata', 'pydata2012')
    assert_frame_equal(observed, pandas.DataFrame(expected))

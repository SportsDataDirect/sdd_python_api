from distutils.core import setup
#started with http://peterdowns.com/posts/first-time-with-pypi.html and then i switched to twine

import sys
if sys.version_info <= (2,7):
  sys.exit("Sorry, Python <= 2.7 is not supported")
elif sys.version_info <= (3,5) or sys.version_info >= (3,7):
  sys.warn('Python versions besides 3.6.1 are untested')

setup(
  name = 'sdd_api',
  packages = ['sdd_api'], # this must be the same as the name above
  version = '0.2.1',
  description = 'Python API for Sports Data Direct',
  author = 'Sports Data Direct',
  author_email = 'admin@sportsdatadirect.com',
  url = 'https://github.com/SportsDataDirect/sdd_python_api', # use the URL to the github repo
  download_url = 'https://github.com/SportsDataDirect/sdd_python_api/releases', # git push --tags origin master
  keywords = ['sports', 'api', 'sports data direct', 'sdd', 'sports data', 'nfl'], # arbitrary keywords
  classifiers = [],
  install_requires=[
          "pandas>=0.16",
          "oauthlib==2.0.2",
          "requests-oauthlib==0.8.0",
            "tqdm==4.19.5"
      ]
)
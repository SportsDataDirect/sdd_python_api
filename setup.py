from distutils.core import setup
#started with http://peterdowns.com/posts/first-time-with-pypi.html and then i switched to twine
setup(
  name = 'sdd_api',
  packages = ['sdd_api'], # this must be the same as the name above
  version = '0.1',
  description = 'Python API for Sports Data Direct',
  author = 'Sports Data Direct',
  author_email = 'admin@sportsdatadirect.com',
  url = 'https://github.com/SportsDataDirect/sdd_python_api', # use the URL to the github repo
  download_url = 'https://github.com/SportsDataDirect/sdd_python_api/archive/0.1.tar.gz', # git push --tags origin master
  keywords = ['sports', 'api', 'sports data direct', 'sdd'], # arbitrary keywords
  classifiers = [],
)
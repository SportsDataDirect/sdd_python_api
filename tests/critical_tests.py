from .context import sdd_api
from sdd_api.api import Api
import unittest
from tests.credentials import *
import pandas as pd

# class TestStringMethods(unittest.TestCase):
#     def test_file(self):
#         assert(1,1)
#         api = Api(config_file_path=__file__+"credentials.cfg")
#         api.gen_token()
#         print(api.get_dataframe("team_names"))

class TestConfig(unittest.TestCase):
    def test_config(self):
        api = Api(username=username, password=password, client_id=client_id, client_secret=client_secret)
        assert type(api.get_dataframe("team_names")), pd.DataFrame

if __name__ == '__main__':
    unittest.main()
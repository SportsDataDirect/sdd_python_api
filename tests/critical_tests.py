from .context import sdd_api
from sdd_api.api import Api
import unittest
from tests.test_credentials import *
import pandas as pd

# class TestStringMethods(unittest.TestCase):
#     def test_file(self):
#         assert(1,1)
#         api = Api(config_file_path=__file__+"credentials.cfg")
#         api.gen_token()
#         print(api.get_dataframe("team_names"))

api = Api(username=username, password=password, client_id=client_id, client_secret=client_secret, server_url="https://localhost", verify=False)
class TestConfig(unittest.TestCase):
    def test_config(self):
        df = api.get_dataframe("matchups",season_start=2016)
        assert len(df),len(df.drop_duplicates())
    #     df = api.get_dataframe("drives")
    #     assert type(df), pd.DataFrame
    # def test_players(self):
    #     df = api.get_dataframe("matchups", season_start=2016)
    #     print(df.sample(10))
    # def no_duplicates(self):
    #     df = api.get_dataframe("matchups",season_start=2016)
    #     assert len(df),len(df.drop_duplicates())

if __name__ == '__main__':
    unittest.main()
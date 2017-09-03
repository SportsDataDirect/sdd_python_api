from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
import pandas as pd
from sdd_api.exceptions import *
import configparser
import json
from collections import OrderedDict

SERVER_URL="https://api.sportsdatadirect.com"
class Api:
    def __init__(self,username=None, password=None, client_id=None, client_secret=None, config_file_path=None):
        if config_file_path:
            raise NotImplemented("This functionality is still under development")
            config = configparser.ConfigParser()
            config.read(config_file_path)
            try:
                self.username=config['main']['username']
                self.password=config['main']['password']
                self.client_id=config['main']['client_id']
                self.client_secret=config['main']['client_secret']
            except:
                raise ConfigFileException("Please follow the example cfg file given in the documentation or supply the credentials as kwargs")
        elif username and password and client_id and client_secret:
            self.username=username
            self.password=password
            self.client_id=client_id
            self.client_secret=client_secret
        else:
            raise ApiInitializationException("Please supply username, password, client_id, and client_secret params or pass a file")

    def gen_token(self):
        self.oauth = OAuth2Session(client=LegacyApplicationClient(client_id=self.client_id))
        self.token = self.oauth.fetch_token(token_url=SERVER_URL + '/oauth/token',
                                  username=self.username, password=self.password, client_id=self.client_id,
                                  client_secret=self.client_secret)

    def get_json(self, table_name, schema_name="nfl", season_start=None):
        request = self.make_request(table_name, schema_name, season_start)
        d = json.loads(request.text,
                       object_pairs_hook=OrderedDict)
        if type(d) == OrderedDict and 'error' in d.keys():
            raise Exception(dict(d))
        else:
            return d

    def get_dataframe(self, table_name, schema_name="nfl", season_start=None):
        json = self.get_json(table_name, schema_name, season_start)
        return pd.DataFrame.from_records(json)

    def make_request(self, table_name, schema_name="nfl", season_start=None):
        url = SERVER_URL + "/table/%s/%s" % (schema_name, table_name)
        params = {}
        if season_start:
            params = {"season": season_start}
        response = self.oauth.get(url, params=params)

        return response
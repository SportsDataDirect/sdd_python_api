from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
import pandas as pd
from sdd_api.exceptions import *
import configparser
import json
from collections import OrderedDict
from tqdm import tqdm
import sys

SERVER_URL="https://api.sportsdatadirect.com"
class Api:
    def __init__(self,username=None, password=None, client_id=None, client_secret=None, config_file_path=None, server_url=None, verify=True):
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
        if server_url:
            self.SERVER_URL = server_url
        self.verify=verify
        self.gen_token()

    def gen_token(self):
        self.oauth = OAuth2Session(client=LegacyApplicationClient(client_id=self.client_id))
        self.token = self.oauth.fetch_token(token_url=self.SERVER_URL + '/oauth/token',
                                  username=self.username, password=self.password, client_id=self.client_id,
                                  client_secret=self.client_secret, verify=self.verify)

    def get_json(self, table_name, schema_name="nfl", season_start=None, season_stop=None):
        request = self.make_request(table_name, schema_name, season_start, season_stop)
        d = json.loads(request.text,
                       object_pairs_hook=OrderedDict)
        if type(d) == OrderedDict and 'error' in d.keys():
            raise Exception(dict(d))
        else:
            return d

    def get_dataframe(self, table_name, schema_name="nfl", season_start=2017, season_stop=None, progress_bar=False):
        df=pd.DataFrame()
        if season_stop is None:
            season_stop=2017

        seasons=range(season_start, season_stop+1)
        if progress_bar:
            with tqdm(total=len(seasons), file=sys.stdout) as pbar:
                for season in seasons:
                    pbar.set_description('loading season: %d' % (season))
                    pbar.update(1)
                    json = self.get_json(table_name, schema_name, season, season)
                    df=df.append(pd.DataFrame.from_records(json))
        else:
            for season in seasons:
                json = self.get_json(table_name, schema_name, season, season)
                df = df.append(pd.DataFrame.from_records(json))
        return df

    def make_request(self, table_name, schema_name="nfl", season_start=None, season_stop=None):
        url = self.SERVER_URL + "/table/%s/%s" % (schema_name, table_name)
        params = {}
        if season_start:
            params["season_start"] = season_start
        if season_stop:
            params["season_stop"] = season_stop
        response = self.oauth.get(url, params=params, verify=False)

        return response
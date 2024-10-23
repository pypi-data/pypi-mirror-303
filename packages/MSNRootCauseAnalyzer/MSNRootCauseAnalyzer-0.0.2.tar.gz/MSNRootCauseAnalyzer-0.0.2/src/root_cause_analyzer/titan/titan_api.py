import requests

from datetime import datetime
from msal import PublicClientApplication


class TitanApi:
    # TODO: A lot of hard-code here, need to be refactored
    def __init__(self, alias_account) -> None:
        """
        alias: alias@microsoft.com
        """
        self.alias_account = alias_account
        self.endpoint = "https://titanapi.westus2.cloudapp.azure.com/v2/query"
        self.token = self.get_token()
        if not self.token:
            raise Exception("Failed to get token")
        

    def get_token(self):

        client_id = 'dcca0492-ea09-452c-bf98-3750d4331d33'
        tenant_id = '72f988bf-86f1-41af-91ab-2d7cd011db47'

        scopes = [ 'api://dcca0492-ea09-452c-bf98-3750d4331d33/signin' ]

        app = PublicClientApplication(client_id, authority = "https://login.microsoftonline.com/" + tenant_id)

        acquire_tokens_result = app.acquire_token_interactive(scopes = scopes, prompt="select_account")

        if 'error' in acquire_tokens_result:
            print(f"{__class__.__name__} Error: " + acquire_tokens_result['error'])
            print(f"{__class__.__name__} Description: " + acquire_tokens_result['error_description'])
            return
        else:
            print(f"{__class__.__name__}: Access token:")
            print(acquire_tokens_result['access_token'])
            return acquire_tokens_result['access_token']
        

    def query_clickhouse(self, query_str, table="MSNAnalytics_Sample"):
        access_token = f"Bearer {self.token}"
        database = "MSN_Prod"

        api_headers = {"Authorization": access_token, "Content-Type": "application/json"}
        api_body = {
        "query": query_str,       
        "DatabaseName": database,
        "TableName": table,
        "UserAlias": self.alias_account,
            "CreatedTimeUtc": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            "UseCache": True,
            "UseDefaultDatabaseName": True
        }
        
        response = requests.post(self.endpoint, json=api_body, headers=api_headers)
        if response.status_code != 200:
            print(f"{__class__.__name__} {response.text}")
            return
        try:
            print(f"{__class__.__name__} {response.status_code}")
            data = response.json()['Result']['data']
            return data
        except:
            print(f"{__class__.__name__} {response.text}")
            return


if __name__ == "__main__":
    titan_api = TitanApi()
    titan_api.query_clickhouse(query_str = "SELECT EventDate, mCFV_FY24 FROM MSNAnalytics WHERE EventDate = toDate('2024-09-01') AND IsNotExcludedStandard_FY24 = 1 AND lower(PageType) IN ('article', 'gallery', 'video', 'watch' ) LIMIT 2 ",
                              table="MSNAnalytics")

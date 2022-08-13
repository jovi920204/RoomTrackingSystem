from pickle import FALSE
from main import GoogleAPIClient
from pprint import pprint
import pandas as pd

class GoogleSheets(GoogleAPIClient):
    def __init__(self) -> None:
        # 呼叫 GoogleAPIClient.__init__()，並提供 serviceName, version, scope
        super().__init__(
            'sheets',
            'v4',
            ['https://www.googleapis.com/auth/spreadsheets'],
        )
    def getWorksheet(self, spreadsheetId: str, range: str):
        request = self.googleAPIService.spreadsheets().values().get(
            spreadsheetId=spreadsheetId,
            range=range,
        )
        response = request.execute()
        return response

room = '10202'
bed = '2'

if __name__ == '__main__':
    myWorksheet = GoogleSheets()
    # pprint(myWorksheet.getWorksheet(
    #     spreadsheetId='1-Z71G5IrXe3oUCXqHVSao_lqksUy7u6Hi07YdoTKHZA',
    #     range='2F'
    # )['values'])
    floorSituation = myWorksheet.getWorksheet(
        spreadsheetId='1-Z71G5IrXe3oUCXqHVSao_lqksUy7u6Hi07YdoTKHZA',
        range='2F'
    )['values']
    df = pd.DataFrame(floorSituation)
    df = df[df[0]==room]
    df = df[df[1]==bed]
    ret = df.iloc[0,2]
    if ret == 'FALSE':
        print("有空位")
    else:
        print("沒空位")


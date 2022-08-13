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
inputText = '201-4'
room = ''
bed = ''
floor = ''
newText = inputText.split('-')
room = newText[0]
if (len(room) == 3):
    floor = room[0:1]
    room = '10'+room
elif (len(room) == 4):
    floor = room[0:2]
    room = '1'+room
bed = newText[1]

if __name__ == '__main__':
    myWorksheet = GoogleSheets()
    try:
        floorSituation = myWorksheet.getWorksheet(
            spreadsheetId='1-Z71G5IrXe3oUCXqHVSao_lqksUy7u6Hi07YdoTKHZA',
            range = floor+'F'
        )['values']
        df = pd.DataFrame(floorSituation)
        df = df[df[0]==room]
        df = df[df[1]==bed]
        ret = df.iloc[0,2]
        print("房號："+room+'-'+bed)
        if ret == 'TRUE':
            print("床位已空，可以入住")
        elif ret == 'FALSE':
            print("尚未退宿，請再等等")
    except:
        print("房號："+room+'-'+bed)
        print("查無此房")

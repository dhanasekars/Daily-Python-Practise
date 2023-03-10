""" 
Created on : 09/03/23 5:05 AM
@author : ds  
"""

from __future__ import print_function
from config import GoogleDrive
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from Mar_07 import gold_rate

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
values = gold_rate()
BODY = {
    "range": GoogleDrive.RANGE,
    "majorDimension": 'COLUMNS',
    "values": values
}


def main():
    """Shows basic usage of the Sheets API.
    Print values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('../../token.json'):
        creds = Credentials.from_authorized_user_file('../../token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('../../token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        request = service.spreadsheets().values(). \
            append(spreadsheetId=GoogleDrive.SPREADSHEET_ID, range=GoogleDrive.RANGE,
                   valueInputOption='USER_ENTERED', body=BODY)

        response = request.execute() # storing in response , later to use during debuggging in case of failure.
        # print(response)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

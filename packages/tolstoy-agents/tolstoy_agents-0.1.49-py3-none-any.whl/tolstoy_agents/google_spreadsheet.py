from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

def authenticate_sheets():
    client_email = os.environ.get('GMAIL_API_ACCOUNT_EMAIL')
    private_key = os.environ.get('GMAIL_API_PRIVATE_KEY', '').replace('\\n', '\n')
    spreadsheet_scope = 'https://www.googleapis.com/auth/spreadsheets'
    
    credentials = service_account.Credentials.from_service_account_info(
        {
            "type": "service_account",
            "client_email": client_email,
            "private_key": private_key,
            "token_uri": "https://oauth2.googleapis.com/token",  # This is a standard Google OAuth 2.0 token URI
        },
        scopes=[spreadsheet_scope]
    )
    
    sheets = build('sheets', 'v4', credentials=credentials)
    return sheets

def search_and_get_adjacent_value(spreadsheet_id: str, sheet_name: str, search_value: str):
    try:
        sheets = authenticate_sheets()
        # Get all values from the first two columns of the sheet
        result = sheets.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=f'{sheet_name}!A:B'
        ).execute()
        
        values = result.get('values', [])
        
        if not values:
            print('No data found.')
            return None
        # Search for the value in the first column and get the adjacent value
        for row in values:
            if len(row) > 0 and row[0] == search_value:
                if len(row) > 1:
                    return row[1]
                else:
                    print(f"Found {search_value}, but no adjacent value exists.")
                    return None
        print(f"Value {search_value} not found in the first column.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
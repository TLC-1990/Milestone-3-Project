import os
from google.oauth2.service_account import Credentials
import gspread

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GOOGLE_CREDS_PATH = os.path.join(BASE_DIR, 'creds.json')
SCOPE = ['https://www.googleapis.com/auth/spreadsheets']
GOOGLE_SHEET_NAME = 'thewurstoftimes_booking_spreadsheet'

creds = Credentials.from_service_account_file(GOOGLE_CREDS_PATH, scopes=SCOPE)
client = gspread.authorize(creds)
sheet = client.open(GOOGLE_SHEET_NAME)

worksheet = sheet.worksheet('customers')
worksheet.append_row(['Test', 'User', '123456', 'test@example.com', '*****'])

print("Row appended successfully!")

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from settings import *

# Подсоединение к Google Таблицам
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("gs_credentials.json", scope)
client = gspread.authorize(credentials)

# sheet = client.create("table_name")
# sheet.share('email', perm_type='user', role='writer')



def send_google_sheet(data):
    sheet = client.open(NAME_TABLE).sheet1
    sheet.append_row(data)

#!/usr/bin/python3

import speedtest as st
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

print("Getting Ping, Download and Upload data...")

def get_new_speeds():
    speed_test = st.Speedtest()
    speed_test.get_best_server()

    # Get ping (miliseconds) and remove decimals
    ping = round(speed_test.results.ping)

    # Perform download and upload speed tests (bits per second)
    download = speed_test.download()
    upload = speed_test.upload()

    # Convert download and upload speeds to megabits per second and remove decimal places
    download_mbs = round(download / (10**6))
    upload_mbs = round(upload / (10**6))
    
    date_today = datetime.today().strftime("%d/%m/%Y")

    return (date_today, ping, download_mbs, upload_mbs)


new_speeds = get_new_speeds()

print("Pushing to Google Sheet...")
# Use creds to create a OAuth2 client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by key and open the first sheet
sheet = client.open_by_key("SHEET_OPEN_KEY_GOES_HERE").sheet1

# Push the data to a new row in the sheet
sheet.append_row(new_speeds)
print("Done!")

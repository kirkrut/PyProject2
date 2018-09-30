import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds= ServiceAccountCredentials.from_json_keyfile_name('secret_file.json', scope)
client= gspread.authorize(creds)

wks= client.open("Numbers").sheet1
wks.clear()
n=10
for i in range(1,n+1):
    for p in range(1,n+1):
        wks.update_cell(i,p,int(random.uniform(1,30)))
i=0
while i<10:
    x = round(random.uniform(1, 10))
    y = round(random.uniform(1, 10))
    if wks.cell(x,y).value != '':
        wks.update_cell(x,y,'')
        i += 1
    if wks.cell(x, y).value ==  '':
        continue
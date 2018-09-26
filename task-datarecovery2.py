import gspread
from oauth2client.service_account import ServiceAccountCredentials
import scipy.stats
import numpy as np
scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds= ServiceAccountCredentials.from_json_keyfile_name('secret_file.json', scope)
client= gspread.authorize(creds)

wks= client.open("Numbers").sheet1

n=10
list = []
for i in range(1,n+1):
    for p in range(1,n+1):
        list.append(int(wks.cell(i, p).value))

print(scipy.stats.mstats.winsorize(list,limits=0.05))


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds= ServiceAccountCredentials.from_json_keyfile_name('secret_file.json', scope)
client= gspread.authorize(creds)

wks= client.open("Numbers").sheet1
ans = [int(i) for i in input("Введите диапазон значений через пробел\n").split()]
for i in range(0,10):
    wks.append_row([random.uniform(ans[0],ans[1]),random.uniform(ans[0],ans[1])])

#num= wks.get_all_records()
#print(num)
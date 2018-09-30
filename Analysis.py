import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("PyProject2-75578ae960a4.json", scope)

gc = gspread.authorize(credentials)

wks = gc.open('Test').sheet1

n = int(input("Введите значение n:"))

wks.clear()
wks.append_row(['x','y'])
for i in range(0,n):
    wks.append_row([int(random.uniform(1,30)),int(random.uniform(1,30))])


print(wks.get_all_records())

#print(wks.get_all_records())



import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds= ServiceAccountCredentials.from_json_keyfile_name('secret_file.json', scope)
client= gspread.authorize(creds)

n = 10

wks= client.open("Numbers").sheet1
ans = [int(i) for i in input("Введите диапазон значений через пробел\n").split()]
wks.clear()
wks.append_row(['x','y'])
for i in range(0,n):
    wks.append_row([int(random.uniform(ans[0],ans[1])),int(random.uniform(ans[0],ans[1]))])

#num= wks.get_all_records()
#print(num)
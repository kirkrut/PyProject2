import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import math
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("PyProject2-75578ae960a4.json", scope)

gc = gspread.authorize(credentials)

wks = gc.open('Test').sheet1

n = int(input("Введите значение n:"))
summ,d  = 0,0
wks.clear()
for i in range(1,n+1):
    for p in range(1,n+1):
        wks.update_cell(i,p,int(random.uniform(1,30)))

for i in range (1,n+1):
    summ = 0
    d = 0
    for p in range(1,n+1):
        summ += int(wks.cell(i,p))
        d += int(wks.cell(i,p))**2
    Wait = summ/n
    Disp = d/n - Wait**2
    print("Row" + str(i) + ":" + Wait, Disp)






print(wks.get_all_records())

#print(wks.get_all_records())



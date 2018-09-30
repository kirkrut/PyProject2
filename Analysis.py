import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import numpy
import math
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("PyProject2-75578ae960a4.json", scope)

gc = gspread.authorize(credentials)

wks = gc.open('Test').sheet1

n = int(input("Введите значение n:"))
summ,d  = 0,0
Disp = []
wks.clear()
mass = []
for i in range(1,n+1):
    mass.append([])
    for p in range(1,n+1):
        wks.update_cell(i,p,int(random.uniform(1,30)))
        mass[i-1].append(int(wks.cell(i,p).value))

print(mass)
coeff = 0
for i in range(0, n):
    k = i + 1
    while k < n:
        coeff = numpy.corrcoef(mass[i],mass[k])
        k += 1
        print('Коэффициент коррелиации для:', i+1,'и ',k, 'рядов', coeff[0][1])

for i in range(1,n+1):
    summ = 0
    d = 0
    for p in range(1,n+1):
        summ += int(wks.cell(i,p).value)
        d += int(wks.cell(i,p).value)**2
    Wait = summ/n
    Di = d/n - Wait**2
    Disp.append(Di)
    print("Для ", i, " ряда:",'математическое ожидание равно ', Wait,', дисперсия равна ', Di)



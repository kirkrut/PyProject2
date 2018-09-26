import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds= ServiceAccountCredentials.from_json_keyfile_name('secret_file.json', scope)
client= gspread.authorize(creds)

wks= client.open("Numbers").sheet1
#пусть имеются данные из task-mnk1 и некоторые из y=0
x=[]
y=[]
n = 10
sum_xy = 0
sum_x = 0
sum_y = 0
sum_x2 = 0
coef_a = 0
coef_b = 0

for i in range (2,n+1):
    if int(wks.cell(i, 2).value)!=0:
        x.append(int(wks.cell(i, 1).value))
        y.append(int(wks.cell(i, 2).value))
        sum_xy = sum_xy +int(wks.cell(i, 1).value)*int(wks.cell(i, 2).value)
        sum_x = sum_x + int(wks.cell(i, 1).value)
        sum_y = sum_y + int(wks.cell(i, 2).value)
        sum_x2 = sum_x2 + int(wks.cell(i, 1).value)**2
coef_a = (n*sum_xy - sum_x * sum_y)/(n * sum_x2 - sum_x**2)
coef_b = (sum_y - coef_a * sum_x)/n

for i in range (2,n+1):
    if int(wks.cell(i, 2).value) == 0:
        wks.update_cell(i,2,int(coef_a*int(wks.cell(i, 1).value)+coef_b))
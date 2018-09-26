import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds= ServiceAccountCredentials.from_json_keyfile_name('secret_file.json', scope)
client= gspread.authorize(creds)

wks= client.open("Numbers").sheet1

ans = [int(i) for i in input("Введите коррелируемые между собой ряды, сначала x потом y\n").split()]

x=[]
y=[]
n = 10
n1 = 0
sum_xy = 0
sum_x = 0
sum_y = 0
sum_x2 = 0
coef_a = 0
coef_b = 0

#for i in range (1,n+1):
#    if int(wks.cell(ans[0], i).value)!=0 and int(wks.cell(ans[1], i).value)!=0:
#        n1+=1
#        x.append(int(wks.cell(ans[0], i).value))
#        y.append(int(wks.cell(ans[1], i).value))
#        sum_xy = sum_xy +int(wks.cell(ans[0], i).value)*int(wks.cell(ans[1], i).value)
#        sum_x = sum_x + int(wks.cell(ans[0], i).value)
#        sum_y = sum_y + int(wks.cell(ans[1], i).value)
#        sum_x2 = sum_x2 + int(wks.cell(ans[0], i).value)**2
#coef_a = (n1*sum_xy - sum_x * sum_y)/(n1 * sum_x2 - sum_x**2)
#coef_b = (sum_y - coef_a * sum_x)/n1

coef_a=4
coef_b=567
for i in range(1,n+1):
    if int(wks.cell(ans[0], i).value)==0 and i==1:
        wks.update_cell(ans[0], i, (int(wks.cell(ans[1], i).value)-coef_b)/coef_a)# если не хватает первого элемента воспользуемся мнк
    if int(wks.cell(ans[1], i).value)==0 and i==1:
        wks.update_cell(ans[1], i, int(wks.cell(ans[0], i).value) * coef_a + coef_b)# если не хватает первого элемента воспользуемся мнк
    if int(wks.cell(ans[0], i).value) == 0:
        wks.update_cell(ans[0], i, int((int(wks.cell(ans[1], i).value)/int(wks.cell(ans[1], i-1).value)*int(wks.cell(ans[0], i-1).value))))
    if int(wks.cell(ans[1], i).value) == 0:
        wks.update_cell(ans[1], i, int((int(wks.cell(ans[0], i).value)/int(wks.cell(ans[0], i-1).value)*int(wks.cell(ans[1], i-1).value))))




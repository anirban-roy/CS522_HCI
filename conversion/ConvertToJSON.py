__author__ = 'Anirban'
import openpyxl
wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.get_sheet_by_name('T3T4')
max_row = sheet.get_highest_row()
max_col = sheet.get_highest_column()
print max_row, max_col
for i in range(1, max_row,1):
    for j in range(1,max_col,1):
        print sheet.cell(row=i, column=j).value


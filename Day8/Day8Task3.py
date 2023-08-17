# Excel Task 3 - User input to find a cricketer

import xlrd

open_book = xlrd.open_workbook("excel.xlsx")
sheet = open_book.sheet_by_index(0)

cricketer_name = input("Enter Cricketer name: ")

for i in range(1, sheet.ncols):
    if cricketer_name == sheet.cell_value(0, i):
        print("Cricketer Found!")
        break
else:
    print("Cricketer not found!")

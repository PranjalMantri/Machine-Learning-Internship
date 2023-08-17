# Excel Task 6 - Maximum score of one cricketer

import xlrd

open_book = xlrd.open_workbook("excel.xlsx")
sheet = open_book.sheet_by_index(0)

max_score = 0
cricketer_name = input("Enter the name of cricketer: ")

for i in range(1, sheet.ncols):
    if cricketer_name == sheet.cell_value(0, i):
        for j in range(1, sheet.nrows):
            if max_score < int(sheet.cell_value(j, i)):
                max_score = sheet.cell_value(j, i)
        break
else:
    print("Cricketer not found!")

print(f"Maximum score of {cricketer_name} is {int(max_score)}")

# Excel Task 4 - User input to find a cricketer and print all of its score

import xlrd

open_book = xlrd.open_workbook("excel.xlsx")
sheet = open_book.sheet_by_index(0)

cricketer_name = input("Enter Cricketer name: ")

for i in range(1, sheet.ncols):
    if cricketer_name == sheet.cell_value(0, i):
        print("Cricketer's scores are: ", end="")
        for j in range(1, sheet.nrows):
            print(sheet.cell_value(j, i), end=" ")
        break
else:
    print("Cricketer not found!")

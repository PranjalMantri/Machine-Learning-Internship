# Excel Task 1 - Print asked values

import xlrd

open_book = xlrd.open_workbook("excel.xlsx")
sheet = open_book.sheet_by_index(0)

print(sheet.cell_value(2, 1))
print(sheet.cell_value(5, 3))
print(sheet.cell_value(0, 3))
print(sheet.cell_value(4, 2))
print(sheet.cell_value(7, 3))

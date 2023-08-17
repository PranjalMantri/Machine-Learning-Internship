# Excel Task 2 - Print names of all cricketers

import xlrd

open_book = xlrd.open_workbook("excel.xlsx")
sheet = open_book.sheet_by_index(0)

for i in range(1, sheet.ncols):
    print(sheet.cell_value(0, i), end=" ")

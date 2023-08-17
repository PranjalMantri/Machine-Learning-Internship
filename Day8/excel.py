# Excel files manipulation

import xlrd

file_location = "excel.xlsx"
open_book = xlrd.open_workbook(file_location)
sheet = open_book.sheet_by_index(0)

print(sheet)
print(sheet.cell_value(0, 0))
print(sheet.cell_value(0, 3))
print(f"Total number of rows: {sheet.nrows}")
print(f"Total number of columns: {sheet.ncols}")

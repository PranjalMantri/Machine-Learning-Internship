# Excel Task 7 - Printing overall max score

import xlrd

open_book = xlrd.open_workbook("excel.xlsx")
sheet = open_book.sheet_by_index(0)

max_score = 0

for i in range(1, sheet.ncols):
    for j in range(1, sheet.nrows):
        if max_score < int(sheet.cell_value(j, i)):
            max_score = sheet.cell_value(j, i)

print(f"The overall maximum score is : {int(max_score)}")

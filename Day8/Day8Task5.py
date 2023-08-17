# Excel Task 5 - Print runs for all batsman for every match

import xlrd

open_book = xlrd.open_workbook("excel.xlsx")
sheet = open_book.sheet_by_index(0)

for i in range(1, sheet.nrows):
    print("For match", i, ":")
    for j in range(1, sheet.ncols):
        print("Score of ", sheet.cell_value(0, j), "=", end=" ")
        print(int(sheet.cell_value(i, j)))


# With user input for match
# match = int(input("Enter match number: "))
#
# for i in range(1, sheet.nrows):
#     if match == sheet.cell_value(i, 0):
#         print("For match ", i, ":")
#         for j in range(1, sheet.ncols):
#             print("Score of ", sheet.cell_value(0, j), "=", end=" ")
#             print(sheet.cell_value(i, j))
#         break
# else:
#     print("Match not found")

from openpyxl import Workbook
from datetime import datetime
import sys

if len(sys.argv) == 1:
	print("No File name")
	exit()

scan_result_file = sys.argv[1]
scan_results = open(scan_result_file, 'r', encoding='utf-8').readlines()

wb = Workbook()
now_time = str(datetime.now().strftime('%y%m%d'))
result_file = ('{}_{}.xlsx'.format(scan_result_file.split('.')[0], now_time))

ws1 = wb.active
ws1.title = 'Result'

row = 1
for scan_result in scan_results:
    data_list = scan_result.split(',')
    col = 1
    for data in data_list:
        data = data.strip()
        data = data.replace(' ', '\n')
        ws1.cell(row = row, column = col).value = data
        col += 1
    row += 1
    col = 1

wb.save(filename = result_file)

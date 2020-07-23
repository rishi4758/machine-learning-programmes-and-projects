import xlrd
from collections import OrderedDict
import simplejson as json
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('rishav1.xlsx')
sh = wb.sheet_by_index(0)
print(sh)
# List to hold dictionaries
gst_list = []
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    gst = OrderedDict()
    row_values = sh.row_values(rownum)
    gst['Description'] = row_values[0]
    gst['central tax'] = row_values[1]
    gst['state tax'] = row_values[2]
    gst['integrated tax'] = row_values[3]
    gst['cess'] = row_values[4]
    gst_list.append(gst)
# Serialize the list of dicts to JSON
j = json.dumps(gst_list)
# Write to file

with open('data1.json', 'w') as f:
    f.write(j)

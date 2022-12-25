
# Using readline()
import xlsxwriter

file = open('questions.txt', 'r')
res = []


while True:

    # Get next line from file
    line = file.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break

    splitArr = line.split("): ")
    res.append(splitArr)

file.close()

#writing to excel
infobook = xlsxwriter.Workbook('amazon_tagged.xlsx')
infosheet = infobook.add_worksheet()
row = 0

for arr in res:
    infosheet.write(row, 0, arr[0])
    infosheet.write(row, 1, arr[1])
    row += 1


infobook.close()
# data1 = ['desktop', 'notes', 'commands', 'downloads', 'wordFile', 'excelFile']
# data2 = ['Desktop', 'Notes', 'Commands', 'Downloads', 'Word File.doc', 'Excel File.doc']
#
# data1 = str(data1).lower().replace(" ", "")
# data2 = str(data2).lower().replace(".doc", "").replace(" ", "")
#
# assert data1 == data2, "Error"


data3 = r'D:\_QA_study\automation_course_brush_up\testfile847.txt'
data4 = r'C:\fakepath\testfile847.txt'

x = data3.split('\\')[-1]
y = data4.split('\\')[-1]

print(x)
print(y)
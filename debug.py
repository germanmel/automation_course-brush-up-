data1 = ['desktop', 'notes', 'commands', 'downloads', 'wordFile', 'excelFile']
data2 = ['Desktop', 'Notes', 'Commands', 'Downloads', 'Word File.doc', 'Excel File.doc']

data1 = str(data1).lower().replace(" ", "")
data2 = str(data2).lower().replace(".doc", "").replace(" ", "")

assert data1 == data2, "Error"


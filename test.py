import os.path

import pandas as pd
from openpyxl import load_workbook

def test():
    if not os.path.exists("D:/123.xlsx"):
        with pd.ExcelWriter("D:/123.xlsx", engine='openpyxl') as writer:
            df = pd.DataFrame(columns=['序号', '姓名'], data=[[1, 2]])
            df.to_excel(writer,sheet_name="sheet1",index=False)
            writer.save()
    else:
            df2=pd.DataFrame(pd.read_excel("D:/123.xlsx",sheet_name="sheet1",engine='openpyxl'))
            df = pd.DataFrame(columns=['序号', '姓名'],data=[[9,10]])
            book = load_workbook('D:/123.xlsx')
            writer= pd.ExcelWriter("D:/123.xlsx", engine='openpyxl')
            start_row=df2.shape[0]
            writer.book = book
            writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
            df.to_excel(writer,sheet_name='sheet1',startrow=start_row+1,index=False,header=False)
            writer.save()
def test2():
    with pd.ExcelWriter("D:/123.xlsx", engine="openpyxl", mode='a') as writer:
        df = pd.DataFrame(columns=['序号', '姓名'],data=[[9,10]] )
        df.to_excel(writer, sheet_name="Sheet2", index=False)
        writer.save()
test()
test2()

import numpy as np
import openpyxl as xl
import string

def scoreboard(name,score):
    add1=[]
    add2=[]
    if name not in add1:
        add1.append(name)
        add2.append(score)
    else:
        x=add1.index(name)
        add2[x]= add2[x]+ score

    table= np.array([add1,add2])
    wb=xl.Workbook()
    ws=wb.active
    ws.title= 'score'
    tableshape = np.shape(table)
    clmn=list(string.ascii_uppercase)
    for i in range(tableshape[0]):
        for j in range(tableshape[1]):
            ws[clmn[i]+str(j+1)]= table[i,j]
    wb.save('scores.xlsx')

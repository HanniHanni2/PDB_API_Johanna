import os
import pandas as pd


a = pd.read_excel("/home/turtle/PycharmProjects/PythonProject/files/ProteinlistaEco.xlsx")
b = pd.read_excel("/home/turtle/PycharmProjects/PythonProject/files/ProteinlistaSal.xlsx")
c = pd.read_excel("/home/turtle/PycharmProjects/PythonProject/files/ProteinlistaLac.xlsx")

listEco = a.iloc[:,1].tolist()
listSal = b.iloc[:,1].tolist()
listLac = c.iloc[:,1].tolist()

print(listEco)
print(listSal)
print(listLac)
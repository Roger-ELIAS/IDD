import re

sqlRequest = "SELECT * FROM tournagesdefilmsparis2011 WHERE titre = 'COUP DE FOUDRE A JAIPUR';"
result = re.search("FROM ([A-Za-z0-9]*)", sqlRequest)
fileName = (result.group())[5:]
print(fileName)
newRequest = sqlRequest.replace(fileName, "data")
print(newRequest)
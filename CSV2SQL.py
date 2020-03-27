#lecture d'un fichier CSV -> dataframe -> table SQL

import pandas as pd
import pandasql as ps
import re
import sqlite3

#sqlRequest = "SELECT * FROM tournagesdefilmsparis2011 WHERE titre = 'COUP DE FOUDRE A JAIPUR';"

class CSV2SQL():
	def translateRequest(self, sqlRequest):
		result = re.search("FROM ([A-Za-z0-9_-]*)", sqlRequest)
		fileName = (result.group())[5:]
		newRequest = sqlRequest.replace(fileName, "data")
		fileName += ".csv"
		return fileName, newRequest

	def fileReader(self, fileName):
		fileName
		data = pd.read_csv(fileName, sep=';')
		return data
		
	def queryOnData(self, data, sqlRequest):
		return ps.sqldf(sqlRequest, locals())
		
	def createTable(self, dataFrame, fileName):
		nomsChamps = list(dataFrame.columns.values)
		typesChamps = list(dataFrame.dtypes)
		lignes = dataFrame.values
		
		requests = []
		
		nom = fileName.split('.')
		sqlQuery = ''
		sqlQuery += 'CREATE TABLE ' + nom[0] + '('
		for i in range(0, len(nomsChamps)-1):
			sqlQuery += nomsChamps[i] + ', '
		sqlQuery += nomsChamps[len(nomsChamps)-1] + ');'
		sqlQuery += '\n'
		
		requests.append(sqlQuery)
		sqlQuery = ""
		
		for i in range(0, len(lignes)-1):
			sqlQuery += 'INSERT INTO ' + nom[0]
			sqlQuery += ' VALUES (\"'
			donnees = lignes[i]
			for i in range(0, len(donnees)-1):
				sqlQuery += str(donnees[i]) + '\", \"'
			sqlQuery += (str(donnees[len(donnees)-1]))
			sqlQuery += '\");'
			requests.append(sqlQuery)
			print(sqlQuery + '\n')
			sqlQuery = ""
		return requests

	def executeRequest(self, request):
		connexion = sqlite3.connect("DatabaseName.db")
		curseur = connexion.cursor()
		for i in range(0, len(request)-1):
			print(i)
			curseur.execute(request[i])
			connexion.commit()
		print("OPERATION FAITE")
		'''curseur.execute("SELECT * FROM tournagesdefilmsparis2011")
		resultat = curseur.fetchall()
		print(resultat)'''
		
	def deleteTable(self, fileName):
		nom = fileName.split('.')
		sqlQuery = "DROP TABLE " + nom[0]
		connexion = sqlite3.connect("DatabaseName.db")
		curseur = connexion.cursor()
		curseur.execute(sqlQuery)
		connexion.commit()


















import pandas as pd
import pandasql as ps
import re
import sqlite3
import CSV2SQL

class Mediateur():
	returnList = []

	def velibParis(self):
		sqlQuery = "CREATE VIEW velibParis AS "
		sqlQuery += "SELECT number, address, cp AS ardt, latitude, longitude, ville "
		sqlQuery += "FROM velib_a_paris_et_communes_limitrophes "
		sqlQuery += "WHERE ville = \"PARIS\""
		sqlQuery += "ORDER BY arrondissement;"
		
		sqlQuery2 = "SELECT number, address, cp AS ardt, latitude, longitude, ville "
		sqlQuery2 += "FROM velib_a_paris_et_communes_limitrophes "
		sqlQuery2 += "WHERE ville = \"PARIS\";"
		self.converterCall("velibParis", sqlQuery, sqlQuery2)
		
	def velibTournage(self):
		sqlQuery = "CREATE VIEW IF NOT EXISTS velibTournage AS "
		sqlQuery += "SELECT DISTINCT name AS Nom_de_la_station, "
		sqlQuery += "velib.adresse AS Adresse, lattitude, longitude, "
		sqlQuery += "cp AS arrondissement, realisateur, "
		sqlQuery += "films.type_de_tournage AS type_film "
		sqlQuery += "FROM velib_a_paris_et_communes_limitrophes AS velib, "
		sqlQuery += "tournagesdefilmsparis2011 AS films"
		sqlQuery += "WHERE velib.cp == films.ardt"
		sqlQuery += "ORDER BY arrondissement;"
		
		sqlQuery2 = "SELECT name, addresse, arrondissement, latitude, longitude "
		sqlQuery2 += "FROM velib_a_paris_et_communes_limitrophes "
		self.converterCall("velibTournage", sqlQuery, sqlQuery2)
		
	def converterCall(self, viewName, request1, request2):
		converter = CSV2SQL.CSV2SQL()
		fName, nRequest = converter.translateRequest(request2)
		d = converter.fileReader(fName)
		df = converter.queryOnData(d, nRequest)
		req = converter.createTable(df, fName)
		converter.executeRequest(req)
		
		connexion = sqlite3.connect("DatabaseName.db")
		curseur = connexion.cursor()
		curseur.execute(request1)
		connexion.commit()
		
		self.returnList = self.returnData(viewName, curseur)
		
		curseur.execute("DROP VIEW IF EXISTS " + viewName)
		connexion.commit()
		converter.deleteTable(fName)
		
	def returnData(self, viewName, curseur):
		curseur.execute("SELECT * FROM " + viewName)
		resultat = curseur.fetchall()
		return (pd.DataFrame(resultat).to_numpy()).tolist()

med = Mediateur()
med.velibParis()
for x in range(0, len(med.returnList)-1):
	print(med.returnList[x])










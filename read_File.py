#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import urllib.request # besoin d'etre installer  


#####################################################################################################################################
###################################                    Les fonctions               ##################################################
#####################################################################################################################################

def read_File(fileName):  # file format is for exemple: txt, csv, ...
	lignes = ""
	try:
		f = open(fileName,'r')
		lignes  = f.readlines()
		nomsChamps = lignes[0].split(';')
		lignesDonnees = []
		for i in range(1, len(lignes)-1):
			lignesDonnees.append(lignes[i])
		f.close()
	except FileNotFoundError:
		print("Wrong file or file path")
	create_Table(fileName, nomsChamps, lignesDonnees)
	
def create_Table(fileName, nomsChamps, lignes):
	nom = fileName.split('.')
	sqlQuery = ''
	sqlQuery += 'CREATE TABLE ' + nom[0] + '('
	for i in range(0, len(nomsChamps)-2):
		sqlQuery += nomsChamps[i] + ', '
	sqlQuery += nomsChamps[len(nomsChamps[:-2])-1] + ')'
	sqlQuery += '\n'
	for i in range(0, len(lignes)-1):
		sqlQuery += 'INSERT INTO ' + nom[0]
		sqlQuery += ' VALUES ('
		donnees = lignes[i].split(';')
		for i in range(0, len(donnees)-2):
			sqlQuery += donnees[i] + ', '
		sqlQuery += (donnees[len(donnees)-1])[:-2]
		sqlQuery += '); '
	print(sqlQuery)

'''
def read_page(link):  # read a we page and the out put will be a text with HTML format
  try:
	with urllib.request.urlopen(link) as response:
		 html = response.read()
  except urllib.error.URLError as e:
	print(e.reason)
  return html
'''

#####################################################################################################################################
###################################           L'utilisation des fonctions          ##################################################
#####################################################################################################################################

read_File("tournagesdefilmsparis2011.csv")

'''
FileData = read_page("url")
print (FileData)
'''



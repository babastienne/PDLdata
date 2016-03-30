import csv
import sqlite3


with open('../datas/activite.csv', 'r') as csvfile:
	conn = sqlite3.connect('ma_base.db') # Permet de créer la base de donnée
	cursor = conn.cursor()
	
	cursor.execute("""
	DROP TABLE activite
	""")
	conn.commit()	

	cursor.execute("""
	CREATE TABLE activite(
	     equipementid INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	     comLib TEXT,
	     actLib TEXT,
	     actCode INTEGER,
	     actNivLib TEXT
	)
	""")
	conn.commit()

	fieldnames = ['ComInsee','comLib', 'Equipementid', 'EqunbEquIdentique', 'ActCode', 'ActLib', 'EquActivitePraticable','EquActivitePratique', 'EquActiviteSalleSpe', 'ActNivLib'] # On associe chaque colonne à un nom
	monRead = csv.DictReader(csvfile, fieldnames=fieldnames)
	accu = 0
	for row in monRead:
		if accu > 0:	
			print(accu)
			cursor.execute("INSERT INTO activite(equipementid, comLib,actLib,actCode,actNivLib) VALUES({0}, {1}, {2}, {3}, {4})".format(row['Equipementid'],row['comLib'],row['ActLib'],row['ActCode'],row['ActNivLib']))
		accu = accu + 1

	db.close()



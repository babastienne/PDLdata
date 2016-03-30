import csv

with open('../datas/activite.csv', 'r') as csvfile:
	fieldnames = ['ComInsee','comLib', 'Equipementid', 'EqunbEquIdentique', 'ActCode', 'ActLib', 'EquActivitePraticable','EquActivitePratique', 'EquActiviteSalleSpe', 'ActNivLib']
	monRead = csv.DictReader(csvfile, fieldnames=fieldnames)
	for row in monRead:
    		 #print  (', '.join(row))
		print(row['comLib'],row['Equipementid'],row['ActLib'])
	
		


import csv
print ('Je commence à écrire le fichier xml')

reader = csv.reader(open('tournagesdefilmsparis2011.csv', 'r'), delimiter=";")
next(reader, None)

f = open('tournages_sortie.xml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
f.write('<!DOCTYPE tournages SYSTEM "tournages.dtd">' + '\n')
f.write('<tournages>' + '\n')

for row in reader:
    f.write('   ' + '<film>' + '\n')
    f.write('       ' + '<titre>' + row[0] + '</titre>' + '\n')
    f.write('       ' + '<réalisateur>' + row[1] + '</réalisateur>' + '\n')
    f.write('       ' + '<adresse>' + row[2] + '</adresse>' + '\n')
    f.write('       ' + '<organisme_demandeur>' + row[3] + '</organisme_demandeur>' + '\n')
    f.write('       ' + '<type_de_tournage>' + row[4] + '</type_de_tournage>' + '\n')
    f.write('       ' + '<arrondissement>' + row[5] + '</arrondissement>' + '\n')
    f.write('       ' + '<date_début>' + row[6] + '</date_début>' + '\n')
    f.write('       ' + '<date_fin>' + row[7] + '</date_fin>' + '\n')
    f.write('       ' + '<xy>' + row[8] + '</xy>' + '\n')
    f.write('   ' + '</film>'+ '\n')
    
f.write('</tournages>')
f.close()
print ('Fini!')
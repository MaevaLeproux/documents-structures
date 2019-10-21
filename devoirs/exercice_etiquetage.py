# coding: utf-8

from lxml import etree
xmlfile = "Duchn-etiquetage.txt.xml"
# Initialiser la lecture du fichier
tree = etree.parse(xmlfile)

# La racine
root = tree.getroot()

# Reconstruire les phrases
var = ""
liste = []
print("Voici les phrases : ")
for element in root.iter('element'):
    var = var + element[2].text + " "
    if element[2].text == '.':
        var = var + '\n'
        liste.append(var)
        
print(liste)

# Extraire tous les déterminants
print("Voici les déterminants: \n")
for element in root.iter('element'):
    for child in element:
        if child.attrib.get('type') == 'type' and 'DET' in child.text:
            print(element[2].text)
            
# Transformer l'affichage en : token/lemme/pos
for element in root.iter('element'):
    print("{}/{}/{}".format(element[2].text, element[1].text, element[0].text))

# Afficher les patrons DET - NOM
i = 0
for element in root.iter('article'):
    for child in element:  
        if "DET" in element[i][0].text:
            if "NOM" in element[i+1][0].text:
                print("{} -> {}".format(element[i][2].text, element[i+1][2].text))
        i += 1  
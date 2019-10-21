# coding: utf-8

from lxml import etree
xmlfile = "valery_ame-et-danse_1921.xml"
# Initialiser la lecture du fichier
tree = etree.parse(xmlfile)

# La racine
root = tree.getroot()

# Utiliser un espace de nom
TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
TEI = "{%s}" % TEI_NAMESPACE

# Afficher le nom de l'éditeur <edition>
for element in root.iter(TEI + 'edition'):
    print("Nom de l'éditeur: {}".format(element.text))
        
# Afficher l'url de la licence <licence>
for element in root.iter(TEI + 'availability'):
    for child in element:
        print("URL de la licence: {}".format(child.attrib.get('target')))

# Afficher le personnage avec le plus de tours de parole (@speaker), et le nombre de répliques
dico = {}
import operator
for element in root.iter( TEI + 'label'):
    dico[element.text] = dico.get(element.text, 0) +1
sorted_dico = sorted(dico.items(), key=operator.itemgetter(1), reverse=True)
print("Voici le personnage qui parle le plus, et son nombre de répliques: {}".format(sorted_dico[0]))

# Ajouter un autre <respStmt> avec deux enfants name et resp contenant du texte

for element in root.iter (TEI + 'editionStmt'):
    child = etree.SubElement(element, "respStmt")
    sub_child1 = etree.SubElement(child, "name")
    sub_child1.text="Blabla"
    sub_child1 = etree.SubElement(child, "resp")
    sub_child1.text="Youpi"
    
# Modifier la valeur de la signature <signature> pour afficher le texte existant en majuscule

for element in root.iter (TEI + 'signed'):
    for child in element:
        print(child.text.upper())
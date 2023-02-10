"""
La ville de Montpellier a équipé ses rues de défibrillateurs pour permettre de sauver des victimes
d'arrêts cardiaques. Les données correspondant à la position de tous les défibrillateurs sont accessibles en ligne.

Sur la base des données fournies dans les tests, vous décidez d'écrire un programme qui permettra aux
usagers de trouver le défibrillateur le plus proche de là où ils se trouvent, grâce à leur téléphone portable.
 	Règles
En entrée de votre programme sont fournies les données dont vous avez besoin, au format texte.
Ces données sont notamment composées de lignes dont chacune représente un défibrillateur.
Chaque défibrillateur est représenté par les champs suivants :
Numéro identifiant le défibrillateur
Nom
Adresse
Numéro de téléphone à joindre
Longitude (en degrés)
Latitude (en degrés)
Ces champs sont séparés par un point-virgule (;)

Attention : les nombres décimaux utilisent la virgule (,) comme séparateur pour la partie décimale.
Pensez à transformer la virgule (,) en point (.) si nécessaire pour utiliser les données dans votre programme.

DISTANCE
La distance d entre deux points A et B sera calculée en utilisant la formule suivante :

x = (longitudeB - longitudeA)*cos((latitudeA + latitudeB)/2)
y = (latitudeB - latitudeA)
d = sqtr(x**2 + y**2)*6371

Note : Dans cette formule, les latitudes et longitudes sont exprimées en radians.
6371 correspond au rayon de la terre en km.

Le programme affichera le nom du défibrillateur se trouvant au plus près de la position de l'utilisateur.
Cette position est fournie en entrée au programme.

Entrées du jeu
Entrée
Ligne 1 : la longitude (en degrés) de l'utilisateur

Ligne 2 : la latitude (en degrés) de l'utilisateur

Ligne 3 le nombre N de défibrillateurs équipant les rues de Montpellier

N lignes suivantes : une description de chaque défibrillateur

Sortie
Le nom du défibrillateur le plus proche de la position de l'utilisateur.
Contraintes
0 < N < 10000

Exemple entrée :
3,879483
43,608177
3
1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217
2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849
3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854

"""

# import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class Defib:
    def __init__(self, id, name, address, phone, longitude, latitude):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.longitude = float(longitude.replace(',', '.'))
        self.latitude = float(latitude.replace(',', '.'))


lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())

defibs = []
for i in range(n):
    defib = input()

    defibs.append(Defib(*defib.split(';')))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

near_defib = defibs[0]
distance = 6371

for defib in defibs:
    x = (lon - defib.longitude) * math.cos((defib.latitude + lat) // 2)
    y = lat - defib.latitude
    d = math.sqrt(x**2 + y**2) * 6371

    if distance > d:
        distance = d
        near_defib = defib

result = near_defib.name

# print("answer")
print(result)

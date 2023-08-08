#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import cgi
form = cgi.FieldStorage()

#Übernahme der Eingaben mit Error-Handling
try:
    input_name = form["var_name"].value
except:
    input_name = 'Keine Eingabe'
try:
    input_einwohner = int(form["var_einwohner"].value)
except:
    input_einwohner = 0
try:
    input_flaeche = int(form["var_flaeche"].value)
except:
    input_flaeche = 0
try:
    randomizer = int(form["var_randomizer"].value)
except:
    randomizer = 0


class Country(object):
    def __init__(self, name, einwohner, flaeche):
        self.name = name
        self.einwohner = einwohner
        self.flaeche = flaeche


# Country declaration
# Einwohnerzahl ist gerundet (bsp. 17,8 Mio)
Deutschland = Country("Deutschland", 84200000, 357588)
Kolumbien = Country("Kolumbien", 52100000, 1141748)
Venezuela = Country("Venezuela", 31700000, 912050)
Ecuador = Country("Ecuador", 17800000, 256370)
Guyana = Country("Guyana", 787000, 214970)
Suriname = Country("Suriname", 500000, 163820)
Frankreich = Country("Frankreich", 68000000, 632733)
Peru = Country("Peru", 32800000, 1285216)
Brasilien = Country("Brasilien", 214500000, 8515770)
Bolivien = Country("Bolivien", 12100000, 1098581)
Paraguay = Country("Paraguay", 7100000, 406752)
Uruguay = Country("Uruguay", 3500000, 176215)
Chile = Country("Chile", 19100000, 756102)
Argentinien = Country("Argentinien", 46000000, 2780400)

# Create Array
Countries = []
Countries.append(Deutschland)
Countries.append(Kolumbien)
Countries.append(Venezuela)
Countries.append(Ecuador)
Countries.append(Guyana)
Countries.append(Suriname)
Countries.append(Frankreich)
Countries.append(Peru)
Countries.append(Brasilien)
Countries.append(Bolivien)
Countries.append(Paraguay)
Countries.append(Uruguay)
Countries.append(Chile)
Countries.append(Argentinien)

# Berechnung der Ausgaben
einwohner_diff = round(abs(input_einwohner - (Countries[randomizer].einwohner/1000000)), 2)
flaeche_diff = round(abs(input_flaeche - Countries[randomizer].flaeche), 2)

# Segment für die Flaggenauswahl
flag = '<div id="flag_div">'
if randomizer == 1:
    flag += '<img src="../Pictures/Flags/co.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 2:
    flag += '<img src="../Pictures/Flags/ve.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 3:
    flag += '<img src="../Pictures/Flags/ec.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 4:
    flag += '<img src="../Pictures/Flags/gy.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 5:
    flag += '<img src="../Pictures/Flags/sr.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 6:
    flag += '<img src="../Pictures/Flags/fr.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 7:
    flag += '<img src="../Pictures/Flags/pe.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 8:
    flag += '<img src="../Pictures/Flags/br.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 9:
    flag += '<img src="../Pictures/Flags/bo.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 10:
    flag += '<img src="../Pictures/Flags/py.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 11:
    flag += '<img src="../Pictures/Flags/uy.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 12:
    flag += '<img src="../Pictures/Flags/cl.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
elif randomizer == 13:
    flag += '<img src="../Pictures/Flags/ar.svg" alt="Bild konnte nicht geladen werden" class="imagesize"></div>'
else:
    flag += '<p>Kein Bild :(</p></div>'

# Segment für die Kartenauswahl
map = '<div id="map_div">'
if randomizer == 1:
    map += '<img src="../Pictures/Maps_Countries/Columbia.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 2:
    map += '<img src="../Pictures/Maps_Countries/Venezuela.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 3:
    map += '<img src="../Pictures/Maps_Countries/Ecuador.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 4:
    map += '<img src="../Pictures/Maps_Countries/Guyana.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 5:
    map += '<img src="../Pictures/Maps_Countries/Suriname.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 6:
    map += '<img src="../Pictures/Maps_Countries/French_Guyana.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 7:
    map += '<img src="../Pictures/Maps_Countries/Peru.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 8:
    map += '<img src="../Pictures/Maps_Countries/Brazil.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 9:
    map += '<img src="../Pictures/Maps_Countries/Bolivia.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 10:
    map += '<img src="../Pictures/Maps_Countries/Paraguay.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 11:
    map += '<img src="../Pictures/Maps_Countries/Uruguay.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 12:
    map += '<img src="../Pictures/Maps_Countries/Chile.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
elif randomizer == 13:
    map += '<img src="../Pictures/Maps_Countries/Argentina.svg" alt="Bild konnte nicht geladen werden" ' \
           'class="imagesize"></div>'
else:
    map += '<p>Kein Bild :(</p></div>'

#Start der HTML-Datei
print("Content-Type: text/html")
print(f'''
<!DOCTYPE html>
<html lang='de'>
<head>
<meta charset="utf-8">
<link rel='stylesheet' href='../css/styles.css'>
<title>RoWis cooles Geographie Quiz - Auflösung</title>
</head>
<body>
<div id="background">
<div>
<h1 id="header">RoWis cooles Geographie Quiz - Auflösung</h1>
</div>
{flag}
{map}
<div id="table_div">
<table>
<tr>
<th></th>
<th>Land</th>
<th>Einwohner</th>
<th>Fläche</th>
</tr>
<tr>
<td>Gesucht:</td>
<td>{Countries[randomizer].name}</td>
<td>{Countries[randomizer].einwohner/1000000} Mio.</td>
<td>{Countries[randomizer].flaeche} km²</td>
</tr>
<tr>
<td>Eingaben:</td>
<td>{input_name}</td>
<td>{input_einwohner} Mio.</td>
<td>{input_flaeche} km²</td> 
</tr>
<tr>
<td>Differenz:</td>
<td></td>
<td>{einwohner_diff} Mio.</td>
<td>{flaeche_diff} km²</td> 
</tr>
<tr>
<td>Vergleich:</td>
<td>{Deutschland.name}</td>
<td>{Deutschland.einwohner/1000000} Mio.</td>
<td>{Deutschland.flaeche} km²</td> 
</tr>
</table>
<br>
<a class="links" id="link" href="http://pan.th-brandenburg.de/~huebner/cgi-bin/Impressum.html"> Studenten + 
Quellen </a>
</div>
</div>
</body>
</html>
''')
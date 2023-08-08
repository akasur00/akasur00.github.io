1#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import random
randomizer = random.randint(1, 13)
# 0=Deutschland

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
    flag += '<img src="../Pictures/Flags/uy.svg" alt="Bild konnte nicht geladen werden" class="imagesize"/></div>'
elif randomizer == 12:
    flag += '<img src="../Pictures/Flags/cl.svg" alt="Bild konnte nicht geladen werden" class="imagesize"/></div>'
elif randomizer == 13:
    flag += '<img src="../Pictures/Flags/ar.svg" alt="Bild konnte nicht geladen werden" class="imagesize"/></div>'
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

# Start der HTML-Datei
print('Content-Type: text/html')
print(f'''
<!DOCTYPE html>
<html lang='de'>
<head>
<meta charset="utf-8">
<link rel='stylesheet' href='../css/styles.css'>
<title>RoWis cooles Geographie Quiz</title>
</head>

<body>
<div id="background">
<div>
<h1 id="header">RoWis cooles Geographie Quiz</h1>
</div>
{flag}
{map}
<div id="form_div">
<form method="post" action="./Auflösung.cgi">
<p>Geben sie die folgenden Daten zum angezeigten Land an:</p>
<p>Name des Landes:<br>
<input type="text" name="var_name"></p>
<div id="tooltip_div">    
<div class="tooltip">Tipp 
<span class="tooltiptext">
Kolumbien, Venezuela, Ecuador, Guyana, Suriname, Frankreich, 
Peru, Brasilien, Bolivien, Paraguay, Uruguay,
Chile, Argentinien
</span>
</div>
</div>
<p>Schätzen sie die Einwohnerzahl in Millionen:<br>
<input type="text" name="var_einwohner"></p>
<p>Schätzen sie die Fläche in km²:<br>
<input type="number" name="var_flaeche"></p>
''')
print(f'<input type="hidden" name="var_randomizer" value="{randomizer}">')
print('''
<p><input type="submit" value="Überprüfen"></p>
</form>
<br>
<a class="links" id="link" href="http://pan.th-brandenburg.de/~huebner/cgi-bin/Impressum.html"> Studenten + 
Quellen </a>
</div>
</div>
</body>
</html>
''')

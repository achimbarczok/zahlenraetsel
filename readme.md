# Zahlenrätsel 

Work in Progress!


Dieses Programm ist noch im pre Alpha Status und funktioniert noch nicht 

Berechnet Zahlenraetsel nach Heinz Böer:

x ? y = z

wobei x und y je eine Würfelzahl von 1 bis 6 annehmen kann (x = y ist möglich).

Beide Würfel dürfen 0 bis 2 mal in einer Rechnung verwendet werden. Genutzt werden dürfen die 4 Grundrechenarten, Potenzen und Fakultäten

Ziel ist es, eine Rechnung zu finden, die z ergibt, wobei Z zwischen 1 und 20 liegt.

Beispiel:

```
1 ? 3 = 18
```

Beispiellösungen:

```
(1+1)*3*3 = 18
3!*3 = 18
```

Aber für

```
1 ? 5 = 18
```

gibt es keine Lösung.


## Voraussetzungen

 * Git ≥ 1.8
 * Python ≥ 3.7
 * Libraries: math


## Installation

```
pip install pipenv
git clone git@github.com:acb-ct/zahlenraetsel.git
cd zahlenraetsel
pipenv install
```

## Aufruf


``` 
pipenv run ./zahlenraetsel.py
```

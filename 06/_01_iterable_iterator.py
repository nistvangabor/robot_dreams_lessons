#ITERABLE: egy objektum amely képes egyesével visszaadni az elemeit (string a karaktereit, lista az elemeit stb.)
#ITERATOR: egy speciális objektum, amely egyszerre egy elemet ad vissza egy iterable-ből, az iter() function-nel hozunk létre egy iteratort és a next() function-nel iterálunk (váltunk a következő elemre)
#ITERATION: az elemenként haladás folyamata, egy elemről a másikra való eljutást nevezzük egy iterációnak
#LOOP: automatizálja az iteration folyamatát

#PÉLDA:

#ITERABLE: Spotify (vagy bármilyen) zene lejátszási lista
#ITERATOR: Mi magunk, akik egyik zeneszámról a következő zeneszámra kattintunk (>>, >>, >>), Tudjuk, hogy melyik szám szól jelenleg, és tudjuk hogy játsszuk le a következőt
#ITERATION: a következő számra való ugrás a next (>>) gombbal
#LOOP: automatikus lejátszás anélkül hogy mi nyomnánk a next gombra, egészen addig amíg a lejátszási lista végére nem érünk.

#ITERABLE:
playlist = ["I'm a barbie girl", "8 óra munka", "Autó egy szerpentinen", "Heavy is the crown"]

#ITERATOR:
it = iter(playlist)
print(type(it))
#ITERATION:
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it))


#Miért jó nekünk egy iteratopr?
#Nem töltődik be az egész collection a memóriába, mindig az aktuális elemet tároljuk
#lazy evaluation: akkor generálódik adat amikor szükség van rá

#LOOP ->




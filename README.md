# HIDÁSZ projektarchívum

42187 becsomagolt fájl; a meglévő ZIP változatlan, darabolt másolata.

Archívum és fájllista: [GitHub Release](https://github.com/istok1488/hidasz-archivum-2c959756a07f/releases/tag/archivum-20260930).

Forráskiválasztás: Projektjelölő nevű mappák teljes tartalma; jelölőnevű vagy szövegesen felismerhető fájlok.

Az eredeti csomagolási státusz: `PARTIAL_OR_FAILED`. 2 hozzáférési/archiválási jelzés; a részletek az EREDMENY.json fájlban maradnak. A hozzáférhetetlen mappák tartalma nem ismert.

A Release a feltöltés és a darabok SHA-256-ellenőrzése után jelenik meg. A .part fájlok egyetlen ZIP bájtszeletei; együtt állítandók vissza.

Töltsd le a Release DARABOK_LETOLTES.json fájlját, majd futtasd:

```sh
python visszaallitas.py DARABOK_LETOLTES.json
```

Ez letölti, ellenőrzi és egy új ZIP-be egyesíti a darabokat. A GitHub által kínált Source code ZIP a tároló útmutatóit tartalmazza; a projektállományok a Release mellékleteiben vannak.

Az EREDMENY.json és OLVASD_EL.txt az eredeti csomagolás naplója: bennük a GitHub-feltöltés még NEM TÖRTÉNT értéke a csomagoláskori állapotot jelöli. A feltöltésnek külön eredményjelentése készül.

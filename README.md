# PisteetKotiin - ainutlaatuinen kotitöiden pisteytyssovellus

[PisteetKotiin](https://pisteetkotiin.herokuapp.com/)

[Käyttäjätarinat](https://github.com/jupste/tsoha-harjoitustyo/blob/master/documentation/userstory.md)

[Tietokantamalli](https://github.com/jupste/tsoha-harjoitustyo/blob/master/documentation/diagram.png)

[Asennus ja käyttöohje](https://github.com/jupste/tsoha-harjoitustyo/blob/master/documentation/installation.md)

Usein kotityöt jäävät tekemättä, kun taloudessa on monta henkilöä ja töiden jako jää puolitiehen. Tähän ongelmaan on kehitteillä PisteetKotiin- kotityösovellus, jonka avulla kotityöt jakautuvat melkein itsestään. 

Sovellus pyrkii pisteyttämään kotitöitä jolloin samassa kotitaloudessa asuvat henkilöt voivat saada pisteitä tekemällä kotitöitä. Sovellukseen on määritelty erilaisia kotityötyyppejä,joista saa tietyn määrän pisteitä. Jokainen käyttäjä kuuluu johonkin kotitalouteen, jolle en määritelty tiety viikkopistemäärä, joka pitää suorittaa. Tämä pistemäärä voi määrittyä esimerkiksi talouden asunnon koon mukaan, kuinka monta lasta tai kotieläintä taloudessa on, tai sen mukaan, mikä yleinen siisteystaso taloudessa halutaan ylläpitää. Pistemäärää voi myös tarvittaessa korottaa tai alentaa, esimerkiksi juhlien tai ulkomaanmatkan takia. 

Jokaiselle kotitaloudelle on määritelty erikseen, mitä kaikkia kotitöitä tässä taloudessa tulee tehdä. Kullekkin kotityölle on merkitty myös tietty aikaväli, jonka välein niitä olisi hyvä suorittaa. Näin ollen sovellus ei tarjoa esimerkiksi imurointia suoritettavaksi kotityöksi silloin, kun edellisenä päivänä vasta imuroitiin. Mikäli jokin kotityö seisoo tekemättä kotitalouden suorittamattomat listassa liian kauan, saattaa sovellus huomauttaa tästä ja tarvittaessa tarjota lisäpisteitä tämän suorittamisesta. Samalla kotityöllä voi olla myös monta tekijää. Tällöin pisteet jakautuvat tekijöiden kesken. Näin sovellukseen saadaan monesta-moneen suhde. 
Käyttäjä pystyy lisäämään uusia automaattisesti generoituvia kotitöitä kotitalouteensa. Hän pystyy myös poistamaan aiempia generoituvia kotitöitä tai muokaamaan esim. niiden aikaväliä. Käyttäjä voi lisätä tarjolla oleviin kotitöihin omia custom-kotitöitä ja poistamaan muiden tekemiä custom-kotitöitä. Näin tietokantaan saadaan kaksi CRUDia (create, read, update, delete) toteuttavaa tietokantataulua. 


Toiminnalisuudet:
- Uuden käyttäjän luominen. Kun uusi käyttäjä luodaan, voi hän liittyä olemassa olevaan kotitalouteen tai hän voi perustaa uuden kotitalouden.
- Kotitalous generoi listan suorittamattomista kotitöistä, josta käyttäjät voivat käydä valitsemassa suoritettavia kotitöitä. Suoritetut kotityöt näkyvät käyttäjän näkymässä.
- Käyttäjät voivat tarvittaessa lisätä generoitavia kotitöitä ja myös lisätä kertaluonteisia kotitaloussuoritteita. 

Sovelluksen käyttäjätunnukset:
tunnus: seppo
salasana: testi

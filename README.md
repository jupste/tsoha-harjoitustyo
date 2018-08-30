# PisteetKotiin - ainutlaatuinen kotitöiden pisteytyssovellus

[PisteetKotiin](https://pisteetkotiin.herokuapp.com/)

[Käyttäjätarinat](https://github.com/jupste/tsoha-harjoitustyo/blob/master/documentation/userstory.md)

[Tietokantamalli](https://github.com/jupste/tsoha-harjoitustyo/blob/master/documentation/diagram.png)

[Asennus ja käyttöohje](https://github.com/jupste/tsoha-harjoitustyo/blob/master/documentation/installation.md)

[SQL CREATE TABLE komennot](https://github.com/jupste/tsoha-harjoitustyo/blob/master/documentation/sql_commands.md)

Usein kotityöt jäävät tekemättä, kun taloudessa on monta henkilöä ja töiden jako jää puolitiehen. Tähän ongelmaan on kehitteillä PisteetKotiin- kotityösovellus, jonka avulla kotityöt jakautuvat melkein itsestään. 

Sovellus pyrkii pisteyttämään kotitöitä jolloin samassa kotitaloudessa asuvat henkilöt voivat saada pisteitä tekemällä kotitöitä. Jokainen käyttäjä kuuluu johonkin kotitalouteen ja jokaisella kotitaloudella on oma lista tekemättömistä sekä viikottaisista kotitöistä. Sovellukseen on määritelty erilaisia kotityötyyppejä, joita käyttäjät voivat tehdä sekä luoda uusia. Käyttäjä pystyy myös määrittelemään kotityöstä saatavan pistemäärän. Tämä pistemäärä voi määrittyä esimerkiksi talouden asunnon koon mukaan, kuinka monta lasta tai kotieläintä taloudessa on, tai sen mukaan, mikä yleinen siisteystaso taloudessa halutaan ylläpitää. Viikottaisten kotitöiden pistemäärää voi myös tarvittaessa korottaa tai alentaa, esimerkiksi juhlien tai ulkomaanmatkan takia. 

Samalla kotityöllä voi olla myös monta tekijää. Tällöin pisteet jakautuvat tekijöiden kesken. Kotityön voi jakaa yhtä monta osaan, kuin mitä sillä on pisteitä. Näin sovellukseen saadaan monesta-moneen suhde. 
Käyttäjä pystyy lisäämään uusia automaattisesti generoituvia kotitöitä kotitalouteensa. Hän pystyy myös poistamaan aiempia generoituvia kotitöitä tai muokaamaan esim. niiden aikaväliä. Käyttäjä voi lisätä tarjolla oleviin kotitöihin custom-kotitöitä sekä poistamaan sekä viikottaisten kotitöiden tuottamia tekemättömiä kotitöitä, että custom-kotitöitä. 


#### Toiminnalisuudet:
- Uuden käyttäjän luominen. Kun uusi käyttäjä luodaan, voi hän liittyä olemassa olevaan kotitalouteen tai hän voi perustaa uuden kotitalouden.
- Kotitalous generoi listan suorittamattomista kotitöistä, josta käyttäjät voivat käydä valitsemassa suoritettavia kotitöitä. Suoritetut kotityöt näkyvät käyttäjän näkymässä.
- Käyttäjät voivat tarvittaessa lisätä generoitavia kotitöitä ja myös lisätä kertaluonteisia kotitaloussuoritteita. 
- Pääkäyttäjä voi alustaa kotitaloustyyppien listan sekä tehdä muiden kuin oman kotitalouden kotitöitä

#### Täyden CRUDin täyttävät tietotaulut:
[AvailableChore](https://github.com/jupste/tsoha-harjoitustyo/blob/master/application/chores/views.py) sekä [WeeklyChore](https://github.com/jupste/tsoha-harjoitustyo/blob/master/application/weeklychore/views.py)

#### Monesta moneen relaation toteuttava tietotaulut

[DoneChore](https://github.com/jupste/tsoha-harjoitustyo/blob/master/application/donechores/views.py)

Tämä tietotaulu mahdollistaa tietotaulujen [User](https://github.com/jupste/tsoha-harjoitustyo/blob/master/application/auth/views.py) sekä [AvailableChore](https://github.com/jupste/tsoha-harjoitustyo/blob/master/application/chores/views.py) välisen monesta moneen suhteen.

#### Sovelluksen käyttäjätunnukset:
tunnus: seppo
salasana: testi

#### Tulevia kehityskohteita:
- Kotitöiden pisteiden automaattinen lisääminen, mikäli ne seisovat liian kauan tekemättöminä
- Tehtyjen kotitöiden tilastointi
- Kotitalouteen liittymiseen salasana tai jokin muu rajaava tekijä
- Kotitöiden dynaaminen pisteyttäminen, ts. suosittujen kotitöiden pisteitä lasketaan kun taas epäsuosittujen nostetaan
- Käyttäjien kokonaispisteiden vertailu jollakin tietyllä aikavälillä
- Pääkäyttäjälle kotityötyyppien lisäysmahdollisuus
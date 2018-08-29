## Käyttöohje ja asennus

Linkki sovellukseen: [Pisteetkotiin](pisteetkotiin.herokuapp.com)

Sovellus on käytettävissä joko testipalvelimella tai paikallisessa virtuaaliympäristössä. 

### Rekisteröiminen 

Kirjautumaton käyttäjä voi tarkastella sovelluksen etusivua sekä hän voi mennä "Häpeälista"- sivulle. Tämä sivu koostaa listan kaikista käyttäjistä, ketkä eivät ole tehneet kotitöitä viikkoon. Jos kirjautumaton käyttäjä yrittää päästä mihinkään muuhun välilehteen, hänet ohjataan sisäänkirjautumissivulle. Mikäli käyttäjällä ei ole tunnuksia, voi hän luoda ne "Uusi käyttäjä"-painikkeesta. Uutta käyttäjää rekisteröidessä tulee valita, mihin kotitalouteen hän kuuluu. 

### Saatavilla olevat kotityöt

Käyttäjä voi tehdä hänen kotitaloudelleen kuuluvia kotitöitä. Kotitöitä tekemään pääsee "Saatavilla olevat kotityöt"- välilehdestä. Käyttäjä voi joko tehdä kotityön kokonaan tai osittain. Kotityön voi jakaa niin moneen osaan, kuin mitä siinä on pisteitä. Kun kotityö on tehty kokonaan eli sen pisteet on nollassa, häviää se saatavilla olevien kotitöiden listalta. Käyttäjä voi myös tarkastella kotityötä tarkemmin "Näytä kotityö"-painikkeesta. Tämän saman painikkeen kautta käyttäjä voi myös muokata kotityön viestiä sekä poistaa kotityön. 

Käyttäjä voi myös luoda omia kotitöitä "Lisää custom-kotityö"-välilehdestä. Tällöin käyttäjän tulee valita kotityön tyyppi, sekä sen pistemäärä. Halutessaan käyttäjä voi lisätä viestin mukaan kotityöhön. Tehdyt kotityöt voi tarkastaa "Kotitalouden tehdyt kotityöt"-välilehdestä, jossa näkyy kaikkien samaan kotitalouteen kuuluvien käyttäjien tehdyt kotityöt.

### Viikottaiset kotityöt

Käyttätäjä voi lisätä kotitaloudelleen uuden viikottaisen kotityön "Viikottaiset kotityöt" -välilehden kautta. Käyttäjän tulee valita viikottaiselle kotityölle sekä pisteet, kotityön tyyppi että aikaväli.  Viikottaiset kotityöt lisäävät saatavilla olevien kotitöiden listaan uusia oman tyyppinsä kotitöitä niille asetetun aikavälin välein. Aikavälit on ilmoitettu päivissä. Käyttäjä voi tarkastella yksittäisiä viikottaisia kotitöitä, sekä vaihtaa niiden pisteitä ja aikavälejä tai poista ne kokonaan.


### Asennusohje

- Lataa sovelluksen tiedostot GitHub-reporitoriosta komennolla

> git clone https://github.com/jupste/tsoha-harjoitustyo

- Luo sovellukselle virtuaaliympäristö kansion juureen komennolla

> python3 -m venv venv

- Aktivoi luotu virtuaaliympäristö komennolla

> source venv/bin/activate

- Asenna sovelluksen riippuvuudet komennolla

> pip install -r requirements.txt

- Käynnistä sovellus komennolla 

> python run.py

Nyt sovellus on käytettävissä osoittessa
[localhost:5000](localhost:5000)

- Ennen kuin sovelusta voi täysimääräisesti käyttää testiympäristössä, tulee kotitalouksien tyypit alustaa

- Sovellukseen pitää olla kirjautunut pääkäyttäjän tunnuksilla (ensimmäinen luotu tunnus saa automaattisesti pääkäyttäjän tunnukset)

- Mene sivulle "Pääkäyttäjän näkymä" ja paina "Alusta"-painiketta
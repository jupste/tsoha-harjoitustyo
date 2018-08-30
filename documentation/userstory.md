## Käyttäjätarinat

### Käyttäjä haluaa lisätä itselleen käyttäjätilan

#### Hyväksymiskriteerit:
- Käyttäjä valitsee uusi käyttäjä välilehden
- Käyttäjä valitsee itselleen nimen ja käyttäjätunnuksen sekä salasanan
- Käyttäjä valitsee, mihin kotitalouteen hän haluaa liittyä, tai jos hän ei halua liittyä mihinkään olemassaolevaan kotitalouteen, voi hän luoda uuden.

#### SQL-kyselyt:
> INSERT INTO account (user, username, password, household) VALUES user, username, password, household;

### Käyttäjä lisää uuden kotitalouden

Hyväksymiskriteerit:
- Käyttäjä painaa "lisää uusi kotitalous" -painiketta
- Käyttäjä valitsee uudelle kotitaloudelle nimen

#### SQL-kyselyt:
> INSERT INTO household (name) VALUES name;

### Käyttäjä listaa tehtävissä olevat kotityöt ja tekee niistä yhden osittain

#### Hyväksymiskriteerit:
- Käyttäjä siirtyy "Saatavilla olevat kotityöt"-välilehteen
- Sovellus näyttää listan kaikista käyttäjän kotitalouden tekemättömistä kotitöistä
- Käyttäjä painaa "Tee osittain"-nappia, jolloin käyttäjälle kirjautuu osasuoritus kyseisestä kotityöstä

#### SQL-kyselyt:
> SELECT * FROM chore WHERE householdid= current_user.household;
> UPDATE chore SET points=points-1 WHERE id=choreid;

Jos tietue ei ole olemassa:
> INSERT INTO done_chore (choreid, userid, points) VALUES choreid, current_user.id, 1;

Jos tietue on olemassa:
> UPDATE done_chore SET points=points+1 WHERE id=choreid;

### Käyttäjä tekee kotityön kokonaan

#### Hyväksymiskriteerit:
- Sama kuin ylhäällä, mutta käyttäjä painaa "Tee kokonaan"-painiketta, jolloin käyttäjälle kirjautuu kokonainen suoritus kyseisestä kotityöstä

#### SQL-kyselyt:

> UPDATE chore SET points=0 WHERE id=choreid;

Jos tietue ei ole olemassa:
> INSERT INTO done_chore (choreid, userid, points) VALUES choreid, current_user.id, chore.points;

Jos tietue on olemassa:
> UPDATE done_chore SET points=points+chore.points WHERE id=choreid;

### Käyttäjä poistaa turhan kotityön

#### Hyväksymiskriteerit: 
- Käyttäjä painaa "Näytä kotityö"-painiketta, josta avautuu näkymä yksittäisen kotityön tietoihin
- Käyttäjä painaa "Poista kotityö"-painiketta, jolloin kyseinen kotityö poistuu

#### SQL-kyselyt;
> DELETE * FROM chore WHERE id=choreid;

### Käyttäjä muuttaa kotityöhön liitettyä viestiä

#### Hyväksymiskriteerit: 
- Käyttäjä painaa "Näytä kotityö"-painiketta, josta avautuu näkymä yksittäisen kotityön tietoihin
- Käyttäjä kirjoittaa uuden viestin ja painaa "Muokkaa viestiä"-painiketta

#### SQL-kyselyt:
> SELECT * FROM chore WHERE id=choreid;
> UPDATE chore SET message=new_message WHERE id=choreid;

### Käyttäjä katsoo kotitaloudessaan suoritetut kotityöt

#### Hyväksymiskriteerit:
- Käyttäjä siirtyy "Kotitalouden tehdyt kotityöt"- sivulle, joka listaa kaikki käyttäjän kotitaloudessa tehdyt kotityöt

#### SQL-kyselyt:
> SELECT account.id, account.name, choretype.name, done_chore.points, done_chore.date_created FROM done_chore 
                    INNER JOIN Account ON done_chore.userid=Account.id 
                    INNER JOIN chore ON done_chore.choreid=chore.id 
                    INNER JOIN household ON account.household= household.id 
                    INNER JOIN choretype ON chore.choretype=choretype.id
                    WHERE account.household= current_user.household

### Käyttäjä lisää uuden viikottaisen kotityön

#### Hyväksymiskriteerit:
- Käyttäjä siirtyy "Viikottaiset kotityöt"- sivulle ja painaa "Lisää uusi" -painiketta
- Käyttäjä valitsee kotityön tyypin, siitä saatavan pistemäärän ja sen aikavälin
- Saatavilla oleviin kotitöihin ilmestyy tätä tyyppiä ja tämän pistemäärän omaava uusi tekemätön kotityö

#### SQL-kyselyt:
> INSERT INTO weekly_chores (choretype, householdid, interval, points, last_made) VALUES choretype, current_user.household, interval, points, datetime.now();

### Käyttäjä muuttaa viikottaista kotityötä

#### Hyväksymiskriteerit:
- Käyttäjä siirtyy "Viikottaiset kotityöt"- sivulle ja painaa "Näytä" -painiketta haluamansa kotityön kohdalla
- Käyttäjä syöttää uudet haluamansa arvot ja painaa "Muokkaa"-painiketta

#### SQL-kyselyt:
> UPDATE weekly_chores SET points=new_points, interval=new_interval WHERE id=weeklyid;

### Käyttäjä poistaa viikkottaisen kotityön

#### Hyväksymiskriteerit:
- Käyttäjä siirtyy "Viikottaiset kotityöt"- sivulle ja painaa "Näytä" -painiketta haluamansa kotityön kohdalla
- Käyttäjä painaa "Poista"-painiketta, jolloin kyseinen viikottainen kotityö poistuu
- Tästä viikottaisesta kotityöstä tuotetut tehtävissä olevat kotityöt eivät poistu samalla, vaan ne pitää poistaa erikseen "Saatavilla olevat kotityöt"-sivulta

#### SQL-kyselyt:
> DELETE * FROM weekly_chores WHERE id=weeklyid;

### Käyttäjä haluaa nähdä kenellä hänen kotitaloudessaan on eniten pisteitä

#### Hyväksymiskriteerit:
- Käyttäjä kirjautuu sisään niin tämä tieto on etusivulla

#### SQL-kyselyt:
>SELECT MAX(sum), id, name FROM (SELECT Account.id AS id, Account.name AS name, SUM(done_chore.points) AS sum FROM done_chore 
                    INNER JOIN Account ON done_chore.userid=Account.id 
                    INNER JOIN household ON account.household= household.id 
                    WHERE account.household= current_user.household GROUP BY userid);


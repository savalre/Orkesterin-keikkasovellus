# Orkesterin keikkasovellus
Sovellus on alunperun tehty "Tietokantasovellus"-kurssia varten. 

Orkesterin keikkasovellus on selainpohjainen sovellus, jossa orkesteri voi lisätä keikkoja ja soittaja voi ilmoittautua keikoille. Sovellus on tarkoitettu yksittäisen orkesterin käyttöön, ei niinkään julkiseksi keikkapalveluksi. Sovelluksen tarkoituksena on hyödyttää orkesteria kokoamalla yleisimmät säätöä aiheuttavat toiminnot yhteen sovellukseen, eli keikkojen ja niiden kokoonpanon hallinnoinnin.

HUOM: Projektin toiminnot ja termistö on mallinnettu Savolaisen Osakunnan Soitannallisen seuran SOSSu ry:n toimintojen perusteella, mutta ovat muokattavissa muidenkin kokoonpanojen tarpeisiin. SOSSu ei ole ollut osallisena tämän sovelluksen kehityksessä, vaan tekijä on tehnyt sen itse oman harrastuneisuutensa pohjalta itsenäisenä orkesterin jäsenenä. 

<h2>LOPULLINEN PALAUTUS</h2>

<h3>Projektin testaus:</h3>
Sovellusta voi testata Herokussa: https://orkesterinkeikkasovellus.herokuapp.com/ 
<br>

 - Käyttäjän toimintoja pääsee testaamaan luomalla itselleen tunnukset järjestelmään.
  - Admin-puolta pääsee testaamaan väliaikaisilla admintunnuksilla (käyttäjätunnus,salasana): testinuotti, 1234

<br>
<br>
Käyttäjä voi:<br>
  * Rekisteröityä palveluun
  * Kirjautua sisään ja ulos sovellusesta
 * Muokata omia profiilitietojaan "Oma profiilisi"-sivulla. Käyttäjä voi lisätä itselleen soittimia, jotka listautuvat profiilitiedoissa
 * Käyttäjä voi lisätä palveluun keikan
 * Käyttäjä voi ilmoittautua keikalle omalla soittimellaan
 * Käyttäjä voi muokata keikan tietoja tai poistaa keikan
 * Käyttäjä voi poistaa ilmoittautumisensa keikalle
 * Käyttäjä voi tarkastella keikan kokoonpanoa, eli keitä muita keikalle on ilmoittautunut ja mihin soittimeen


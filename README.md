# Orkesterin keikkasovellus
Sovellus on tehty "Tietokantasovellus"-kurssia varten. 

Orkesterin keikkasovellus on selainpohjainen sovellus, jossa orkesteri voi lisätä keikkoja ja soittaja voi ilmoittautua keikoille. Sovellus on tarkoitettu yksittäisen orkesterin käyttöön, ei niinkään julkiseksi keikkapalveluksi. Sovelluksen tarkoituksena on hyödyttää orkesteria kokoamalla yleisimmät säätöä aiheuttavat toiminnot yhteen sovellukseen, eli keikkojen ja niiden kokoonpanon hallinnoinnin.

HUOM: Projektin toiminnot ja termistö on mallinnettu Savolaisen Osakunnan Soitannallisen seuran SOSSu ry:n toimintojen perusteella, mutta ovat muokattavissa muidenkin kokoonpanojen tarpeisiin. SOSSu ei ole ollut osallisena tämän sovelluksen kehityksessä, vaan tekijä on tehnyt sen itse oman harrastuneisuutensa pohjalta itsenäisenä orkesterin jäsenenä. 

<h2>Sovelluksen tukemat selaimet ja alustat:</h2>
Sovellus toimii sekä mobiiliselaimella että tietokoneella. Sovelluksen käyttö on testattu Firefoxilla, Chromella ja Safarilla, ja näillä sovellus toimii. Sovelluksen toimintaa ei ole testattu Internet Explorerilla.

<h2>LOPULLINEN PALAUTUS</h2>

<h3>Projektin testaus:</h3>
Sovellusta voi testata Herokussa: https://orkesterinkeikkasovellus.herokuapp.com/ 
<br>

 - Käyttäjän toimintoja pääsee testaamaan luomalla itselleen tunnukset järjestelmään.
  - Admin-puolta pääsee testaamaan väliaikaisilla admintunnuksilla (käyttäjätunnus,salasana): testinuotti, 1234
<br>
<h3>Peruskäyttäjä voi:</h3>
<br>

 - Rekisteröityä palveluun
 - Kirjautua sisään ja ulos sovelluksesta
 - Muokata profiilitietojaan: Käyttäjä voi lisätä itselleen soittimia ja ilmoittautua aktiiviseksi/poissaolevaksi orkesterista.
 - Käyttäjä voi ilmottautua keikalle haluamallaan soittimella (mutta vain 1/keikka). Käyttäjä näkee omalla sivulla keikat, joihin on ilmoittautunut. Käyttäjä voi poistaa ilmoittautumisensa keikalta.
 - Käyttäjä näkee keikan kokoonpanon, eli ketä muita soittajia keikalle on ilmoittautunut
 <br>
 <h3>Admin voi:</h3>
 <br>
 
 - Tehdä samat asiat kuin peruskäyttäjä, mutta lisäksi:
  -  Lisätä palveluun keikan
  -  Muokata keikan tietoja tai poistaa keikan järjestelmästä
  -  Lisätä ja poistaa admin-oikeuksia muilta käyttäjiltä
  -  Nähdä kokoonpanosivulla aktiiviset käyttäjät, jotka eivät ole vielä ilmoittautuneet keikalle. Näin admin tietää ketä voi pyytää täydentämään sektioita
<br>
<h3>Tulevaisuuden kehitysideat:</h3>
<br>

 - Käyttäjätunnusten poiston mahdollistaminen niin adminille kuin peruskäyttäjälle. 
 - Muiden roolien lisäämisen mahdollistaminen, esimerkiksi puheenjohtaja, varapuheenjohtaja jne. 
 - Käyttäjänimen voi muuttaa
 - Estää keikalle ilmoittautuminen, jos et soita kokoonpanoon kuuluvaa soitinta (nyt mahdollista, mutta kyseinen ilmoittautuminen ei listaudu mihinkään)

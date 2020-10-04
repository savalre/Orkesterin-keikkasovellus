# Orkesterin keikkasovellus
Sovellus on alunperun tehty "Tietokantasovellus"-kurssia varten. 

Orkesterin keikkasovellus on selainpohjainen sovellus, jossa orkesteri voi lisätä keikkoja ja soittaja voi ilmoittautua keikoille. Sovellus on tarkoitettu yksittäisen orkesterin käyttöön, ei niinkään julkiseksi keikkapalveluksi. Tarkoituksena on luoda sovellus, joka hyödyttää orkesteria kokoamalla yleisimmät säätöä aiheuttavat toiminnot yhteen sovellukseen, eli keikkojen ja niiden kokoonpanon hallinnoinnin.

Projektin ulkoasu ja toiminnot on mallinnettu Savolaisen Osakunnan Soitannallisen seuran SOSSu ry:n toimintojen perusteella, mutta ovat muokattavissa muidenkin kokoonpanojen tarpeisiin.


<h2>VÄLIPALAUTUS 3:</h2>

<h3>Projektin tämänhetkinen tilanne:</h3>

Tällä hetkellä sovellus toimii kuten sen pitääkin. Sovelluksessa voi tehdä kaiken Projektin testaus -valikossa luetellun. 
  
Puuttuvat ominaisuudet/To do -lista:<br>
  * Admin-sivu, jossa admin voi antaa muille käyttäjille adminoikeudet
  * Tiettyjen toimintojen näkyvyyden poisrajaaminen peruskäyttäjiltä
 * Kokoonpano-sivun tuloste nätimmäksi
 * Varoitus ennen keikan poistoa, sekä varoitus väärästä salasanasta/käyttäjätunnuksesta 
 * Kosmeettiset korjaukset: sivujen asettelun parantaminen ja siistiminen
 * Koodin siistiminen: muuttujien ja metodien kielen yhtenäistäminen (nyt sekaisin englantia ja suomea)

<h3>Projektin testaus:</h3>
Sovellusta voi testata Herokussa: https://orkesterinkeikkasovellus.herokuapp.com/
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

<h2>Projektin aihe: Orkesterin keikkasovellus</h2>

Käyttäjä voi olla joko admin tai soittaja (ns. "peruskäyttäjä"). Admin-oikeudet omaava voi myös olla soittaja. Admin-roolin saaja voi olla esimerkiksi joko orkesterin kapellimestari, puheenjohtaja tai hallituslainen.

Admin voi lisätä sovellukseen keikkoja. Keikalla tulee olla nimi, kuvaus ja päivämäärä, sekä tapahtumapaikka. Lisäksi admin voi määritellä keikkaa luotaessa onko kyseessä pienryhmäkeikka, koko orkesterin keikka vai jokin muokattu kokoonpano. Ohjelma luo automaattisesti pohjan siitä, mitä soittimia tarvitaan mukaan keikalle eli mikä keikan kokoonpano on. 

Admin voi poistaa sovelluksesta peruuntuneen keikan. 

Käyttäjä luo järjestelmään tunnukset, jossa määritellään oma orkesterinimi ("käyttäjänimi"), mitä soittimia hän orkesterissa soittaa ja onko hän aktiivisesti orkesterin toiminnassa mukana (aktiivinen-tila). Aktiivinen-tilaa pääsee muokkaamaan omassa profiilissaan. Lisäksi soittaja voi lisätä ja poistaa soittimia, joita hän orkesterissa soittaa. 

Käyttäjä voi ilmoittautua keikalle valitsemallaan soittimella. Käyttäjä näkee myös mille keikoille hän on ilmoittautunut. Käyttäjä näkee keikasta tiedot sekä jo ilmoittautuneet soittajat, muttei pääse muokkaamaan kokoonpanoa. Käyttäjä voi poistaa itsensä keikalta. 

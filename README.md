# Orkesterin-keikkasovellus
Kurssin Tietokantasovellus repositorio 

<h2>VÄLIPALAUTUS 2:</h2>


<h2>Projektin aihe: Orkesterin keikkasovellus</h2>

Orkesterin keikkasovellus on selainpohjainen sovellus, jossa orkesteri voi lisätä keikkoja ja soittaja voi ilmoittautua keikoille. Sovellus on tarkoitettu yksittäisen orkesterin käyttöön, ei niinkään julkiseksi keikkapalveluksi. Tarkoituksena on luoda sovellus, joka hyödyttää orkesteria kokoamalla yleisimmät säätöä aiheuttavat toiminnot yhteen sovellukseen, eli keikkojen ja niiden kokoonpanon hallinnoinnin. Ulkoasu ja toiminnot on mallinnettu Savolaisen Osakunnan Soitannallisen seuran SOSSu ry:n toimintojen perusteella, mutta ovat muokattavissa muidenkin kokoonpanojen tarpeisiin.

Käyttäjä voi olla joko admin tai soittaja (ns. "peruskäyttäjä"). Admin-oikeudet omaava voi myös olla soittaja. Admin-roolin saaja voi olla esimerkiksi joko orkesterin kapellimestari, puheenjohtaja tai hallituslainen.

Admin voi lisätä sovellukseen keikkoja. Keikalla tulee olla nimi, kuvaus ja päivämäärä, sekä tapahtumapaikka. Lisäksi admin voi määritellä keikkaa luotaessa onko kyseessä pienryhmäkeikka, koko orkesterin keikka vai jokin muokattu kokoonpano. Ohjelma luo automaattisesti pohjan siitä, mitä soittimia tarvitaan mukaan keikalle eli mikä keikan kokoonpano on. 

Admin voi poistaa sovelluksesta peruuntuneen keikan. 

Käyttäjä luo järjestelmään tunnukset, jossa määritellään oma orkesterinimi ("käyttäjänimi"), mitä soittimia hän orkesterissa soittaa ja onko hän aktiivisesti orkesterin toiminnassa mukana (aktiivinen-tila). Aktiivinen-tilaa pääsee muokkaamaan omassa profiilissaan. Lisäksi soittaja voi lisätä ja poistaa soittimia, joita hän orkesterissa soittaa. 

Käyttäjä voi ilmoittautua keikalle valitsemallaan soittimella. Käyttäjä näkee myös mille keikoille hän on ilmoittautunut. Käyttäjä näkee keikasta tiedot sekä jo ilmoittautuneet soittajat, muttei pääse muokkaamaan kokoonpanoa. Käyttäjä voi poistaa itsensä keikalta. 


Admin näkee keikan kokoonpanon, eli keikalle ilmoittautuneet soittajat soitinryhmittäin: 

Esimerkki:<br>
Pasuunat: <br>
  -ps1: "Lambi"
  -ps2: "Wolfgang"
  -ps3: "TYHJÄ"

Ylläolevassa tilanteessa pasuuna 3:een ei ole ilmoittautunut soittajaa. Admin voi hakea listan pasuunaa soittavista orkesterilaisista, jotka ovat listanneet statuksekseen "aktiivinen". Näin admin saa selville suoraan ketä voi pyytää keikalle. Samoin voi toimia minkä tahansa soittimen kohdalla.

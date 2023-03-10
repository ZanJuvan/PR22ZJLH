# Preiskovanje povezav med različnimi glasbami

## 1. Uvod
Projekt bova izdelovala Žan Juvan in Luka Hrvatin, izpeljan bo kot seminarska naloga pri predmetu podatkovno rudarjene. Za to temo sva se odločila saj oba veliko poslušava glasbo. 

## 2. Podatki 
### 2.1. Opis podatkov
Podatke sestavljajo skladbe od leta 1950 do 2019. Dataset sva dobila na spletni strani [Mendeley Data](https://data.mendeley.com/datasets/3t9vbwxgr5/2). Podatki so bili nazadnje posodobljeni 23. oktobra 2020. Za ta dataset sva se odločila saj nama ponuja široko ponudbo. V primerjavi z drugimi sva bila omejena na stare podatke kot je naprimer [Figshare](https://figshare.com/articles/dataset/Main_Dataset_for_Evolution_of_Popular_Music_USA_1960_2010_/1309953) ali sva pa z količino podatkov kot naprimer [Spotify API](https://corgis-edu.github.io/corgis/csv/music/), ki ima omejitev na količino pridobljenih podatkov. 
### 2.2. Atributi
Pridobljeni dataset je sestavljen iz 30 atributov. Za boljšo predstavo bodo spodaj našteti z kratkim opisom.
 - artist_name
 - track_name 
 - release_date 
 - genre 
 - lyrics 
 - len 
 - dating 
 - violence
 - world/life
 - night/time
 - shake the audience
 - family/gospel
 - romantic
 - communication
 - obscene
 - music
 - movement/places
 - light/visual perceptions
 - family/spiritual
 - like/girls
 - sadness 
 - feelings 
 - danceability 
 - loudness 
 - acousticness
 - instrumentalness 
 - valence 
 - energy 
 - topic
 - age



## 3. Vprašanja
Najini cilji so razdeljeni na dva dela.
### 3.1. Predlaganje podobne glasbe
Od uporabnika bi pridobili seznam nekaj pesmi (npr. 10) nato bi poskusili pridobiti podobne pesmi glede na njegov dosedanji izbor. Testirala bi lahko tako, da bi naredila poskus na kolegih. Zaupali bi nama 10 pesmi in nato bi program vrnil eno ali dve pesmi. Najino mnenje je, da bi lahko bil ta poskus kar uspešen saj nam je pri glasbi pomembno več faktorjev, katere imava podane v podatkih

**Hipoteza:**
 * V več kot 60% poskusov bova lahko napovedala tako pesem, da bo poslušalcu všeč glede na njegov predizbor desetih pesmi.
### 3.2. Sprememba glasbenih trendov skozi čas
Pri tej cilju se bova najbloj osredotočila na zvrst in temo pesmi. Seveda pa bova opazovala tudi vse druge parametre. Zanimivo bo tudi videti kako se spreminja naprimer nasilje v pesmih in pa energija.

**Hipotezi:**
 * Po letu 2010 je več pesmi, na katere se bolje pleše (dancability).
 * Na porastu so bolj žalostne pesmi kot včasih, še posebej po letu 2015.

### 3.3. Več izdanih pesmi sedaj
Meniva da je v povprečju v zadnjih letih več izdanih pesmi kot je bilo pred letom 2000. Najino mnenje je, da za to pripomogla tudi digitalizacija, ki nam omogoča lažjo izdajo pesmi in večjo povezljivost med avtorji.

**Hipoteza:**
 * Pred letom 2000 je bilo v povprečju manj izdanih pesmi kot po letu 2000.
## 4. Zaključek
Upava, da sva pravilno napovedala vsaj polovico hipotez. 

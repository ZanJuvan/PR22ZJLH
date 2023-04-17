# Preiskovanje povezav med različnimi glasbami

## 1. Opis problema
Zanima naju kakšne povezave lahko najdeva med različnimi tipi ali žanri glasbe, kot tudi povezave med avtorji. Veva, da v večini avtorji skozi leta spremenijo stil glasbe in naju zanima če je to res in kako se to pozna. Pogledala bova tudi če so se trendi skozi čas zelo spreminjali, tu se bova osredotočila predvsem na spremembo žanrov, kako dobra je pesem za ples in podobno. 

Kot sva navedla že v osnutku je najin največji cilj še vedno podobnost med glasbami kot sem napisal zgoraj podobnost med žanri in temami, kot seveda tudi med ustvarjalci le teh. Tu bova rarzdelila glasbe v več različnih časovnih obdobji in bova znotraj vsakeka poskusila dobiti neke podobnosti, ali le povprečne spremembe med obdobji. 

Podala sva tudi, da bi lahko na podlagi 10 pesmi lahko napovedala uporabniko podobne pesmi. Ampak kot sva že malo pregledala celoten dataset sva ugotovila, da je bila najina hipoteza, da bova v 60% primerov napovedala tako pesem, da bo uporabniku všeč glede na njihov predizbor, malo pre več optimistična, saj so razlike med glasbami zelo male. in bo res težko dobiti najbolj idealno pesem glede na izbor 10ih pesmi.

Pregledala bova tudi kako hitro se povečuje število izdanih pesmi glede na vsako leto. tu bova spremljala tudi različne teme in žanre, ne smo izdaje. 

### Hipoteze
 * V več kot 60% poskusov bova lahko napovedala tako pesem, da bo poslušalcu všeč glede na njegov predizbor desetih pesmi.
 * Po letu 2010 je več pesmi, na katere se bolje pleše (dancability).
 * Na porastu so bolj žalostne pesmi kot včasih, še posebej po letu 2015.
 * Pred letom 2000 je bilo v povprečju manj izdanih pesmi kot po letu 2000.


## 2. Opis podatkov
Za uporabo sva se odločila, da bova uporabila dataset iz spletne strani [Mendeley Data](https://data.mendeley.com/datasets/3t9vbwxgr5/2). V datasetu imamo shranjenih 28373 glasbe in vsaka od njih ima po 30 parametrov, kateri so spodaj našteti in imajo kratek opis. Ta dataset je biu ustvarjen z starejšimi odordji, ki v današnjih dneh nimajo več veliko podpore in niso popularni zato točnih opisov podatkov žal nisva mogla dobiti. Narejen je bil s pomočjo Echo Nest API-ja in pa spotipy, ki je paket za python, kateri se uporablja za pridobivanje glasenih podatkov preko Spotify-a.

Podatki: 
 * id - identifikacijska številka skladbe
 * artist_name - umetinkovo ime
 * track_name - naslov glasbe
 * release_date - leto izdaje
 * genre - žanr glasbe (7 skupin)
 * lyrics - besedilo glasbe
 * len - število besed v besedilu
 * dating - ali je primerna za pare
 * violence - ali vsebuje veliko nasilja
 * world/life - ali je znana po svetu
 * night/time - ali je bolj primerna za nočni čas
 * shake the audience - ali vzburi publiko da se razživi 
 * family/gospel - ali je pesem za družine ali evangelistična
 * romantic - ali je pesem romantična
 * communication - kakšna je komunikacija v pesmi
 * obscene - 
 * music - 
 * movement/places - 
 * light/visual perceptions
 * family/spiritual - ali je pesem za družine ali je dohovna 
 * like/girls - 
 * sadness - kako žalostna je pesem 
 * feelings - ali nam izraža dobra ali slaba čustva več je boljša
 * danceability - kako dobro se lahko na njo pleše
 * loudness - kako zelo je glasna
 * acousticness - kako zelo je akustična 
 * instrumentalness - kako zelo je inštrumentalna
 * valence - kako vezljiva je pesem 
 * energy - kako energična je glsaba 
 * topic - tema glasbe (8 skupin)
 * age - razpon starosti izražen s številko
  

## 3. Glavne ugotovitve

## 4. Izvedene alaize

## 5. Glavni rezultati
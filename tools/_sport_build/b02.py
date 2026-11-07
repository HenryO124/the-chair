# -*- coding: utf-8 -*-
# Batch 2: Finnish Olympic gold medallists, ice hockey world champions,
#          Finnish F1 drivers, Tour de France winners before 2020
# Sources:
#  https://en.wikipedia.org/wiki/Finland_at_the_Olympics
#  https://en.wikipedia.org/wiki/List_of_IIHF_World_Championship_medalists
#  https://en.wikipedia.org/wiki/Formula_One_drivers_from_Finland
#  https://en.wikipedia.org/wiki/List_of_Tour_de_France_general_classification_winners
Q = []
def q(en, fi):
    Q.append((["Sport"] + list(en), ["Sport"] + list(fi)))

# ------------------------------------------------- Finnish Olympic gold medallists
q(["In which sport did Verner Weckman win Finland's first ever Olympic gold, in 1908?", "Wrestling", "Athletics", "Shooting", "Gymnastics",
   "Finland was still a Grand Duchy of Russia, and its athletes were allowed no flag of their own at those Games."],
  ["Missä lajissa Verner Weckman voitti Suomen kaikkien ensimmäisen olympiakullan vuonna 1908?", "Painissa", "Yleisurheilussa", "Ampumisessa", "Voimistelussa",
   "Suomi oli yhä Venäjän suuriruhtinaskunta, eivätkä sen urheilijat saaneet noissa kisoissa omaa lippua."])

q(["At which Games did Finland win fifteen Olympic golds, more than at any other?", "Antwerp 1920", "Helsinki 1952", "Paris 1924", "Los Angeles 1932",
   "A country of three million took fifteen golds and 34 medals in all, and finished near the top of the medal table."],
  ["Missä kisoissa Suomi voitti viisitoista olympiakultaa, enemmän kuin missään muissa?", "Antwerpen 1920", "Helsinki 1952", "Pariisi 1924", "Los Angeles 1932",
   "Kolmen miljoonan asukkaan maa otti viisitoista kultaa ja kaikkiaan 34 mitalia ja sijoittui mitalitaulukon kärkipäähän."])

q(["How many Olympic gold medals has Finland won in all, summer and winter together?", "146", "61", "212", "99",
   "101 came at the Summer Games and 45 at the Winter, and more than half the summer ones were won before 1940."],
  ["Kuinka monta olympiakultaa Suomi on voittanut kaikkiaan, kesä ja talvi yhteen laskien?", "146 kultaa", "61 kultaa", "212 kultaa", "99 kultaa",
   "Kesäkisoista tuli 101 ja talvikisoista 45, ja yli puolet kesäkulloista voitettiin ennen vuotta 1940."])

q(["When did Finland last win an Olympic gold medal in athletics?", "Atlanta 1996", "Seoul 1988", "Sydney 2000", "Barcelona 1992",
   "Heli Rantanen's javelin was the last of them, and the country that once owned the distance races has not thrown or run for gold since."],
  ["Milloin Suomi voitti viimeksi olympiakultaa yleisurheilussa?", "Atlanta 1996", "Seoul 1988", "Sydney 2000", "Barcelona 1992",
   "Heli Rantasen keihäs oli viimeinen, eikä kestävyysjuoksut aikoinaan omistanut maa ole sen jälkeen heittänyt tai juossut kultaa."])

q(["Hannes Kolehmainen won three Olympic titles on the track in 1912. Which did he add in 1920?", "The marathon", "The 1500 metres", "The steeplechase", "The 800 metres",
   "He won it by thirteen seconds over a course measured at 42.75 km, and it was said he had run Finland onto the map."],
  ["Hannes Kolehmainen voitti kolme olympiakultaa radalla 1912. Minkä hän lisäsi vuonna 1920?", "Maratonin", "1500 metrin", "Estejuoksun", "800 metrin",
   "Hän voitti sen kolmellatoista sekunnilla 42,75 kilometriksi mitatulla radalla, ja sanottiin että hän juoksi Suomen maailmankartalle."])

q(["Which Finn won four golds in Paris in 1924 and another in Amsterdam in 1928?", "Ville Ritola", "Hannes Kolehmainen", "Volmari Iso-Hollo", "Albin Stenroos",
   "He had emigrated to New York as a young man and only took up serious running at 25, after watching a Finnish club meeting there."],
  ["Kuka suomalainen voitti neljä kultaa Pariisissa 1924 ja vielä yhden Amsterdamissa 1928?", "Ville Ritola", "Hannes Kolehmainen", "Volmari Iso-Hollo", "Albin Stenroos",
   "Hän oli muuttanut nuorena New Yorkiin ja alkoi juosta tosissaan vasta 25-vuotiaana nähtyään siellä suomalaisen seuran kilpailut."])

q(["In which sport did Clas Thunberg win five Olympic golds for Finland in the 1920s?", "Speed skating", "Cross-country skiing", "Ski jumping", "Nordic combined",
   "He had never raced abroad before his first Games, and all five golds came after he had turned thirty."],
  ["Missä lajissa Clas Thunberg voitti Suomelle viisi olympiakultaa 1920-luvulla?", "Pikaluistelussa", "Maastohiihdossa", "Mäkihypyssä", "Yhdistetyssä",
   "Hän ei ollut kilpaillut ulkomailla ennen ensimmäisiä kisojaan, ja kaikki viisi kultaa tulivat kolmenkymmenen ikävuoden jälkeen."])

q(["Which Finn won the Olympic javelin gold in 1932 and broke the world record ten times?", "Matti Jarvinen", "Jonni Myyra", "Armas Taipale", "Pauli Nevala",
   "The tower of the Helsinki Olympic Stadium was built to 72.71 metres because that was the length of his best throw."],
  ["Kuka suomalainen voitti keihään olympiakullan 1932 ja rikkoi maailmanennätyksen kymmenen kertaa?", "Matti Järvinen", "Jonni Myyrä", "Armas Taipale", "Pauli Nevala",
   "Helsingin olympiastadionin torni rakennettiin 72,71 metrin korkuiseksi, koska se oli hänen parhaan heittonsa pituus."])

q(["Which Finn won the 1928 Olympic decathlon, having trained alone on his own farm with no coach?", "Paavo Yrjola", "Akilles Jarvinen", "Volmari Iso-Hollo", "Matti Jarvinen",
   "He set a world record in winning it and went on competing between the harvests at Hauho for another eight years."],
  ["Kuka suomalainen voitti kymmenottelun olympiakullan 1928 harjoiteltuaan yksin omalla maatilallaan ilman valmentajaa?", "Paavo Yrjölä", "Akilles Järvinen", "Volmari Iso-Hollo", "Matti Järvinen",
   "Hän teki voittaessaan maailmanennätyksen ja jatkoi kilpailemista Hauhon peltotöiden lomassa vielä kahdeksan vuotta."])

q(["In the 1932 Olympic steeplechase final the lap counter lost count. How far did the runners go?", "3460 metres", "3000 metres", "2800 metres", "3200 metres",
   "Volmari Iso-Hollo of Finland won the extra lap too, and because of the error his time was never ratified as a record."],
  ["Vuoden 1932 olympiaestejuoksun finaalissa kierroslaskija meni sekaisin. Kuinka pitkälle juostiin?", "3460 metriä", "3000 metriä", "2800 metriä", "3200 metriä",
   "Suomen Volmari Iso-Hollo voitti ylimääräisen kierroksenkin, ja virheen takia hänen aikaansa ei koskaan hyväksytty ennätykseksi."])

q(["Three Finns shared the gold medal on the same gymnastics apparatus in 1948. Which apparatus?", "The pommel horse", "The rings", "The high bar", "The vault",
   "Paavo Aaltonen, Veikko Huhtanen and Heikki Savolainen all scored exactly the same, and Finland won the team title as well."],
  ["Kolme suomalaista jakoi kultamitalin samalla voimistelutelineellä vuonna 1948. Millä telineellä?", "Hevosella", "Renkailla", "Rekillä", "Hyppytelineellä",
   "Paavo Aaltonen, Veikko Huhtanen ja Heikki Savolainen saivat täsmälleen samat pisteet, ja Suomi voitti myös joukkuekilpailun."])

q(["Finland has won Olympic boxing gold twice. Who won the second, in front of a home crowd in 1952?", "Pentti Hamalainen", "Olli Maki", "Risto Luukkonen", "Elis Ask",
   "Sten Suvio had won the first in Berlin in 1936, and no Finn has won boxing gold in the seventy years since."],
  ["Suomi on voittanut nyrkkeilyn olympiakultaa kahdesti. Kuka voitti toisen kotiyleisön edessä 1952?", "Pentti Hämäläinen", "Olli Mäki", "Risto Luukkonen", "Elis Ask",
   "Sten Suvio voitti ensimmäisen Berliinissä 1936, eikä yksikään suomalainen ole voittanut nyrkkeilykultaa sen jälkeisinä seitsemänkymmenenä vuotena."])

q(["Sylvi Saimo won an Olympic gold at Helsinki in 1952, at the age of 38. In which sport?", "Canoeing", "Rowing", "Shooting", "Fencing",
   "She is still the only Finnish woman to have won an Olympic canoeing title, and she had trained on the lake by her home."],
  ["Sylvi Saimo voitti olympiakultaa Helsingissä 1952 38-vuotiaana. Missä lajissa?", "Melonnassa", "Soudussa", "Ampumisessa", "Miekkailussa",
   "Hän on yhä ainoa suomalainen nainen, joka on voittanut melonnan olympiakultaa, ja hän oli harjoitellut kotinsa viereisellä järvellä."])

q(["Pentti Linnosvuo won Olympic shooting golds eight years apart. What did he use?", "Two different pistols", "The same pistol twice", "A rifle both times", "A shotgun both times",
   "The free pistol at fifty metres in 1956 and the rapid-fire pistol in 1964, two events that share almost nothing but the hand."],
  ["Pentti Linnosvuo voitti ampumisen olympiakultaa kahdeksan vuoden välein. Millä aseella?", "Kahdella eri pistoolilla", "Samalla pistoolilla kahdesti", "Kiväärillä molemmat", "Haulikolla molemmat",
   "Vapaapistoolilla viideltäkymmeneltä metriltä 1956 ja isopistoolin pikalaukauksilla 1964, lajeissa joilla ei ole yhteistä kuin käsi."])

q(["Which Finn beat the Kenyan favourite Kipchoge Keino to the Olympic 1500 metres gold in 1972?", "Pekka Vasala", "Lasse Viren", "Juha Vaatainen", "Martti Vainio",
   "He stayed at the back for twelve hundred metres and then ran a final lap of about 53 seconds."],
  ["Kuka suomalainen päihitti kenialaisen ennakkosuosikin Kipchoge Keinon 1500 metrin olympiakullasta 1972?", "Pekka Vasala", "Lasse Virén", "Juha Väätäinen", "Martti Vainio",
   "Hän pysyi takajoukoissa kaksitoistasataa metriä ja juoksi sitten noin 53 sekunnin loppukierroksen."])

q(["Which Finnish fireman won the Olympic single sculls at three Games in a row from 1976?", "Pertti Karppinen", "Esko Rechardt", "Tomi Poikolainen", "Kaarlo Kangasniemi",
   "Two metres tall and rowing out of Vehmaa, he beat the East German Peter-Michael Kolbe in two of those three finals."],
  ["Kuka suomalainen palomies voitti soudun yksikön olympiakullan kolmissa kisoissa putkeen vuodesta 1976?", "Pertti Karppinen", "Esko Rechardt", "Tomi Poikolainen", "Kaarlo Kangasniemi",
   "Kaksimetrinen vehmaalainen kaatoi itäsaksalaisen Peter-Michael Kolben kahdessa näistä kolmesta finaalista."])

q(["Finland's last two Olympic golds in men's throwing events came at the same Games. Which Games?", "Los Angeles 1984", "Moscow 1980", "Seoul 1988", "Munich 1972",
   "Juha Tiainen took the hammer and Arto Harkonen the javelin, four days apart, and no Finnish man has thrown for gold since."],
  ["Suomen kaksi viimeisintä miesten heittolajien olympiakultaa tulivat samoista kisoista. Mistä kisoista?", "Los Angeles 1984", "Moskova 1980", "Seoul 1988", "München 1972",
   "Juha Tiainen voitti moukarin ja Arto Härkönen keihään neljän päivän välein, eikä suomalaismies ole sen jälkeen heittänyt kultaa."])

q(["Tapio Korjus won the 1988 Olympic javelin with the last throw of the competition. By what margin?", "16 centimetres", "two metres", "half a metre", "four centimetres",
   "He beat Jan Zelezny, who went on to set the world record and win three Olympic titles of his own."],
  ["Tapio Korjus voitti vuoden 1988 olympiakeihään kilpailun viimeisellä heitolla. Kuinka pienellä erolla?", "16 senttimetriä", "Kaksi metriä", "Puoli metriä", "Neljä senttimetriä",
   "Hän kaatoi Jan Železnýn, josta tuli maailmanennätysmies ja kolminkertainen olympiavoittaja."])

q(["Heli Rantanen was the first Finnish woman to win an Olympic athletics gold. What won it for her?", "The first throw of the final", "A last-round throw", "A world record", "A throw-off",
   "She threw it in 1996 and then watched eleven rivals fail to pass it, having never won a major medal before or after."],
  ["Heli Rantanen oli ensimmäinen suomalainen nainen, joka voitti yleisurheilun olympiakultaa. Mikä sen toi?", "Finaalin ensimmäinen heitto", "Viimeisen kierroksen heitto", "Maailmanennätys", "Uusintaheitto",
   "Hän heitti sen 1996 ja katsoi sitten yhdentoista kilpakumppanin yrittävän turhaan ohi; muita arvomitaleita ei uralle tullut."])

q(["Satu Makela-Nummela won Finland's most recent Summer Olympic gold in 2008. In which sport?", "Shooting", "Sailing", "Rowing", "Wrestling",
   "The tally has not moved since: Finland came home from London, Rio, Tokyo and Paris without a single gold medal."],
  ["Satu Mäkelä-Nummela voitti Suomen tuoreimman kesäolympiakullan vuonna 2008. Missä lajissa?", "Ampumisessa", "Purjehduksessa", "Soudussa", "Painissa",
   "Luku ei ole sen jälkeen liikahtanut: Suomi tuli Lontoosta, Riosta, Tokiosta ja Pariisista ilman yhtäkään kultaa."])

q(["Lydia Wideman won Finland's first women's Winter Olympic gold in 1952. Why not earlier?", "Women had not been allowed to ski", "She was too young", "Finland was banned", "Her event was cancelled",
   "Women's cross-country skiing was on the Olympic programme for the first time that year, as a single 10-kilometre race."],
  ["Lydia Wideman voitti Suomen ensimmäisen naisten talviolympiakullan 1952. Miksei aiemmin?", "Naiset eivät olleet saaneet hiihtää", "Hän oli liian nuori", "Suomi oli kilpailukiellossa", "Hänen lajinsa oli peruttu",
   "Naisten maastohiihto oli olympiaohjelmassa ensimmäisen kerran tuona vuonna, yhtenä kymmenen kilometrin kilpailuna."])

q(["Antti Hyvarinen won Finland's first Olympic ski jumping gold in 1956. With what?", "A flatter, arms-back style", "Longer skis", "A new binding", "A V-shaped flight",
   "The Norwegians thought the style ugly and unsporting, and his team-mate Aulis Kallakorpi took silver with it the same day."],
  ["Antti Hyvärinen voitti Suomen ensimmäisen mäkihypyn olympiakullan 1956. Millä?", "Matalammalla, kädet taakse -tyylillä", "Pidemmillä suksilla", "Uudella siteellä", "V-tyylillä",
   "Norjalaiset pitivät tyyliä rumana ja epäurheilijamaisena, ja tallikaveri Aulis Kallakorpi otti sillä hopeaa samana päivänä."])

q(["Marja-Liisa Hamalainen won three cross-country golds at Sarajevo in 1984. What was Finland's fourth gold there?", "The large hill ski jump", "The men's relay", "The biathlon", "Speed skating",
   "Matti Nykanen won it, and Finland came away from those Games with thirteen medals in all."],
  ["Marja-Liisa Hämäläinen voitti kolme hiihtokultaa Sarajevossa 1984. Mikä oli Suomen neljäs kulta siellä?", "Suurmäen mäkihyppy", "Miesten viesti", "Ampumahiihto", "Pikaluistelu",
   "Matti Nykänen voitti sen, ja Suomi toi noista kisoista kaikkiaan kolmetoista mitalia."])

q(["Toni Nieminen set a record at the 1992 Winter Olympics that still stands. Which record?", "Youngest male champion", "Longest jump", "Most golds at one Games", "Youngest competitor",
   "He was sixteen years and 259 days old when he won the large hill, and no younger man has won a Winter Olympic title since."],
  ["Toni Nieminen teki vuoden 1992 talviolympialaisissa ennätyksen, joka on yhä voimassa. Minkä?", "Nuorin miesten olympiavoittaja", "Pisin hyppy", "Eniten kultia yksissä kisoissa", "Nuorin osallistuja",
   "Hän oli kuusitoistavuotias ja 259 päivää voittaessaan suurmäen, eikä nuorempi mies ole sen jälkeen voittanut talviolympiakultaa."])

q(["Samppa Lajunen won three golds at Salt Lake City in 2002 and then did what?", "Retired at 25", "Switched to ski jumping", "Became a coach", "Was banned",
   "He had won the sprint, the individual and the team Nordic combined, and quit two years later saying there was nothing left to win."],
  ["Samppa Lajunen voitti kolme kultaa Salt Lake Cityssä 2002 ja teki sitten mitä?", "Lopetti 25-vuotiaana", "Siirtyi mäkihyppyyn", "Ryhtyi valmentajaksi", "Sai kilpailukiellon",
   "Hän oli voittanut yhdistetyn sprintin, henkilökohtaisen kilpailun ja joukkuekilpailun ja lopetti kaksi vuotta myöhemmin todeten ettei voitettavaa ollut."])

q(["Janne Lahtela's 2002 Olympic gold was Finland's first on skis away from which two sports?", "Cross-country and ski jumping", "Biathlon and combined", "Alpine and freestyle", "Combined and relay",
   "He won the moguls, and until then every Finnish Olympic skiing medal had come from the tracks or the hills."],
  ["Janne Lahtelan vuoden 2002 olympiakulta oli Suomen ensimmäinen suksilla minkä kahden lajin ulkopuolelta?", "Maastohiihdon ja mäkihypyn", "Ampumahiihdon ja yhdistetyn", "Alppihiihdon ja freestylen", "Yhdistetyn ja viestin",
   "Hän voitti kumparelaskun, ja siihen asti jokainen suomalainen olympiahiihtomitali oli tullut ladulta tai mäestä."])

q(["Mika Myllyla won the Olympic cross-country gold of 1998 over which distance?", "30 kilometres", "15 kilometres", "50 kilometres", "10 kilometres",
   "Three years later he was one of six Finns caught in the doping scandal at the Lahti world championships, and Finnish skiing never regained its standing."],
  ["Mika Myllylä voitti maastohiihdon olympiakullan 1998. Millä matkalla?", "30 kilometrin", "15 kilometrin", "50 kilometrin", "10 kilometrin",
   "Kolme vuotta myöhemmin hän oli yksi kuudesta Lahden MM-kisojen dopingkäryyn joutuneesta suomalaisesta, eikä Suomen hiihto palannut entiseen arvoonsa."])

# ------------------------------------------------- Ice hockey world champions
q(["In which country did Finland win its first ice hockey world championship, in 1995?", "Sweden", "Finland", "Austria", "Czech Republic",
   "Taking it in the neighbour's own capital made the homecoming in Helsinki bigger than the final; the market square filled with a hundred thousand people."],
  ["Missä maassa Suomi voitti ensimmäisen jääkiekon maailmanmestaruutensa vuonna 1995?", "Ruotsissa", "Suomessa", "Itävallassa", "Tšekissä",
   "Mestaruus naapurin omassa pääkaupungissa teki kotiinpaluusta suuremman kuin finaalista; Kauppatori täyttyi sadastatuhannesta ihmisestä."])

q(["By how many goals did Finland beat Sweden in the 2011 ice hockey world championship final?", "Five", "One", "Two", "Three",
   "The final went 6-1, the heaviest beating in a world championship final for decades, and the tournament was played in Slovakia."],
  ["Kuinka monen maalin erolla Suomi kaatoi Ruotsin vuoden 2011 jääkiekon MM-finaalissa?", "Viiden", "Yhden", "Kahden", "Kolmen",
   "Finaali päättyi 6-1, raskaimpaan tappioon MM-finaalissa vuosikymmeniin, ja turnaus pelattiin Slovakiassa."])

q(["Finland won the 2022 ice hockey world championship at home. In which city was the final played?", "Tampere", "Helsinki", "Turku", "Oulu",
   "It was settled in overtime against Canada, in an arena that had opened only months before."],
  ["Suomi voitti vuoden 2022 jääkiekon MM-kullan kotonaan. Missä kaupungissa finaali pelattiin?", "Tampereella", "Helsingissä", "Turussa", "Oulussa",
   "Se ratkesi jatkoajalla Kanadaa vastaan hallissa, joka oli avattu vain kuukausia aiemmin."])

q(["Finland won the 2019 ice hockey world championship with almost no NHL players. Whom did it beat in the final?", "Canada", "Sweden", "Russia", "Czech Republic",
   "The squad was built out of Liiga players and young professionals, and it won 3-1 in Bratislava against a team of stars."],
  ["Suomi voitti vuoden 2019 jääkiekon maailmanmestaruuden lähes ilman NHL-pelaajia. Kenet se kaatoi finaalissa?", "Kanadan", "Ruotsin", "Venäjän", "Tšekin",
   "Joukkue koottiin Liiga-pelaajista ja nuorista ammattilaisista, ja se voitti 3-1 Bratislavassa tähtijoukkuetta vastaan."])

q(["Finland first reached an ice hockey world championship final in 1992. Who beat it there?", "Sweden", "Canada", "Russia", "Czechoslovakia",
   "The final in Prague went 5-2 against Finland, and the first gold came only three years afterwards."],
  ["Suomi pääsi ensimmäisen kerran jääkiekon MM-finaaliin vuonna 1992. Kuka kaatoi sen siellä?", "Ruotsi", "Kanada", "Venäjä", "Tšekkoslovakia",
   "Finaali Prahassa päättyi 5-2 Suomen tappioon, ja ensimmäinen kulta tuli vasta kolme vuotta myöhemmin."])

q(["Which Finnish city staged an ice hockey world championship for the first time, in 1965?", "Tampere", "Helsinki", "Turku", "Lahti",
   "The Soviet Union won it there, one of nine world titles it took in a row between 1963 and 1971."],
  ["Mikä suomalainen kaupunki järjesti jääkiekon MM-kilpailut ensimmäisen kerran, vuonna 1965?", "Tampere", "Helsinki", "Turku", "Lahti",
   "Neuvostoliitto voitti siellä yhden niistä yhdeksästä perättäisestä mestaruudesta, jotka se otti 1963-1971."])

q(["Which country won nine ice hockey world championships in a row?", "Soviet Union", "Canada", "Sweden", "Czechoslovakia",
   "Nine from 1963 to 1971, and 22 world titles in all before the country ceased to exist."],
  ["Mikä maa voitti yhdeksän jääkiekon maailmanmestaruutta putkeen?", "Neuvostoliitto", "Kanada", "Ruotsi", "Tšekkoslovakia",
   "Yhdeksän vuosina 1963-1971, ja kaikkiaan 22 maailmanmestaruutta ennen kuin maa lakkasi olemasta."])

q(["The first ice hockey world championship, in 1920, was played as part of what?", "The Antwerp Summer Olympics", "A Canadian tour", "The Chamonix Winter Games", "A Swiss exhibition",
   "A winter sport was settled at a Summer Games, indoors in April, months before the rest of the Olympic programme."],
  ["Ensimmäinen jääkiekon maailmanmestaruusturnaus vuonna 1920 pelattiin minkä osana?", "Antwerpenin kesäolympialaisten", "Kanadan kiertueen", "Chamonix'n talvikisojen", "Sveitsiläisen näytöskilpailun",
   "Talvilaji ratkaistiin kesäkisoissa sisähallissa huhtikuussa, kuukausia ennen muuta olympiaohjelmaa."])

q(["Which country won the ice hockey world championship of 1936, the only time it ever has?", "Great Britain", "Switzerland", "Austria", "Germany",
   "Its team was built almost entirely from players raised in Canada who happened to hold British passports."],
  ["Mikä maa voitti jääkiekon maailmanmestaruuden 1936, ainoan kerran historiassaan?", "Iso-Britannia", "Sveitsi", "Itävalta", "Saksa",
   "Joukkue koottiin lähes kokonaan Kanadassa kasvaneista pelaajista, joilla satui olemaan brittipassi."])

q(["Which country broke the Soviet Union's run by winning the 1972 world championship at home in Prague?", "Czechoslovakia", "Sweden", "Poland", "Finland",
   "It was the first time in ten years that the Soviet Union had not won, and the crowd would not stop singing."],
  ["Mikä maa katkaisi Neuvostoliiton putken voittamalla vuoden 1972 MM-kullan kotonaan Prahassa?", "Tšekkoslovakia", "Ruotsi", "Puola", "Suomi",
   "Se oli ensimmäinen kerta kymmeneen vuoteen, kun Neuvostoliitto ei voittanut, eikä yleisö lopettanut laulamista."])

q(["Which country won its only ice hockey world championship in 2002, nine years after becoming independent?", "Slovakia", "Latvia", "Belarus", "Switzerland",
   "It beat Russia 4-3 in Gothenburg with a goal in the last two minutes of the final."],
  ["Mikä maa voitti ainoan jääkiekon maailmanmestaruutensa 2002, yhdeksän vuotta itsenäistymisensä jälkeen?", "Slovakia", "Latvia", "Valko-Venäjä", "Sveitsi",
   "Se kaatoi Venäjän 4-3 Göteborgissa maalilla, joka tuli kaksi minuuttia ennen finaalin loppua."])

# ------------------------------------------------- Finnish Formula One drivers
q(["Who was the first Finn to start a Formula One race, back in 1974?", "Leo Kinnunen", "Keke Rosberg", "Mikko Kozarowitzky", "JJ Lehto",
   "His only start was the Swedish Grand Prix, in a privately entered Surtees, and he retired after eight laps."],
  ["Kuka oli ensimmäinen suomalainen, joka starttasi formula ykkösten kilpailussa, jo vuonna 1974?", "Leo Kinnunen", "Keke Rosberg", "Mikko Kozarowitzky", "JJ Lehto",
   "Hänen ainoa lähtönsä oli Ruotsin osakilpailu yksityisellä Surteesilla, ja hän keskeytti kahdeksan kierroksen jälkeen."])

q(["One man on every list of Finnish Formula One drivers never started a race. Who?", "Mikko Kozarowitzky", "Leo Kinnunen", "Mika Salo", "JJ Lehto",
   "He entered two Grands Prix in 1977 and failed to qualify for both, so his whole career is two entries and no laps."],
  ["Yksi mies kaikilla suomalaisten F1-kuljettajien listoilla ei koskaan starttasi kilpailussa. Kuka?", "Mikko Kozarowitzky", "Leo Kinnunen", "Mika Salo", "JJ Lehto",
   "Hän ilmoittautui kahteen osakilpailuun 1977 eikä karsiutunut kumpaankaan, joten koko ura on kaksi ilmoittautumista ja nolla kierrosta."])

q(["How many Grands Prix did Keke Rosberg win in the season he became world champion?", "One", "Five", "Three", "Eight",
   "One was enough in 1982, a year in which eleven different drivers won a race; he won five in his whole career."],
  ["Kuinka monta osakilpailua Keke Rosberg voitti sillä kaudella, jolla hänestä tuli maailmanmestari?", "Yhden", "Viisi", "Kolme", "Kahdeksan",
   "Vuonna 1982 yksi riitti, sillä kauden aikana voitti yksitoista eri kuljettajaa; koko urallaan hän voitti viisi."])

q(["Which Finn was ordered to let his Ferrari team-mate past while leading the 1999 German Grand Prix?", "Mika Salo", "Mika Hakkinen", "JJ Lehto", "Heikki Kovalainen",
   "He was standing in for the injured Michael Schumacher, obeyed the order, and never won a race in 109 starts."],
  ["Kuka suomalainen sai käskyn päästää Ferrari-tallikaverinsa ohi johtaessaan vuoden 1999 Saksan osakilpailua?", "Mika Salo", "Mika Häkkinen", "JJ Lehto", "Heikki Kovalainen",
   "Hän tuurasi loukkaantunutta Michael Schumacheria, totteli käskyä eikä voittanut 109 lähdössään yhtäkään kilpailua."])

q(["By how many points did Kimi Raikkonen win the Formula One world championship of 2007?", "One", "Seven", "Twelve", "Twenty-two",
   "He had been seventeen points behind with two races to go, and the title was settled in the last half-hour of the season."],
  ["Kuinka monen pisteen erolla Kimi Räikkönen voitti formula ykkösten maailmanmestaruuden 2007?", "Yhden pisteen", "Seitsemän pisteen", "Kahdentoista pisteen", "Kahdenkymmenenkahden pisteen",
   "Hän oli ollut seitsemäntoista pistettä takana kaksi kilpailua ennen loppua, ja mestaruus ratkesi kauden viimeisellä puolituntisella."])

q(["Which Finn has driven more Formula One races than any other Finn?", "Kimi Raikkonen", "Valtteri Bottas", "Mika Hakkinen", "Keke Rosberg",
   "349 starts across two separate spells, with two years away driving rally cars in between them."],
  ["Kuka suomalainen on ajanut enemmän formula ykkösten kilpailuja kuin yksikään toinen suomalainen?", "Kimi Räikkönen", "Valtteri Bottas", "Mika Häkkinen", "Keke Rosberg",
   "349 lähtöä kahdessa eri jaksossa, ja välissä kaksi vuotta rallikuskina."])

q(["Heikki Kovalainen won exactly one Formula One race. Which one?", "Hungary 2008", "Monaco 2009", "Brazil 2007", "Italy 2010",
   "He inherited it when the leader's engine blew with three laps left; he was McLaren's second driver that season."],
  ["Heikki Kovalainen voitti täsmälleen yhden formula ykkösten kilpailun. Minkä?", "Unkarin 2008", "Monacon 2009", "Brasilian 2007", "Italian 2010",
   "Hän peri voiton, kun johtajan moottori räjähti kolme kierrosta ennen loppua; hän oli sen kauden McLarenin kakkoskuljettaja."])

q(["Nico Rosberg, son of a Finnish world champion, raced under which flag?", "Germany", "Finland", "Monaco", "Sweden",
   "He was born in Wiesbaden and brought up in Monaco, and chose his German mother's country over his father's."],
  ["Minkä maan lipun alla ajoi Nico Rosberg, suomalaisen maailmanmestarin poika?", "Saksan", "Suomen", "Monacon", "Ruotsin",
   "Hän syntyi Wiesbadenissa ja kasvoi Monacossa ja valitsi saksalaisen äitinsä maan isänsä maan sijasta."])

q(["Three Finns have won the Formula One world championship. Which of these has not?", "Valtteri Bottas", "Keke Rosberg", "Mika Hakkinen", "Kimi Raikkonen",
   "He was runner-up twice as team-mate to a seven-time champion, with ten Grand Prix wins and twenty poles to show for it."],
  ["Kolme suomalaista on voittanut formula ykkösten maailmanmestaruuden. Kuka näistä ei ole?", "Valtteri Bottas", "Keke Rosberg", "Mika Häkkinen", "Kimi Räikkönen",
   "Hän oli kahdesti toinen seitsenkertaisen mestarin tallikaverina, ja saldona on kymmenen osakilpailuvoittoa ja kaksikymmentä paalupaikkaa."])

# ------------------------------------------------- Tour de France before 2020
q(["The first Tour de France, in 1903, was made up of how many stages?", "Six", "Twelve", "Twenty-one", "Three",
   "Maurice Garin rode the 2,428 kilometres in just over 94 hours, and the race had been invented to sell newspapers."],
  ["Kuinka monta etappia ensimmäisessä Tour de Francessa vuonna 1903 oli?", "Kuusi", "Kaksitoista", "Kaksikymmentäyksi", "Kolme",
   "Maurice Garin ajoi 2 428 kilometriä runsaassa 94 tunnissa, ja kilpailu oli keksitty sanomalehden myynnin vauhdittamiseksi."])

q(["Which rider won the overall, the climbers' and the points competitions of one Tour de France?", "Eddy Merckx", "Bernard Hinault", "Jacques Anquetil", "Miguel Indurain",
   "He did it in 1969, the first of his five wins, and nobody has taken all three in one Tour since."],
  ["Kuka ajaja voitti saman Tour de Francen kokonaiskilpailun, mäkimiesten kilpailun ja pistekilpailun?", "Eddy Merckx", "Bernard Hinault", "Jacques Anquetil", "Miguel Induráin",
   "Hän teki sen 1969, ensimmäisellä viidestä voitostaan, eikä kukaan ole sen jälkeen ottanut kaikkia kolmea yhdessä Tourissa."])

q(["Four riders have won the Tour de France five times. Which of them won five in consecutive years?", "Miguel Indurain", "Eddy Merckx", "Jacques Anquetil", "Bernard Hinault",
   "1991 to 1995; the other three spread their wins out over longer careers, and he never lost the lead once he had it."],
  ["Neljä ajajaa on voittanut Tour de Francen viidesti. Kuka heistä voitti viisi perättäisinä vuosina?", "Miguel Induráin", "Eddy Merckx", "Jacques Anquetil", "Bernard Hinault",
   "Vuosina 1991-1995; kolme muuta hajauttivat voittonsa pidemmälle uralle, eikä hän menettänyt johtoa kerran saatuaan sen."])

q(["Who was the last French rider to win the Tour de France?", "Bernard Hinault", "Laurent Fignon", "Richard Virenque", "Thibaut Pinot",
   "He won in 1985, and no home rider has won since, by far the longest drought in the race's history."],
  ["Kuka oli viimeinen ranskalainen Tour de Francen voittaja?", "Bernard Hinault", "Laurent Fignon", "Richard Virenque", "Thibaut Pinot",
   "Hän voitti 1985, eikä yksikään kotimainen ajaja ole voittanut sen jälkeen, mikä on kilpailun historian selvästi pisin kuivuus."])

q(["Which Tour de France winner was shot by accident while hunting and came back to win twice more?", "Greg LeMond", "Bernard Hinault", "Stephen Roche", "Pedro Delgado",
   "He took a shotgun blast in the back and side in 1987 and won the 1989 Tour by eight seconds, the narrowest margin ever."],
  ["Kuka Tour de Francen voittaja sai vahingossa laukauksen metsällä ja palasi voittamaan vielä kaksi kertaa?", "Greg LeMond", "Bernard Hinault", "Stephen Roche", "Pedro Delgado",
   "Hän sai haulikonlaukauksen selkään ja kylkeen 1987 ja voitti vuoden 1989 Tourin kahdeksalla sekunnilla, kaikkien aikojen niukimmalla erolla."])

q(["Gino Bartali's two Tour de France wins are the furthest apart in history. How many years lie between?", "Ten", "Four", "Fifteen", "Six",
   "He won in 1938 and 1948; the war took most of the gap, and he spent part of it smuggling forged papers in his bicycle frame."],
  ["Gino Bartalin kaksi Tour de France -voittoa ovat historian kaukaisimmat toisistaan. Montako vuotta väliin jää?", "Kymmenen", "Neljä", "Viisitoista", "Kuusi",
   "Hän voitti 1938 ja 1948; sota vei suurimman osan välistä, ja osan siitä hän kuljetti väärennettyjä papereita pyörän rungossa."])

q(["Lance Armstrong's seven Tour de France titles were struck from the record. Who got them instead?", "Nobody", "The runners-up", "His team-mates", "The climbers' winners",
   "The organisers decided those years should simply stand empty, so the official list of winners has seven blank lines in it."],
  ["Lance Armstrongin seitsemän Tour de France -voittoa pyyhittiin tuloksista. Kuka sai ne?", "Ei kukaan", "Kakkossijoittuneet", "Hänen tallikaverinsa", "Mäkikilpailujen voittajat",
   "Järjestäjät päättivät jättää nuo vuodet tyhjiksi, joten virallisessa voittajalistassa on seitsemän tyhjää riviä."])

q(["Which rider won the Giro d'Italia, the Tour de France and the world road race title all in 1987?", "Stephen Roche", "Eddy Merckx", "Greg LeMond", "Pedro Delgado",
   "Only Eddy Merckx had managed the treble before him, and nobody has managed it since."],
  ["Kuka ajaja voitti Giro d'Italian, Tour de Francen ja maantieajon maailmanmestaruuden kaikki vuonna 1987?", "Stephen Roche", "Eddy Merckx", "Greg LeMond", "Pedro Delgado",
   "Vain Eddy Merckx oli tehnyt kolmoisvoiton ennen häntä, eikä kukaan sen jälkeen."])

q(["What cut short the decisive mountain stage of the 2019 Tour de France?", "A hailstorm", "A protest", "A crash", "A landslide",
   "Hail and mud buried the road, the stage was stopped, and Egan Bernal became the first Colombian winner at the age of 22."],
  ["Mikä katkaisi vuoden 2019 Tour de Francen ratkaisevan vuoristoetapin?", "Rakeet", "Mielenosoitus", "Kolari", "Maanvyöry",
   "Rakeet ja muta hautasivat tien, etappi pysäytettiin, ja Egan Bernalista tuli 22-vuotiaana ensimmäinen kolumbialainen voittaja."])

q(["Bradley Wiggins was the first British winner of the Tour de France. What did he win ten days later?", "Olympic time trial gold", "The Vuelta", "A world title", "The Giro",
   "The 2012 Tour finished on 22 July and the London Olympic time trial was on 1 August, which he won on home roads."],
  ["Bradley Wiggins oli ensimmäinen brittiläinen Tour de Francen voittaja. Minkä hän voitti kymmenen päivää myöhemmin?", "Olympialaisten aika-ajon kullan", "Vueltan", "Maailmanmestaruuden", "Giron",
   "Vuoden 2012 Tour päättyi 22. heinäkuuta ja Lontoon olympia-aika-ajo oli 1. elokuuta; sen hän voitti kotiteillä."])

q(["The 2006 Tour de France winner lost the title to a failed test. Who was given it instead?", "Oscar Pereiro", "Carlos Sastre", "Alberto Contador", "Andy Schleck",
   "He had been let into a breakaway nobody bothered to chase, gained nearly half an hour, and lost most of it again in the Alps."],
  ["Vuoden 2006 Tour de Francen voittaja menetti tittelin dopingtestiin. Kenelle se annettiin?", "Óscar Pereirolle", "Carlos Sastrelle", "Alberto Contadorille", "Andy Schleckille",
   "Hänet oli päästetty karkuryhmään jota kukaan ei jahdannut, hän sai lähes puoli tuntia ja menetti siitä valtaosan Alpeilla."])

q(["Bjarne Riis admitted doping after winning the 1996 Tour de France. What is his official status?", "Still the winner", "Stripped of the win", "Second place", "Removed from the list",
   "The organisers no longer treat him as the winner, but the cycling union never changed the result, so his name is still in the record book."],
  ["Bjarne Riis myönsi dopingin voitettuaan vuoden 1996 Tour de Francen. Mikä on hänen virallinen asemansa?", "Yhä voittaja", "Voitto riistetty", "Toinen sija", "Poistettu listalta",
   "Järjestäjät eivät enää pidä häntä voittajana, mutta pyöräilyliitto ei muuttanut tulosta, joten nimi on yhä tilastoissa."])

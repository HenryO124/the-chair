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
q(["In which sport did Verner Weckman take Finland's first ever Olympic gold, in 1908?", "Wrestling", "Athletics", "Shooting", "Gymnastics",
   "Finland was still a Grand Duchy of Russia, and its athletes were not allowed a flag of their own at those Games."],
  ["Missä lajissa Verner Weckman voitti Suomen kaikkien ensimmäisen olympiakullan vuonna 1908?", "Paini", "Yleisurheilu", "Ampuminen", "Voimistelu",
   "Suomi oli yhä Venäjän suuriruhtinaskunta, eivätkä sen urheilijat saaneet noissa kisoissa omaa lippua."])

q(["Hannes Kolehmainen won three golds in 1912 on the track. Which title did he add in 1920?", "The marathon", "The 1500 metres", "The steeplechase", "The 800 metres",
   "He won it by thirteen seconds, the narrowest Olympic marathon margin for 76 years, on a course measured 42.75 km."],
  ["Hannes Kolehmainen voitti kolme kultaa radalla 1912. Minkä mestaruuden hän lisäsi vuonna 1920?", "Maratonin", "1500 metrin", "Estejuoksun", "800 metrin",
   "Hän voitti kolmellatoista sekunnilla, olympiamaratonin niukimmalla erolla 76 vuoteen, ja matka oli mitattu 42,75 kilometriksi."])

q(["Which Finn won four golds in Paris in 1924 and another in Amsterdam in 1928?", "Ville Ritola", "Hannes Kolehmainen", "Volmari Iso-Hollo", "Albin Stenroos",
   "He had emigrated to New York and only started running seriously at 25, after seeing a Finnish club's meeting there."],
  ["Kuka suomalainen voitti neljä kultaa Pariisissa 1924 ja vielä yhden Amsterdamissa 1928?", "Ville Ritola", "Hannes Kolehmainen", "Volmari Iso-Hollo", "Albin Stenroos",
   "Hän oli muuttanut New Yorkiin ja alkoi juosta tosissaan vasta 25-vuotiaana nähtyään siellä suomalaisen seuran kilpailut."])

q(["In which sport did Clas Thunberg win five Olympic golds for Finland in the 1920s?", "Speed skating", "Cross-country skiing", "Ski jumping", "Nordic combined",
   "He had never raced abroad before his first Games, and he won all five of his golds after turning thirty."],
  ["Missä lajissa Clas Thunberg voitti Suomelle viisi olympiakultaa 1920-luvulla?", "Pikaluistelu", "Maastohiihto", "Mäkihyppy", "Yhdistetty",
   "Hän ei ollut kilpaillut ulkomailla ennen ensimmäisiä kisojaan, ja kaikki viisi kultaa tulivat kolmenkymmenen ikävuoden jälkeen."])

q(["Which Finn won the Olympic javelin gold in 1932, in a family of throwers?", "Matti Jarvinen", "Jonni Myyra", "Armas Taipale", "Pauli Nevala",
   "He broke the world record ten times, and the Helsinki Olympic Stadium tower was built to the height of his best throw."],
  ["Kuka suomalainen voitti keihäänheiton olympiakullan 1932 heittäjäsuvun jäsenenä?", "Matti Järvinen", "Jonni Myyrä", "Armas Taipale", "Pauli Nevala",
   "Hän rikkoi maailmanennätyksen kymmenen kertaa, ja Helsingin olympiastadionin tornin korkeus mitattiin hänen parhaan heittonsa mukaan."])

q(["Which Finn won the Olympic decathlon in Amsterdam in 1928?", "Paavo Yrjola", "Akilles Jarvinen", "Volmari Iso-Hollo", "Matti Jarvinen",
   "He trained alone on his farm in Hauho and set a world record in winning, with no coach at all."],
  ["Kuka suomalainen voitti kymmenottelun olympiakullan Amsterdamissa 1928?", "Paavo Yrjölä", "Akilles Järvinen", "Volmari Iso-Hollo", "Matti Järvinen",
   "Hän harjoitteli yksin maatilallaan Hauholla ja teki voittaessaan maailmanennätyksen täysin ilman valmentajaa."])

q(["Which Finn won the Olympic steeplechase in both 1932 and 1936?", "Volmari Iso-Hollo", "Lauri Lehtinen", "Gunnar Hockert", "Ilmari Salminen",
   "In the 1932 final a lap counter lost track and the field ran 3460 metres instead of 3000, and his time was never ratified."],
  ["Kuka suomalainen voitti estejuoksun olympiakullan sekä 1932 että 1936?", "Volmari Iso-Hollo", "Lauri Lehtinen", "Gunnar Höckert", "Ilmari Salminen",
   "Vuoden 1932 finaalissa kierroslaskija unohti kierroksen ja juostiin 3460 metriä, joten aikaa ei koskaan hyväksytty."])

q(["Which Finnish boxer won an Olympic gold in front of a home crowd in 1952?", "Pentti Hamalainen", "Sten Suvio", "Olli Maki", "Risto Luukkonen",
   "Finland has won Olympic boxing gold exactly twice, and this was the second; Sten Suvio had taken the first in Berlin."],
  ["Kuka suomalainen nyrkkeilijä voitti olympiakultaa kotiyleisön edessä vuonna 1952?", "Pentti Hämäläinen", "Sten Suvio", "Olli Mäki", "Risto Luukkonen",
   "Suomi on voittanut nyrkkeilyn olympiakultaa täsmälleen kahdesti, ja tämä oli toinen; Sten Suvio otti ensimmäisen Berliinissä."])

q(["Sylvi Saimo won Olympic gold at Helsinki in 1952. In which sport?", "Canoeing", "Rowing", "Swimming", "Shooting",
   "She was 38 years old and is still the only Finnish woman to have won an Olympic canoeing title."],
  ["Sylvi Saimo voitti olympiakultaa Helsingissä 1952. Missä lajissa?", "Melonta", "Soutu", "Uinti", "Ampuminen",
   "Hän oli 38-vuotias ja on yhä ainoa suomalainen nainen, joka on voittanut melonnan olympiakultaa."])

q(["In which sport did Pentti Linnosvuo win Olympic gold in 1956 and again in 1964?", "Shooting", "Wrestling", "Archery", "Fencing",
   "He won with the free pistol first and the rapid-fire pistol eight years later, two very different events."],
  ["Missä lajissa Pentti Linnosvuo voitti olympiakultaa 1956 ja uudelleen 1964?", "Ampuminen", "Paini", "Jousiammunta", "Miekkailu",
   "Hän voitti ensin vapaapistoolilla ja kahdeksan vuotta myöhemmin isopistoolin pikalaukauksilla, kahdessa hyvin erilaisessa lajissa."])

q(["Which Finn won the Olympic 1500 metres in Munich in 1972?", "Pekka Vasala", "Lasse Viren", "Juha Vaatainen", "Martti Vainio",
   "He beat the Kenyan favourite Kipchoge Keino with a last lap of 53 seconds after sitting at the back for 1200 metres."],
  ["Kuka suomalainen voitti 1500 metrin olympiakullan Münchenissä 1972?", "Pekka Vasala", "Lasse Virén", "Juha Väätäinen", "Martti Vainio",
   "Hän kaatoi kenialaisen ennakkosuosikin Kipchoge Keinon 53 sekunnin loppukierroksella oltuaan 1200 metriä takajoukoissa."])

q(["Which Finn won Olympic gold in rowing at three Games in a row from 1976?", "Pertti Karppinen", "Esko Rechardt", "Tomi Poikolainen", "Kaarlo Kangasniemi",
   "He was a fireman from Vehmaa, two metres tall, and won the single sculls in 1976, 1980 and 1984."],
  ["Kuka suomalainen voitti soudun olympiakultaa kolmissa kisoissa putkeen vuodesta 1976?", "Pertti Karppinen", "Esko Rechardt", "Tomi Poikolainen", "Kaarlo Kangasniemi",
   "Hän oli kaksimetrinen palomies Vehmaalta ja voitti yksikköjen kilpailun 1976, 1980 ja 1984."])

q(["Finland won two athletics golds at Los Angeles in 1984. Juha Tiainen won which event?", "The hammer throw", "The javelin", "The shot put", "The discus",
   "Arto Harkonen took the javelin at the same Games; they are Finland's last two Olympic men's throwing golds."],
  ["Suomi voitti kaksi yleisurheilukultaa Los Angelesissa 1984. Minkä lajin Juha Tiainen voitti?", "Moukarinheiton", "Keihäänheiton", "Kuulantyönnön", "Kiekonheiton",
   "Arto Härkönen voitti samoissa kisoissa keihään; nämä ovat Suomen kaksi viimeisintä miesten heittolajien olympiakultaa."])

q(["Which Finn won the Olympic javelin gold at Seoul in 1988?", "Tapio Korjus", "Arto Harkonen", "Seppo Raty", "Kimmo Kinnunen",
   "He threw his winning mark on the very last attempt of the competition, by 16 centimetres."],
  ["Kuka suomalainen voitti keihäänheiton olympiakullan Seoulissa 1988?", "Tapio Korjus", "Arto Härkönen", "Seppo Räty", "Kimmo Kinnunen",
   "Hän heitti voittotuloksensa kilpailun aivan viimeisellä yrityksellä, 16 senttimetrin erolla."])

q(["Heli Rantanen became the first Finnish woman to win Olympic athletics gold in 1996. In which event?", "The javelin", "The shot put", "The 10,000 metres", "The high jump",
   "Her first throw of the final was the winning one, and she then watched eleven rivals fail to pass it."],
  ["Heli Rantanen oli ensimmäinen suomalainen nainen, joka voitti yleisurheilun olympiakultaa 1996. Missä lajissa?", "Keihäänheitossa", "Kuulantyönnössä", "10 000 metrillä", "Korkeushypyssä",
   "Finaalin ensimmäinen heitto oli voittoheitto, ja hän katsoi sitten yhdentoista kilpakumppanin yrittävän turhaan ohi."])

q(["Which Finn won the Olympic shot put at Sydney in 2000?", "Arsi Harju", "Timo Aaltonen", "Ville Porhola", "Conny Karlsson",
   "He was a short thrower among giants and won the competition with his very first put of the final."],
  ["Kuka suomalainen voitti kuulantyönnön olympiakullan Sydneyssä 2000?", "Arsi Harju", "Timo Aaltonen", "Ville Pörhölä", "Conny Karlsson",
   "Hän oli lyhyt työntäjä jättiläisten joukossa ja voitti kilpailun finaalin ensimmäisellä työnnöllään."])

q(["Satu Makela-Nummela won Finland's most recent Summer Olympic gold, in 2008. In which sport?", "Shooting", "Sailing", "Rowing", "Wrestling",
   "No Finn has won a Summer Olympic gold since; the count has stood still through Rio, Tokyo and Paris."],
  ["Satu Mäkelä-Nummela voitti Suomen tuoreimman kesäolympiakullan vuonna 2008. Missä lajissa?", "Ampuminen", "Purjehdus", "Soutu", "Paini",
   "Yksikään suomalainen ei ole voittanut kesäolympiakultaa sen jälkeen; luku on seisonut Rion, Tokion ja Pariisin läpi."])

q(["Lydia Wideman won Finland's first women's Winter Olympic gold in 1952. In which sport?", "Cross-country skiing", "Figure skating", "Speed skating", "Alpine skiing",
   "Women's cross-country skiing was in the Olympics for the first time that year, over a single 10-kilometre race."],
  ["Lydia Wideman voitti Suomen ensimmäisen naisten talviolympiakullan 1952. Missä lajissa?", "Maastohiihto", "Taitoluistelu", "Pikaluistelu", "Alppihiihto",
   "Naisten maastohiihto oli silloin ensi kerran olympialaisissa, ja ohjelmassa oli vain yksi kymmenen kilometrin kilpailu."])

q(["Which Finn won the first Olympic ski jumping gold for Finland, at Cortina in 1956?", "Antti Hyvarinen", "Veikko Kankkonen", "Jouko Tormanen", "Matti Nykanen",
   "He and his team-mate took gold and silver with a new flatter, arms-back style that the Norwegians called ugly."],
  ["Kuka suomalainen voitti Suomen ensimmäisen mäkihypyn olympiakullan Cortinassa 1956?", "Antti Hyvärinen", "Veikko Kankkonen", "Jouko Törmänen", "Matti Nykänen",
   "Hän ja joukkuekaverinsa veivät kullan ja hopean uudella matalammalla tyylillä, jota norjalaiset pitivät rumana."])

q(["Which Finnish ski jumper won the large hill gold at Lake Placid in 1980?", "Jouko Tormanen", "Matti Nykanen", "Pentti Kokkonen", "Jari Puikkonen",
   "It was Finland's only gold of those Games, which otherwise brought five silvers and three bronzes."],
  ["Kuka suomalainen mäkihyppääjä voitti suurmäen olympiakullan Lake Placidissa 1980?", "Jouko Törmänen", "Matti Nykänen", "Pentti Kokkonen", "Jari Puikkonen",
   "Se oli Suomen ainoa kulta noissa kisoissa, joista tuli sen lisäksi viisi hopeaa ja kolme pronssia."])

q(["Which Finnish woman won three cross-country skiing golds at Sarajevo in 1984?", "Marja-Liisa Hamalainen", "Marjo Matikainen", "Helena Takalo", "Marjut Lukkarinen",
   "She won every individual women's race at those Games, and Finland's fourth gold there came from Matti Nykanen on the large hill."],
  ["Kuka suomalainen nainen voitti kolme maastohiihdon kultaa Sarajevossa 1984?", "Marja-Liisa Hämäläinen", "Marjo Matikainen", "Helena Takalo", "Marjut Lukkarinen",
   "Hän voitti kaikki naisten henkilökohtaiset matkat, ja Suomen neljäs kulta tuli Matti Nykäsen suurmäestä."])

q(["Which Finn became the youngest male Winter Olympic champion by winning the large hill in 1992?", "Toni Nieminen", "Matti Nykanen", "Janne Ahonen", "Jani Soininen",
   "He was sixteen years and 259 days old, and the record has stood ever since."],
  ["Kuka suomalainen nousi nuorimmaksi talviolympiavoittajaksi miehissä voittamalla suurmäen 1992?", "Toni Nieminen", "Matti Nykänen", "Janne Ahonen", "Jani Soininen",
   "Hän oli kuusitoistavuotias ja 259 päivää, ja ennätys on pitänyt siitä asti."])

q(["Which Finn won three Nordic combined golds at Salt Lake City in 2002?", "Samppa Lajunen", "Hannu Manninen", "Jaakko Tallus", "Heikki Hasu",
   "He won the sprint, the individual and the team event, and retired two years later at 25."],
  ["Kuka suomalainen voitti kolme yhdistetyn kultaa Salt Lake Cityssä 2002?", "Samppa Lajunen", "Hannu Manninen", "Jaakko Tallus", "Heikki Hasu",
   "Hän voitti sprintin, henkilökohtaisen kilpailun ja joukkuekilpailun ja lopetti kaksi vuotta myöhemmin 25-vuotiaana."])

q(["Janne Lahtela won an Olympic gold in 2002 in which sport?", "Freestyle skiing", "Snowboarding", "Ski jumping", "Biathlon",
   "His event was the moguls, and Finland had never before won a medal on skis that were not cross-country or jumping."],
  ["Janne Lahtela voitti olympiakultaa 2002. Missä lajissa?", "Freestylehiihto", "Lumilautailu", "Mäkihyppy", "Ampumahiihto",
   "Laji oli kumpare, ja Suomi ei ollut aiemmin voittanut mitalia suksilla muualla kuin maastossa tai mäessä."])

q(["Which Finn won the Olympic 50 km classical cross-country title at Pyeongchang in 2018?", "Iivo Niskanen", "Matti Heikkinen", "Sami Jauhojarvi", "Mika Myllyla",
   "He led from the start and won by eighteen seconds in a race that lasted over two hours."],
  ["Kuka suomalainen voitti 50 kilometrin perinteisen olympiakullan Pyeongchangissa 2018?", "Iivo Niskanen", "Matti Heikkinen", "Sami Jauhojärvi", "Mika Myllylä",
   "Hän johti alusta loppuun ja voitti kahdeksallatoista sekunnilla yli kaksi tuntia kestäneessä kilpailussa."])

q(["Mika Myllyla won an Olympic cross-country gold in 1998 over which distance?", "30 kilometres", "15 kilometres", "50 kilometres", "10 kilometres",
   "The next year he won several golds at the Ramsau world championships, and the Lahti doping scandal of 2001 ended his career."],
  ["Mika Myllylä voitti maastohiihdon olympiakullan 1998. Millä matkalla?", "30 kilometriä", "15 kilometriä", "50 kilometriä", "10 kilometriä",
   "Seuraavana vuonna hän voitti Ramsaun MM-kisoissa useita kultia, ja vuoden 2001 Lahden dopingskandaali päätti hänen uransa."])

# ------------------------------------------------- Ice hockey world champions
q(["In which country was the ice hockey world championship held when Finland first won it, in 1995?", "Sweden", "Finland", "Austria", "Czech Republic",
   "Winning it in the neighbours' capital made the homecoming parade in Helsinki bigger than the final itself."],
  ["Missä maassa jääkiekon MM-kilpailut pidettiin, kun Suomi voitti ne ensimmäisen kerran 1995?", "Ruotsi", "Suomi", "Itävalta", "Tšekki",
   "Mestaruuden voittaminen naapurin pääkaupungissa teki Helsingin kotiinpaluujuhlasta suuremman kuin itse finaalin."])

q(["Finland won its second ice hockey world title in 2011. In which country?", "Slovakia", "Sweden", "Germany", "Latvia",
   "The final against Sweden ended 6-1, the heaviest beating in a world championship final for decades."],
  ["Suomi voitti toisen jääkiekon maailmanmestaruutensa 2011. Missä maassa?", "Slovakiassa", "Ruotsissa", "Saksassa", "Latviassa",
   "Finaali Ruotsia vastaan päättyi 6-1, raskaimpaan tappioon MM-finaalissa vuosikymmeniin."])

q(["Finland won the 2022 ice hockey world championship on home ice. In which city was the final?", "Tampere", "Helsinki", "Turku", "Oulu",
   "The final against Canada was settled in overtime in an arena that had opened only months before."],
  ["Suomi voitti vuoden 2022 jääkiekon MM-kullan kotijäällä. Missä kaupungissa finaali pelattiin?", "Tampereella", "Helsingissä", "Turussa", "Oulussa",
   "Finaali Kanadaa vastaan ratkesi jatkoajalla hallissa, joka oli avattu vain kuukausia aiemmin."])

q(["Which country did Finland beat in the 2019 ice hockey world championship final?", "Canada", "Sweden", "Russia", "Czech Republic",
   "Finland went into that tournament without a single NHL star and beat Canada 3-1 in Bratislava."],
  ["Minkä maan Suomi kaatoi vuoden 2019 jääkiekon MM-finaalissa?", "Kanadan", "Ruotsin", "Venäjän", "Tšekin",
   "Suomi meni turnaukseen ilman yhtäkään NHL-tähteä ja kaatoi Kanadan 3-1 Bratislavassa."])

q(["Which Finnish city hosted the ice hockey world championship for the first time, in 1965?", "Tampere", "Helsinki", "Turku", "Lahti",
   "The Soviet Union won there, one of the nine world titles in a row it took between 1963 and 1971."],
  ["Mikä suomalainen kaupunki järjesti jääkiekon MM-kilpailut ensimmäisen kerran vuonna 1965?", "Tampere", "Helsinki", "Turku", "Lahti",
   "Neuvostoliitto voitti siellä yhden niistä yhdeksästä perättäisestä mestaruudesta, jotka se otti vuosina 1963-1971."])

q(["Which country won the ice hockey world championship in 1992, the year Finland first took silver?", "Sweden", "Russia", "Canada", "Czechoslovakia",
   "Finland lost that final 5-2 in Prague and then had to wait three more years for a gold of its own."],
  ["Mikä maa voitti jääkiekon maailmanmestaruuden 1992, vuonna jolloin Suomi otti ensimmäisen hopeansa?", "Ruotsi", "Venäjä", "Kanada", "Tšekkoslovakia",
   "Suomi hävisi finaalin 5-2 Prahassa ja joutui sitten odottamaan omaa kultaa vielä kolme vuotta."])

q(["Which country won its only ice hockey world championship in 2002?", "Slovakia", "Latvia", "Germany", "Switzerland",
   "It beat Russia 4-3 in Gothenburg, nine years after the country became independent."],
  ["Mikä maa voitti ainoan jääkiekon maailmanmestaruutensa vuonna 2002?", "Slovakia", "Latvia", "Saksa", "Sveitsi",
   "Se kaatoi Venäjän 4-3 Göteborgissa, yhdeksän vuotta maan itsenäistymisen jälkeen."])

q(["Which country won the ice hockey world championship of 1993, its first under a new name?", "Russia", "Czech Republic", "Slovakia", "Ukraine",
   "The Soviet Union had won 22 world titles; its successor has managed five since."],
  ["Mikä maa voitti jääkiekon maailmanmestaruuden 1993, ensimmäisen uudella nimellään?", "Venäjä", "Tšekki", "Slovakia", "Ukraina",
   "Neuvostoliitto oli voittanut 22 maailmanmestaruutta; sen seuraaja on voittanut viisi sen jälkeen."])

q(["Which country won the ice hockey world championship at home in Prague in 1972?", "Czechoslovakia", "Soviet Union", "Sweden", "Poland",
   "It was the first time in ten years that the Soviet Union had not won, and the crowd sang for twenty minutes."],
  ["Mikä maa voitti jääkiekon maailmanmestaruuden kotikisoissa Prahassa 1972?", "Tšekkoslovakia", "Neuvostoliitto", "Ruotsi", "Puola",
   "Se oli ensimmäinen kerta kymmeneen vuoteen, kun Neuvostoliitto ei voittanut, ja yleisö lauloi kaksikymmentä minuuttia."])

q(["Which country won the ice hockey world championship in 1936, the only time it has done so?", "Great Britain", "Switzerland", "Austria", "Germany",
   "Its team was mostly Canadian-raised players with British passports, and the title came at the Garmisch Olympics."],
  ["Mikä maa voitti jääkiekon maailmanmestaruuden 1936, ainoan kerran historiassaan?", "Iso-Britannia", "Sveitsi", "Itävalta", "Saksa",
   "Joukkue koostui lähinnä Kanadassa kasvaneista pelaajista brittipassilla, ja mestaruus tuli Garmischin olympialaisissa."])

q(["Which country won the ice hockey world championship of 1963, the start of a nine-year run?", "Soviet Union", "Canada", "Sweden", "Czechoslovakia",
   "Nine titles in a row from 1963 to 1971 is the longest winning streak in the tournament's history."],
  ["Mikä maa voitti jääkiekon maailmanmestaruuden 1963 ja aloitti yhdeksän vuoden putken?", "Neuvostoliitto", "Kanada", "Ruotsi", "Tšekkoslovakia",
   "Yhdeksän perättäistä mestaruutta 1963-1971 on turnauksen historian pisin voittoputki."])

q(["Which country won the first ice hockey world championship, in 1920?", "Canada", "United States", "Sweden", "Czechoslovakia",
   "It was played as part of the Antwerp Summer Olympics, on an indoor rink in April, before the Games proper."],
  ["Mikä maa voitti ensimmäisen jääkiekon maailmanmestaruuden vuonna 1920?", "Kanada", "Yhdysvallat", "Ruotsi", "Tšekkoslovakia",
   "Turnaus pelattiin Antwerpenin kesäolympialaisten osana sisähallissa huhtikuussa, ennen varsinaisia kisoja."])

q(["In which Finnish city was the 1974 ice hockey world championship held?", "Helsinki", "Tampere", "Turku", "Jyvaskyla",
   "The Soviet Union won it, and this was the second time Finland had staged the tournament, after Tampere in 1965."],
  ["Missä suomalaisessa kaupungissa pidettiin vuoden 1974 jääkiekon MM-kilpailut?", "Helsingissä", "Tampereella", "Turussa", "Jyväskylässä",
   "Neuvostoliitto voitti, ja Suomi järjesti turnauksen tällöin toisen kerran, Tampereen 1965 jälkeen."])

q(["Which country won the ice hockey world championship in 2024?", "Czechia", "Switzerland", "Sweden", "Canada",
   "The final was played in Prague, where the home side had not won the title since 2010."],
  ["Mikä maa voitti jääkiekon maailmanmestaruuden 2024?", "Tšekki", "Sveitsi", "Ruotsi", "Kanada",
   "Finaali pelattiin Prahassa, jossa isäntämaa ei ollut voittanut mestaruutta vuoden 2010 jälkeen."])

q(["Which country won the ice hockey world championship of 1998, in Switzerland?", "Sweden", "Finland", "Czech Republic", "Canada",
   "Finland took the silver, one of five it collected in the ten years between 1992 and 2001."],
  ["Mikä maa voitti jääkiekon maailmanmestaruuden 1998 Sveitsissä?", "Ruotsi", "Suomi", "Tšekki", "Kanada",
   "Suomi otti hopean, yhden niistä viidestä, jotka se keräsi vuosina 1992-2001."])

# ------------------------------------------------- Finnish F1 drivers
q(["Who was the first Finnish driver to start a Formula One race, back in 1974?", "Leo Kinnunen", "Keke Rosberg", "Mikko Kozarowitzky", "JJ Lehto",
   "His single start came at the Swedish Grand Prix, where he retired after eight laps in a privately entered Surtees."],
  ["Kuka oli ensimmäinen suomalainen, joka starttasi formula ykkösten kilpailussa, jo vuonna 1974?", "Leo Kinnunen", "Keke Rosberg", "Mikko Kozarowitzky", "JJ Lehto",
   "Hänen ainoa lähtönsä oli Ruotsin osakilpailussa, jossa hän keskeytti kahdeksan kierroksen jälkeen yksityisellä Surteesilla."])

q(["Which Finn has started more Formula One Grands Prix than any other, with 349?", "Kimi Raikkonen", "Mika Hakkinen", "Valtteri Bottas", "Keke Rosberg",
   "He raced in two separate spells, left for rallying in between, and came back after two years away."],
  ["Kuka suomalainen on ajanut enemmän formula ykkösten osakilpailuja kuin kukaan muu maanmiehensä?", "Kimi Räikkönen", "Mika Häkkinen", "Valtteri Bottas", "Keke Rosberg",
   "Hän ajoi kahdessa jaksossa, lähti välissä rallin pariin ja palasi kahden vuoden tauon jälkeen."])

q(["In which year did Kimi Raikkonen win his Formula One world title?", "2007", "2005", "2009", "2012",
   "He took it by one point at the last race in Brazil after trailing by seventeen with two rounds left."],
  ["Minä vuonna Kimi Räikkönen voitti formula ykkösten maailmanmestaruutensa?", "Vuonna 2007", "Vuonna 2005", "Vuonna 2009", "Vuonna 2012",
   "Hän otti sen yhdellä pisteellä kauden viimeisessä kilpailussa Brasiliassa, vaikka oli kahta osakilpailua ennen seitsemäntoista pisteen takamatkalla."])

q(["Which Finnish driver won the Hungarian Grand Prix of 2008, his only Formula One win?", "Heikki Kovalainen", "Mika Salo", "JJ Lehto", "Valtteri Bottas",
   "He got it after the leader's engine blew with three laps left, and he was McLaren's number two driver that year."],
  ["Kuka suomalaiskuljettaja voitti Unkarin osakilpailun 2008, ainoan formula ykkösvoittonsa?", "Heikki Kovalainen", "Mika Salo", "JJ Lehto", "Valtteri Bottas",
   "Hän sai sen, kun johtajan moottori räjähti kolme kierrosta ennen loppua, ja hän oli sinä vuonna McLarenin kakkoskuljettaja."])

q(["How many Formula One Grand Prix wins did Keke Rosberg take in his career?", "Five", "One", "Twelve", "Twenty",
   "He won the 1982 championship with a single win all season, the same tally Mike Hawthorn managed in 1958."],
  ["Montako formula ykkösten osakilpailuvoittoa Keke Rosberg otti urallaan?", "Viisi", "Yhden", "Kaksitoista", "Kaksikymmentä",
   "Hän voitti vuoden 1982 mestaruuden yhdellä ainoalla kausivoitolla, samalla saldolla kuin Mike Hawthorn 1958."])

q(["Which Finn stood in at Ferrari in 1999 and took the only two podiums of his Formula One career?", "Mika Salo", "JJ Lehto", "Heikki Kovalainen", "Leo Kinnunen",
   "He led in Germany and was ordered to let Eddie Irvine past, handing away what would have been his first win."],
  ["Kuka suomalainen tuurasi Ferrarilla 1999 ja otti uransa kaksi ainoaa palkintokorokesijaa?", "Mika Salo", "JJ Lehto", "Heikki Kovalainen", "Leo Kinnunen",
   "Hän johti Saksassa ja sai käskyn päästää Eddie Irvinen ohi, jolloin ensimmäinen voitto jäi saamatta."])

q(["Three Finns have won the Formula One world championship. Who is NOT one of them?", "Valtteri Bottas", "Keke Rosberg", "Mika Hakkinen", "Kimi Raikkonen",
   "He finished runner-up twice as team-mate to a seven-time champion but never led the standings at the end of a year."],
  ["Kolme suomalaista on voittanut formula ykkösten maailmanmestaruuden. Kuka ei ole heistä?", "Valtteri Bottas", "Keke Rosberg", "Mika Häkkinen", "Kimi Räikkönen",
   "Hän oli kahdesti toinen seitsenkertaisen mestarin tallikaverina mutta ei johtanut sarjaa yhdenkään kauden päättyessä."])

q(["Nico Rosberg, son of a Finnish world champion, raced under which flag?", "Germany", "Finland", "Monaco", "Sweden",
   "He was born in Wiesbaden and grew up in Monaco, and he chose his mother's country rather than his father's."],
  ["Minkä maan lipun alla ajoi Nico Rosberg, suomalaisen maailmanmestarin poika?", "Saksan", "Suomen", "Monacon", "Ruotsin",
   "Hän syntyi Wiesbadenissa ja kasvoi Monacossa, ja hän valitsi äitinsä maan isänsä maan sijasta."])

q(["Which Finnish driver entered two Formula One races in 1977 but failed to qualify for either?", "Mikko Kozarowitzky", "Leo Kinnunen", "Keke Rosberg", "Mika Salo",
   "He is in every list of Finnish Formula One drivers and has never started a lap of a Grand Prix."],
  ["Kuka suomalaiskuljettaja ilmoittautui kahteen formula ykkösten kilpailuun 1977 mutta ei karsiutunut mukaan kumpaankaan?", "Mikko Kozarowitzky", "Leo Kinnunen", "Keke Rosberg", "Mika Salo",
   "Hän on kaikissa suomalaisten F1-kuljettajien listoissa eikä ole ajanut yhtäkään kierrosta osakilpailussa."])

q(["Which Finn took 26 Formula One pole positions in the 1990s and after?", "Mika Hakkinen", "Keke Rosberg", "Mika Salo", "JJ Lehto",
   "Michael Schumacher later said he was the rival he respected most, and the two fought two championships out to the last races."],
  ["Kuka suomalainen otti 26 paalupaikkaa formula ykkösissä 1990-luvulla ja sen jälkeen?", "Mika Häkkinen", "Keke Rosberg", "Mika Salo", "JJ Lehto",
   "Michael Schumacher sanoi myöhemmin kunnioittaneensa häntä kilpakumppaneista eniten, ja kaksikko ratkoi kaksi mestaruutta viimeisiin kilpailuihin."])

# ------------------------------------------------- Tour de France before 2020
q(["Who won the very first Tour de France, in 1903?", "Maurice Garin", "Henri Cornet", "Lucien Petit-Breton", "Octave Lapize",
   "The race was invented to sell newspapers, had six stages, and he rode the 2,428 kilometres in just over 94 hours."],
  ["Kuka voitti kaikkien ensimmäisen Tour de Francen vuonna 1903?", "Maurice Garin", "Henri Cornet", "Lucien Petit-Breton", "Octave Lapize",
   "Kilpailu keksittiin myymään sanomalehtiä, siinä oli kuusi etappia, ja hän ajoi 2 428 kilometriä runsaassa 94 tunnissa."])

q(["Which Belgian won the Tour de France five times between 1969 and 1974?", "Eddy Merckx", "Lucien Van Impe", "Philippe Thys", "Firmin Lambot",
   "In 1969 he won the overall, the climbers' and the points competitions all at once, which nobody has done since."],
  ["Kuka belgialainen voitti Tour de Francen viidesti vuosina 1969-1974?", "Eddy Merckx", "Lucien Van Impe", "Philippe Thys", "Firmin Lambot",
   "Vuonna 1969 hän voitti kokonaiskilpailun, mäkimiesten ja pistekilpailun yhtä aikaa, mihin kukaan ei ole sen jälkeen pystynyt."])

q(["Which Spaniard won five Tours de France in a row, from 1991 to 1995?", "Miguel Indurain", "Pedro Delgado", "Federico Bahamontes", "Alberto Contador",
   "He is the only rider to have won five in consecutive years; Anquetil, Merckx and Hinault also won five, but not in a row."],
  ["Kuka espanjalainen voitti viisi Tour de Francea putkeen vuosina 1991-1995?", "Miguel Induráin", "Pedro Delgado", "Federico Bahamontes", "Alberto Contador",
   "Hän on ainoa viiden perättäisen voiton ajaja; Anquetil, Merckx ja Hinault voittivat myös viisi, mutta eivät putkeen."])

q(["Which Frenchman was the last home winner of the Tour de France, in 1985?", "Bernard Hinault", "Laurent Fignon", "Bernard Thevenet", "Richard Virenque",
   "No French rider has won it since, the longest drought the race has known in its own country."],
  ["Kuka ranskalainen oli viimeinen kotimainen Tour de Francen voittaja, vuonna 1985?", "Bernard Hinault", "Laurent Fignon", "Bernard Thévenet", "Richard Virenque",
   "Yksikään ranskalainen ei ole voittanut sen jälkeen, mikä on kilpailun pisin kuivuus omassa maassaan."])

q(["Who was the first American to win the Tour de France, in 1986?", "Greg LeMond", "Lance Armstrong", "Andy Hampsten", "Floyd Landis",
   "A year later he was shot by accident while turkey hunting and still came back to win twice more."],
  ["Kuka oli ensimmäinen amerikkalainen Tour de Francen voittaja, vuonna 1986?", "Greg LeMond", "Lance Armstrong", "Andy Hampsten", "Floyd Landis",
   "Vuotta myöhemmin hän sai vahingossa haulikon laukauksen kalkkunametsällä ja voitti silti vielä kaksi kertaa."])

q(["Which Frenchman won five Tours de France between 1957 and 1964?", "Jacques Anquetil", "Louison Bobet", "Roger Pingeon", "Antonin Magne",
   "He was the first rider to win five, and in 1964 he beat his rival Raymond Poulidor by 55 seconds."],
  ["Kuka ranskalainen voitti viisi Tour de Francea vuosina 1957-1964?", "Jacques Anquetil", "Louison Bobet", "Roger Pingeon", "Antonin Magne",
   "Hän oli ensimmäinen viiden voiton ajaja, ja 1964 hän päihitti kilpakumppaninsa Raymond Poulidorin 55 sekunnilla."])

q(["Which Italian won the Tour de France in 1938 and again ten years later, in 1948?", "Gino Bartali", "Fausto Coppi", "Ottavio Bottecchia", "Felice Gimondi",
   "The ten-year gap between wins is the longest in the race's history, and the war took most of it."],
  ["Kuka italialainen voitti Tour de Francen 1938 ja uudelleen kymmenen vuotta myöhemmin 1948?", "Gino Bartali", "Fausto Coppi", "Ottavio Bottecchia", "Felice Gimondi",
   "Kymmenen vuoden väli voittojen välissä on kilpailun historian pisin, ja sota vei siitä suurimman osan."])

q(["Lance Armstrong's seven Tour de France titles were struck from the record in 2012. Which years?", "1999-2005", "1996-2002", "2000-2006", "1998-2004",
   "The organisers decided not to award those years to anybody else, so the record books show seven blanks."],
  ["Lance Armstrongin seitsemän Tour de France -voittoa pyyhittiin tuloksista 2012. Mitkä vuodet?", "1999-2005", "1996-2002", "2000-2006", "1998-2004",
   "Järjestäjät päättivät olla antamatta noita vuosia kenellekään muulle, joten tilastoissa on seitsemän tyhjää kohtaa."])

q(["Who became the first British winner of the Tour de France, in 2012?", "Bradley Wiggins", "Chris Froome", "Geraint Thomas", "Mark Cavendish",
   "He went on to win an Olympic time trial gold ten days after that Tour finished."],
  ["Kuka oli ensimmäinen brittiläinen Tour de Francen voittaja, vuonna 2012?", "Bradley Wiggins", "Chris Froome", "Geraint Thomas", "Mark Cavendish",
   "Hän voitti olympialaisten aika-ajon kullan kymmenen päivää kyseisen Tourin päätyttyä."])

q(["Which Dane won the Tour de France in 1996 and later admitted doping?", "Bjarne Riis", "Jonas Vingegaard", "Rolf Sorensen", "Michael Rasmussen",
   "The organisers no longer count him as the winner, but the cycling union has never changed the official result."],
  ["Kuka tanskalainen voitti Tour de Francen 1996 ja myönsi myöhemmin dopingin?", "Bjarne Riis", "Jonas Vingegaard", "Rolf Sørensen", "Michael Rasmussen",
   "Järjestäjät eivät enää pidä häntä voittajana, mutta pyöräilyliitto ei ole koskaan muuttanut virallista tulosta."])

q(["Who was the first Irish winner of the Tour de France, in 1987?", "Stephen Roche", "Sean Kelly", "Shay Elliott", "Nicolas Roche",
   "That same year he also won the Giro d'Italia and the world road race title, a treble only one other rider has managed."],
  ["Kuka oli ensimmäinen irlantilainen Tour de Francen voittaja, vuonna 1987?", "Stephen Roche", "Sean Kelly", "Shay Elliott", "Nicolas Roche",
   "Samana vuonna hän voitti myös Giro d'Italian ja maantieajon maailmanmestaruuden, kolmoisvoiton johon vain yksi muu on pystynyt."])

q(["Who was the first Colombian to win the Tour de France, in 2019?", "Egan Bernal", "Nairo Quintana", "Rigoberto Uran", "Lucho Herrera",
   "He was 22, and a hailstorm cut the decisive stage short while he was in the lead on the climb."],
  ["Kuka oli ensimmäinen kolumbialainen Tour de Francen voittaja, vuonna 2019?", "Egan Bernal", "Nairo Quintana", "Rigoberto Urán", "Lucho Herrera",
   "Hän oli 22-vuotias, ja rakeet katkaisivat ratkaisevan etapin kesken, kun hän johti nousussa."])

q(["Which Australian won the Tour de France in 2011, the first from his country?", "Cadel Evans", "Richie Porte", "Phil Anderson", "Simon Gerrans",
   "He was 34 and had finished second twice before, and he took the lead for the first time on the final time trial."],
  ["Kuka australialainen voitti Tour de Francen 2011, ensimmäisenä maastaan?", "Cadel Evans", "Richie Porte", "Phil Anderson", "Simon Gerrans",
   "Hän oli 34-vuotias ja ollut aiemmin kahdesti toinen, ja hän nousi johtoon ensi kerran vasta päätösaika-ajossa."])

q(["Floyd Landis lost the 2006 Tour de France to a failed test. Who was given the title instead?", "Oscar Pereiro", "Carlos Sastre", "Alberto Contador", "Andy Schleck",
   "He had been allowed into a long breakaway nobody chased, gained half an hour, and lost it all again by the Alps."],
  ["Floyd Landis menetti vuoden 2006 Tour de Francen dopingtestiin. Kenelle voitto annettiin?", "Óscar Pereirolle", "Carlos Sastrelle", "Alberto Contadorille", "Andy Schleckille",
   "Hänet oli päästetty pitkään karkuryhmään jota kukaan ei jahdannut, hän sai puoli tuntia ja menetti sen Alpeilla."])

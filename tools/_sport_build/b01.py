# -*- coding: utf-8 -*-
# Batch 1: Olympic Games (summer + winter hosts), World Cup finals, F1 champions
# Every row must survive the test: when the answer is revealed, somebody says
# "I didn't know that." Plain year-to-city recall was cut.
# Sources:
#  https://en.wikipedia.org/wiki/List_of_Olympic_Games_host_cities
#  https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals
#  https://en.wikipedia.org/wiki/List_of_Formula_One_World_Drivers%27_Champions
Q = []
def q(en, fi):
    Q.append((["Sport"] + list(en), ["Sport"] + list(fi)))

# ------------------------------------------------------------------ Olympic Games
q(["At which Olympics did women compete for the first time?", "Paris 1900", "Athens 1896", "St. Louis 1904", "London 1908",
   "Twenty-two women took part among nearly a thousand men, in golf, tennis, croquet and sailing, and several did not know they were in the Olympics at all."],
  ["Missä olympialaisissa naiset kilpailivat ensimmäisen kerran?", "Pariisi 1900", "Ateena 1896", "St. Louis 1904", "Lontoo 1908",
   "Mukana oli 22 naista lähes tuhannen miehen joukossa golfissa, tenniksessä, krokeetissa ja purjehduksessa, eivätkä kaikki tienneet kilpailevansa olympialaisissa."])

q(["The 1904 Olympics were awarded to Chicago and then taken away. Which city got them?", "St. Louis", "New York", "Boston", "Philadelphia",
   "St. Louis was staging a World's Fair and threatened to run a rival sports festival, so the Games were simply moved to it."],
  ["Vuoden 1904 olympialaiset myönnettiin Chicagolle ja otettiin sitten pois. Mikä kaupunki sai ne?", "St. Louis", "New York", "Boston", "Philadelphia",
   "St. Louis järjesti maailmannäyttelyn ja uhkasi panna pystyyn kilpailevat urheilukisat, joten kisat vain siirrettiin sinne."])

q(["Rome gave up the 1908 Olympics after Mount Vesuvius erupted. Which city took them on?", "London", "Paris", "Berlin", "Stockholm",
   "The Italian money went to rebuilding Naples instead, and London put the Games together in under two years."],
  ["Rooma luopui vuoden 1908 olympialaisista Vesuviuksen purkauksen jälkeen. Mikä kaupunki otti ne?", "Lontoo", "Pariisi", "Berliini", "Tukholma",
   "Italian rahat menivät Napolin jälleenrakennukseen, ja Lontoo kokosi kisat alle kahdessa vuodessa."])

q(["At which Games did an Olympic flame first burn in the stadium?", "Amsterdam 1928", "Antwerp 1920", "Berlin 1936", "Los Angeles 1932",
   "It burned in the tower by the marathon gate; the torch relay from Olympia was only invented eight years later."],
  ["Missä kisoissa olympiatuli paloi ensimmäisen kerran stadionilla?", "Amsterdam 1928", "Antwerpen 1920", "Berliini 1936", "Los Angeles 1932",
   "Tuli paloi maratonportin tornissa, ja soihtuviesti Olympiasta keksittiin vasta kahdeksan vuotta myöhemmin."])

q(["At which Games was the Olympic flag flown for the first time?", "Antwerp 1920", "Stockholm 1912", "Paris 1924", "Amsterdam 1928",
   "Germany, Austria, Hungary, Bulgaria and Turkey were not invited to those first Games after the war."],
  ["Missä kisoissa olympialippu liehui ensimmäisen kerran?", "Antwerpen 1920", "Tukholma 1912", "Pariisi 1924", "Amsterdam 1928",
   "Saksaa, Itävaltaa, Unkaria, Bulgariaa ja Turkkia ei kutsuttu näihin ensimmäisiin kisoihin sodan jälkeen."])

q(["In which year was Olympic competition shown on television for the first time?", "1936", "1948", "1956", "1964",
   "Pictures from Berlin were piped to about twenty-five viewing halls around the city; nobody had a set at home."],
  ["Minä vuonna olympiakilpailuja näytettiin televisiossa ensimmäisen kerran?", "Vuonna 1936", "Vuonna 1948", "Vuonna 1956", "Vuonna 1964",
   "Kuvaa Berliinistä vietiin noin kahteenkymmeneenviiteen katselusaliin kaupungilla; kenelläkään ei ollut kotona vastaanotinta."])

q(["Tokyo gave up the 1940 Olympics. Which capital was to take over before they were cancelled?", "Helsinki", "Stockholm", "Oslo", "Rome",
   "The stadium was built and the tickets printed; the war took the Games and the city had to wait another twelve years."],
  ["Tokio luopui vuoden 1940 olympialaisista. Mihin pääkaupunkiin ne siirrettiin ennen peruutusta?", "Helsinki", "Tukholma", "Oslo", "Rooma",
   "Stadion rakennettiin ja liput painettiin, mutta sota vei kisat ja kaupunki sai odottaa vielä kaksitoista vuotta."])

q(["At the 1956 Melbourne Olympics, one sport was contested 15,000 km away in Stockholm. Which?", "Equestrian", "Sailing", "Shooting", "Rowing",
   "Australian quarantine law would not let foreign horses in, so the riders went to Sweden five months before the rest of the Games."],
  ["Melbournen 1956 olympialaisissa yksi laji kilpailtiin 15 000 kilometrin päässä Tukholmassa. Mikä?", "Ratsastus", "Purjehdus", "Ampuminen", "Soutu",
   "Australian karanteenilaki ei päästänyt ulkomaisia hevosia maahan, joten ratsastajat matkasivat Ruotsiin viisi kuukautta ennen muita kisoja."])

q(["Who won the 1960 Olympic marathon through the streets of Rome, running barefoot?", "Abebe Bikila", "Emil Zatopek", "Alain Mimoun", "Mamo Wolde",
   "An Ethiopian palace guard, he won again in Tokyo four years later, in shoes, forty days after an appendix operation."],
  ["Kuka voitti vuoden 1960 olympiamaratonin Rooman kaduilla paljain jaloin?", "Abebe Bikila", "Emil Zátopek", "Alain Mimoun", "Mamo Wolde",
   "Etiopialainen palatsinkaartin sotilas voitti uudelleen Tokiossa neljä vuotta myöhemmin, kengissä, neljäkymmentä päivää umpilisäkkeen poiston jälkeen."])

q(["Which Olympic host opened a new high-speed railway days before the Games began?", "Tokyo 1964", "Seoul 1988", "Munich 1972", "Barcelona 1992",
   "The Tokaido Shinkansen cut the journey to Osaka almost in half and was built largely to move Olympic crowds."],
  ["Mikä olympiajärjestäjä avasi uuden luotijunaradan päiviä ennen kisojen alkua?", "Tokio 1964", "Seoul 1988", "München 1972", "Barcelona 1992",
   "Tokaido-Shinkansen puolitti matka-ajan Osakaan ja rakennettiin pitkälti olympiayleisöä varten."])

q(["Waldi the dachshund was the first official mascot of which Olympics?", "Munich 1972", "Montreal 1976", "Moscow 1980", "Los Angeles 1984",
   "West Germany wanted something cheerful after 1936 and chose a rainbow-striped sausage dog; every Games has had a mascot since."],
  ["Mäyräkoira Waldi oli ensimmäinen virallinen maskotti missä olympialaisissa?", "München 1972", "Montreal 1976", "Moskova 1980", "Los Angeles 1984",
   "Länsi-Saksa halusi jotain iloista vuoden 1936 jälkeen ja valitsi sateenkaariraidallisen makkarakoiran; siitä lähtien joka kisoilla on ollut maskotti."])

q(["Which Olympic host city took thirty years to pay off its main stadium?", "Montreal", "Athens", "Sochi", "Sarajevo",
   "The debt from 1976 was cleared only in 2006, and locals had nicknamed the unfinished tower the Big Owe."],
  ["Mikä olympiakaupunki maksoi päästadioninsa velkaa kolmekymmentä vuotta?", "Montreal", "Ateena", "Sotši", "Sarajevo",
   "Vuoden 1976 velka maksettiin loppuun vasta 2006, ja paikalliset olivat ristineet keskeneräisen tornin Isoksi laskuksi."])

q(["Some teams at the 1980 Moscow Olympics marched under which flag instead of their own?", "The Olympic flag", "A white flag", "The United Nations flag", "No flag at all",
   "Sixty-odd countries stayed away over Afghanistan, and several that came would not show their own colours."],
  ["Jotkin joukkueet marssivat Moskovan 1980 olympialaisissa oman lippunsa sijasta minkä lipun alla?", "Olympialipun", "Valkoisen lipun", "YK:n lipun", "Ilman lippua",
   "Runsaat kuusikymmentä maata jäi kokonaan pois Afganistanin takia, eivätkä kaikki saapuneet halunneet näyttää omia värejään."])

q(["How was the cauldron lit at the opening of the 1992 Barcelona Olympics?", "With a flaming arrow", "With a laser beam", "By a diver", "By a hot-air balloon",
   "A Paralympic archer shot it over the rim in front of 65,000 people, and the arrow landed in the stadium moat."],
  ["Miten olympiamalja sytytettiin Barcelonan 1992 kisojen avajaisissa?", "Liekehtivällä nuolella", "Lasersäteellä", "Sukeltajan toimesta", "Kuumailmapallolla",
   "Paralympiajousiampuja ampui nuolen maljan yli 65 000 katsojan edessä, ja nuoli putosi stadionin vallihautaan."])

q(["Which sport returned to the Olympic programme in 2016 after 112 years away?", "Golf", "Rugby sevens", "Baseball", "Tennis",
   "It had last been played in 1904; several of the world's best players skipped Rio anyway, citing the Zika virus."],
  ["Mikä laji palasi olympiaohjelmaan vuonna 2016 sadan ja kahdentoista vuoden tauon jälkeen?", "Golf", "Rugby seven", "Baseball", "Tennis",
   "Lajia oli pelattu viimeksi 1904, ja osa maailman parhaista pelaajista jätti Rion silti väliin vedoten zikavirukseen."])

q(["At the 2004 Athens Olympics one event was staged in the ancient stadium at Olympia. Which?", "The shot put", "The marathon", "The discus", "The javelin",
   "It was thrown on grass with no seating, the crowd sitting on the banks as spectators did two and a half thousand years ago."],
  ["Ateenan 2004 olympialaisissa yksi laji kilpailtiin muinaisella Olympian stadionilla. Mikä?", "Kuulantyöntö", "Maraton", "Kiekonheitto", "Keihäänheitto",
   "Laji kilpailtiin ruoholla ilman katsomoita, ja yleisö istui rinteillä kuten kaksi ja puoli tuhatta vuotta sitten."])

q(["Which city was the first to host both a Summer and a Winter Olympics?", "Beijing", "Tokyo", "Los Angeles", "Innsbruck",
   "It had the Summer Games in 2008 and the Winter Games in 2022, which were run almost entirely on artificial snow."],
  ["Mikä kaupunki järjesti ensimmäisenä sekä kesä- että talviolympialaiset?", "Peking", "Tokio", "Los Angeles", "Innsbruck",
   "Kesäkisat olivat 2008 ja talvikisat 2022, ja jälkimmäiset hiihdettiin lähes kokonaan keinolumella."])

q(["Which sport made its Olympic debut at Garmisch-Partenkirchen in 1936?", "Alpine skiing", "Ski jumping", "Biathlon", "Luge",
   "Ski instructors were ruled professionals and barred, so Switzerland and Austria boycotted the event in protest."],
  ["Mikä laji nähtiin ensimmäisen kerran olympialaisissa Garmisch-Partenkirchenissä 1936?", "Alppihiihto", "Mäkihyppy", "Ampumahiihto", "Rattikelkkailu",
   "Hiihdonopettajat luokiteltiin ammattilaisiksi ja kiellettiin, joten Sveitsi ja Itävalta boikotoivat lajia vastalauseena."])

q(["The 1952 Winter Olympic flame was not lit in Greece. Where was it lit?", "A cottage hearth in Norway", "A glacier in Switzerland", "A volcano in Iceland", "A cathedral in Oslo",
   "It was lit in Morgedal, in the fireplace of the house where Sondre Norheim, the father of modern skiing, grew up."],
  ["Vuoden 1952 talviolympiatulta ei sytytetty Kreikassa. Missä se sytytettiin?", "Norjalaisen talon takassa", "Sveitsin jäätiköllä", "Islannin tulivuorella", "Oslon katedraalissa",
   "Tuli sytytettiin Morgedalissa sen talon takassa, jossa nykyhiihdon isä Sondre Norheim kasvoi."])

q(["Which Winter Olympics were the first at which drug and sex tests were carried out?", "Grenoble 1968", "Sapporo 1972", "Innsbruck 1976", "Lake Placid 1980",
   "They were also the first Winter Games broadcast in colour, so viewers could finally tell the teams apart."],
  ["Mitkä talviolympialaiset olivat ensimmäiset, joissa tehtiin doping- ja sukupuolitestejä?", "Grenoble 1968", "Sapporo 1972", "Innsbruck 1976", "Lake Placid 1980",
   "Ne olivat myös ensimmäiset väreissä lähetetyt talvikisat, joten katsojat erottivat vihdoin joukkueet toisistaan."])

q(["Colorado voters refused to pay for the 1976 Winter Olympics. Which city took them instead?", "Innsbruck", "Lake Placid", "Sapporo", "Grenoble",
   "Denver is the only host in Olympic history to have handed the Games back after winning them."],
  ["Coloradon äänestäjät kielsivät maksamasta vuoden 1976 talviolympialaisia. Mikä kaupunki otti ne?", "Innsbruck", "Lake Placid", "Sapporo", "Grenoble",
   "Denver on olympiahistorian ainoa järjestäjä, joka on palauttanut kisat sen jälkeen kun oli ne voittanut."])

q(["Which American village of a few thousand people has hosted two Winter Olympics?", "Lake Placid", "Aspen", "Park City", "Squaw Valley",
   "It staged the Games in 1932 and 1980, more than New York, Chicago and Boston have managed between them."],
  ["Mikä parin tuhannen asukkaan amerikkalainen kylä on järjestänyt kahdet talviolympialaiset?", "Lake Placid", "Aspen", "Park City", "Squaw Valley",
   "Kisat olivat siellä 1932 ja 1980, enemmän kuin New York, Chicago ja Boston yhteensä."])

q(["Bobsleigh was dropped from one Winter Olympics for lack of entries. Which Games?", "Squaw Valley 1960", "Oslo 1952", "Cortina 1956", "Innsbruck 1964",
   "Only nine countries entered, so the organisers refused to build a track at all, the only Winter Games without the sport since 1924."],
  ["Rattikelkkailu jätettiin yksistä talviolympialaisista pois osallistujien puutteessa. Mistä kisoista?", "Squaw Valley 1960", "Oslo 1952", "Cortina 1956", "Innsbruck 1964",
   "Vain yhdeksän maata ilmoittautui, joten järjestäjät kieltäytyivät rakentamasta rataa lainkaan."])

q(["After which Games did the Winter Olympics stop sharing a year with the Summer ones?", "Albertville 1992", "Calgary 1988", "Lillehammer 1994", "Sarajevo 1984",
   "The next Winter Games came after only two years, to put the two Olympics on alternating even years."],
  ["Minkä kisojen jälkeen talviolympialaiset lakkasivat osumasta samaan vuoteen kesäkisojen kanssa?", "Albertville 1992", "Calgary 1988", "Lillehammer 1994", "Sarajevo 1984",
   "Seuraavat talvikisat tulivat vain kahden vuoden päästä, jotta kisat saatiin vuorottelemaan parillisina vuosina."])

q(["Which sport was added to the Winter Olympics at Nagano in 1998?", "Snowboarding", "Freestyle skiing", "Short track", "Curling",
   "The first halfpipe champion lost his gold over a cannabis test and got it back when it turned out the drug was not on the banned list."],
  ["Mikä laji lisättiin talviolympialaisiin Naganossa 1998?", "Lumilautailu", "Freestylehiihto", "Pikaluistelun lyhyt rata", "Curling",
   "Ensimmäinen halfpipe-mestari menetti kultansa kannabistestiin ja sai sen takaisin, kun aine ei sittenkään ollut kiellettyjen listalla."])

q(["Which Winter Olympic host was so warm that snow had to be brought in by lorry and helicopter?", "Vancouver 2010", "Sochi 2014", "Turin 2006", "Nagano 1998",
   "It is the warmest city ever to have staged a Winter Games, and the freestyle hill was built on straw bales under trucked-in snow."],
  ["Mikä talviolympiajärjestäjä oli niin lämmin, että lunta tuotiin rekoilla ja helikoptereilla?", "Vancouver 2010", "Sotši 2014", "Torino 2006", "Nagano 1998",
   "Se on lämpimin koskaan talvikisat järjestänyt kaupunki, ja freestylerinne rakennettiin olkipaalien päälle tuodun lumen alle."])

q(["The bobsleigh track and ski jumps of which Winter Olympics stand in ruins today?", "Sarajevo 1984", "Grenoble 1968", "Albertville 1992", "Sochi 2014",
   "They were shelled during the siege of the city eight years after the Games, and the bob run is now covered in graffiti."],
  ["Minkä talviolympialaisten rattikelkkarata ja hyppyrimäet ovat nykyään raunioina?", "Sarajevo 1984", "Grenoble 1968", "Albertville 1992", "Sotši 2014",
   "Niitä ammuttiin kaupungin piirityksessä kahdeksan vuotta kisojen jälkeen, ja rata on nyt graffitien peitossa."])

q(["At which Winter Olympics did North and South Korea put out a joint women's ice hockey team?", "Pyeongchang 2018", "Sochi 2014", "Beijing 2022", "Nagano 1998",
   "They also marched in together under a unification flag, and the combined team lost all five of its matches."],
  ["Missä talviolympialaisissa Pohjois- ja Etelä-Korea kokosivat yhteisen naisten jääkiekkojoukkueen?", "Pyeongchang 2018", "Sotši 2014", "Peking 2022", "Nagano 1998",
   "Maat marssivat myös yhdessä sisään yhdistymislipun alla, ja yhteisjoukkue hävisi kaikki viisi otteluaan."])

# ------------------------------------------------------------------ World Cup
q(["The 1930 champions refused to come back and defend the trophy in 1934. Who were they?", "Uruguay", "Italy", "Argentina", "Brazil",
   "It was still angry that most European teams had not bothered to sail to Montevideo four years earlier."],
  ["Vuoden 1930 mestarit kieltäytyivät tulemasta puolustamaan pokaalia 1934. Ketkä he olivat?", "Uruguay", "Italia", "Argentiina", "Brasilia",
   "Maa oli yhä katkera siitä, etteivät useimmat eurooppalaiset joukkueet olleet vaivautuneet Montevideoon neljä vuotta aiemmin."])

q(["Which was the first country to win two football World Cups in a row?", "Italy", "Brazil", "Uruguay", "West Germany",
   "It won in 1934 and 1938, and nobody repeated the double until Brazil in 1958 and 1962."],
  ["Mikä maa voitti ensimmäisenä kaksi jalkapallon maailmanmestaruutta putkeen?", "Italia", "Brasilia", "Uruguay", "Länsi-Saksa",
   "Se voitti 1934 ja 1938, eikä kukaan toistanut temppua ennen Brasiliaa vuosina 1958 ja 1962."])

q(["The 1950 football World Cup had no final match. How was the winner decided?", "By a four-team group", "By a coin toss", "By goal difference", "By a replay",
   "Brazil needed only a draw in the last game and lost 2-1 to Uruguay in front of some two hundred thousand people."],
  ["Vuoden 1950 jalkapallon MM-kilpailuissa ei ollut finaalia. Miten voittaja ratkesi?", "Neljän joukkueen lohkossa", "Kolikonheitolla", "Maalierolla", "Uusintaottelulla",
   "Brasilialle riitti viimeisestä pelistä tasapeli, ja se hävisi 1-2 Uruguaylle noin kahdensadantuhannen katsojan edessä."])

q(["Which team was unbeaten for four years, beat its opponents 8-3 in the group, and still lost the 1954 final?", "Hungary", "Austria", "Brazil", "Uruguay",
   "West Germany won the final 3-2 in the rain in Bern, and Hungary never won a World Cup at all."],
  ["Mikä joukkue oli ollut neljä vuotta häviötön, voitti vastustajansa 8-3 ja hävisi silti 1954 finaalin?", "Unkari", "Itävalta", "Brasilia", "Uruguay",
   "Länsi-Saksa voitti finaalin 3-2 sateessa Bernissä, eikä Unkari voittanut koskaan maailmanmestaruutta."])

q(["How old was Pele when he scored twice in the World Cup final of 1958?", "Seventeen", "Nineteen", "Twenty-one", "Sixteen",
   "He is still the youngest man to have played in a World Cup final, let alone won one, and he cried on the pitch afterwards."],
  ["Kuinka vanha Pelé oli, kun hän teki kaksi maalia vuoden 1958 MM-finaalissa?", "Seitsemäntoista", "Yhdeksäntoista", "Kaksikymmentäyksi", "Kuusitoista",
   "Hän on yhä nuorin MM-finaalissa pelannut ja sen voittanut mies, ja hän purskahti kentällä kyyneliin."])

q(["The World Cup trophy was stolen in England in 1966. What found it a week later?", "A dog", "A child", "A dustman", "A policeman",
   "A mongrel called Pickles sniffed out a newspaper parcel under a hedge in south London; he got a year's free dog food."],
  ["MM-pokaali varastettiin Englannissa 1966. Mikä löysi sen viikkoa myöhemmin?", "Koira", "Lapsi", "Roskakuski", "Poliisi",
   "Pickles-nimineen sekarotuinen koira nuuski sanomalehtikäärön pensaan alta Lontoossa ja sai palkkioksi vuoden koiranruoat."])

q(["Why did Brazil get to keep the original World Cup trophy outright in 1970?", "It had won three times", "It had hosted twice", "It paid for it", "It won every match",
   "The solid gold cup was stolen from a cabinet in Rio in 1983 and has never been found; it was probably melted down."],
  ["Miksi Brasilia sai pitää alkuperäisen MM-pokaalin omanaan vuonna 1970?", "Se oli voittanut kolmesti", "Se oli isäntänä kahdesti", "Se maksoi pokaalin", "Se voitti kaikki pelinsä",
   "Umpikultainen pokaali varastettiin Rion vitriinistä 1983, eikä sitä ole löydetty; se luultavasti sulatettiin."])

q(["In the 1974 final the Netherlands scored before a German had touched the ball. Who won the match?", "West Germany", "The Netherlands", "Brazil", "Poland",
   "Johan Neeskens converted a penalty after eighty seconds, and the Dutch did not score again; they lost 2-1."],
  ["Vuoden 1974 finaalissa Hollanti teki maalin ennen kuin yksikään saksalainen oli koskenut palloon. Kuka voitti?", "Länsi-Saksa", "Hollanti", "Brasilia", "Puola",
   "Johan Neeskens teki rangaistuspotkumaalin 80 sekunnin kohdalla, eikä Hollanti tehnyt enää toista; tappio oli 1-2."])

q(["Which player returned from a two-year betting ban to win the 1982 World Cup golden boot?", "Paolo Rossi", "Karl-Heinz Rummenigge", "Zbigniew Boniek", "Michel Platini",
   "He had scored nothing in the first four matches and then scored six in three, including a hat-trick against Brazil."],
  ["Kuka pelaaja palasi kahden vuoden vedonlyöntipannasta ja voitti vuoden 1982 MM-maalikuninkuuden?", "Paolo Rossi", "Karl-Heinz Rummenigge", "Zbigniew Boniek", "Michel Platini",
   "Hän ei tehnyt neljässä ensimmäisessä ottelussa mitään ja teki sitten kuusi maalia kolmessa, niistä kolme Brasiliaa vastaan."])

q(["Against which team did Maradona score the Hand of God goal in 1986?", "England", "Belgium", "Uruguay", "West Germany",
   "Four minutes later he beat half the same team on a sixty-metre run to score what a FIFA poll called the goal of the century."],
  ["Mitä joukkuetta vastaan Maradona teki Jumalan käden maalin vuonna 1986?", "Englantia", "Belgiaa", "Uruguayta", "Länsi-Saksaa",
   "Neljä minuuttia myöhemmin hän ohitti puolet samasta joukkueesta 60 metrin juoksulla ja teki maalin, jota FIFA on kutsunut vuosisadan maaliksi."])

q(["Which country won the football World Cup in 1990 and stopped existing under that name months later?", "West Germany", "Czechoslovakia", "Soviet Union", "Yugoslavia",
   "The final was in July and the country was reunified in October, so the title is held by a state that no longer exists."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1990 ja lakkasi kuukausia myöhemmin olemasta sillä nimellä?", "Länsi-Saksa", "Tšekkoslovakia", "Neuvostoliitto", "Jugoslavia",
   "Finaali oli heinäkuussa ja maa yhdistyi lokakuussa, joten mestaruus kuuluu valtiolle jota ei enää ole."])

q(["Which was the first World Cup final to be decided by a penalty shoot-out?", "1994", "1982", "1990", "2006",
   "Roberto Baggio put the last kick over the bar in Pasadena after a goalless two hours in brutal heat."],
  ["Mikä MM-finaali ratkesi ensimmäisenä rangaistuspotkukilpailulla?", "Vuoden 1994", "Vuoden 1982", "Vuoden 1990", "Vuoden 2006",
   "Roberto Baggio ampui viimeisen laukauksen yli Pasadenassa maalittoman kahden tunnin ja armottoman helteen jälkeen."])

q(["Which favourite played the 1998 World Cup final hours after a convulsive fit at the team hotel?", "Ronaldo", "Zinedine Zidane", "Rivaldo", "Davor Suker",
   "He was taken off the team sheet and then put back on; Brazil lost 3-0 and he said afterwards he remembered almost nothing."],
  ["Kuka ennakkosuosikki pelasi vuoden 1998 MM-finaalin tuntien päästä hotellilla saadusta kohtauksesta?", "Ronaldo", "Zinedine Zidane", "Rivaldo", "Davor Šuker",
   "Hän poistettiin kokoonpanosta ja palautettiin siihen; Brasilia hävisi 0-3, ja hän kertoi jälkeenpäin ettei muistanut juuri mitään."])

q(["Which football World Cup was shared between two host countries?", "2002", "1994", "2010", "1974",
   "Japan and South Korea were both bidding and neither would give way, so FIFA gave it to the pair of them."],
  ["Mitkä jalkapallon MM-kilpailut jaettiin kahden isäntämaan kesken?", "Vuoden 2002", "Vuoden 1994", "Vuoden 2010", "Vuoden 1974",
   "Japani ja Etelä-Korea olivat kumpikin hakijoina eikä kumpikaan väistänyt, joten FIFA antoi kisat molemmille."])

q(["Spain won the 2010 World Cup having scored how many goals in the whole tournament?", "Eight", "Fourteen", "Twenty", "Eleven",
   "That is the fewest by any champion; four of its knockout matches finished 1-0, including the final."],
  ["Espanja voitti vuoden 2010 MM-kilpailut tehtyään koko turnauksessa kuinka monta maalia?", "Kahdeksan", "Neljätoista", "Kaksikymmentä", "Yksitoista",
   "Se on vähiten minkään mestarin tekemistä; neljä pudotuspeliä päättyi 1-0, finaali mukaan lukien."])

q(["Germany beat the hosts 7-1 in a 2014 World Cup semi-final. What do Brazilians call that match?", "The Mineirazo", "The Maracanazo", "The Disaster of Belo", "The Seven of July",
   "The name echoes the Maracanazo of 1950, the other home defeat Brazilians have never got over."],
  ["Saksa kaatoi isännät 7-1 vuoden 2014 MM-välierässä. Miksi brasilialaiset kutsuvat ottelua?", "Mineirazo", "Maracanazo", "Belon katastrofi", "Heinäkuun seitsemäs",
   "Nimi kaikuu vuoden 1950 Maracanazoa, toista kotitappiota josta brasilialaiset eivät ole päässeet yli."])

q(["Croatia reached the 2018 World Cup final with a population of roughly how many?", "Four million", "Twelve million", "Twenty million", "Forty million",
   "It is the smallest country to reach a final since Uruguay in 1950, and it played three straight extra-time knockout matches to get there."],
  ["Kroatia pääsi vuoden 2018 MM-finaaliin suunnilleen minkä kokoisena maana?", "Neljä miljoonaa", "Kaksitoista miljoonaa", "Kaksikymmentä miljoonaa", "Neljäkymmentä miljoonaa",
   "Se on pienin finaaliin päässyt maa Uruguayn jälkeen vuodesta 1950, ja se pelasi matkalla kolme jatkoaikaottelua putkeen."])

q(["Which ground hosted the World Cup finals of both 1970 and 1986?", "Estadio Azteca", "Maracana", "Wembley", "Olympiastadion Munich",
   "No other stadium had hosted two finals until the Maracana did it in 2014, 64 years after its first."],
  ["Mikä kenttä isännöi sekä vuoden 1970 että vuoden 1986 MM-finaalia?", "Estadio Azteca", "Maracanã", "Wembley", "Münchenin olympiastadion",
   "Mikään muu stadion ei ollut isännöinyt kahta finaalia ennen kuin Maracanã teki sen 2014, 64 vuotta ensimmäisensä jälkeen."])

q(["Zidane was sent off in the 2006 World Cup final, the last match of his career. What for?", "Headbutting an opponent", "A two-footed tackle", "Arguing with the referee", "Handling the ball",
   "Italy won the shoot-out, and he had still been voted the best player of the tournament a day earlier."],
  ["Zidane ajettiin ulos vuoden 2006 MM-finaalissa, uransa viimeisessä ottelussa. Mistä?", "Vastustajan puskemisesta", "Kaksin jaloin taklauksesta", "Tuomarin kanssa kiistelystä", "Pallon käsin koskemisesta",
   "Italia voitti rangaistuspotkukilpailun, ja hän oli silti valittu päivää aiemmin turnauksen parhaaksi pelaajaksi."])

# ------------------------------------------------------------------ Formula One
q(["Who won the first Formula One drivers' championship, in 1950?", "Giuseppe Farina", "Juan Manuel Fangio", "Alberto Ascari", "Stirling Moss",
   "He beat his own Alfa Romeo team-mate Fangio by three points, and Fangio then won five of the next seven titles."],
  ["Kuka voitti ensimmäisen formula ykkösten kuljettajien maailmanmestaruuden vuonna 1950?", "Giuseppe Farina", "Juan Manuel Fangio", "Alberto Ascari", "Stirling Moss",
   "Hän päihitti oman Alfa Romeo -tallikaverinsa Fangion kolmella pisteellä, ja Fangio voitti sitten viisi seuraavista seitsemästä tittelistä."])

q(["Juan Manuel Fangio won his five world titles driving for how many different makes of car?", "Four", "One", "Two", "Six",
   "Alfa Romeo, Maserati, Mercedes and Ferrari; no champion since has won titles with more than two different marques."],
  ["Kuinka monen eri automerkin autolla Juan Manuel Fangio voitti viisi maailmanmestaruuttaan?", "Neljän", "Yhden", "Kahden", "Kuuden",
   "Alfa Romeo, Maserati, Mercedes ja Ferrari; yksikään mestari ei ole sen jälkeen voittanut titteleitä kahta useammalla merkillä."])

q(["Which driver won nine Formula One Grands Prix in a row across the 1952 and 1953 seasons?", "Alberto Ascari", "Juan Manuel Fangio", "Giuseppe Farina", "Mike Hawthorn",
   "No one matched the run for sixty years, and he was killed testing a sports car at Monza in 1955, aged 36."],
  ["Kuka kuljettaja voitti yhdeksän formula ykkösten osakilpailua putkeen kausilla 1952 ja 1953?", "Alberto Ascari", "Juan Manuel Fangio", "Giuseppe Farina", "Mike Hawthorn",
   "Kukaan ei toistanut putkea kuuteenkymmeneen vuoteen, ja hän kuoli testatessaan urheiluautoa Monzassa 1955, 36-vuotiaana."])

q(["Which driver has won a Formula One world title in a car bearing his own name?", "Jack Brabham", "Bruce McLaren", "Enzo Ferrari", "Jackie Stewart",
   "He did it in 1966, in a car his own firm built, and he is still the only one; he was 40 years old."],
  ["Kuka kuljettaja on voittanut formula ykkösten maailmanmestaruuden autolla, joka kantoi hänen omaa nimeään?", "Jack Brabham", "Bruce McLaren", "Enzo Ferrari", "Jackie Stewart",
   "Hän teki sen 1966 oman yhtiönsä rakentamalla autolla ja on yhä ainoa; hän oli tuolloin 40-vuotias."])

q(["Which driver was awarded the Formula One world title of 1970 after his death?", "Jochen Rindt", "Jim Clark", "Gilles Villeneuve", "Francois Cevert",
   "He was killed at Monza with four races of the season left, and nobody caught his points total."],
  ["Kuka kuljettaja sai formula ykkösten maailmanmestaruuden 1970 kuolemansa jälkeen?", "Jochen Rindt", "Jim Clark", "Gilles Villeneuve", "François Cevert",
   "Hän kuoli Monzassa, kun kaudesta oli neljä kilpailua jäljellä, eikä kukaan ehtinyt hänen pistesaldonsa ohi."])

q(["Which champion led the campaign for seat belts, barriers and medical cars in Formula One?", "Jackie Stewart", "Niki Lauda", "Graham Hill", "James Hunt",
   "He reckoned a driver who raced through his era had about a two-in-three chance of being killed, and he went to a great many funerals."],
  ["Kuka mestari johti kampanjaa turvavöiden, kaiteiden ja lääkäriautojen puolesta formula ykkösissä?", "Jackie Stewart", "Niki Lauda", "Graham Hill", "James Hunt",
   "Hän laski, että hänen aikansa läpi ajaneella kuljettajalla oli noin kahden kolmen todennäköisyys kuolla, ja hautajaisia riitti."])

q(["Niki Lauda pulled out of the last race of 1976 in the rain in Japan. Who took the title by a point?", "James Hunt", "Jody Scheckter", "Mario Andretti", "Carlos Reutemann",
   "Lauda had been dragged from a burning car at the Nurburgring six weeks earlier and was back racing in 42 days."],
  ["Niki Lauda keskeytti vuoden 1976 viimeisen kilpailun sateessa Japanissa. Kuka otti mestaruuden pisteellä?", "James Hunt", "Jody Scheckter", "Mario Andretti", "Carlos Reutemann",
   "Lauda oli raahattu palavasta autosta Nürburgringillä kuusi viikkoa aiemmin ja ajoi taas 42 päivän kuluttua."])

q(["Which Formula One champion was nicknamed the Professor?", "Alain Prost", "Niki Lauda", "Nelson Piquet", "Jackie Stewart",
   "He won on tyre wear and arithmetic rather than lap records, and often finished a race with a car that still looked clean."],
  ["Mikä formula ykkösten mestari sai lempinimen Professori?", "Alain Prost", "Niki Lauda", "Nelson Piquet", "Jackie Stewart",
   "Hän voitti renkaiden kulutuksella ja laskuopilla eikä kierrosennätyksillä, ja maalissa auto näytti usein yhä siistiltä."])

q(["Ayrton Senna took 65 pole positions. In how many Grand Prix starts?", "161", "280", "99", "204",
   "That is a pole in more than two races out of five, a rate nobody in the history of the sport has come near."],
  ["Ayrton Senna otti 65 paalupaikkaa. Kuinka monessa osakilpailulähdössä?", "161 lähdössä", "280 lähdössä", "99 lähdössä", "204 lähdössä",
   "Se on paalupaikka yli kahdessa kilpailussa viidestä, eikä kukaan lajin historiassa ole päässyt lähellekään."])

q(["Michael Schumacher was struck out of the 1997 standings for driving into a rival. Who became champion?", "Jacques Villeneuve", "Damon Hill", "Mika Hakkinen", "David Coulthard",
   "The collision at Jerez put them both off the track, but Schumacher's car stopped and his rival's carried on to finish third."],
  ["Schumacher pyyhittiin vuoden 1997 pistetaulukosta kilpakumppanin päälle ajamisesta. Kuka tuli mestariksi?", "Jacques Villeneuve", "Damon Hill", "Mika Häkkinen", "David Coulthard",
   "Kolari Jerezissä vei kummatkin ulos radalta, mutta Schumacherin auto jäi siihen ja kilpakumppanin jatkoi kolmanneksi."])

q(["Which driver won five Formula One world titles in a row?", "Michael Schumacher", "Lewis Hamilton", "Sebastian Vettel", "Juan Manuel Fangio",
   "From 2000 to 2004; in 2002 he won eleven of the seventeen races and had the championship settled by July."],
  ["Kuka kuljettaja voitti viisi formula ykkösten maailmanmestaruutta putkeen?", "Michael Schumacher", "Lewis Hamilton", "Sebastian Vettel", "Juan Manuel Fangio",
   "Vuosina 2000-2004; kaudella 2002 hän voitti yksitoista seitsemästätoista kilpailusta ja mestaruus oli selvä heinäkuussa."])

q(["What did Nico Rosberg do five days after winning the 2016 Formula One title?", "He retired", "He changed teams", "He was banned", "He bought the team",
   "He had spent ten years trying to beat Lewis Hamilton, said he had nothing left to prove, and never raced again at 31."],
  ["Mitä Nico Rosberg teki viisi päivää vuoden 2016 formula ykkösten mestaruuden jälkeen?", "Lopetti uransa", "Vaihtoi tallia", "Sai kilpailukiellon", "Osti tallin",
   "Hän oli yrittänyt kymmenen vuotta päihittää Lewis Hamiltonin, sanoi ettei hänellä ollut enää näytettävää, eikä ajanut enää 31-vuotiaana."])

q(["Which Formula One champion gave every one of his racing cars a girl's name?", "Sebastian Vettel", "Fernando Alonso", "Jenson Button", "Nigel Mansell",
   "Kate, Luscious Liz, Hungry Heidi and Suzie among them, and he talked to the car on the grid before the start."],
  ["Mikä formula ykkösten mestari antoi jokaiselle kilpa-autolleen tytön nimen?", "Sebastian Vettel", "Fernando Alonso", "Jenson Button", "Nigel Mansell",
   "Niiden joukossa olivat Kate, Luscious Liz, Hungry Heidi ja Suzie, ja hän jutteli autolle lähtöruudukossa ennen starttia."])

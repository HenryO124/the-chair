# -*- coding: utf-8 -*-
# Batch 1: Summer Olympic hosts, Winter Olympic hosts, World Cup winners, F1 champions
# Sources:
#  https://en.wikipedia.org/wiki/List_of_Olympic_Games_host_cities
#  https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals
#  https://en.wikipedia.org/wiki/List_of_Formula_One_World_Drivers%27_Champions
Q = []
def q(en, fi):
    Q.append((["Sport"] + list(en), ["Sport"] + list(fi)))

# ---------------------------------------------------------- Summer Olympic hosts
q(["In which city were the 1900 Summer Olympics held?", "Paris", "Brussels", "Amsterdam", "Antwerp",
   "The Games were spread over five months as a sideshow to the World's Fair, and women competed for the first time."],
  ["Missä kaupungissa pidettiin vuoden 1900 kesäolympialaiset?", "Pariisi", "Bryssel", "Amsterdam", "Antwerpen",
   "Kisat venyivät viiden kuukauden mittaisiksi maailmannäyttelyn sivujuonteena, ja naiset kilpailivat niissä ensi kerran."])

q(["The 1904 Summer Olympics were the first outside Europe. Which city held them?", "St. Louis", "Chicago", "New York", "Boston",
   "Chicago had already been chosen, but St. Louis was staging a World's Fair and refused to let the Games go elsewhere."],
  ["Vuoden 1904 kesäolympialaiset olivat ensimmäiset Euroopan ulkopuolella. Mikä kaupunki?", "St. Louis", "Chicago", "New York", "Boston",
   "Kisat oli jo myönnetty Chicagolle, mutta St. Louis järjesti maailmannäyttelyn eikä suostunut päästämään niitä muualle."])

q(["Which city staged the Summer Olympics of 1908?", "London", "Paris", "Rome", "Berlin",
   "Rome had the Games first but gave them up after Vesuvius erupted in 1906 and the money went to rebuilding Naples."],
  ["Mikä kaupunki järjesti vuoden 1908 kesäolympialaiset?", "Lontoo", "Pariisi", "Rooma", "Berliini",
   "Rooma sai kisat ensin mutta luopui niistä, kun Vesuvius purkautui 1906 ja rahat menivät Napolin jälleenrakennukseen."])

q(["The first Games after the First World War, in 1920, were held where?", "Antwerp", "Amsterdam", "Brussels", "Stockholm",
   "Belgium was given them as a battered host country, and the five-ring Olympic flag was flown at a Games for the first time."],
  ["Ensimmäiset olympialaiset ensimmäisen maailmansodan jälkeen, vuonna 1920, pidettiin missä?", "Antwerpen", "Amsterdam", "Bryssel", "Tukholma",
   "Belgia sai kisat sodan runtelemana maana, ja viisirenkainen olympialippu liehui silloin ensi kerran kisoissa."])

q(["In which city were the 1928 Summer Olympics held?", "Amsterdam", "Antwerp", "Brussels", "Copenhagen",
   "The marathon tower there burned an Olympic flame for the first time, a habit every host has kept since."],
  ["Missä kaupungissa pidettiin vuoden 1928 kesäolympialaiset?", "Amsterdam", "Antwerpen", "Bryssel", "Kopenhamina",
   "Stadionin maratontornissa poltettiin olympiatulta ensi kerran, ja tavasta tuli perinne kaikille myöhemmille järjestäjille."])

q(["Which city hosted the Summer Olympics of 1936?", "Berlin", "Munich", "Hamburg", "Vienna",
   "Jesse Owens took four golds there, and the Games were the first shown on television, to a few halls around the city."],
  ["Mikä kaupunki järjesti vuoden 1936 kesäolympialaiset?", "Berliini", "München", "Hampuri", "Wien",
   "Jesse Owens voitti neljä kultaa, ja kisat olivat ensimmäiset televisioidut: kuvaa näytettiin muutamassa salissa kaupungilla."])

q(["Tokyo gave up the 1940 Olympics. Which capital was to take over before they were cancelled?", "Helsinki", "Stockholm", "Oslo", "Rome",
   "The stadium was built and the tickets printed; the war took the Games, and the city had to wait twelve more years."],
  ["Tokio luopui vuoden 1940 kisoista. Minkä maan pääkaupunkiin ne siirrettiin ennen peruutusta?", "Helsinki", "Tukholma", "Oslo", "Rooma",
   "Stadion rakennettiin ja liput painettiin, mutta sota vei kisat ja kaupunki sai odottaa vielä kaksitoista vuotta."])

q(["The 1956 Summer Olympics went to the southern hemisphere. Which city?", "Melbourne", "Sydney", "Perth", "Auckland",
   "Australian quarantine law barred foreign horses, so the equestrian events were ridden in Stockholm instead."],
  ["Vuoden 1956 kesäolympialaiset menivät eteläiselle pallonpuoliskolle. Mikä kaupunki?", "Melbourne", "Sydney", "Perth", "Auckland",
   "Australian karanteenilaki esti ulkomaisten hevosten tuonnin, joten ratsastuslajit kilpailtiin Tukholmassa."])

q(["Which city hosted the Summer Olympics of 1960?", "Rome", "Milan", "Naples", "Athens",
   "A barefoot Ethiopian soldier, Abebe Bikila, won the marathon along the old Appian Way."],
  ["Mikä kaupunki järjesti vuoden 1960 kesäolympialaiset?", "Rooma", "Milano", "Napoli", "Ateena",
   "Paljain jaloin juossut etiopialainen sotilas Abebe Bikila voitti maratonin vanhaa Via Appiaa pitkin."])

q(["Which city held the first Summer Olympics in Asia, in 1964?", "Tokyo", "Seoul", "Beijing", "Osaka",
   "A new bullet train line opened days before them, built to carry the crowds from the capital to Osaka."],
  ["Mikä kaupunki järjesti ensimmäiset kesäolympialaiset Aasiassa vuonna 1964?", "Tokio", "Seoul", "Peking", "Osaka",
   "Uusi luotijunarata avattiin päiviä ennen kisoja, ja se rakennettiin kuljettamaan yleisöä pääkaupungista Osakaan."])

q(["The 1968 Summer Olympics were held 2,200 metres above sea level. In which city?", "Mexico City", "Bogota", "Quito", "La Paz",
   "The thin air wrecked the distance races and flattered the sprints: Bob Beamon's long jump record stood for 23 years."],
  ["Vuoden 1968 kesäolympialaiset pidettiin 2 200 metrin korkeudessa. Missä kaupungissa?", "Mexico City", "Bogotá", "Quito", "La Paz",
   "Ohut ilma tuhosi kestävyysjuoksut ja suosi pikamatkoja: Bob Beamonin pituushyppyennätys kesti 23 vuotta."])

q(["Which German city hosted the Summer Olympics of 1972?", "Munich", "Berlin", "Frankfurt", "Cologne",
   "West Germany meant them as a cheerful answer to 1936, and the mascot was a rainbow-striped dachshund called Waldi."],
  ["Mikä saksalainen kaupunki järjesti vuoden 1972 kesäolympialaiset?", "München", "Berliini", "Frankfurt", "Köln",
   "Länsi-Saksa halusi iloisen vastakohdan vuodelle 1936, ja maskottina oli sateenkaariraidallinen mäyräkoira Waldi."])

q(["Which Canadian city hosted the Summer Olympics of 1976?", "Montreal", "Toronto", "Vancouver", "Ottawa",
   "The city took thirty years to pay off the stadium, and locals called the unfinished tower the Big Owe."],
  ["Mikä kanadalainen kaupunki järjesti vuoden 1976 kesäolympialaiset?", "Montreal", "Toronto", "Vancouver", "Ottawa",
   "Kaupunki maksoi stadionin velkaa kolmekymmentä vuotta, ja keskeneräistä tornia kutsuttiin pilkalla Isoksi laskuksi."])

q(["Which city hosted the Summer Olympics of 1980, boycotted by many Western teams?", "Moscow", "Leningrad", "Kiev", "Prague",
   "Sixty-odd countries stayed away over Afghanistan, and some of those who came marched under the Olympic flag."],
  ["Mikä kaupunki järjesti vuoden 1980 kesäolympialaiset, joita monet länsimaat boikotoivat?", "Moskova", "Leningrad", "Kiev", "Praha",
   "Runsaat kuusikymmentä maata jäi pois Afganistanin takia, ja osa saapuneista marssi olympialipun alla."])

q(["Which Asian city hosted the Summer Olympics of 1988?", "Seoul", "Tokyo", "Beijing", "Bangkok",
   "Table tennis joined the programme there, and the men's 100 metres winner lost his gold to a drugs test."],
  ["Mikä aasialainen kaupunki järjesti vuoden 1988 kesäolympialaiset?", "Seoul", "Tokio", "Peking", "Bangkok",
   "Pöytätennis otettiin silloin ohjelmaan, ja miesten satasen voittaja menetti kultansa dopingtestissä."])

q(["Which Spanish city hosted the Summer Olympics of 1992?", "Barcelona", "Madrid", "Seville", "Valencia",
   "An archer lit the cauldron with a flaming arrow, and the Games turned a run-down waterfront into a beach."],
  ["Mikä espanjalainen kaupunki järjesti vuoden 1992 kesäolympialaiset?", "Barcelona", "Madrid", "Sevilla", "Valencia",
   "Jousiampuja sytytti maljan liekehtivällä nuolella, ja kisat muuttivat rähjäisen satama-alueen uimarannaksi."])

q(["Which American city hosted the Summer Olympics of 1996?", "Atlanta", "Los Angeles", "Chicago", "Miami",
   "Muhammad Ali, his hands shaking from Parkinson's, lit the flame in front of a hushed stadium."],
  ["Mikä yhdysvaltalainen kaupunki järjesti vuoden 1996 kesäolympialaiset?", "Atlanta", "Los Angeles", "Chicago", "Miami",
   "Muhammad Ali sytytti tulen Parkinsonin taudista vapisevin käsin hiljentyneen stadionin edessä."])

q(["Which city hosted the Summer Olympics of 2000?", "Sydney", "Melbourne", "Brisbane", "Perth",
   "Cathy Freeman won the 400 metres in a hooded bodysuit and then carried both the Australian and Aboriginal flags."],
  ["Mikä kaupunki järjesti vuoden 2000 kesäolympialaiset?", "Sydney", "Melbourne", "Brisbane", "Perth",
   "Cathy Freeman voitti 400 metriä hupullisessa kokovartalopuvussa ja kantoi sitten Australian ja aboriginaalien lippuja."])

q(["The Summer Olympics came back to their birthplace in 2004. Which city?", "Athens", "Rome", "Paris", "Istanbul",
   "The shot put was held at ancient Olympia itself, on the grass of the original stadium, with no seats."],
  ["Kesäolympialaiset palasivat syntysijoilleen vuonna 2004. Mikä kaupunki?", "Ateena", "Rooma", "Pariisi", "Istanbul",
   "Kuulantyöntö kilpailtiin muinaisessa Olympiassa, alkuperäisen stadionin ruoholla ilman katsomoita."])

q(["In which city were the first Summer Olympics in South America held, in 2016?", "Rio de Janeiro", "Buenos Aires", "Sao Paulo", "Santiago",
   "Golf returned to the programme there after 112 years away, on a course built in a nature reserve."],
  ["Missä kaupungissa pidettiin ensimmäiset kesäolympialaiset Etelä-Amerikassa vuonna 2016?", "Rio de Janeiro", "Buenos Aires", "São Paulo", "Santiago",
   "Golf palasi ohjelmaan 112 vuoden tauon jälkeen, ja kenttä rakennettiin luonnonsuojelualueelle."])

q(["Which city was the first to host both a Summer and a Winter Olympics?", "Beijing", "Tokyo", "Los Angeles", "Innsbruck",
   "It took the Summer Games in 2008 and the Winter Games in 2022, the latter run almost entirely on artificial snow."],
  ["Mikä kaupunki järjesti ensimmäisenä sekä kesä- että talviolympialaiset?", "Peking", "Tokio", "Los Angeles", "Innsbruck",
   "Kesäkisat olivat 2008 ja talvikisat 2022, ja jälkimmäiset hiihdettiin lähes kokonaan keinolumella."])

# ---------------------------------------------------------- Winter Olympic hosts
q(["Which Swiss resort hosted the Winter Olympics of 1928 and again of 1948?", "St. Moritz", "Davos", "Zermatt", "Interlaken",
   "Skeleton sledding grew up on the town's Cresta Run, a track still built from scratch out of snow every winter."],
  ["Mikä sveitsiläinen lomakohde järjesti talviolympialaiset 1928 ja uudelleen 1948?", "St. Moritz", "Davos", "Zermatt", "Interlaken",
   "Skeleton syntyi kylän Cresta Run -radalla, joka rakennetaan yhä joka talvi tyhjästä pelkästä lumesta."])

q(["Which American town hosted the Winter Olympics of 1932 and again of 1980?", "Lake Placid", "Aspen", "Denver", "Squaw Valley",
   "A village of a few thousand people has staged two Winter Games, more than New York or Chicago have managed."],
  ["Mikä amerikkalainen pikkukaupunki järjesti talviolympialaiset 1932 ja uudelleen 1980?", "Lake Placid", "Aspen", "Denver", "Squaw Valley",
   "Parin tuhannen asukkaan kylä on järjestänyt kahdet talvikisat, enemmän kuin New York tai Chicago yhteensä."])

q(["Which Bavarian double town hosted the Winter Olympics of 1936?", "Garmisch-Partenkirchen", "Oberstdorf", "Innsbruck", "Kitzbuhel",
   "Alpine skiing made its Olympic debut there, and ski instructors were barred as professionals."],
  ["Mikä baijerilainen kaksoiskaupunki järjesti vuoden 1936 talviolympialaiset?", "Garmisch-Partenkirchen", "Oberstdorf", "Innsbruck", "Kitzbühel",
   "Alppihiihto nähtiin siellä ensi kerran olympialaisissa, ja hiihdonopettajat kiellettiin ammattilaisina."])

q(["In which city were the 1952 Winter Olympics held?", "Oslo", "Stockholm", "Helsinki", "Copenhagen",
   "The flame for them was lit not in Greece but in a hearth in Morgedal, the cottage where Sondre Norheim grew up."],
  ["Missä kaupungissa pidettiin vuoden 1952 talviolympialaiset?", "Oslo", "Tukholma", "Helsinki", "Kopenhamina",
   "Tuli sytytettiin näihin kisoihin Kreikan sijasta Morgedalin takassa, Sondre Norheimin lapsuudenkodissa."])

q(["Which Italian resort hosted the Winter Olympics of 1956?", "Cortina d'Ampezzo", "Turin", "Bormio", "Sestriere",
   "The torchbearer tripped on a television cable in the stadium, got up, and carried the flame on."],
  ["Mikä italialainen lomakohde järjesti vuoden 1956 talviolympialaiset?", "Cortina d'Ampezzo", "Torino", "Bormio", "Sestriere",
   "Soihdunkantaja kompastui stadionilla televisiokaapeliin, nousi ylös ja vei tulen perille."])

q(["Which Californian valley hosted the Winter Olympics of 1960?", "Squaw Valley", "Lake Tahoe", "Mammoth", "Aspen",
   "Bobsleigh was left out because only nine countries entered and the organisers would not build a track."],
  ["Mikä kalifornialainen laakso järjesti vuoden 1960 talviolympialaiset?", "Squaw Valley", "Lake Tahoe", "Mammoth", "Aspen",
   "Rattikelkkailu jätettiin pois, koska vain yhdeksän maata ilmoittautui eikä järjestäjä halunnut rakentaa rataa."])

q(["Which Austrian city hosted the Winter Olympics of both 1964 and 1976?", "Innsbruck", "Salzburg", "Vienna", "Graz",
   "In 1964 the army had to cart snow down from the mountains by hand after a warm, bare winter."],
  ["Mikä itävaltalainen kaupunki järjesti talviolympialaiset sekä 1964 että 1976?", "Innsbruck", "Salzburg", "Wien", "Graz",
   "Vuonna 1964 armeija kuljetti lunta vuorilta käsin alas, kun talvi oli ollut lämmin ja rinteet paljaat."])

q(["Which French city hosted the Winter Olympics of 1968?", "Grenoble", "Albertville", "Chamonix", "Lyon",
   "These were the first Winter Games in colour television and the first with drug and sex testing."],
  ["Mikä ranskalainen kaupunki järjesti vuoden 1968 talviolympialaiset?", "Grenoble", "Albertville", "Chamonix", "Lyon",
   "Nämä olivat ensimmäiset väritelevisiossa näytetyt talvikisat ja ensimmäiset, joissa tehtiin doping- ja sukupuolitestejä."])

q(["Which Japanese city hosted the first Winter Olympics in Asia, in 1972?", "Sapporo", "Nagano", "Tokyo", "Sendai",
   "The downhill favourite was thrown out days before for taking money from a coffee firm."],
  ["Mikä japanilainen kaupunki järjesti ensimmäiset talviolympialaiset Aasiassa vuonna 1972?", "Sapporo", "Nagano", "Tokio", "Sendai",
   "Syöksylaskun ennakkosuosikki hylättiin päiviä ennen kisoja, koska hän oli ottanut rahaa kahviyhtiöltä."])

q(["Denver was awarded the 1976 Winter Olympics but gave them back. Which city stepped in?", "Innsbruck", "Lake Placid", "Grenoble", "Sapporo",
   "Colorado voters refused to pay for them in a referendum, the only time a host has handed the Games back."],
  ["Denver sai vuoden 1976 talviolympialaiset mutta luopui niistä. Mikä kaupunki otti ne?", "Innsbruck", "Lake Placid", "Grenoble", "Sapporo",
   "Coloradon äänestäjät kielsivät kansanäänestyksessä maksamasta kisoja, ainoa kerta kun järjestäjä on palauttanut kisat."])

q(["Which Yugoslav city hosted the Winter Olympics of 1984?", "Sarajevo", "Belgrade", "Zagreb", "Ljubljana",
   "The bobsleigh track and the ski jumps were shelled in the siege eight years later and stand ruined today."],
  ["Mikä jugoslavialainen kaupunki järjesti vuoden 1984 talviolympialaiset?", "Sarajevo", "Belgrad", "Zagreb", "Ljubljana",
   "Rattikelkkarata ja hyppyrimäet ammuttiin piirityksessä kahdeksan vuotta myöhemmin, ja ne ovat raunioina vielä nyt."])

q(["Which Canadian city hosted the Winter Olympics of 1988?", "Calgary", "Montreal", "Vancouver", "Edmonton",
   "A Jamaican bobsleigh team and the British ski jumper Eddie the Eagle were better remembered than most winners."],
  ["Mikä kanadalainen kaupunki järjesti vuoden 1988 talviolympialaiset?", "Calgary", "Montreal", "Vancouver", "Edmonton",
   "Jamaikan rattikelkkajoukkue ja brittiläinen mäkihyppääjä Eddie the Eagle muistetaan paremmin kuin useimmat voittajat."])

q(["Which French town hosted the Winter Olympics of 1992?", "Albertville", "Grenoble", "Chamonix", "Val d'Isere",
   "These were the last Winter Games in the same year as the Summer ones; the next came after only two years."],
  ["Mikä ranskalainen kaupunki järjesti vuoden 1992 talviolympialaiset?", "Albertville", "Grenoble", "Chamonix", "Val d'Isère",
   "Nämä olivat viimeiset talvikisat samana vuonna kesäkisojen kanssa; seuraavat pidettiin vain kahden vuoden päästä."])

q(["Which Japanese city hosted the Winter Olympics of 1998?", "Nagano", "Sapporo", "Osaka", "Niigata",
   "Snowboarding was added there, and the first halfpipe gold was briefly taken away over a cannabis test."],
  ["Mikä japanilainen kaupunki järjesti vuoden 1998 talviolympialaiset?", "Nagano", "Sapporo", "Osaka", "Niigata",
   "Lumilautailu lisättiin ohjelmaan, ja ensimmäinen halfpipe-kulta vietiin hetkeksi pois kannabistestin takia."])

q(["Which American city hosted the Winter Olympics of 2002?", "Salt Lake City", "Denver", "Lake Placid", "Minneapolis",
   "The bidding for them set off a bribery scandal that forced the Olympic committee to rewrite its rules."],
  ["Mikä amerikkalainen kaupunki järjesti vuoden 2002 talviolympialaiset?", "Salt Lake City", "Denver", "Lake Placid", "Minneapolis",
   "Kisojen hakuvaiheesta paljastui lahjusskandaali, joka pakotti olympiakomitean kirjoittamaan sääntönsä uusiksi."])

q(["Which Italian city hosted the Winter Olympics of 2006?", "Turin", "Milan", "Cortina d'Ampezzo", "Bolzano",
   "A city of cars and coffee had no snow of its own; the alpine events were held in valleys an hour or two away."],
  ["Mikä italialainen kaupunki järjesti vuoden 2006 talviolympialaiset?", "Torino", "Milano", "Cortina d'Ampezzo", "Bolzano",
   "Autojen ja kahvin kaupungissa ei ollut omaa lunta, ja alppilajit kilpailtiin tunnin tai kahden päässä laaksoissa."])

q(["Which Canadian city hosted the Winter Olympics of 2010?", "Vancouver", "Calgary", "Toronto", "Quebec",
   "It was the warmest host in Winter Games history and had to truck and helicopter snow onto the freestyle hill."],
  ["Mikä kanadalainen kaupunki järjesti vuoden 2010 talviolympialaiset?", "Vancouver", "Calgary", "Toronto", "Quebec",
   "Se oli talvikisojen historian lämpimin järjestäjä ja joutui kuljettamaan lunta rekoilla ja helikoptereilla rinteeseen."])

q(["Which Black Sea resort hosted the Winter Olympics of 2014?", "Sochi", "Vladivostok", "Krasnoyarsk", "Yalta",
   "They were the costliest Games ever staged, in a town where palm trees grow by the beach."],
  ["Mikä Mustanmeren lomakohde järjesti vuoden 2014 talviolympialaiset?", "Sotši", "Vladivostok", "Krasnojarsk", "Jalta",
   "Ne olivat kalleimmat koskaan järjestetyt kisat, ja kaupungissa kasvaa palmuja rannan tuntumassa."])

q(["Which South Korean county hosted the Winter Olympics of 2018?", "Pyeongchang", "Seoul", "Busan", "Incheon",
   "North and South Korea marched in together and put out a joint women's ice hockey team."],
  ["Mikä eteläkorealainen kunta järjesti vuoden 2018 talviolympialaiset?", "Pyeongchang", "Seoul", "Busan", "Incheon",
   "Pohjois- ja Etelä-Korea marssivat yhdessä sisään ja kokosivat yhteisen naisten jääkiekkojoukkueen."])

# ---------------------------------------------------------- World Cup winners
q(["Which country won the football World Cup of 1934?", "Italy", "Czechoslovakia", "Hungary", "Austria",
   "The hosts beat Czechoslovakia in extra time, and the holders Uruguay refused to come at all."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1934?", "Italia", "Tšekkoslovakia", "Unkari", "Itävalta",
   "Isäntämaa kaatoi Tšekkoslovakian jatkoajalla, ja hallitseva mestari Uruguay kieltäytyi kokonaan saapumasta."])

q(["Which country won the football World Cup of 1938, held in France?", "Italy", "Hungary", "Brazil", "France",
   "They became the first team to defend the trophy, and nobody managed it again until Brazil in 1962."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1938 Ranskassa?", "Italia", "Unkari", "Brasilia", "Ranska",
   "Joukkue puolusti mestaruutta ensimmäisenä, eikä kukaan onnistunut samassa ennen Brasiliaa 1962."])

q(["Who won the 1950 World Cup, decided in front of 170,000 people in Rio?", "Uruguay", "Brazil", "Sweden", "Spain",
   "There was no final that year: a four-team group decided it, and the hosts needed only a draw and lost 2-1."],
  ["Kuka voitti vuoden 1950 MM-kilpailut, jotka ratkesivat 170 000 katsojan edessä Rio de Janeirossa?", "Uruguay", "Brasilia", "Ruotsi", "Espanja",
   "Varsinaista finaalia ei ollut: neljän joukkueen lohko ratkaisi mestaruuden, ja isännille riitti tasapeli mutta tuli 1-2."])

q(["Which country won the football World Cup of 1954?", "West Germany", "Hungary", "Austria", "Uruguay",
   "Hungary had beaten them 8-3 in the group stage and had not lost a match in four years before the final."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1954?", "Länsi-Saksa", "Unkari", "Itävalta", "Uruguay",
   "Unkari oli kaatanut saman joukkueen alkulohkossa 8-3 eikä ollut häviönyt ottelua neljään vuoteen ennen finaalia."])

q(["Which country won the 1958 World Cup, beating the hosts Sweden in the final?", "Brazil", "France", "West Germany", "Hungary",
   "A seventeen-year-old called Pele scored twice in that final, and it remains the only World Cup won in Europe by a South American side."],
  ["Mikä maa voitti vuoden 1958 MM-kilpailut kaatamalla finaalissa isäntämaan Ruotsin?", "Brasilia", "Ranska", "Länsi-Saksa", "Unkari",
   "Seitsemäntoistavuotias Pelé teki finaalissa kaksi maalia, ja tämä on yhä ainoa eurooppalaisissa kisoissa voitettu eteläamerikkalainen mestaruus."])

q(["Which country won the football World Cup of 1962 in Chile?", "Brazil", "Czechoslovakia", "Chile", "Yugoslavia",
   "Pele was injured in the second match and Garrincha carried the team to the title almost alone."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1962 Chilessä?", "Brasilia", "Tšekkoslovakia", "Chile", "Jugoslavia",
   "Pelé loukkaantui toisessa ottelussa, ja Garrincha kantoi joukkueen mestaruuteen lähes yksin."])

q(["Which country won the football World Cup of 1966?", "England", "West Germany", "Portugal", "Soviet Union",
   "The trophy had been stolen from an exhibition months earlier and was found under a hedge by a dog called Pickles."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1966?", "Englanti", "Länsi-Saksa", "Portugali", "Neuvostoliitto",
   "Palkintopokaali oli varastettu näyttelystä kuukausia aiemmin, ja Pickles-nimineen koira löysi sen pensaan alta."])

q(["Which country won the football World Cup of 1970 in Mexico?", "Brazil", "Italy", "West Germany", "Uruguay",
   "A third title let them keep the original gold trophy for good, and it was stolen from a Rio cabinet in 1983."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1970 Meksikossa?", "Brasilia", "Italia", "Länsi-Saksa", "Uruguay",
   "Kolmas mestaruus toi alkuperäisen kultapokaalin pysyvästi, ja se varastettiin Rion vitriinistä vuonna 1983."])

q(["Which country won the football World Cup of 1974?", "West Germany", "Netherlands", "Poland", "Brazil",
   "The Dutch scored from a penalty before a German had touched the ball, and still lost 2-1."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1974?", "Länsi-Saksa", "Alankomaat", "Puola", "Brasilia",
   "Hollanti teki rangaistuspotkumaalin ennen kuin yksikään vastustaja oli koskenut palloon, ja hävisi silti 1-2."])

q(["Which country won the football World Cup of 1978, as hosts?", "Argentina", "Netherlands", "Brazil", "Italy",
   "The Dutch hit the post in the last minute of normal time in that final and then lost in extra time."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1978 isäntänä?", "Argentiina", "Alankomaat", "Brasilia", "Italia",
   "Hollanti osui tolppaan varsinaisen ajan viimeisellä minuutilla ja hävisi sitten jatkoajalla."])

q(["Which country won the football World Cup of 1982 in Spain?", "Italy", "West Germany", "Poland", "Brazil",
   "Paolo Rossi came back from a two-year betting ban to score six goals and win the golden boot."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1982 Espanjassa?", "Italia", "Länsi-Saksa", "Puola", "Brasilia",
   "Paolo Rossi palasi kahden vuoden vedonlyöntipannasta, teki kuusi maalia ja voitti maalikuninkuuden."])

q(["Which country won the football World Cup of 1986?", "Argentina", "West Germany", "France", "Belgium",
   "In one quarter-final Maradona scored with his hand and then ran past five England players to score again."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1986?", "Argentiina", "Länsi-Saksa", "Ranska", "Belgia",
   "Yhdessä puolivälierässä Maradona teki maalin kädellä ja juoksi sitten viiden englantilaisen ohi uuteen maaliin."])

q(["Which country won the football World Cup of 1990 in Italy?", "West Germany", "Argentina", "Italy", "England",
   "It was the last title won under that name: the country was reunified three months after the final."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1990 Italiassa?", "Länsi-Saksa", "Argentiina", "Italia", "Englanti",
   "Se oli viimeinen tällä nimellä voitettu mestaruus: maa yhdistyi kolme kuukautta finaalin jälkeen."])

q(["Which country won the 1994 World Cup final, the first settled on penalties?", "Brazil", "Italy", "Sweden", "Bulgaria",
   "Roberto Baggio sent the last penalty over the bar, and the match had finished 0-0 in blazing Pasadena heat."],
  ["Mikä maa voitti vuoden 1994 MM-finaalin, ensimmäisen rangaistuspotkuihin ratkenneen?", "Brasilia", "Italia", "Ruotsi", "Bulgaria",
   "Roberto Baggio ampui viimeisen laukauksen yli, ja ottelu oli päättynyt 0-0 Pasadenan hellekuumuudessa."])

q(["Which country won the football World Cup of 1998?", "France", "Brazil", "Croatia", "Netherlands",
   "Zinedine Zidane headed in two corners in the final, and Ronaldo played after a fit in the team hotel."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 1998?", "Ranska", "Brasilia", "Kroatia", "Alankomaat",
   "Zinedine Zidane puski finaalissa kaksi kulmapotkua sisään, ja Ronaldo pelasi hotellilla saadun kohtauksen jälkeen."])

q(["Which country won the football World Cup of 2002?", "Brazil", "Germany", "South Korea", "Turkey",
   "It was the only World Cup shared by two hosts, Japan and South Korea, and the first held in Asia."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 2002?", "Brasilia", "Saksa", "Etelä-Korea", "Turkki",
   "Nämä olivat ainoat kahden isäntämaan, Japanin ja Etelä-Korean, yhdessä järjestämät kisat ja ensimmäiset Aasiassa."])

q(["Which country won the football World Cup of 2006 in Germany?", "Italy", "France", "Portugal", "Brazil",
   "Zidane was sent off in the final of his last match for butting an opponent in the chest."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 2006 Saksassa?", "Italia", "Ranska", "Portugali", "Brasilia",
   "Zidane ajettiin viimeisen ottelunsa finaalissa ulos puskettuaan vastustajaa rintaan."])

q(["Which country won the football World Cup of 2010, their first title?", "Spain", "Netherlands", "Germany", "Uruguay",
   "They won the trophy having scored only eight goals in the whole tournament, the fewest of any champion."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 2010, ensimmäisen mestaruutensa?", "Espanja", "Alankomaat", "Saksa", "Uruguay",
   "Joukkue voitti pokaalin tehtyään koko turnauksessa vain kahdeksan maalia, vähiten yhdenkään mestarin historiassa."])

q(["Which country won the football World Cup of 2014 in Brazil?", "Germany", "Argentina", "Netherlands", "Brazil",
   "On the way they beat the hosts 7-1 in a semi-final that Brazilians still call the Mineirazo."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 2014 Brasiliassa?", "Saksa", "Argentiina", "Alankomaat", "Brasilia",
   "Matkalla joukkue kaatoi isännät 7-1 välierässä, jota brasilialaiset kutsuvat yhä nimellä Mineirazo."])

q(["Which country won the football World Cup of 2018 in Russia?", "France", "Croatia", "Belgium", "England",
   "Croatia reached that final with a nation of four million people, the smallest finalist since Uruguay in 1950."],
  ["Mikä maa voitti jalkapallon maailmanmestaruuden 2018 Venäjällä?", "Ranska", "Kroatia", "Belgia", "Englanti",
   "Kroatia pääsi finaaliin neljän miljoonan asukkaan maana, pienimpänä finalistina Uruguayn jälkeen vuodesta 1950."])

q(["In which London stadium was the 1966 World Cup final played?", "Wembley", "Highbury", "White City", "Crystal Palace",
   "The ground's twin towers stood for 80 years and came down in 2003 to make room for an arch."],
  ["Millä lontoolaisella stadionilla pelattiin vuoden 1966 MM-finaali?", "Wembley", "Highbury", "White City", "Crystal Palace",
   "Stadionin kaksoistornit seisoivat 80 vuotta ja purettiin 2003, jotta tilalle saatiin kaari."])

q(["Two World Cup finals have been played at the Estadio Azteca. In which city does it stand?", "Mexico City", "Guadalajara", "Monterrey", "Puebla",
   "The 1970 and 1986 finals were both played there, which no other ground had managed until 2014."],
  ["Estadio Aztecalla on pelattu kaksi MM-finaalia. Missä kaupungissa se sijaitsee?", "Mexico City", "Guadalajara", "Monterrey", "Puebla",
   "Vuosien 1970 ja 1986 finaalit pelattiin siellä, eikä mikään muu kenttä ollut siihen pystynyt vuoteen 2014 asti."])

# ---------------------------------------------------------- F1 champions
q(["Who took the very first drivers' title in Formula One, in 1950?", "Giuseppe Farina", "Juan Manuel Fangio", "Alberto Ascari", "Jack Brabham",
   "He beat his Alfa Romeo team-mate Fangio by three points, and Fangio then won five of the next seven."],
  ["Kuka voitti kaikkien ensimmäisen formula ykkösten kuljettajien tittelin vuonna 1950?", "Giuseppe Farina", "Juan Manuel Fangio", "Alberto Ascari", "Jack Brabham",
   "Hän päihitti Alfa Romeo -tallikaverinsa Fangion kolmella pisteellä, ja Fangio voitti sitten viisi seuraavista seitsemästä."])

q(["Which Argentine won five Formula One world titles in the 1950s?", "Juan Manuel Fangio", "Alberto Ascari", "Giuseppe Farina", "Mike Hawthorn",
   "He took them with four different makes of car, something nobody has done since."],
  ["Kuka argentiinalainen voitti viisi formula ykkösten maailmanmestaruutta 1950-luvulla?", "Juan Manuel Fangio", "Alberto Ascari", "Giuseppe Farina", "Mike Hawthorn",
   "Hän voitti ne neljällä eri automerkillä, mihin kukaan ei ole sen jälkeen pystynyt."])

q(["Which Italian won the Formula One title in both 1952 and 1953?", "Alberto Ascari", "Giuseppe Farina", "Luigi Villoresi", "Nino Vaccarella",
   "He won nine races in a row across those two seasons, a run no driver matched for sixty years."],
  ["Kuka italialainen voitti formula ykkösten maailmanmestaruuden sekä 1952 että 1953?", "Alberto Ascari", "Giuseppe Farina", "Luigi Villoresi", "Nino Vaccarella",
   "Hän voitti näiden kahden kauden aikana yhdeksän kilpailua putkeen, eikä kukaan toistanut sitä kuuteenkymmeneen vuoteen."])

q(["Which Australian won the Formula One title in 1966 in a car bearing his own name?", "Jack Brabham", "Alan Jones", "Denny Hulme", "Jackie Stewart",
   "He is still the only driver to have won the championship in a car he built himself."],
  ["Kuka australialainen voitti formula ykkösten mestaruuden 1966 autolla, joka kantoi hänen omaa nimeään?", "Jack Brabham", "Alan Jones", "Denny Hulme", "Jackie Stewart",
   "Hän on yhä ainoa kuljettaja, joka on voittanut mestaruuden itse rakentamallaan autolla."])

q(["Which Scot won Formula One titles in 1969, 1971 and 1973?", "Jackie Stewart", "Jim Clark", "Graham Hill", "Nigel Mansell",
   "He pushed for seat belts, barriers and medical cars after burying a long list of friends."],
  ["Kuka skotti voitti formula ykkösten mestaruuden 1969, 1971 ja 1973?", "Jackie Stewart", "Jim Clark", "Graham Hill", "Nigel Mansell",
   "Hän ajoi turvavöiden, kaiteiden ja lääkäriautojen puolesta haudattuaan pitkän listan ystäviä."])

q(["Which driver won the Formula One title in 1970 after he had already died?", "Jochen Rindt", "Jim Clark", "Ronnie Peterson", "Gilles Villeneuve",
   "He was killed at Monza with four races left, and nobody caught his points total."],
  ["Kuka kuljettaja voitti formula ykkösten mestaruuden 1970 jo kuoltuaan?", "Jochen Rindt", "Jim Clark", "Ronnie Peterson", "Gilles Villeneuve",
   "Hän kuoli Monzassa, kun neljä kilpailua oli jäljellä, eikä kukaan ehtinyt hänen pistesaldonsa ohi."])

q(["Which Englishman won the Formula One title in 1976 by one point?", "James Hunt", "Nigel Mansell", "Graham Hill", "John Surtees",
   "Niki Lauda, burned at the Nurburgring that year, pulled out of the last race in the rain in Japan."],
  ["Kuka englantilainen voitti formula ykkösten mestaruuden 1976 yhden pisteen erolla?", "James Hunt", "Nigel Mansell", "Graham Hill", "John Surtees",
   "Niki Lauda, joka oli palanut samana vuonna Nürburgringillä, keskeytti viimeisen kilpailun sateessa Japanissa."])

q(["Which Brazilian won Formula One titles in 1981, 1983 and 1987?", "Nelson Piquet", "Ayrton Senna", "Emerson Fittipaldi", "Rubens Barrichello",
   "He won two of his titles with Brabham and one with Williams, and his son Nelsinho later raced in Formula One too."],
  ["Kuka brasilialainen voitti formula ykkösten mestaruuden 1981, 1983 ja 1987?", "Nelson Piquet", "Ayrton Senna", "Emerson Fittipaldi", "Rubens Barrichello",
   "Kaksi mestaruutta tuli Brabhamilla ja yksi Williamsilla, ja hänen poikansa Nelsinho ajoi myöhemmin myös formula ykkösissä."])

q(["Which Frenchman won four Formula One titles between 1985 and 1993?", "Alain Prost", "Jacques Laffite", "Rene Arnoux", "Didier Pironi",
   "He was nicknamed the Professor for winning on tyre wear and arithmetic rather than lap records."],
  ["Kuka ranskalainen voitti neljä formula ykkösten mestaruutta vuosina 1985-1993?", "Alain Prost", "Jacques Laffite", "René Arnoux", "Didier Pironi",
   "Häntä kutsuttiin Professoriksi, koska hän voitti renkaiden kulutuksella ja laskuopilla eikä kierrosennätyksillä."])

q(["Which Brazilian won Formula One titles in 1988, 1990 and 1991?", "Ayrton Senna", "Nelson Piquet", "Emerson Fittipaldi", "Felipe Massa",
   "He took 65 pole positions in 161 starts, a strike rate no one has come near."],
  ["Kuka brasilialainen voitti formula ykkösten mestaruuden 1988, 1990 ja 1991?", "Ayrton Senna", "Nelson Piquet", "Emerson Fittipaldi", "Felipe Massa",
   "Hän otti 65 paalupaikkaa 161 lähdössä, eikä kukaan ole päässyt lähellekään samaa osuvuutta."])

q(["Which Canadian won the Formula One title in 1997?", "Jacques Villeneuve", "Damon Hill", "Michael Schumacher", "Lance Stroll",
   "His rival was struck out of the standings for driving into him at the last race of the year."],
  ["Kuka kanadalainen voitti formula ykkösten mestaruuden 1997?", "Jacques Villeneuve", "Damon Hill", "Michael Schumacher", "Lance Stroll",
   "Hänen kilpakumppaninsa pyyhittiin pistetaulukosta, kun tämä ajoi häneen kauden viimeisessä kilpailussa."])

q(["Which driver won seven Formula One titles, five of them in a row from 2000?", "Michael Schumacher", "Lewis Hamilton", "Sebastian Vettel", "Alain Prost",
   "Those five straight titles are still the longest run, and he won eleven of the seventeen races in 2002 alone."],
  ["Kuka kuljettaja voitti seitsemän formula ykkösten mestaruutta, viisi niistä putkeen vuodesta 2000?", "Michael Schumacher", "Lewis Hamilton", "Sebastian Vettel", "Alain Prost",
   "Viisi perättäistä mestaruutta on yhä pisin putki, ja hän voitti pelkästään 2002 yksitoista seitsemästätoista kilpailusta."])

q(["Which Spaniard won Formula One titles in 2005 and 2006?", "Fernando Alonso", "Carlos Sainz", "Pedro de la Rosa", "Jaime Alguersuari",
   "At 24 he was the youngest champion to that date, and he has started more Grands Prix than anyone."],
  ["Kuka espanjalainen voitti formula ykkösten mestaruuden 2005 ja 2006?", "Fernando Alonso", "Carlos Sainz", "Pedro de la Rosa", "Jaime Alguersuari",
   "Hän oli 24-vuotiaana siihenastinen nuorin mestari, ja hän on ajanut enemmän osakilpailuja kuin kukaan muu."])

q(["Which German won four Formula One titles in a row from 2010 to 2013?", "Sebastian Vettel", "Nico Rosberg", "Nico Hulkenberg", "Ralf Schumacher",
   "He gave each of his cars a girl's name and spoke to the chassis before the start."],
  ["Kuka saksalainen voitti neljä formula ykkösten mestaruutta putkeen vuosina 2010-2013?", "Sebastian Vettel", "Nico Rosberg", "Nico Hülkenberg", "Ralf Schumacher",
   "Hän antoi jokaiselle autolleen tytön nimen ja jutteli korille ennen lähtöä."])

q(["Which German won the Formula One title in 2016 and retired five days later?", "Nico Rosberg", "Sebastian Vettel", "Michael Schumacher", "Timo Glock",
   "His father Keke had won the same title 34 years earlier; they are the second father and son pair to manage it, after the Hills."],
  ["Kuka saksalainen voitti formula ykkösten mestaruuden 2016 ja lopetti viisi päivää myöhemmin?", "Nico Rosberg", "Sebastian Vettel", "Michael Schumacher", "Timo Glock",
   "Hänen isänsä Keke oli voittanut saman tittelin 34 vuotta aiemmin; he ovat Hillien jälkeen toinen isä-poika-mestaripari."])

q(["Which constructor won the drivers' title in 1998, 1999 and 2008?", "McLaren", "Ferrari", "Williams", "Benetton",
   "The team's cars were painted silver for those years but had been orange and then red and white before."],
  ["Mikä talli voitti kuljettajien mestaruuden 1998, 1999 ja 2008?", "McLaren", "Ferrari", "Williams", "Benetton",
   "Tallin autot olivat näinä vuosina hopeiset, mutta aiemmin ne olivat olleet oranssit ja sitten puna-valkoiset."])

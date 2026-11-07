# -*- coding: utf-8 -*-
# Batch 4: Finnish clubs and their cities, ski jumping hills,
#          stadiums and capacities, national team nicknames
# Sources:
#  https://en.wikipedia.org/wiki/Liiga
#  https://en.wikipedia.org/wiki/List_of_ice_hockey_arenas_in_Finland
#  https://en.wikipedia.org/wiki/List_of_ski_jumping_hills
#  https://en.wikipedia.org/wiki/List_of_stadiums_by_capacity
#  https://en.wikipedia.org/wiki/List_of_UEFA_national_association_football_teams_by_nickname
Q = []
def q(en, fi):
    Q.append((["Sport"] + list(en), ["Sport"] + list(fi)))

# ------------------------------------------------- Finnish clubs and their cities
q(["Which club has won more Finnish ice hockey championships than any other?", "Tappara", "TPS", "Karpat", "HIFK",
   "Twenty-one in all, fourteen of them since the league turned professional in 1975, and it plays in Tampere."],
  ["Mikä seura on voittanut enemmän Suomen mestaruuksia jääkiekossa kuin yksikään toinen?", "Tappara", "TPS", "Kärpät", "HIFK",
   "Kaikkiaan kaksikymmentäyksi, niistä neljätoista sen jälkeen kun liiga ammattilaistui 1975, ja seura pelaa Tampereella."])

q(["Which Finnish club has sixteen championships but has won only one since 1975?", "Ilves", "Assat", "HPK", "Lukko",
   "Fifteen of its titles came before the SM-liiga existed, and its last one was in 1985."],
  ["Mikä suomalainen seura on voittanut kuusitoista mestaruutta mutta vain yhden vuoden 1975 jälkeen?", "Ilves", "Ässät", "HPK", "Lukko",
   "Viisitoista mestaruutta tuli ennen SM-liigan perustamista, ja viimeisin oli vuonna 1985."])

q(["Which club won five Finnish championships and no longer plays in the Liiga at all?", "Jokerit", "Kiekko-Espoo", "KooKoo", "Sport",
   "Four titles in the 1990s and one in 2002, and then it left for the Russian league in 2014."],
  ["Mikä seura voitti viisi Suomen mestaruutta eikä pelaa enää lainkaan Liigassa?", "Jokerit", "Kiekko-Espoo", "KooKoo", "Sport",
   "Neljä mestaruutta 1990-luvulla ja yksi 2002, ja sitten se siirtyi Venäjän liigaan vuonna 2014."])

q(["Lukko of Rauma has won two Finnish championships. How far apart are they?", "58 years", "Six years", "Twenty years", "Two years",
   "The first came in 1963 and the second in 2021, which is a long time to keep a town hoping."],
  ["Rauman Lukko on voittanut kaksi Suomen mestaruutta. Kuinka kaukana toisistaan ne ovat?", "58 vuotta", "Kuusi vuotta", "Kaksikymmentä vuotta", "Kaksi vuotta",
   "Ensimmäinen tuli 1963 ja toinen 2021, mikä on pitkä aika pitää kaupunkia toivossa."])

q(["Which club won four Finnish ice hockey championships in five years from 2004?", "Karpat", "Pelicans", "Jukurit", "SaiPa",
   "It won again in 2014, 2015 and 2018, making eight titles in fifteen years for a city of 200,000."],
  ["Mikä seura voitti neljä jääkiekon Suomen mestaruutta viidessä vuodessa vuodesta 2004?", "Kärpät", "Pelicans", "Jukurit", "SaiPa",
   "Se voitti uudelleen 2014, 2015 ja 2018, eli kahdeksan mestaruutta viidessätoista vuodessa kahdensadantuhannen asukkaan kaupungille."])

q(["Which club has won the Finnish championship exactly twice, in 2006 and in 2019?", "HPK", "Ilves", "JYP", "KalPa",
   "It won in 2006 and 2019, and both times it had finished the regular season well down the table."],
  ["Mikä seura on voittanut Suomen mestaruuden täsmälleen kahdesti, vuosina 2006 ja 2019?", "HPK", "Ilves", "JYP", "KalPa",
   "Se voitti 2006 ja 2019, ja kummallakin kerralla runkosarja oli päättynyt kaukana kärjestä."])

q(["Which club won its first ever Finnish ice hockey championship in 2025?", "KalPa", "JYP", "Jukurit", "KooKoo",
   "The club had been playing since the 1920s and had reached a final only once before."],
  ["Mikä seura voitti kaikkien ensimmäisen jääkiekon Suomen mestaruutensa vuonna 2025?", "KalPa", "JYP", "Jukurit", "KooKoo",
   "Seura oli pelannut 1920-luvulta asti ja päässyt finaaliin aiemmin vain kertaalleen."])

q(["Which Liiga club plays in a rink still called a sports park, Kisapuisto?", "SaiPa", "Lukko", "Pelicans", "Sport",
   "It is in Lappeenranta, it is the smallest ground in the league, and the club has never won the championship."],
  ["Mikä Liiga-seura pelaa hallissa, jota kutsutaan yhä kisapuistoksi?", "SaiPa", "Lukko", "Pelicans", "Sport",
   "Se on Lappeenrannassa, se on liigan pienin kenttä, eikä seura ole koskaan voittanut mestaruutta."])

q(["Which club has won the Finnish championship in 2009 and 2012 and at no other time?", "JYP", "KalPa", "HPK", "Jukurit",
   "They are its only two titles, and in between it beat several KHL clubs in European competition."],
  ["Mikä seura on voittanut Suomen mestaruuden 2009 ja 2012 eikä muulloin?", "JYP", "KalPa", "HPK", "Jukurit",
   "Ne ovat sen ainoat kaksi mestaruutta, ja välissä se kaatoi useita KHL-seuroja eurokilpailuissa."])

q(["What do the letters HS stand for on a modern ski jumping hill?", "Hill size", "High speed", "Hill slope", "Height standard",
   "It is the distance from the take-off to the point where the landing slope flattens out too much to land on safely, and it replaced the K-point as the figure everyone quotes."],
  ["Mitä kirjaimet HS tarkoittavat nykyaikaisessa hyppyrimäessä?", "Mäen kokoa", "Suurta nopeutta", "Mäen kaltevuutta", "Korkeusnormia",
   "Se on etäisyys hyppyristä siihen kohtaan, jossa alastulorinne loivenee liikaa turvalliseen laskeutumiseen, ja se korvasi K-pisteen yleisimmin mainittuna lukuna."])

q(["How large must a hill be before it counts as a ski flying hill?", "HS 185 or more", "HS 140 or more", "HS 120 or more", "HS 220 or more",
   "There are only five certified ski flying hills in the world, in Austria, Germany, Norway, Slovenia and the Czech Republic."],
  ["Kuinka suuri mäen on oltava, jotta se lasketaan lentomäeksi?", "HS 185 tai enemmän", "HS 140 tai enemmän", "HS 120 tai enemmän", "HS 220 tai enemmän",
   "Maailmassa on vain viisi hyväksyttyä lentomäkeä: Itävallassa, Saksassa, Norjassa, Sloveniassa ja Tšekissä."])

q(["Which is the largest ski jumping hill in Finland?", "Rukatunturi at Kuusamo", "Salpausselka at Lahti", "Puijo at Kuopio", "Ounasvaara at Rovaniemi",
   "At HS 142 it is bigger than Lahti and Kuopio, both HS 130, and Finland has no ski flying hill at all."],
  ["Mikä on Suomen suurin hyppyrimäki?", "Rukatunturi Kuusamossa", "Salpausselkä Lahdessa", "Puijo Kuopiossa", "Ounasvaara Rovaniemellä",
   "Kokoluokka HS 142 on suurempi kuin Lahden ja Kuopion HS 130, eikä Suomessa ole lainkaan lentomäkeä."])

q(["Two hills in the world are built to HS 240. One is Vikersund in Norway. Where is the other?", "Planica, Slovenia", "Oberstdorf, Germany", "Bad Mitterndorf, Austria", "Harrachov, Czech Republic",
   "The two share the title of largest hill on earth, and every world record jump of recent decades has been made on one of them."],
  ["Maailmassa on kaksi HS 240 -kokoista mäkeä. Toinen on Vikersund Norjassa. Missä on toinen?", "Planicassa Sloveniassa", "Oberstdorfissa Saksassa", "Bad Mitterndorfissa Itävallassa", "Harrachovissa Tšekissä",
   "Nämä kaksi jakavat maailman suurimman mäen tittelin, ja kaikki viime vuosikymmenten maailmanennätyshypyt on tehty jommassakummassa."])

q(["The Lahti ski jumping hills are named Salpausselka. What is a Salpausselka?", "An Ice Age ridge", "A kind of pine", "A lake", "An old parish",
   "The ridges were pushed up at the edge of the retreating ice sheet, and the jumps are built on the side of one of them."],
  ["Lahden hyppyrimäet on nimetty Salpausselän mukaan. Mikä Salpausselkä on?", "Jääkauden reunamuodostuma", "Männyn laji", "Järvi", "Vanha pitäjä",
   "Harjut syntyivät perääntyvän mannerjäätikön reunaan, ja mäet on rakennettu yhden niistä kylkeen."])

q(["Which of Finland's main ski jumping hills is the smallest?", "Ounasvaara at Rovaniemi", "Puijo at Kuopio", "Salpausselka at Lahti", "Rukatunturi at Kuusamo",
   "At HS 97 it is a normal hill rather than a large one, which makes it the furthest north and the least used in competition."],
  ["Mikä Suomen päähyppyrimäistä on pienin?", "Ounasvaara Rovaniemellä", "Puijo Kuopiossa", "Salpausselkä Lahdessa", "Rukatunturi Kuusamossa",
   "HS 97 tekee siitä normaalimäen eikä suurmäkeä, ja se on pohjoisin ja vähiten kilpailukäytössä."])

q(["Which country has the largest hill in the world that is not a ski flying hill?", "Germany", "Austria", "Norway", "Japan",
   "The Muhlenkopfschanze at Willingen is HS 147, and the World Cup event there regularly draws crowds of forty thousand."],
  ["Millä maalla on maailman suurin mäki, joka ei ole lentomäki?", "Saksalla", "Itävallalla", "Norjalla", "Japanilla",
   "Willingenin Mühlenkopfschanze on HS 147, ja sen maailmancupin kilpailu vetää säännöllisesti neljänkymmenentuhannen yleisön."])

# ------------------------------------------------- stadiums and their capacities
q(["What is the largest stadium in the world by capacity?", "A cricket ground in India", "A football ground in Spain", "An American football ground", "An athletics stadium in China",
   "The Narendra Modi Stadium in Ahmedabad holds 132,000, some 33,000 more than Camp Nou, the biggest football-only ground."],
  ["Mikä on maailman suurin stadion katsojamäärältään?", "Krikettistadion Intiassa", "Jalkapallostadion Espanjassa", "Amerikkalaisen jalkapallon stadion", "Yleisurheilustadion Kiinassa",
   "Ahmedabadin Narendra Modi Stadiumille mahtuu 132 000, noin 33 000 enemmän kuin Camp Nou'lle, suurimmalle pelkän jalkapallon kentälle."])

q(["Which sport accounts for most of the ten largest stadiums on earth?", "American college football", "Association football", "Cricket", "Baseball",
   "Eight of the top ten are university grounds in the United States, several of them in towns smaller than Porvoo."],
  ["Mikä laji vastaa suurimmasta osasta maailman kymmentä suurinta stadionia?", "Amerikkalainen jalkapallo yliopistoissa", "Jalkapallo", "Kriketti", "Baseball",
   "Kahdeksan kymmenen kärjessä on yhdysvaltalaisia yliopistokenttiä, useat niistä Porvoota pienemmissä kaupungeissa."])

q(["Which is the largest stadium in Europe?", "Camp Nou", "Wembley", "The Bernabeu", "Croke Park",
   "It holds 99,354 in Barcelona; Wembley at 90,000 is second in Europe, the Bernabeu third and Croke Park in Dublin fourth."],
  ["Mikä on Euroopan suurin stadion?", "Camp Nou", "Wembley", "Bernabéu", "Croke Park",
   "Sille mahtuu Barcelonassa 99 354; Wembley 90 000 katsojallaan on Euroopassa toinen, Bernabéu kolmas ja Dublinin Croke Park neljäs."])

q(["Which country has the world's second largest stadium, holding over 113,000?", "North Korea", "China", "Brazil", "Iran",
   "The Rungrado 1st of May Stadium in Pyongyang is used for mass gymnastic displays as much as for football."],
  ["Millä maalla on maailman toiseksi suurin stadion, jolle mahtuu yli 113 000?", "Pohjois-Korealla", "Kiinalla", "Brasilialla", "Iranilla",
   "Pjongjangin Rungrado 1. toukokuun stadionia käytetään joukkovoimistelunäytöksiin yhtä paljon kuin jalkapalloon."])

q(["Nearly 200,000 people saw the 1950 World Cup decider at the Maracana. What does it hold now?", "About 73,000", "About 120,000", "About 95,000", "About 50,000",
   "Seating and safety rules have cut it by more than half; the 1950 crowd remains the largest ever at a football match."],
  ["Lähes 200 000 ihmistä näki vuoden 1950 MM-ratkaisun Maracanãlla. Kuinka monta sille mahtuu nyt?", "Noin 73 000", "Noin 120 000", "Noin 95 000", "Noin 50 000",
   "Istumapaikat ja turvamääräykset ovat leikanneet sen yli puoleen; vuoden 1950 yleisö on yhä jalkapallo-ottelun suurin koskaan."])

q(["Which is the largest stadium in the southern hemisphere?", "The Melbourne Cricket Ground", "FNB Stadium, Johannesburg", "Estadio Monumental, Buenos Aires", "Stadium Australia, Sydney",
   "It holds 100,024 and is used for cricket in summer and Australian rules football in winter."],
  ["Mikä on eteläisen pallonpuoliskon suurin stadion?", "Melbourne Cricket Ground", "FNB Stadium Johannesburgissa", "Estadio Monumental Buenos Airesissa", "Stadium Australia Sydneyssä",
   "Sille mahtuu 100 024 katsojaa, ja sitä käytetään kesällä krikettiin ja talvella australialaiseen jalkapalloon."])

q(["The Finnish men's football team is called Huuhkajat. What is a huuhkaja?", "An eagle owl", "A wolverine", "A northern pike", "A sea eagle",
   "One flew onto the pitch during a Finland-Belgium match in 2007, stopped play, Finland won, and the bird gave the team its name."],
  ["Suomen miesten jalkapallomaajoukkuetta kutsutaan Huuhkajiksi. Mikä huuhkaja on?", "Pöllölaji", "Näätäeläin", "Kalalaji", "Kotkalaji",
   "Yksi lensi kentälle Suomi-Belgia-ottelussa 2007, keskeytti pelin, Suomi voitti, ja lintu antoi joukkueelle nimensä."])

q(["Finland's women's football team is known as Helmarit. What does the name mean?", "Pearl owls", "Pearl divers", "Pearl girls", "Little pearls",
   "It blends helmi, a pearl, with huuhkaja, the eagle owl of the men's team, and was chosen by a public vote."],
  ["Suomen naisten jalkapallomaajoukkue tunnetaan Helmareina. Mitä nimi tarkoittaa?", "Helmihuuhkajia", "Helmensukeltajia", "Helmityttöjä", "Pikkuhelmiä",
   "Se yhdistää helmen ja miesten joukkueen huuhkajan, ja se valittiin yleisöäänestyksellä."])

q(["Which country's football team has been called the Wunderteam since the 1930s?", "Austria", "Germany", "Hungary", "Switzerland",
   "The name came from a fourteen-match unbeaten run under Hugo Meisl, and it has outlived the team's success by ninety years."],
  ["Minkä maan jalkapallomaajoukkuetta on kutsuttu Wunderteamiksi 1930-luvulta asti?", "Itävallan", "Saksan", "Unkarin", "Sveitsin",
   "Nimi syntyi neljäntoista ottelun häviöttömästä putkesta Hugo Meislin johdolla, ja se on elänyt menestystä yhdeksänkymmentä vuotta pidempään."])

q(["Why was the Dutch football team of the 1970s called Clockwork Orange?", "For its precise passing", "For its orange boots", "For a sponsor", "For its violent play",
   "A pun on the film title, applied to a side so well drilled that it reached two World Cup finals and lost both."],
  ["Miksi 1970-luvun Hollannin jalkapallomaajoukkuetta kutsuttiin nimellä Clockwork Orange?", "Täsmällisen syöttöpelin takia", "Oranssien kenkien takia", "Sponsorin takia", "Kovan pelin takia",
   "Sanaleikki elokuvan nimestä, annettu joukkueelle joka oli niin harjoitettu että pääsi kahteen MM-finaaliin ja hävisi molemmat."])

q(["Italy's football team is Gli Azzurri, the Blues. Where does the blue come from?", "The House of Savoy", "The Mediterranean", "The flag", "A kit sponsor",
   "It is the colour of the royal family's coat of arms, and Italy kept it long after it stopped being a monarchy."],
  ["Italian jalkapallomaajoukkue on Gli Azzurri, siniset. Mistä sininen tulee?", "Savoian suvusta", "Välimerestä", "Lipusta", "Pelipaidan sponsorista",
   "Se on kuningassuvun vaakunan väri, ja Italia säilytti sen kauan sen jälkeen kun maa lakkasi olemasta kuningaskunta."])

q(["England's nickname, the Three Lions, comes from a coat of arms first recorded in which century?", "The twelfth", "The sixteenth", "The eighteenth", "The fourteenth",
   "The three lions appear on a royal seal of 1198, so the badge is some seven hundred years older than the football association."],
  ["Englannin lempinimi Kolme leijonaa tulee vaakunasta, joka on ensi kerran kirjattu millä vuosisadalla?", "1100-luvulla", "1500-luvulla", "1700-luvulla", "1300-luvulla",
   "Kolme leijonaa esiintyy vuoden 1198 kuninkaallisessa sinetissä, joten tunnus on noin seitsemänsataa vuotta jalkapalloliittoa vanhempi."])

q(["Which country's football team is nicknamed Drillos, after a man rather than a symbol?", "Norway", "Denmark", "Sweden", "Iceland",
   "Egil Olsen, known as Drillo, managed the team in the 1990s and his nickname attached itself to the whole side."],
  ["Minkä maan jalkapallomaajoukkuetta kutsutaan Drilloksiksi, miehen eikä tunnuksen mukaan?", "Norjan", "Tanskan", "Ruotsin", "Islannin",
   "Egil Olsen, kutsumanimeltään Drillo, valmensi joukkuetta 1990-luvulla, ja hänen lempinimensä tartutettiin koko joukkueeseen."])

q(["Portugal's team is the Selecao das Quinas. What are the quinas?", "Shields on the coat of arms", "Five hills", "Coastal towns", "A kind of wine",
   "They are the five small shields arranged on the national arms, each bearing five dots, and the national team is named after them rather than a colour or an animal."],
  ["Portugalin maajoukkue on Seleção das Quinas. Mitä quinat ovat?", "Vaakunan kilpiä", "Viisi kukkulaa", "Rannikkokaupunkeja", "Viinilaji",
   "Ne ovat kansallisvaakunan viisi pientä kilpeä, joissa kussakin on viisi pistettä, ja maajoukkue on nimetty niiden eikä värin tai eläimen mukaan."])

q(["What does Croatia's football nickname Vatreni mean?", "The fiery ones", "The chequered ones", "The brave ones", "The sons of the sea",
   "Vatra means fire; the team is also called Kockasti, the chequered ones, after the red and white squares on the shirt."],
  ["Mitä Kroatian jalkapallolempinimi Vatreni tarkoittaa?", "Tulisia", "Ruudullisia", "Rohkeita", "Meren poikia",
   "Vatra tarkoittaa tulta; joukkuetta kutsutaan myös nimellä Kockasti, ruudulliset, pelipaidan puna-valkoisten ruutujen mukaan."])

q(["Switzerland's football team is simply called Nati. What is that short for?", "Nationalmannschaft", "Nativi", "National Eleven", "Nati Rossi",
   "It is the German for national team, used in a country with four official languages because no better compromise was found."],
  ["Sveitsin jalkapallomaajoukkuetta kutsutaan vain Natiksi. Minkä lyhenne se on?", "Sanasta Nationalmannschaft", "Sanasta Nativi", "Sanoista National Eleven", "Sanoista Nati Rossi",
   "Se on saksan kielen maajoukkue, käytössä neljän virallisen kielen maassa, koska parempaa kompromissia ei löytynyt."])

q(["Which decade gave the Danish football team the nickname Danish Dynamite?", "The 1980s", "The 1950s", "The 1990s", "The 2010s",
   "The side of Elkjaer and Laudrup played thrilling football, were everyone's second favourite team, and won nothing at all."],
  ["Mikä vuosikymmen antoi Tanskan jalkapallomaajoukkueelle lempinimen Danish Dynamite?", "1980-luku", "1950-luku", "1990-luku", "2010-luku",
   "Elkjaerin ja Laudrupin joukkue pelasi vauhdikasta jalkapalloa, oli kaikkien kakkossuosikki eikä voittanut yhtään mitään."])

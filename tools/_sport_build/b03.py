# -*- coding: utf-8 -*-
# Batch 3: long-standing athletics world records, the marathon distance,
#          boxing weight classes, dropped Olympic sports, Grand Slam venues
# Sources:
#  https://en.wikipedia.org/wiki/List_of_world_records_in_athletics
#  https://en.wikipedia.org/wiki/Athletics_at_the_1908_Summer_Olympics_%E2%80%93_Men%27s_marathon
#  https://en.wikipedia.org/wiki/Weight_class_(boxing)
#  https://www.topendsports.com/events/discontinued/list.htm
#  https://stadiumdb.com/news/2018/10/comparing_the_big_four_global_tennis_stadiums
Q = []
def q(en, fi):
    Q.append((["Sport"] + list(en), ["Sport"] + list(fi)))

# ----------------------------------------------- athletics records that have stood
q(["Jarmila Kratochvilova's world record of 1:53.28, set in 1983, is in which event?", "The women's 800 metres", "The women's 1500 metres", "The women's 400 metres", "The women's mile",
   "It is the oldest standing record in athletics; no woman has come within a second of it in more than forty years."],
  ["Jarmila Kratochvílován vuonna 1983 tekemä maailmanennätys 1.53,28 on missä lajissa?", "Naisten 800 metrillä", "Naisten 1500 metrillä", "Naisten 400 metrillä", "Naisten mailissa",
   "Se on yleisurheilun vanhin voimassa oleva ennätys; yksikään nainen ei ole päässyt sekunnin päähän siitä yli neljässäkymmenessä vuodessa."])

q(["In which event did Marita Koch of East Germany run 47.60 in 1985?", "The 400 metres", "The 200 metres", "The 800 metres", "The 300 metres",
   "It is still quicker than any woman has run since, and the East German records of that decade have never been struck from the books."],
  ["Missä lajissa itäsaksalainen Marita Koch juoksi 47,60 vuonna 1985?", "400 metrillä", "200 metrillä", "800 metrillä", "300 metrillä",
   "Se on yhä nopeampi kuin yksikään naisen juoksema aika sen jälkeen, eikä tuon vuosikymmenen itäsaksalaisia ennätyksiä ole koskaan pyyhitty pois."])

q(["Mike Powell jumped 8.95 metres in Tokyo in 1991. Whose record did that beat?", "Bob Beamon's", "Carl Lewis's", "Jesse Owens's", "Ralph Boston's",
   "Beamon's 8.90 from the thin air of Mexico City had stood for 23 years, and Carl Lewis jumped 8.91 in the same competition with too much wind."],
  ["Mike Powell hyppäsi 8,95 metriä Tokiossa 1991. Kenen ennätyksen se kaatoi?", "Bob Beamonin", "Carl Lewisin", "Jesse Owensin", "Ralph Bostonin",
   "Beamonin 8,90 Mexico Cityn ohuesta ilmasta oli kestänyt 23 vuotta, ja Carl Lewis hyppäsi samassa kilpailussa 8,91 liian kovassa myötätuulessa."])

q(["Javier Sotomayor's high jump world record of 2.45 m has stood since 1993. How tall is he?", "1.95 m", "2.10 m", "1.75 m", "2.25 m",
   "So he cleared half a metre above his own head, and no one has matched the bar in over thirty years."],
  ["Javier Sotomayorin korkeushypyn maailmanennätys 2,45 m on ollut voimassa vuodesta 1993. Kuinka pitkä hän on?", "195 cm", "210 cm", "175 cm", "225 cm",
   "Hän ylitti siis puoli metriä oman päänsä yläpuolelta, eikä kukaan ole toistanut korkeutta yli kolmessakymmenessä vuodessa."])

q(["Jonathan Edwards broke the triple jump world record twice in 1995. How far apart?", "Twenty minutes", "Three weeks", "A year", "Two days",
   "He jumped 18.16 and then 18.29 in consecutive attempts at the Gothenburg world championships, and the second still stands."],
  ["Jonathan Edwards rikkoi kolmiloikan maailmanennätyksen kahdesti vuonna 1995. Kuinka pitkän ajan sisällä?", "Kahdenkymmenen minuutin", "Kolmen viikon", "Vuoden", "Kahden päivän",
   "Hän loikkasi 18,16 ja heti perään 18,29 Göteborgin MM-kisoissa, ja jälkimmäinen on yhä voimassa."])

q(["Why has nobody thrown a javelin 100 metres?", "The javelin was redesigned to fly shorter", "The run-up was shortened", "The javelin was made heavier", "Tailwinds were banned",
   "In 1986 the centre of gravity was moved forward so that throws would stop landing among the spectators; the record with the new spear is 98.48 m."],
  ["Miksi kukaan ei ole heittänyt keihästä sataa metriä?", "Keihäs muutettiin lentämään lyhyemmin", "Vauhdinottoa lyhennettiin", "Keihästä painotettiin", "Myötätuuli kiellettiin",
   "Vuonna 1986 painopistettä siirrettiin eteen, jotta heitot lakkaisivat putoamasta katsojien keskelle; uuden keihään ennätys on 98,48 metriä."])

q(["Yuriy Sedykh set a world record in 1986 that still stands. In which event?", "The hammer throw", "The discus", "The shot put", "The javelin",
   "86.74 metres, and no hammer thrower in forty years has come within a metre of it."],
  ["Juri Sedyh teki vuonna 1986 maailmanennätyksen, joka on yhä voimassa. Missä lajissa?", "Moukarinheitossa", "Kiekonheitossa", "Kuulantyönnössä", "Keihäänheitossa",
   "86,74 metriä, eikä yksikään moukarinheittäjä neljässäkymmenessä vuodessa ole päässyt metrin päähän siitä."])

q(["Florence Griffith Joyner's 100 metres record of 10.49 has been argued over ever since. Why?", "The wind gauge read zero", "The track was short", "The timing failed", "She was disqualified later",
   "Nearby gauges at the 1988 US trials showed a strong tailwind while hers showed none, and the mark has stood for nearly forty years."],
  ["Florence Griffith Joynerin satasen ennätyksestä 10,49 on kiistelty siitä asti. Miksi?", "Tuulimittari näytti nollaa", "Rata oli liian lyhyt", "Ajanotto petti", "Hänet hylättiin jälkikäteen",
   "Vuoden 1988 USA:n karsinnoissa lähellä olevat mittarit näyttivät kovaa myötätuulta ja hänen omansa ei mitään, ja tulos on kestänyt lähes neljäkymmentä vuotta."])

q(["Usain Bolt ran 9.58 for 100 metres in 2009. At which championships?", "Berlin", "London", "Beijing", "Moscow",
   "He took eleven hundredths off his own record, the biggest single improvement since electronic timing began."],
  ["Usain Bolt juoksi sadan metrin ajan 9,58 vuonna 2009. Missä arvokilpailuissa?", "Berliinissä", "Lontoossa", "Pekingissä", "Moskovassa",
   "Hän otti omasta ennätyksestään yksitoista sadasosaa, suurimman yksittäisen parannuksen sähköisen ajanoton aikana."])

q(["Which country's runner has held the men's 1500 metres world record since 1998?", "Morocco", "Kenya", "Ethiopia", "Algeria",
   "Hicham El Guerrouj ran 3:26.00 in Rome, having fallen in two Olympic finals before he finally won in Athens in 2004."],
  ["Minkä maan juoksija on pitänyt miesten 1500 metrin maailmanennätystä vuodesta 1998?", "Marokon", "Kenian", "Etiopian", "Algerian",
   "Hicham El Guerrouj juoksi Roomassa 3.26,00, ja hän oli kaatunut kahdessa olympiafinaalissa ennen kuin voitti vihdoin Ateenassa 2004."])

q(["The women's shot put world record of 22.63 m dates from which decade?", "The 1980s", "The 1960s", "The 2000s", "The 2010s",
   "Natalya Lisovskaya set it in 1987, and no woman has thrown within a metre of it since."],
  ["Miltä vuosikymmeneltä naisten kuulantyönnön maailmanennätys 22,63 m on?", "1980-luvulta", "1960-luvulta", "2000-luvulta", "2010-luvulta",
   "Natalja Lisovskaja työnsi sen 1987, eikä yksikään nainen ole sen jälkeen päässyt metrin päähän."])

q(["Jackie Joyner-Kersee's heptathlon world record has stood since which year?", "1988", "1996", "2004", "1980",
   "She scored 7291 points at the Seoul Olympics, and nobody since has come within 200 points of it."],
  ["Miltä vuodelta Jackie Joyner-Kerseen seitsenottelun maailmanennätys on?", "Vuodelta 1988", "Vuodelta 1996", "Vuodelta 2004", "Vuodelta 1980",
   "Hän keräsi 7291 pistettä Seoulin olympialaisissa, eikä kukaan ole sen jälkeen päässyt kahdensadan pisteen päähän."])

q(["The men's 4x400 metres relay world record has stood since 1993. Which country set it?", "United States", "Jamaica", "Kenya", "Soviet Union",
   "The four men averaged about 43.6 seconds each, with Michael Johnson running the anchor leg in Stuttgart."],
  ["Miesten 4x400 metrin viestin maailmanennätys on ollut voimassa vuodesta 1993. Mikä maa sen teki?", "Yhdysvallat", "Jamaika", "Kenia", "Neuvostoliitto",
   "Neljä miestä juoksi keskimäärin noin 43,6 sekuntia kukin, ja Michael Johnson ankkuroi Stuttgartissa."])

# ----------------------------------------------- the marathon distance
q(["The 1908 Olympic marathon fixed the distance still run today. What decided the odd 385 yards?", "The position of the Royal Box", "A measuring error", "The length of a lap", "A bet",
   "The runners entered the stadium opposite the box and the direction of running was reversed so the finish could be seen from it, leaving 385 yards instead of a full lap."],
  ["Vuoden 1908 olympiamaraton vakiinnutti nykyisin juostavan matkan. Mikä ratkaisi oudot 385 jaardia?", "Kuninkaallisen aition paikka", "Mittausvirhe", "Kierroksen pituus", "Vedonlyönti",
   "Juoksijat tulivat stadionille aitiota vastapäätä ja juoksusuunta käännettiin, jotta maali näkyisi aitiosta, joten kierroksen sijaan jäi 385 jaardia."])

q(["Where did the 1908 Olympic marathon start?", "At Windsor Castle", "At Hyde Park", "At Tower Bridge", "At Greenwich",
   "It began on the path beside the castle's East Lawn and finished in front of the Royal Box at White City, 26 miles and 385 yards later."],
  ["Mistä vuoden 1908 olympiamaraton lähti?", "Windsorin linnalta", "Hyde Parkista", "Tower Bridgeltä", "Greenwichistä",
   "Se alkoi linnan itäisen puiston viereiseltä tieltä ja päättyi kuninkaallisen aition eteen White Cityssä 26 mailia ja 385 jaardia myöhemmin."])

q(["In which year was 42.195 km made the official marathon distance?", "1921", "1908", "1896", "1936",
   "Thirteen years after the London race it copies, and the governing body never properly explained why that particular course was chosen."],
  ["Minä vuonna 42,195 kilometristä tehtiin maratonin virallinen matka?", "Vuonna 1921", "Vuonna 1908", "Vuonna 1896", "Vuonna 1936",
   "Kolmetoista vuotta sen Lontoon kilpailun jälkeen, jota se jäljittelee, eikä kattojärjestö koskaan selittänyt kunnolla miksi juuri tuo rata valittiin."])

q(["Dorando Pietri crossed the line first in the 1908 Olympic marathon. Why was he not the winner?", "Officials had helped him up", "He had run the wrong way", "He had started early", "He was over the age limit",
   "He collapsed five times inside the stadium and umpires lifted him each time; he was disqualified, and Queen Alexandra gave him a cup the next day instead."],
  ["Dorando Pietri ylitti maaliviivan ensimmäisenä vuoden 1908 olympiamaratonissa. Miksei hän ollut voittaja?", "Toimitsijat olivat auttaneet hänet ylös", "Hän oli juossut väärään suuntaan", "Hän oli lähtenyt etuajassa", "Hän oli yli ikärajan",
   "Hän kaatui stadionilla viisi kertaa ja tuomarit nostivat hänet joka kerta; hänet hylättiin, ja kuningatar Aleksandra antoi hänelle seuraavana päivänä pokaalin."])

q(["The 1896 Olympic marathon was run over what distance?", "40 kilometres", "42.195 kilometres", "35 kilometres", "45 kilometres",
   "The distance changed from Games to Games until 1921, so the early winners' times cannot be compared with anything."],
  ["Minkä matkan vuoden 1896 olympiamaraton oli?", "40 kilometriä", "42,195 kilometriä", "35 kilometriä", "45 kilometriä",
   "Matka vaihtui kisoista kisoihin vuoteen 1921 asti, joten varhaisten voittajien aikoja ei voi verrata mihinkään."])

# ----------------------------------------------- boxing weight classes
q(["Which of these is NOT one of boxing's original eight weight divisions?", "Super middleweight", "Flyweight", "Welterweight", "Light heavyweight",
   "The traditional eight are flyweight, bantamweight, featherweight, lightweight, welterweight, middleweight, light heavyweight and heavyweight; the rest were added after the 1960s."],
  ["Mikä näistä ei kuulu nyrkkeilyn kahdeksaan alkuperäiseen painoluokkaan?", "Supervälisarja", "Kärpässarja", "Välisarja", "Raskaansarjan alasarja",
   "Perinteiset kahdeksan ovat kärpäs-, bantam-, kevyen-, kevyt-, väli-, keskiraskas-, raskaan alasarja ja raskas; muut lisättiin 1960-luvun jälkeen."])

q(["How many professional boxing weight divisions are recognised today?", "Nineteen", "Eight", "Twelve", "Twenty-six",
   "Eighteen have a ceiling and heavyweight has none; there were eight until the governing bodies split and began inventing super and junior classes."],
  ["Kuinka monta ammattilaisnyrkkeilyn painoluokkaa on nykyään tunnustettu?", "Yhdeksäntoista", "Kahdeksan", "Kaksitoista", "Kaksikymmentäkuusi",
   "Kahdeksallatoista on yläraja ja raskaalla sarjalla ei ole; luokkia oli kahdeksan, kunnes kattojärjestöt hajaantuivat ja alkoivat keksiä super- ja juniorisarjoja."])

q(["Which boxing division did the WBC invent in 2020, between cruiserweight and heavyweight?", "Bridgerweight", "Super heavyweight", "Megaweight", "Prime weight",
   "Its ceiling is 224 pounds, the WBA calls it super cruiserweight, and hardly anyone fights in it."],
  ["Minkä nyrkkeilyluokan WBC keksi vuonna 2020 cruiser- ja raskaansarjan väliin?", "Bridgersarja", "Superraskas sarja", "Megasarja", "Priimasarja",
   "Sen yläraja on 224 paunaa, WBA kutsuu sitä supercruisersarjaksi, eikä siinä nyrkkeile juuri kukaan."])

q(["In how many of boxing's original eight divisions did Manny Pacquiao win world titles?", "Four", "Two", "Six", "Eight",
   "Flyweight, featherweight, lightweight and welterweight, a span of 35 pounds, which is about sixteen kilos of the same man."],
  ["Kuinka monessa nyrkkeilyn kahdeksasta alkuperäisestä luokasta Manny Pacquiao voitti maailmanmestaruuden?", "Neljässä", "Kahdessa", "Kuudessa", "Kahdeksassa",
   "Kärpäs-, kevyen-, kevyt- ja välisarjassa, eli 35 paunan haarukassa, mikä on noin kuusitoista kiloa samaa miestä."])

q(["Which American law of 1920 gave boxing its standard weight limits?", "The Walker Law", "The Volstead Act", "The Queensberry Act", "The Dempsey Law",
   "It set up the New York State Athletic Commission; before 1909 sources could not even agree what counted as a light weight."],
  ["Mikä yhdysvaltalainen laki vuodelta 1920 antoi nyrkkeilylle vakiopainorajat?", "Walkerin laki", "Volsteadin laki", "Queensberryn laki", "Dempseyn laki",
   "Se perusti New Yorkin osavaltion urheilukomission; ennen vuotta 1909 lähteet eivät päässeet yksimielisyyteen siitä, mikä oli kevyt paino."])

# ----------------------------------------------- Olympic sports that were dropped
q(["Which sport was an Olympic event at six Games up to 1920 and has never come back?", "Tug of war", "Croquet", "Polo", "Lacrosse",
   "It ran from 1900 to 1920, and in 1908 British police teams took all three medals between them."],
  ["Mikä laji oli olympialaji kuusissa kisoissa vuoteen 1920 eikä ole koskaan palannut?", "Köydenveto", "Krokeetti", "Poolo", "Lacrosse",
   "Se oli ohjelmassa 1900-1920, ja vuonna 1908 brittiläiset poliisijoukkueet jakoivat keskenään kaikki kolme mitalia."])

q(["Which of these has genuinely been an Olympic sport?", "Croquet", "Darts", "Bowling", "Chess",
   "Paris 1900 only; every competitor was French and the crowd is said to have consisted of one paying spectator."],
  ["Mikä näistä on todella ollut olympialaji?", "Krokeetti", "Tikanheitto", "Keilailu", "Shakki",
   "Vain Pariisissa 1900; kaikki kilpailijat olivat ranskalaisia, ja yleisöä kerrotaan olleen yksi maksanut katsoja."])

q(["Which contest handed out Olympic medals from 1912 to 1948 without any sport being played?", "Art competitions", "Fair play awards", "Sports journalism", "Coaching",
   "There were medals for painting, sculpture, architecture, literature and music on sporting themes, and Pierre de Coubertin won a literature gold under a pseudonym."],
  ["Mikä kilpailu jakoi olympiamitaleja vuosina 1912-1948 ilman että mitään lajia urheiltiin?", "Taidekilpailut", "Reilun pelin palkinnot", "Urheilujournalismi", "Valmennus",
   "Mitaleja jaettiin urheiluaiheisesta maalaustaiteesta, kuvanveistosta, arkkitehtuurista, kirjallisuudesta ja musiikista, ja Pierre de Coubertin voitti kirjallisuuskullan salanimellä."])

q(["Which swimming event, held once in 1904, was won without swimming a stroke?", "The plunge for distance", "The obstacle race", "Underwater swimming", "The sailors' freestyle",
   "Competitors dived in and glided face down, motionless, and whoever drifted furthest won; the sport was judged too dull to repeat."],
  ["Mikä uintilaji, joka järjestettiin kertaalleen 1904, voitettiin uimatta yhtäkään vetoa?", "Pituussukellus", "Esterata", "Vedenalainen uinti", "Merimiesten vapaauinti",
   "Kilpailijat hyppäsivät veteen ja liukuivat kasvot alaspäin liikkumatta, ja pisimmälle valunut voitti; lajia pidettiin liian tylsänä toistettavaksi."])

q(["Which motorised sport awarded Olympic medals in 1908?", "Motor boating", "Motor racing", "Motorcycling", "Aviation",
   "It is the only time engines have competed for Olympic medals, and the weather was so bad that in two of the three races only one boat finished."],
  ["Mikä moottoroitu laji jakoi olympiamitaleja vuonna 1908?", "Moottoriveneily", "Autourheilu", "Moottoripyöräily", "Lentäminen",
   "Se on ainoa kerta, kun moottorit ovat kilpailleet olympiamitaleista, ja sää oli niin huono, että kahdessa kolmesta kilpailusta maaliin tuli vain yksi vene."])

q(["Which gymnastics event was an Olympic sport five times, the last in 1932?", "Rope climbing", "Club swinging", "Tumbling", "The sidehorse vault",
   "It was contested in 1896, 1904, 1906, 1924 and 1932, judged on speed and, in the early years, on style as well."],
  ["Mikä voimistelulaji oli olympialaji viisi kertaa, viimeksi 1932?", "Köysikiipeily", "Keilojen heiluttelu", "Trampoliinivoltit", "Sivuttaishyppy",
   "Se kilpailtiin 1896, 1904, 1906, 1924 ja 1932, ja arvostelu perustui nopeuteen ja alkuvuosina myös tyyliin."])

q(["Which cycling event, raced by two riders on one bicycle, left the Olympics after 1972?", "The tandem sprint", "The madison", "The points race", "The team pursuit",
   "Two men on one bike over 2000 metres, in and out of the programme since 1906, and gone for good when the track events were reorganised."],
  ["Mikä pyöräilylaji, jossa kaksi ajajaa oli samalla pyörällä, poistui olympialaisista vuoden 1972 jälkeen?", "Tandemsprintti", "Madison", "Pistekilpailu", "Joukkueajo",
   "Kaksi miestä yhdellä pyörällä 2000 metrin matkalla, ohjelmassa ja pois siitä vuodesta 1906, ja lopullisesti pois ratalajien uudistuksessa."])

q(["Which swimming event was in the Olympics in 1984, 1988 and 1992 and then dropped?", "Solo synchronised swimming", "The 200 metres freestyle", "Plain high diving", "The 400 metres breaststroke",
   "A judged sport with no opponent in the pool at all; the duet and the team event survived, the soloist did not."],
  ["Mikä uintilaji oli olympialaisissa 1984, 1988 ja 1992 ja poistettiin sitten?", "Taitouinnin yksinohjelma", "200 metrin vapaauinti", "Korkeussukellus", "400 metrin rintauinti",
   "Arvosteltava laji, jossa altaassa ei ollut lainkaan vastustajaa; pari- ja joukkuekilpailu jäivät, yksinuija ei."])

q(["Which of these was an Olympic athletics event before 1913?", "The standing long jump", "The standing shot put", "The standing hurdles", "The standing pole vault",
   "The standing high, long and triple jumps were all contested up to 1912, and the American Ray Ewry won eight golds in them."],
  ["Mikä näistä oli olympialaisten yleisurheilulaji ennen vuotta 1913?", "Pituushyppy paikaltaan", "Kuulantyöntö paikaltaan", "Aitajuoksu paikaltaan", "Seiväshyppy paikaltaan",
   "Korkeus-, pituus- ja kolmiloikka paikaltaan olivat kaikki ohjelmassa vuoteen 1912, ja amerikkalainen Ray Ewry voitti niissä kahdeksan kultaa."])

q(["Which team sport was in the Olympics only in 1936, played eleven a side on a full-sized field?", "Field handball", "Field hockey", "Water polo", "Korfball",
   "Germany won it at home in front of a huge crowd; the indoor seven-a-side version replaced it when handball returned in 1972."],
  ["Mikä joukkuelaji oli olympialaisissa vain 1936, pelattuna yksitoista vastaan yksitoista isolla kentällä?", "Kenttäkäsipallo", "Maahockey", "Vesipallo", "Korfball",
   "Saksa voitti sen kotonaan suuren yleisön edessä; sisätilojen seitsemän pelaajan versio korvasi sen, kun käsipallo palasi 1972."])

q(["Which sport was an Olympic event five times, the last in 1936, and is played on horseback?", "Polo", "Vaulting", "Horse long jump", "Tent pegging",
   "It appeared in 1900, 1908, 1920, 1924 and 1936, and Argentina won the last two tournaments."],
  ["Mikä laji oli olympialaji viisi kertaa, viimeksi 1936, ja sitä pelataan hevosen selässä?", "Poolo", "Volttiratsastus", "Hevosen pituushyppy", "Keihäspoiminta",
   "Se oli ohjelmassa 1900, 1908, 1920, 1924 ja 1936, ja Argentiina voitti kaksi viimeistä turnausta."])

q(["Which equestrian events were contested at the 1900 Olympics and never again?", "High jump and long jump", "Steeplechase and polo", "Sidesaddle and vaulting", "Chariot racing",
   "Horses jumped for height and distance as athletes do, and both events disappeared after one outing in Paris."],
  ["Mitkä ratsastuslajit kilpailtiin vuoden 1900 olympialaisissa eikä enää koskaan?", "Korkeus- ja pituushyppy", "Esteratsastus ja poolo", "Sivusatula ja voltti", "Vaunuajot",
   "Hevoset hyppäsivät korkeutta ja pituutta kuten urheilijat, ja molemmat lajit katosivat yhden Pariisin esiintymisen jälkeen."])

q(["Which old French racket game, played off the walls indoors, was an Olympic sport in 1908?", "Jeu de paume", "Basque pelota", "Rackets", "Roque",
   "Real tennis, the game lawn tennis descends from; it appeared once and has never returned."],
  ["Mikä vanha ranskalainen mailapeli, jota pelataan sisällä seinistä, oli olympialaji vuonna 1908?", "Jeu de paume", "Pelota", "Rackets", "Roque",
   "Kyseessä on kuningastennis, josta nykyinen tennis on kehittynyt; se nähtiin kertaalleen eikä ole palannut."])

q(["Which two bat-and-ball sports were dropped after 2008 and brought back for one Games in 2021?", "Baseball and softball", "Cricket and rounders", "Pesapallo and baseball", "Softball and lacrosse",
   "The Tokyo organisers were allowed to add sports of local interest, and both went out again straight afterwards."],
  ["Mitkä kaksi maila- ja pallolajia poistettiin vuoden 2008 jälkeen ja tuotiin takaisin yksiin kisoihin 2021?", "Baseball ja softball", "Kriketti ja rounders", "Pesäpallo ja baseball", "Softball ja lacrosse",
   "Tokion järjestäjät saivat lisätä paikallisesti kiinnostavia lajeja, ja molemmat lensivät heti perään ulos."])

# ----------------------------------------------- Grand Slam venues
q(["Which Grand Slam complex is named after a First World War fighter pilot?", "Roland-Garros", "Flushing Meadows", "Melbourne Park", "The All England Club",
   "Roland Garros was an aviator who died in 1918 and had nothing to do with tennis; a friend who ran the club insisted on the name."],
  ["Mikä Grand Slam -keskus on nimetty ensimmäisen maailmansodan hävittäjälentäjän mukaan?", "Roland-Garros", "Flushing Meadows", "Melbourne Park", "All England Club",
   "Roland Garros oli lentäjä, joka kuoli 1918 eikä ollut tekemisissä tenniksen kanssa; seuraa johtanut ystävä vaati nimeä."])

q(["Which Grand Slam show court was the first to get a retractable roof?", "Rod Laver Arena", "Centre Court", "Arthur Ashe Stadium", "Court Philippe-Chatrier",
   "Melbourne built it in 1988, two decades before Wimbledon; the city's heat was as much the reason as its rain."],
  ["Mikä Grand Slam -pääkenttä sai ensimmäisenä avattavan katon?", "Rod Laver Arena", "Centre Court", "Arthur Ashe Stadium", "Court Philippe-Chatrier",
   "Melbourne rakensi sen 1988, kaksi vuosikymmentä ennen Wimbledonia; syynä oli yhtä lailla kaupungin helle kuin sade."])

q(["Which Grand Slam has the largest main stadium?", "The US Open", "Wimbledon", "The Australian Open", "The French Open",
   "Arthur Ashe Stadium holds about 23,000, against roughly 15,000 at Centre Court and 14,800 at Rod Laver Arena."],
  ["Millä Grand Slamilla on suurin pääkenttä?", "US Openilla", "Wimbledonilla", "Australian avoimilla", "Ranskan avoimilla",
   "Arthur Ashe Stadiumille mahtuu noin 23 000, kun Centre Courtille mahtuu noin 15 000 ja Rod Laver Arenalle 14 800."])

q(["The US Open is played on the site of what?", "A World's Fair ground", "A racecourse", "A naval yard", "A film studio",
   "Flushing Meadows hosted the World's Fairs of 1939 and 1964, and the park was built on what had been an ash dump."],
  ["US Open pelataan minkä paikalla?", "Maailmannäyttelyn alueella", "Raviradan paikalla", "Laivastotelakan paikalla", "Filmistudion paikalla",
   "Flushing Meadows isännöi maailmannäyttelyitä 1939 ja 1964, ja puisto rakennettiin entiselle tuhkankaatopaikalle."])

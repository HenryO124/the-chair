# -*- coding: utf-8 -*-
# Batch 5: rules that changed, and why
# Sources:
#  https://en.wikipedia.org/wiki/Back-pass_rule
#  https://en.wikipedia.org/wiki/Rules_of_basketball
Q = []
def q(en, fi):
    Q.append((["Sport"] + list(en), ["Sport"] + list(fi)))

q(["Football's back-pass rule arrived in 1992. Which tournament had made it necessary?", "The 1990 World Cup", "The 1988 European Championship", "The 1986 World Cup", "The 1991 Copa America",
   "It was widely called the dullest World Cup ever played, full of back-passes and goalkeepers standing on the ball to run the clock down."],
  ["Jalkapallon takapotkusääntö tuli 1992. Mikä turnaus oli tehnyt siitä tarpeellisen?", "Vuoden 1990 MM-kilpailut", "Vuoden 1988 EM-kilpailut", "Vuoden 1986 MM-kilpailut", "Vuoden 1991 Copa América",
   "Niitä pidettiin laajalti tylsimpinä koskaan pelattuina MM-kisoina: täynnä takapotkuja ja pallon päällä aikaa kuluttavia maalivahteja."])

q(["Despite its name, football's back-pass rule applies to a pass in which direction?", "Any direction", "Backwards only", "Backwards or sideways", "Towards the goal line",
   "What matters is that a team-mate deliberately kicked it to the keeper, not where on the pitch either of them was standing."],
  ["Nimestään huolimatta jalkapallon takapotkusääntö koskee syöttöä mihin suuntaan?", "Mihin tahansa suuntaan", "Vain taaksepäin", "Taakse tai sivulle", "Maaliviivaa kohti",
   "Ratkaisevaa on se, että joukkuekaveri potkaisi pallon maalivahdille tarkoituksella, eikä se, missä kohdassa kenttää kumpikaan seisoi."])

q(["A keeper may not pick up a team-mate's deliberate kick. What about a deliberate header?", "He may pick it up", "He may not touch it", "He may only kick it", "He must let it go out",
   "The laws define a kick as using the foot, so head, chest, shin and knee are all fine; but a defender may not flick the ball up on purpose to get round the rule."],
  ["Maalivahti ei saa nostaa joukkuekaverin tarkoituksellista potkua. Miten on tarkoituksellisen puskun kanssa?", "Hän saa nostaa sen", "Hän ei saa koskea siihen", "Hän saa vain potkaista sitä", "Hänen on päästettävä se ulos",
   "Säännöt määrittelevät potkun jalalla tehdyksi, joten pää, rinta, sääri ja polvi ovat sallittuja; puolustaja ei silti saa nostaa palloa tahallaan kiertääkseen säännön."])

q(["What is the punishment for a goalkeeper breaking the back-pass rule?", "An indirect free kick", "A penalty", "A yellow card", "A corner",
   "It is taken where the handling happened, or from the nearest point on the six-yard line if that was inside the six-yard box."],
  ["Mikä on seuraus siitä, että maalivahti rikkoo takapotkusääntöä?", "Epäsuora vapaapotku", "Rangaistuspotku", "Keltainen kortti", "Kulmapotku",
   "Se potkaistaan siitä, missä käsin koskeminen tapahtui, tai lähimmästä pisteestä maalialueen rajalla jos paikka oli maalialueen sisällä."])

q(["In 1997 the back-pass rule was extended to cover the ball reaching the keeper from what?", "A team-mate's throw-in", "A corner", "A goal kick", "A headed clearance",
   "The first season under the original rule had shown that teams were simply throwing the ball to the goalkeeper instead of kicking it."],
  ["Vuonna 1997 takapotkusääntö laajennettiin kattamaan maalivahdille tulevan pallon mistä?", "Joukkuekaverin sivurajaheitosta", "Kulmapotkusta", "Maalipotkusta", "Puskutorjunnasta",
   "Ensimmäinen kausi alkuperäisellä säännöllä oli osoittanut, että joukkueet vain heittivät pallon maalivahdille potkimisen sijaan."])

q(["In which year did the NBA introduce the 24-second shot clock?", "1954", "1938", "1967", "1979",
   "Teams had been sitting on the ball once ahead; one game in 1950 finished 19-18, and the clock roughly doubled scoring within a few seasons."],
  ["Minä vuonna NBA otti käyttöön 24 sekunnin heittokellon?", "Vuonna 1954", "Vuonna 1938", "Vuonna 1967", "Vuonna 1979",
   "Joukkueet olivat jääneet makaamaan pallon päälle johdossa; yksi vuoden 1950 peli päättyi 19-18, ja kello lähes kaksinkertaisti pisteet parissa kaudessa."])

q(["Until 1938, what happened in basketball after every single basket?", "A centre jump", "A free throw", "A throw-in by the scorer", "A substitution break",
   "Play restarted with a jump ball in the middle every time, which is why tall men who could do nothing else still had a job."],
  ["Mitä koripallossa tapahtui vuoteen 1938 asti jokaisen onnistuneen korin jälkeen?", "Aloitusheitto keskiympyrässä", "Vapaaheitto", "Sisäänheitto korin tekijälle", "Vaihtotauko",
   "Peli käynnistettiin joka kerta keskiympyrän aloitusheitosta, minkä vuoksi pitkille miehille löytyi paikka vaikka muuta taitoa ei olisi ollut."])

q(["Dribbling was allowed in basketball from 1901, but with what restriction?", "You could not shoot afterwards", "You could not use your left hand", "You could not move your feet", "You had three seconds",
   "Only one bounce was permitted and the dribble had to end in a pass; the modern continuous dribble was legalised in 1909."],
  ["Kuljetus sallittiin koripallossa vuodesta 1901, mutta millä rajoituksella?", "Sen jälkeen ei saanut heittää koriin", "Vasenta kättä ei saanut käyttää", "Jalkoja ei saanut liikuttaa", "Aikaa oli kolme sekuntia",
   "Vain yksi pompautus oli luvallinen ja kuljetuksen oli päätyttävä syöttöön; nykyinen yhtäjaksoinen kuljetus laillistettiin 1909."])

q(["In Naismith's original rules, what happened if one side committed three fouls in a row?", "The opponents were given a goal", "A player was sent off", "Two free throws", "The ball changed hands",
   "Fouls meant striking, holding, pushing or tripping; three in a row and the other side simply had a point written down."],
  ["Naismithin alkuperäisissä säännöissä: mitä tapahtui, jos toinen puoli teki kolme virhettä putkeen?", "Vastustajille annettiin kori", "Pelaaja ajettiin ulos", "Kaksi vapaaheittoa", "Pallo vaihtoi puolta",
   "Virheeksi laskettiin lyöminen, pitäminen, työntäminen ja kampittaminen; kolme putkeen, ja vastapuolelle vain kirjattiin piste."])

q(["In the original basketball rules a goal counted only if the ball did what?", "Stayed in the basket", "Touched the backboard", "Was thrown from outside the circle", "Was batted, not thrown",
   "So after every score somebody had to fetch the ball out again, which is also why the game was slower than it looks on paper."],
  ["Koripallon alkuperäisissä säännöissä kori hyväksyttiin vain jos pallo teki mitä?", "Jäi koriin", "Kosketti taustalevyä", "Heitettiin piirin ulkopuolelta", "Lyötiin, ei heitetty",
   "Jokaisen korin jälkeen pallo oli siis haettava pois, mikä osaltaan selittää miksi peli oli hitaampaa kuin paperilla näyttää."])

q(["Naismith's rules banned punching the ball. What was allowed instead?", "Batting it with an open hand", "Kicking it", "Carrying it two steps", "Rolling it",
   "The ball could be thrown or batted in any direction with one hand or both, but never struck with a fist."],
  ["Naismithin säännöt kielsivät pallon lyömisen nyrkillä. Mikä oli sen sijaan sallittua?", "Lyönti avoimella kädellä", "Potkaisu", "Kaksi askelta pallo kädessä", "Vierittäminen",
   "Palloa sai heittää tai lyödä mihin suuntaan tahansa yhdellä kädellä tai kahdella, mutta ei koskaan nyrkillä."])

q(["Goaltending, swatting away a shot on its way down, became a basketball foul in which year?", "1944", "1912", "1972", "1996",
   "It had been perfectly legal for the first half-century of the game; offensive goaltending followed only in 1958."],
  ["Minä vuonna torjunnan lyöminen laskevasta pallosta tuli koripallossa virheeksi?", "Vuonna 1944", "Vuonna 1912", "Vuonna 1972", "Vuonna 1996",
   "Se oli ollut täysin sallittua pelin ensimmäisen puolen vuosisadan ajan; hyökkäyspuolen vastaava sääntö tuli vasta 1958."])

q(["The NBA added a restricted-zone arc under the basket in 1997 to stop what?", "Defenders standing there to draw charges", "Dunking from the baseline", "Blocking from behind", "Hanging on the rim",
   "A defender could park himself under the basket and collect a foul every time an attacker landed on him; FIBA copied the idea in 2010 with a smaller arc."],
  ["NBA lisäsi korin alle rajoitusalueen kaaren vuonna 1997 estämään minkä?", "Puolustajien asettumisen sinne virheitä kalastelemaan", "Donkkaamisen päätyrajalta", "Takaapäin torjumisen", "Korin reunassa roikkumisen",
   "Puolustaja saattoi asettua korin alle ja kerätä virheen aina kun hyökkääjä laskeutui hänen päälleen; FIBA kopioi idean 2010 pienemmällä kaarella."])

q(["How long were the two halves in basketball's original rules?", "Fifteen minutes", "Twenty minutes", "Ten minutes", "Twelve minutes",
   "Fifteen minutes each with five minutes' rest, and a throw-in had to be taken within five seconds, a limit that has survived everything else."],
  ["Kuinka pitkiä olivat koripallon alkuperäisten sääntöjen kaksi puoliaikaa?", "Viisitoista minuuttia", "Kaksikymmentä minuuttia", "Kymmenen minuuttia", "Kaksitoista minuuttia",
   "Viisitoista minuuttia kumpikin ja viiden minuutin tauko, ja sisäänheitto oli tehtävä viidessä sekunnissa, raja joka on säilynyt kaiken muun yli."])

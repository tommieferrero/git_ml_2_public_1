Tommie Ferrero Linderoth
Inlämningsdatum 26-02-26
YH Akademin
BI25M Machine Learning
Inlämningsuppgift: Kunskapskontroll 2 – Teoretiska frågor


Teoretiska frågor Svara gärna kort och koncist.


1. All data i Python representeras av objekt. I Python består varje objekt av tre grundläggande delar. Vilka är dessa delar? Beskriv varje del kort.

Svar:
    • Identitet:
En unik identitet tilldelas varje objekt som skapas. Denna representeras av ett heltal och är objektets adress i datorns minne och ändras inte efter det att objektet skapats. (Inbyggd kod-funktion: ”id()” - returnerar identitet på objekt).

    • Datatyp:
Vilka operationer som kan utföras på objektet och vilka värden som blir möjliga för objektet att ha avgörs av datatyp som tilldelats. Efter att ett objekt är skapat, kan datatyp ej ändras. (Inbyggd kod-funktion: ”type()” - returnerar datatyp på objekt).
I python är följande begrepp samma sak: datatyp, typ samt klass. Begrepp beroende på sammanhang.

    • Värde:
Den data objektet representerar är dess värde, ex. text sträng, (string), som ”Hello world!” och hel- eller decimaltal, (123 / 1.23). Om ett objekts värde kan ändras på efter att de skapats beror på just vilket värde objektet har.

2. Förklara skillnaden mellan mutabla och immutabla objekt i Python och ge exempel på varje.
Mutable betyder kortfattat att det är möjligt att ändra värdet i ett objekt. Immutable är motsatsen, alltså att det ej är möjligt att utföra.
Svar:

    • Mutable exempel:
Vissa datastructures, som ex. list, dictionaries (dict), set samt datatyper som exempelvis integers, floats och booleans.
    • Immutable:
Vissa datastructures, som ex. tuple och frozenset. Även av typerna range och string.

3. Vad är ett set i Python? Vilka egenskaper särskiljer det från listor? Ge ett praktiskt exempel där det är mer effektivt att använda ett set än en lista.

Svar: 
Set är en datastruktur som är oordnad, vilket innebär att den ej har koll på i vilken ordning på de värden den innehåller när den defineras. Indexering kan därför ej användas för att komma åt värden i ett set. Till skillnad från listor, så innehåller ett set enbart unika värden, vilket kan vara till fördel om man vill omvandla en lista, som innehåller dublett-värden, till ett set om det passar ändamålet. Set är mutable, till skillnad från den andra versionen (frozenset). (set kan defineras med den inbyggda kod-funktionen set(), eller inom klammerparenteser ”{}”.

4. Förklara vad en loop är och ge exempel på när den används.

Svar: 
Python har 2st typer av loopar, ”for-loop” och ”while-loop”.
    • For-loop:
Används exempelvis för att iterera över en sekvens i datatyper som list, range, tuple, set, str, samt dict. Man sätter en iterationsvariabel för att bestämma antal iterationer/varv som önskas för objektet. Exempelvis för att iterera igenom index ien lista inom en satt range.
    • While-loop:
Loopar som är kombinerade med logik. Till skillnad från for-loop och iterering så kan en krav specificeras. Exempelvis att man för varje integer 5, fyll på med en integer 10. (så länge ett bestämt villkor utvärderas till sant (True)). Ett exempel kan vara att köra en funktion fram till/medans något är uppfyllt eller sant, True.

5. Vad är en klass och hur skiljer sig en instans från själva klassen?

Svar: 
Med klasser, som är en typ av objekt, kan data och funktionalitet kombineras. En klass är som en blueprint eller mall för att skapa objekt. Genom att använda klasser så sätts data och funktioner samman vilket skapar en ökad hanterbarhet över dessa. När en klass skapas så defineras en ny typ av objekt, vilket man kan skapa flertal instanser av. Instanser refererar till specifika objekt, från en klass. En instans har sitt eget läge som representeras av dess attribut och kan utföra handlingar definerade av klassens metod. Python har även möjlighet att skapa, mindre, underklasser som i sin tur kan ärva delar ur en huvudklass. Dett är något som underlättar i programmeringen, eftersom man ofta kan hämta/kalla på kod som redan finns och slippa upprepande kodning, något som sparar både tid och ökar läsbarhet.

6. Vad är en funktion och varför använder programmerare dem? Förklara skillnaden mellan en funktion med returvärde och en som inte returnerar något.

Svar:
Som förklarat i föregående fråga, så är funktioner i sig ett hjälpmedel för att undvika att upprepa kod, som blir lättare och ger ökad läsbarhet. Funktioner är ett centralt begrepp inom Python och kan beksrivas som block av uttryck som gör en specifik sak/uppgift. Funktioner sätts med ”def” följt av valt namn samt parametrar. Inne i funktionen definirar vi exempelvis if-satser och loopar inom funktionens egna kodblock. Här kan olika kombinationer bygga starka funktioner, som då är återanvändbar längre in i koden.

7. Förklara begreppet parameter jämfört med argument Python.

Svar: 
Parametrar och argument används i samband med att man passar information till en funktion. Parameter är en variabel som satts inom parentesen i funktionens definition, agerar placeholder för de kommande värdet (argument). Argument är värdet som satts för att kalla på funktionen. Dessa värden ersätter parametrar som definierats inom funktionen.

8. Titta på följande video om R: R Programming. Vad är skillnaden mellan R och Python?
R Programming

Svar:
    • Egna tankar:
Jag har stött på R en gång tidigare, i försök att reparera skador som skett i ett Power BI arbete, tidigare kurs. Det var intressant att få se mer av språket. Vad jag tänker efter att ha sett videon är att det ser väldigt likt ut, jämfört med Python. Liknande struktur i koder, som loopar och ifsatser, funktioner m.m. Även variabler är liknande. Syntax skiljer sig något men det upplevs inte så långt ifrån varandra. Jag tyckte mig se R som någon blanding av SQL och Python (andra språk är ofta mycket mer annorlunda utformat). Det verkade även som att det var ett långsammare språk, kan möjligtvis förklaras om det är så att R jobbar mer med den lokala prestandan och minnet, till skillnad från Python som ofta brukar snabba bibliotek som skrivits i snabbare språk, exempelvis inom C-språken. Dock förstår jag att även R brukar bibliotek, men vad dom är skriva i vet jag ej. Kanske är det så, kanske inte. Videon var mycket sevärd och jag har laddat ner materialet som presenterades, för att själv ”leka” runt lite. Extra bonus poäng för att fått se C-3PO och R2-D2’s BMI ^^

Men för att utveckla jämförelsen lite bättre och främst för egen skull, så har jag googlat mer konkreta skillnader.
    • Vad jag får fram:
Python: Stykor – lättläst samt lättlärd syntax. Ett språk som ofta används i samband då man kombinerar dataanalys med större system/produktionsmiljöer med typiska användningsområden som maskininlärning i skalbar miljö, dataanalys kopplad till applikationer och/eller API:er, integration i större mjukvaroprojekt. Exempel kan vara ansiktsigenkänning i mobilapp eller att utveckla ML-modeller som ska köras i produktion.
R: Starkt fokus på statistik, statistiska modeller, specialiserad analys och visualiseringar. Det verkar uppskattas i arbete som innefattar kundbeteendeanalyser, biostatistik och genforskning.
Informationen är hämtad från IBM (verkade inte nödvändigt med källförteckning och fotnot här).

    • Ytterligare egna tankar:
Efter jämförelsen som tänker jag nog ändå att de har liknande funktionalitet, speciellt efter arbete med statistik och ML i python kurserna. R verkar vara mer specificerat riktat mot den vetenskapliga världen och data-science. Det verkar vara betydligt lägre andel programmerare med R kunskaper i nu jämfört med förr, kanske eftersom Python stigit i populäritet på senare tid. Skulle tro att det dels beror på att det är ett lättillängligt språk att lära sig, det finns otaligt material att komma åt gratis, speciellt efter AI’s framsteg men också eftersom jag ser utbildningar i skolor, även från lägre åldrar. Men det finns nog en hel del system där ute som fortfarande kör i R. Intressant ämne, helt klart!

9. Kalle ska bygga en ML-modell och delar upp sin data i ”Träning”, ”Validering” och ”Test”, vad används respektive del för?

Svar: 

10. Julia delar upp sin data i träning och test. På träningsdatan så tränar hon tre modeller; ”Linjär Regression”, ”Lasso regression” och en ”Random Forest modell”. Hur skall hon välja vilken av de tre modellerna hon skall fortsätta använda när hon inte skapat ett explicit ”valideringsdataset”?

Svar: 

11. Vad är ”regressionsproblem? Kan du ge några exempel på modeller som används och potentiella tillämpningsområden?

Svar: 

12. Hur kan du tolka RMSE och vad används det till.

Svar: 

13. Vad är ”klassificieringsproblem? Kan du ge några exempel på modeller som används och potentiella tillämpningsområden?

Svar: 

14. Vad är en ”Confusion Matrix”?

Svar: 

15. Vad är K-means modellen för något? Ge ett exempel på vad det kan tillämpas på.

Svar: 

16. Förklara (gärna med ett exempel): Ordinal encoding, one-hot encoding, dummy variable encoding.

Svar: 

17. Göran påstår att datan antingen är ”ordinal” eller ”nominal”. Julia säger att detta måste tolkas. Hon ger ett exempel med att färger såsom {röd, grön, blå} generellt sett inte har någon inbördes ordning (nominal) men om du har en röd skjorta så är du vackrast på festen (ordinal) – vem har rätt?

Svar: 

18. Vad är skillnaden mellan parametrar och hyperparametrar i en maskininlärningsmodell? Ge ett exempel på varje och förklara varför de inte kan optimeras på samma sätt.

Svar: 

19. Förklara skillnaden mellan overfitting och underfitting i en maskininlärningsmodell. Beskriv även hur man kan upptäcka respektive åtgärda dem.

Svar: 


Du ska även genomföra en självutvärdering där du besvarar följande tre frågor:

1. Har något varit utmanande i kursen/kunskapskontrollerna? Om ja, hur har du hanterat det?
Svar:


2. Vilket betyg anser du att du ska ha och varför?
Svar:


3. Något du vill lyfta fram till Terese?
Svar:

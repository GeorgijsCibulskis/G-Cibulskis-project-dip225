# NutriBoost

**Georgijs Cibuļskis; 231RDB192, 1. kurss, 5. grupa**

**NutriBoost – uzdevums:**

&nbsp;&nbsp;&nbsp;&nbsp;Palīdzēt automatizēt informācijas apkopošanu par nepieciešamo kaloriju un barības vielu daudzuma uzņemšanu uzturā lai, trenējoties zālē vai nodarbojoties ar kādu sporta veidu, uzņemtu svaru (muskuļus). Arī palīdzēt automatizēt pierakstīšanu un sekošanu līdzi apēstu kaloriju un barības vielu daudzumam, apkopojot informāciju tabulās, kur katra tabula ir 1 nedēļas apkopošana.


**NutriBoost – programmas lietotāji:**

* &nbsp;&nbsp;&nbsp;&nbsp;Pirmkārt, šī programma atvieglo paša autora ikdienas darbu, jo viņš diezgan nopietni nodarbojas ar sportu un seko līdzi savam veselības stāvoklim, kā arī viņam ir mērķis uzņemties svarā, tāpēc jau kādu laiku viņš reģistrē visu, ko viņš ēd, skatās cik ir kaloriju un barības vielu ir visos produktos, nolasot to no pašiem produktiem vai meklējot to internetā. Taču autors arī ir cilvēks, tāpēc dažkārt tiek izlaistas dienas vai pat nedēļas slinkuma dēļ, jo visu ievadīt manuāli nav ērti, kā arī dažreiz meklēšanas process aizņem daudz laika. Autors arī nekad nebija sekojis tam, cik daudz viņam tieši ir jāēd un kas (kādas barības vielas un kādi produkti) jāēd, lai uzņemtos svarā pareizi, veselīgi un ātri. Šo iemeslu dēļ, viņš ir izlēmis izstrādāt programmu, kura varēs šīs darbības automatizēt un apkopot.

* &nbsp;&nbsp;&nbsp;&nbsp;Otrkārt, šo programmu varēs potenciāli pārdod citiem sportistiem vai cilvēkiem ar līdzīgiem mērķiem, vai arī parastiem cilvēkiem, kuri grib sekot līdzi cik un ko viņi ēd dienas laikā. Vēl viena programmas pārdošanas auditorija ir personīgie profesionāli treneri, kuri seko līdzi savu klientu (parasti ļoti turīgie cilvēki vai izlases līmeņa sportisti) uzturam un kuriem ir ļoti svarīgi ievērot speciālas dietas un ēst tik, cik ir izrēķinājis dietologs.

**NutriBoost – programmas būtība un izmantošanas metodes:**

Programma piedava 2 funkcijas:


* Izveidot jauno fitnesa plānu (Excel tipa failā), balstoties uz lietotāja datiem (svars, vēlamais svars, augums, vecums, dzimums, laiks, pa kuru lietotājs vēlas uzņemt svaru un aktivitātes līmenis);


* Meklēt atbilstošus produktus (to barības vielas - kalorijas, taukus, ogļhidrātus un olbaltumvielas) un pievienot to plānam pēc lietotāja vārda, uzvārda un apēsta produkta daudzuma. Programmas iekšā arī ir pārdomāta dienu un nedēļu kontrole, lai taisītu jaunas tabulas vai pārietu uz nākamo dienu, kas palīdzēs apkopot informāciju piemērotā cilvēkam veidā.

&nbsp;&nbsp;&nbsp;&nbsp;Programmas ievade notiek izstrādātā lietotāja interfeisā (**TĀPĒC JĀPALAIŽ FAILS user_interface.py caur VSC vai citu programmēšanas rīku!!!** ), tāpēc darbs ar pašu programmu ir ērts un piemērots visiem cilvēkiem, nevis tikai zinošiem, kuri māk strādāt ar programmēšanas izstrādes vidēm un termināliem.

**Izmantotas Python bibliotēkas:**

**OpenPyxl:**

Šī bibliotēka tika lietota, lai:


* Taisītu jauno excel failu;

 
* Ievietotu tajā izrēķinātus lietotāja datus un barības vielu daudzumu katrā plāna nedēļā;


* Ievietotu datus par produkta barības vielām un kalorijām;


* Taisītu pārskatāmas tabulas, ar izceltām robežās;


* Kontrolētu dienas un nedēļas beigas, lai veidotu vairākas mazas tabulas, nevis vienu milzīgo.


Parasti šie uzdevumi tika pildīti ar Workbook klases un funkcijas load_workbook palīdzību.


**openpyxl.utils:**


&nbsp;&nbsp;&nbsp;&nbsp;Šīs modulis tika izmantots, lai importētu funkciju get_column_letter, kura bija neieciešama pašizstrādātajā funkcijā correct_width, kura savukārt laboja šūnu platumu, lai vairākas šūnas nepārklātos.


**openpyxl.styles:**


No šī moduļa tika importētas klases:


* Alignment – kontrolētu, lai visas šūnas būtu centrētas;


* Border – izveidotu objektu ar šūnas robežu parametriem;


* Side – objekti, kuri kontrolē katru šūnas robežas malu un tās iestatījumus.

**Selenium:**

&nbsp;&nbsp;&nbsp;&nbsp;Šī bibliotēka tika lietota datu skrāpēšanai no tīmekļa vietnes (dati plānam par nepieciešamo kaloriju un barības vielu daudzumu, produkta kalorijas un barības vielu daudzums, produkta meklēšana un saraksta izveide utt.), kā arī tīmekļa vietnes darbības automatizēšanai (ierakstīšanai atbilstošās vietās, pogu klikšķināšanai, meklēšanas procesam utt.).

**selenium.webdriver.support.ui (Select):**


* Izmantota klase, lai būtu iespējams izvēlēties kādu variantu no opciju sarakstiem (option menu) tīmekļa vietnē.

**selenium.webdriver.chrome.service (Options, Service, webdriver):**


* Izmantotas, lai uzsāktu tīmekļa vietnes darbību un iestatītu fona režīmu (lai lietotājs neredzētu kā atveras tīmeklis un kas tajā notiek).


**selenium.webdriver.common.by (By):**


* Bija nepieciešams vairāku elementu meklēšanai tīmekļa vietnes kodā (HTML valodā).


**selenium.webdriver.common.keys (Keys):**


* Tika izmantots tikai vienu reizi meklēšanas procesā, lai programma uzspiestu pogu ‘Enter’ uz klaviatūras, lai sameklētu atbilstošu produktu, jo tīmekļa vietnē nebija atsevišķas pogas ‘Search’, uz kuru būtu iespējams uzspiest.


**selenium.common.exceptions (NoSuchElementException):**


* Tika izmantots, lai kontrolētu kļūdas programmas gaitā un, ja tā rodas, tad paziņotu par to lietotājam un pateiktu iemeslu kāpēc tas notika.


**Time:**

&nbsp;&nbsp;&nbsp;&nbsp;Bibliotēka lietota tikai, lai apturētu programmas darbību, kamēr tīmekļa vietne tiek ielādēta un lai novērstu konfliktus vai kļūdas.

**Datetime:**

&nbsp;&nbsp;&nbsp;&nbsp;Bibliotēka lietota tikai lai dabūtu datumu, kad tiek uztaisīts jauns fitnesa plāns.

**CustomTkinter:**

&nbsp;&nbsp;&nbsp;&nbsp;Bibliotēka tika lietota, lai uztaisītu lietotāja interfeisu – galveno logu, fonu, uzrakstus, pogas, ievades laukus, radio izvēles pogas, izvēles tabulas, progresa radītāji, teksta kastes. Tika izvēlēta tieši šī bibliotēka, jo autoram jau bija pieredze ar bibliotēku tkinter (ar kuru bija ļoti daudz sintakses līdzību), bet ar šo bibliotēku bija iespējams izveidot mūsdienīgu dizainu.


**Tkinter:**

&nbsp;&nbsp;&nbsp;&nbsp;Izmantota 1 iemesla dēļ – lai attēlotu kļūdas ar messagebox palīdzību, jo CutomTkinter iekšā nav iebūvētas funkcijas, lai attēlotu kļūdas.


**Thread:**

&nbsp;&nbsp;&nbsp;&nbsp;Izmantota, lai, kamēr ir atvērts lietotāja interfeiss un notiek plāna izveidošana vai produkta meklēšana, vai produkta barības vielu ierakstīšana failā, pats interfeiss neiesaldētos un būtu funkcionāls. Tas nozīmē, ka katrs fails darbojas savā plūsmā vienlaicīgi un netraucē viens otram, tāpēc nerodas konflikti.

**PAPILDUS INFORMĀCIJA PAR PROGRAMMU**

&nbsp;&nbsp;&nbsp;&nbsp;Izstrādājot šo programmu autors saskarās ar ļoti grūto problēmu - ātrumu, kurš, nemainot pašas programmas kodu, mainījās. Autors mēģināja no tas izvairīties, mainot plūsmju darbību, neizmantojot time.sleep() funkcijas, neizmantotjot tīmekļa darbību fona režīmā, bet tapat ātrums negribēja stabilizēties. Piemēram bija tāds gadījums, kad vakarā excel paplašināšana ar produktu aizņema 30 SEKUNDES VIENAM PRODUKTAM, bet jau nākamajā rītā programma varēja to izdarīt 5-7 sekundēs. Šo iemeslu dēļ autors secina, ka ātruma nestabilitāte ir atkarīga no tīmekļa vietņu (https://www.prokerala.com/health/health-calculators/weight-gain-calculator.php UN https://www.nutritionvalue.org) serveru pieejamību un struktūru. Varbūt uz tiem iz uzlikti algoritmi, kuri neaktivitātes stundās (vakaros un nakti) ierobežo servera resursus, varbūt notiek izmaiņas pašā servera struktūrā no izstrādātāju puses vai kaut kas cits, tāpēc autora programmas ātrums medz atšķirties dažādos laika posmos. (Ja Jums pašlaik programma strādā lēni, tad Jūs varat pārliecināties par to ātrumdarbību video materiālā: https://youtu.be/h-gCoZWfeeY)

**Izmantotie avoti:**


    1.  https://stackoverflow.com/questions/24917201/applying-borders-to-a-cell-in-openpyxl


    2.  https://github.com/TomSchimansky/CustomTkinter/wiki/CTkTextbox


    3.  https://stackoverflow.com/questions/27369675/inserting-to-a-textbox-with-tkinter


    4.  https://subscription.packtpub.com/book/programming/9781849515740/1/ch01lvl1sec16/locating-elements-using-text#:~:text=Using%20CSS%20selector%20Contains%20Pseudo,findElement(By)


    5.  https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread


    6.  https://journeyofquality.com/2022/03/01/handle-non-breaking-space-in-xpath/


    7.  https://stackoverflow.com/questions/29792134/how-we-can-use-iter-rows-in-python-openpyxl-package


    8.  https://www.browserstack.com/guide/css-selectors-in-selenium#:~:text=CSS%20(Cascading%20Style%20Sheets)%20Selectors,faster%20as%20compared%20to%20XPath


    9.  https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget


    10. https://stackoverflow.com/questions/41371815/how-can-i-stop-my-tkinter-gui-from-freezing-when-i-click-my-button


    11. https://github.com/TomSchimansky/CustomTkinter


    12. https://www.pythontutorial.net/tkinter/tkinter-progressbar/


    13. https://www.geeksforgeeks.org/using-lambda-in-gui-programs-in-python/


    14. https://stackoverflow.com/questions/70406400/understanding-python-lambda-behavior-with-tkinter-button


    16. https://stackoverflow.com/questions/41371815/how-can-i-stop-my-tkinter-gui-from-freezing-when-i-click-my-button#:~:text=the%20reason%20your%20Tk%20GUI,when%20you%20click%20the%20button


    17. https://www.geeksforgeeks.org/using-lambda-in-gui-programs-in-python/


    18. https://www.pythontutorial.net/tkinter/tkinter-progressbar/
# eBerza — Product Research & Video Brief

16. 10. 2026. · FAZA 1 — Istraživanje

> Snimak dokumenta. Živa verzija (za komentare i odgovore): https://claude.ai/code/artifact/d7b768d7-c26e-42ce-9c6d-ac541cd4980b

## Sažetak i metod istraživanja

eBerza je B2B platforma za udruženu (grupnu) kupovinu: prodavac nudi cenu koja pada sa ukupnom količinom, a kupci se udružuju da zajedno stignu do nižeg praga. Osnovni model je jasan i dobro se objašnjava videom, a pravila trgovine sada su poznata iz dokumenta „Business rules on eBerza“. Otvoreni su još provizije, depozit kupca i izgled ekrana trgovine.

**Važno ograničenje:** sajt eberza.rs i YouTube nisu mogli da se otvore iz ovog radnog okruženja. Mrežna politika okruženja dozvoljava samo GitHub i package managere. Sajt sam video samo kroz vaše snimke ekrana stranice za registraciju; FAQ (eberza.rs/en/faq) takođe nije dostupan.

Nalazi ispod potiču iz web pretrage: tekstovi stranica eberza.rs koje je pretraživač indeksirao i medijski članci. Pretraga vraća automatski sažet tekst, pa citati sa sajta moraju da se uporede sa živim sajtom pre nego što uđu u naraciju.

| Izvor | Šta je dobijeno | Pouzdanost |
| --- | --- | --- |
| Snimci ekrana registracije (od klijenta, 16. 10. 2026.) | Ko može da se registruje, sva polja forme, navigacija, boje i izgled interfejsa | Direktno viđeno |
| [Business rules on eBerza](https://eberza.com/api/documents/152/document) (dokument na eberza.com, EN) | Ponuda kupca, uslovi kupovine, rok do 90 dana, izbor kupaca, obustava, depozit, PDV, sporovi | Pravila platforme, posredno (izvodi preko pretrage) |
| [eberza.rs/sr](https://eberza.rs/sr) (početna) | Opis platforme, navigacija: Kupci, Prodavci, Franšiza, Pravila, FAQ, Vesti; kontakt u footeru | Tekst sa sajta, posredno |
| [eberza.rs/sr/buyers](https://eberza.rs/sr/buyers) | Poruke za kupce, poziv „Pridružite se besplatno“; footer sa godinom 2020 | Tekst sa sajta, posredno |
| [eberza.rs/en/sellers](https://eberza.rs/en/sellers) | Poruke za prodavce (engleska verzija) | Tekst sa sajta, posredno; srpsku verziju treba uporediti |
| [eberza.rs/en/franchise](https://eberza.rs/en/franchise) | Tok grupne kupovine, ugovor, odgovornost za isporuku | Tekst sa sajta, posredno |
| [Danas, 2018](https://www.danas.rs/vesti/ekonomija/eberza-resenje-za-ulazak-srpskih-firmi-na-globalno-trziste/) | Mehanizam, primer sa peškirima | Intervju sa osnivačima, star oko 8 godina |
| [Elektronsko bankarstvo, 27. 11. 2018.](https://www.elektronskobankarstvo.rs/e-berza-pomaze-srpskim-firmama-da-udju-na-globalno-trziste/) | Isti mehanizam, izjava jednog korisnika | Medij, star oko 8 godina |
| [International Franchise Expo 2024](https://www.franchiseexpo.com/ife/exhibitors/afeja-belgrade) | B2B model, franšizni model, operator AFEJA | Profil izlagača (samoopis) |
| [Facebook: „eBerza - pametna trgovina“](https://www.facebook.com/eberza.rs/) | Naziv stranice i slogan | Samo naslov stranice |

**Nije provereno:** FAQ, pun tekst pravila (samo izvodi), ekrani ponude i trgovine posle prijave, aktivne ponude, logo i oba referentna videa. Referentne snimke nisam pogledao (sekcija o referencama).

## 1. Šta je eBerza, jednostavno objašnjeno

eBerza je internet berza za firme na kojoj više kupaca zajedno kupuje istu robu, da bi svi dobili cenu koja inače važi samo za velike porudžbine.

Zvanični opis sa početne strane: „eberza je platforma koja povezuje kupce i prodavce, omogućavajući im da ostvare najpovoljnije cene kroz udruženu trgovinu i količinske popuste.“

- **Prodavac** postavlja ponudu sa količinskim popustom: što se ukupno kupi više, cena po jedinici je niža.
- **Kupac** bira količinu koja mu treba i pridružuje se drugim kupcima iste robe. Sa stranice za kupce: „Kada se skupi dovoljno zainteresovanih dobijate najbolju cenu.“
- **Plaćanje** ne ide odmah: roba se plaća tek kada se dostigne željena cena, a na kraju trgovine platforma generiše ugovor.

| Činjenica | Vrednost | Izvor |
| --- | --- | --- |
| Operator | „AFEJA“ d.o.o., Bulevar Oslobođenja 51, Beograd | Kontakt na sajtu |
| Kontakt | eberza@afeja.com, +381 69 664557 | Kontakt na sajtu |
| Pokrenuta | 2018. (predstavljena u medijima novembra 2018.) | Danas, Elektronsko bankarstvo |
| Ko učestvuje | Samo poslovni subjekti: firme, preduzetnici, vlasnici radnji i lica registrovana za obavljanje delatnosti; domaći i strani | Forma za registraciju; pravila poslovanja |
| Uloga platforme | „Poziv na razmenu ponuda“, ne katalog robe; platforma ne određuje cene i ne garantuje isporuku | Pravila poslovanja; stranica o franšizi |
| Cene | U dinarima, bez PDV-a (osim za strane učesnike) | Pravila poslovanja |
| Sporovi | Ugovoreni sud ili ugovoreni arbitar | Pravila poslovanja |
| Širenje | Teritorijalne franšize: franšizant promoviše platformu lokalnim firmama i pomaže korisnicima | [eberza.rs/en/franchise](https://eberza.rs/en/franchise) |
| Jezici sajta | srpski (/sr) i engleski (/en) | URL-ovi stranica |

**Odgovoreno:** registracija je namenjena firmama, preduzetnicima i licima koja obavljaju registrovanu delatnost. Opis na stranici za registraciju: „Who engages in business activities, as well as owners of businesses and other individuals who carry out a business activity under a registered occupation.“ Video zato govori firmama i preduzetnicima, ne građanima.

## 2. Kako platforma funkcioniše, korak po korak

Trgovina ima osam koraka, od registracije do isporuke; pravila za korake 2–6 poznata su iz dokumenta „Business rules on eBerza“. Oznake: **\[pravila\]** = taj dokument, **\[sajt\]** = tekst sa eberza.rs, **\[registracija\]** = vaši snimci ekrana, **\[2018\]** = intervju u medijima, **\[?\]** = nije opisano.

1. **Registracija firme.** Forma ima tri koraka. *Info*: korisničko ime, lozinka, e-pošta, naziv i pun naziv firme, telefon, država, grad, adresa. *Company*: PIB, matični broj, broj registracionog dokumenta, tekući račun, dokaz o upisu u registar, PDV broj (ako postoji), delatnost, oblik organizovanja, kontakt osoba i PR tekst do 1.100 znakova. *Networks*: društvene mreže, neobavezno. Obavezno je prihvatanje pravila. \[registracija\] Da li eBerza proverava priložena dokumenta, nije poznato. \[?\]
2. **Prodavac objavljuje oglas.** Nudi zalihu uz tabelu količinskih popusta „od–do“ i sam određuje datum i čas završetka. Oglas traje najviše 90 dana; AFEJA ga izuzetno može produžiti. \[pravila\] Popuste određuje prodavac, ne platforma. \[sajt\]
3. **Kupac daje ponudu.** Unosi tačnu količinu, bira cenu iz tabele „Quantity discount“ i uslov kupovine iz „Conditions of purchase“. Jedan uslov je kupovina po bilo kojoj ceni iz raspona, ali ne iznad cene koju je kupac ponudio. \[pravila\]
4. **Potražnja se sabira.** Cena se formira iz zbira pojedinačnih ponuda registrovanih kupaca. Zbir nije zajednička ponuda: kupci ne odgovaraju jedni za druge. Ako ponuda poslednjeg kupca premaši preostalu količinu, on dobija samo ostatak. \[pravila\]
5. **Izmena i povlačenje do roka.** Kupac može da izmeni, dopuni ili povuče ponudu do isteka oglasa, a posle toga ne može. Za kasnije povlačenje prodavac može da aktivira depozit koji je kupac dao kao garanciju ili da prihvati odustanak. \[pravila\] Iznos depozita i kada se plaća, nije opisano. \[?\]
6. **Prodavac bira kupce.** Po isteku roka prodavac odlučuje kome dodeljuje ugovor; pravila preporučuju potvrdu izabranom kupcu u roku od 5 radnih dana. Ugovor nastaje kada kupac primi tu potvrdu. Ako uslovi nisu ispunjeni, preporuka je da prodavac obustavi trgovinu i obavesti kupce. \[pravila\]
7. **Ugovor.** Platforma generiše obrazac ugovora koji postaje obavezujući potpisom. \[sajt\] Način potpisa nije poznat. \[?\]
8. **Plaćanje i isporuka.** Roba se plaća tek kada se dostigne željena cena. \[sajt\] Plaćanje ide po dogovoru kupca i prodavca, ne preko portala. \[2018\] Isporuka je obaveza prodavca. \[sajt\] Vrstu i iznos poreza kupac saznaje posle zaključenja ugovora. \[pravila\]

![Tok grupne kupovine](assets/tok-grupne-kupovine.png)

Osenčen korak, sabiranje potražnje, jeste srž poruke videa; isprekidani deo je alternativni ishod: ako uslovi nisu ispunjeni, pravila preporučuju da prodavac obustavi trgovinu i obavesti kupce.

**Privatnost i poverenje:** kupci nastupaju pod korisničkim imenom, a identitet kupca zna samo prodavac čiju robu kupuje. \[2018\] Forma za registraciju nudi opciju „Shopping privacy“; da li je to isti izbor, treba potvrditi. \[registracija\] Prodavac može da odbije kupce koji su skoro kršili pravila, davali netačne podatke ili odbijali da potpišu ugovor. \[pravila\] Posle trgovine učesnici vide uslove kupovine i isporuke i kontakt druge strane. \[sajt\]

**Ilustracija iz medija (2018., nije stvarna aktuelna ponuda):** prodavac nudi 100 peškira po 300 dinara, ponuda važi oko mesec dana. Kupcu trebaju tri peškira, koja u maloprodaji koštaju po 1.000 dinara; na eBerzi plaća 900 dinara. Ostalih 97 peškira u istom periodu kupuju drugi kupci.

## 3. Glavne prednosti za kupce

Glavna korist za kupca: cena velike porudžbine bez obaveze da sam naruči celu količinu. Ostale prednosti ispod su potvrđene tekstom sajta ili intervjuom iz 2018.

| Prednost | Šta kaže izvor | Izvor |
| --- | --- | --- |
| Niža cena kroz udruživanje | „Vi i drugi kupci možete se udružiti i zajedno naručiti veće količine, ostvarujući značajne popuste.“ | Stranica za kupce |
| Kupac sam postavlja granicu cene | Uslov kupovine: bilo koja cena iz raspona popusta, ali ne iznad cene koju je kupac ponudio | Pravila poslovanja |
| Kupuje tačno koliko mu treba | Ponuda se daje za tačnu količinu koju kupac želi | Pravila poslovanja |
| Bez zajedničke odgovornosti | Zbir ponuda nije zajednička ponuda; kupci ne odgovaraju jedni za druge | Pravila poslovanja |
| Fleksibilnost do roka | Ponuda se može izmeniti, dopuniti ili povući do isteka oglasa | Pravila poslovanja |
| Plaćanje tek po dostizanju cene | Roba se plaća tek kada se dostigne željena cena | Stranica o franšizi |
| Besplatno učlanjenje | „Pridružite se besplatno“ | Stranica za kupce |
| Pravna sigurnost | Ugovor obavezujući potpisom; sporovi pred ugovorenim sudom ili arbitrom | Stranica o franšizi; pravila |
| Diskrecija | Kupac nastupa pod korisničkim imenom; pri registraciji postoji opcija „Shopping privacy“ | Danas, 2018.; forma za registraciju |

**Šta video ne sme da tvrdi bez potvrde:** procenat uštede; garanciju isporuke (platforma je ne garantuje); da je korišćenje potpuno besplatno (provizije nisu poznate); da kupac ništa ne plaća unapred (pravila pominju depozit kao garanciju); da kupac uvek dobija najnižu cenu; da su sve firme provereno pouzdane (provera dokumenata nije potvrđena).

## 4. Glavne prednosti za prodavce

Glavna korist za prodavca: jedna ponuda doseže više kupaca odjednom i prodaje veću količinu, bilo da je u pitanju višak zaliha ili planirana proizvodnja. Pretraživač je vratio samo englesku verziju stranice za prodavce; srpski tekst (/sr/sellers) treba uzeti sa živog sajta.

| Prednost | Šta kaže izvor | Izvor |
| --- | --- | --- |
| Prodaja većih količina | „Whether you have excess inventory or are planning production, eBerza allows you to sell larger quantities of goods efficiently.“ | Stranica za prodavce (EN) |
| Kupci dolaze sami | „Buyers search for your products on their own and join together for larger orders.“ | Stranica za prodavce (EN) |
| Rast prodaje i dostupnosti | „As a seller, eBerza offers you a unique opportunity to increase the sales and availability of your products.“ | Stranica za prodavce (EN) |
| Prodavac upravlja uslovima | Sam određuje količinske popuste, pragove i rok oglasa (najviše 90 dana) | Stranica o franšizi; pravila |
| Prodavac bira kupce | Po isteku roka odlučuje kome dodeljuje ugovor; može da odbije kupce koji su kršili pravila ili odbijali ugovor | Pravila poslovanja |
| Zaštita od odustajanja | Za povlačenje posle roka može da aktivira depozit kupca; uz klauzulu u oglasu može da obustavi trgovinu ako jedan kupac odustane | Pravila poslovanja |
| Rešava zalihe koje vezuju novac | Prodavci kroz „količinske popuste“ rešavaju problem plasmana postojećih zaliha | Danas, 2018. |
| Planiranje proizvodnje | Jedan proizvođač (Li-kom plus, Gročka) naveo je da mu portal olakšava planiranje proizvodnje | Elektronsko bankarstvo, 2018. |
| Ugovor po završetku | Platforma generiše ugovor; sporovi idu pred ugovoreni sud ili arbitra | Stranica o franšizi; pravila |

**Tvrdnje sa sajta koje treba proveriti pre upotrebe:** prema sažetku pretrage, engleska stranica pominje brži obrt zaliha „bez dodatnog ulaganja u marketing“ i „bez dodatnih troškova za izlazak na međunarodna tržišta“. Tačne formulacije nisu potvrđene, pa ih video za sada ne koristi. Izjava korisnika iz 2018. može u video samo uz njegovu saglasnost i proveru da je i danas aktuelna.

**Obaveza prodavca koju video treba pošteno da pokaže:** isporuka je odgovornost prodavca.

## Ciljni korisnici, problemi i razlika od internet prodavnice

eBerza se obraća firmama na obe strane: onima koje imaju robu u većim količinama i onima koje bi da kupe povoljnije, a same nemaju obim za veleprodajnu cenu.

**Ciljni korisnici (prema izvorima):**

- **Prodavci:** proizvođači, veleprodaje i distributeri, posebno oni sa viškom zaliha ili planiranom proizvodnjom. Prema pravilima to mogu biti registrovani preduzetnici, pravna lica, vlasnici radnji i lica registrovana za obavljanje delatnosti, domaći i strani.
- **Kupci:** firme i preduzetnici koji nabavljaju robu. Registracija traži PIB, matični broj i dokaz o upisu u registar, pa građani nisu publika.
- **Franšizanti:** partneri koji razvijaju mrežu na svojoj teritoriji; nisu publika ovog videa, osim ako se ne odluči drugačije.

**Problemi koje platforma rešava:**

- Mali kupac ne može sam da naruči količinu za koju važi najbolja cena.
- Prodavac ima zalihe koje vezuju novac i teško ih plasira kroz pojedinačne porudžbine. (Danas, 2018.)
- Domaće firme teško prelaze lokalnu i regionalnu izolovanost. (Danas, 2018.)

|  | Klasična internet prodavnica | eBerza |
| --- | --- | --- |
| Ko određuje cenu | Prodavnica, ista cena za sve | Prodavac daje pragove; cena se formira iz zbira ponuda svih kupaca |
| Odnos kupac–prodavac | Jedan na jedan, odmah | „Nije trgovina jedan na jedan“: više kupaca na jednom oglasu |
| Kupac bira | Količinu po fiksnoj ceni | Tačnu količinu, cenu iz tabele popusta i uslov kupovine |
| Plaćanje | Odmah, pri porudžbini | Tek kad se dostigne željena cena, prema ugovoru |
| Trenutak kupovine | Odmah po porudžbini | Po isteku roka oglasa (do 90 dana), kada prodavac potvrdi kupce |
| Pravni okvir | Opšti uslovi prodavnice | Ugovor koji platforma generiše; sporovi pred ugovorenim sudom ili arbitrom |
| Isporuka | Prodavnica | Prodavac, na adresu kupca ili dogovorenu lokaciju |

**Moguća zabuna koju video treba da preduhitri (moja procena):** „grupna kupovina“ u Srbiji se često veže za sajtove sa kuponima za usluge. eBerza nije sajt sa kuponima: nema unapred zadatog popusta, već cenu određuje ukupna količina robe.

## Vizuelni identitet

Vaši snimci ekrana pokazuju interfejs u tamnoplavoj, sivoplavoj i svetloplavoj boji, sa bordo akcentom i mnogo belog prostora. Logo nisam video. Boje ispod su uzorkovane sa snimaka i nisu zvanična paleta.

| Element | Šta je poznato | Status |
| --- | --- | --- |
| Naziv | U upotrebi su „eBerza“ (registracija, Facebook, mediji), „e-Berza“ (naslov početne strane), „e-berza“ (stranica za kupce) i „eberza“ (tekst na sajtu) | Interfejs koristi „eBerza“; potvrditi za video |
| Slogan | „pametna trgovina“, iz naziva Facebook stranice | Potvrditi da li je aktuelan |
| Zaštićeni znak | Prijava „EB EBERZA“ u SAD, broj 79374476, podneta 6. 4. 2023., vlasnik AFEJA ([Justia](https://trademarks.justia.com/793/74/eb-79374476.html)) | Izgled znaka nije viđen |
| Logo | Nije viđen na snimcima | Potreban SVG |
| Boje interfejsa (uzorak) | Tamnoplava #193965 (aktivno dugme); skoro crna plava #0B1A2D (naslovi); sivoplava #6E829E (opisi, neaktivno dugme); svetloplava #87CEEB do #9DD7EF (aktivni tab, linkovi, ikone); bordo #823A4C (dugme za čet, poruke o grešci u istoj nijansi); svetla roze-siva #F7EAEC (prelaz u footeru) | Približne vrednosti; bordo može biti boja čet-alata, ne brenda |
| Font | Geometrijski sans-serif, zaobljenih oblika; naziv nije poznat | Proveriti u CSS-u ili brand book-u |
| Stil interfejsa | Uske forme na belom, polja sa tankim okvirom i zaobljenim uglovima, ikonice uz tabove, navigacija: Buyers, Sellers, Franchise / eBerza, Regulation, FAQ, News | Viđeno na snimcima |
| Ton komunikacije | Obraćanje sa „Vi“, kratke poruke u imperativu: „Pridružite se besplatno“, „Registrujte se“; EN naslov „Increase sales.“ | Iz teksta sajta |
| Ažurnost sajta | Footer stranice za kupce prikazuje 2020.; registracija koristi Cloudflare Turnstile i ima dugme za čet | Proveriti godinu u footeru |

**Potrebni materijali od klijenta:**

- Logo u vektorskom formatu (SVG, AI ili PDF), sa varijantom za tamnu i svetlu pozadinu.
- Brand book ili bar HEX kodove boja i nazive fontova.
- Postojeće fotografije, bannere, prezentacije i ranije video-snimke, ako postoje.
- Pristup sajtu za snimanje ekrana u punoj rezoluciji (vidi sekciju sa pitanjima).

## 5. Najvažnije funkcionalnosti za video

U središtu videa treba da bude oglas sa količinskim pragovima i trenutak kada udružena potražnja spusti cenu. Od svih ekrana viđena je samo registracija; za ostale je potreban stvarni snimak, a gde ekran ne postoji, grafika označena kao ilustracija.

| Prioritet | Funkcionalnost | Šta gledalac treba da vidi | Postojanje | Ekran |
| --- | --- | --- | --- | --- |
| 1 | Oglas sa količinskim pragovima | Proizvod, tabela „od–do“ količina sa cenom po jedinici, rok oglasa | Potvrđeno (pravila) | Nije viđen |
| 2 | Ponuda kupca | Tačna količina, cena iz tabele popusta, uslov kupovine | Potvrđeno (pravila) | Nije viđen |
| 3 | Udružena potražnja | Zbir ponuda raste i dostiže niži prag | Mehanizam potvrđen | Nije poznato da li sajt prikazuje zbir; ako ne, animacija označena kao ilustracija |
| 4 | Prodavac bira kupce | Po isteku roka prodavac potvrđuje izabrane kupce | Potvrđeno (pravila) | Nije viđen |
| 5 | Ugovor | Platforma generiše obrazac ugovora koji se potpisuje | Potvrđeno tekstom | Nije viđen |
| 6 | Uslovi isporuke i kontakt | Učesnici vide uslove kupovine, isporuke i kontakt druge strane | Potvrđeno tekstom | Nije viđen |
| 7 | Izmena ili povlačenje ponude | Kupac menja ponudu do isteka roka | Potvrđeno (pravila) | Nije viđen |
| 8 | Registracija firme | Tri koraka (Info, Company, Networks); PIB, matični broj, dokaz o upisu u registar | Potvrđeno | Viđen (vaši snimci) |
| 9 | Diskretna kupovina | Opcija „Shopping privacy“ pri registraciji | Opcija postoji; značenje potvrditi | Viđen (polje za izbor) |

**Preporuka za snimanje:** kontrolisani demo nalozi, jedan kupac i jedan prodavac, i test-oglas sa izmišljenim proizvodom, označenim kao primer. Tako se ceo tok može snimiti bez prikazivanja stvarnih firmi i cena. Registracija je dugačka (tri koraka i prilozi), pa je u videu treba prikazati kratko, kao poruku da učestvuju samo registrovane firme.

## 6. Najčešće nedoumice koje video treba da razjasni

Nedoumice označene sa „Da“ imaju odgovor u izvorima i mogu odmah u scenario; za ostale je potreban odgovor klijenta pre nego što se pomenu u videu. Ovo su očekivana pitanja publike, izvedena iz modela, a ne podaci iz ankete.

| Nedoumica gledaoca | Odgovor iz izvora | Spremno za video |
| --- | --- | --- |
| Ko može da učestvuje? | Firme, preduzetnici i registrovane delatnosti, domaći i strani | Da |
| Da li mogu da platim više nego što želim? | Ne, ako izabere uslov „ne iznad ponuđene cene“ | Da |
| Ko isporučuje robu? | Prodavac, na adresu kupca ili dogovorenu lokaciju | Da |
| Da li je kupovina pravno sigurna? | Ugovor obavezujući potpisom; sporovi pred ugovorenim sudom ili arbitrom | Da |
| Da li je učlanjenje besplatno? | Za kupce: „Pridružite se besplatno“ | Da, samo za registraciju |
| Koliko traje trgovina i ko određuje rok? | Rok određuje prodavac, najviše 90 dana | Da |
| Mogu li da se predomislim? | Da, do isteka roka; posle toga prodavac može da aktivira depozit | Da, uz pomen depozita |
| Odgovaram li za druge kupce? | Ne; zbir ponuda nije zajednička ponuda | Da |
| Šta ako se ne skupi dovoljno kupaca? | Preporuka: prodavac obustavlja trgovinu i obaveštava kupce | Posle potvrde (preporuka, ne obaveza) |
| Moram li da platim unapred? | Roba se plaća kad se dostigne cena; pravila pominju depozit kao garanciju | Posle potvrde depozita |
| Ko vidi moje podatke? | Korisničko ime; opcija „Shopping privacy“ | Posle potvrde |
| Koliko košta prodavca? | Provizija ili članarina nisu javno opisane | Ne |
| Koju robu mogu da prodam? | Kategorije nisu poznate | Ne |
| Po čemu se razlikuje od sajtova sa kuponima? | Cena zavisi od zbira ponuda, ne od unapred zadatog popusta | Da |

## Analiza referentnih video-snimaka

Oba referentna videa nisam pogledao i ne mogu da ih analiziram: YouTube nije dostupan iz ovog okruženja, a pretraga po ID-u nije vratila ni naslov ni kanal. Ništa o njihovoj strukturi, tempu, muzici ili grafici zato ne navodim.

| Referenca | Naslov i kanal | Status |
| --- | --- | --- |
| [youtube.com/watch?v=SH9MDkLsQMw](https://www.youtube.com/watch?v=SH9MDkLsQMw) | Nepoznato | Nije pogledano |
| [youtube.com/watch?v=u-KLsP8bzMw](https://www.youtube.com/watch?v=u-KLsP8bzMw) | Nepoznato | Nije pogledano |

**Šta mi je potrebno (dovoljna je jedna opcija):**

1. **Dozvola za YouTube u okruženju.** U podešavanjima okruženja (Network access) dodati domene youtube.com, googlevideo.com i ytimg.com. Tada mogu da preuzmem titlove i izdvojim kadrove na svakih nekoliko sekundi, pa da analiziram strukturu, montažu i grafiku. Zvuk i muziku ne mogu da čujem; govor mogu da pratim samo kroz titlove, ako video ima titlove.
2. **Transkript i snimci ekrana.** Transkript sa YouTube-a („Prikaži transkript“) i 10–15 snimaka ekrana ključnih kadrova sa vremenskom oznakom.
3. **Video fajlovi.** MP4 fajlovi oba videa, dodati u repozitorijum ili poslati na drugi način.

**Uz materijal, kratko napišite šta vam se dopada u svakom videu:** ton, tempo, prezenter, grafika ili način objašnjavanja. Analiza će onda obuhvatiti strukturu priče, tempo i trajanje scena, odnos naracije, snimaka ekrana i animacija, primere, muziku, titlove i poziv na akciju, sa tehnikama primenljivim na eBerzu.

## 7. Informacije za potvrdu pre produkcije

Otvoreno je još 21 od 27 pitanja; šest je odgovoreno iz pravila poslovanja i vaših snimaka, a odgovore iz pravila treba samo potvrditi. Pitanja 1–10 određuju kako će scenario objasniti trgovinu. Odgovore možete upisati direktno u kolonu „Odgovor“.

| # | Tema | Pitanje | Zašto je važno | Odgovor |
| --- | --- | --- | --- | --- |
| 1 | Pravila | Ko određuje rok trgovine i koliko ona obično traje? | Scena primera grupne kupovine | Prodavac; najviše 90 dana (pravila) |
| 2 | Pravila | Kada se trgovina zatvara? | Kraj primera u videu | Istekom roka iz oglasa; zatim prodavac bira kupce, preporučeno u roku od 5 radnih dana (pravila) |
| 3 | Pravila | Šta se dešava ako se željeni prag ne dostigne? Može li kupac da odustane? | Najčešća nedoumica kupaca | Preporuka: prodavac obustavlja trgovinu i obaveštava kupce; kupac može da povuče ponudu do roka (pravila) |
| 4 | Pravila | Da li kupac unosi „željenu cenu“ ili samo količinu? | Prikaz izbora na ekranu | Tačnu količinu, cenu iz tabele popusta i uslov kupovine (pravila) |
| 5 | Pravila | Postoji li minimalna količina po kupcu ili po trgovini? | Primer sa brojevima |  |
| 6 | Pravila | Kako se potpisuje ugovor: elektronski ili na papiru? | Scena ugovora |  |
| 7 | Pravila | Kako i kada se plaća: direktno prodavcu, avansno, u kom roku? | Poruka o plaćanju |  |
| 8 | Pravila | Depozit kupca: da li je obavezan, koliki je i kada se daje? | Poruka „plaća se tek kad se dostigne cena“ |  |
| 9 | Pravila | Koji su svi uslovi kupovine u „Conditions of purchase“? | Prikaz ponude kupca |  |
| 10 | Pravila | Da li je dokument „Business rules on eBerza“ aktuelan i postoji li na srpskom? | Svi nalazi iz pravila |  |
| 11 | Učesnici | Ko može da kupuje: samo firme i preduzetnici ili i fizička lica? | Publika i jezik videa | Firme, preduzetnici i registrovane delatnosti (forma za registraciju) |
| 12 | Učesnici | Kako izgleda registracija firme i da li se firma verifikuje? | Scena registracije, poverenje | Tri koraka, PIB, matični broj i dokaz o upisu (snimci); otvoreno je da li eBerza proverava dokumenta |
| 13 | Učesnici | Šta tačno uključuje opcija „Shopping privacy“? | Poruka o diskreciji |  |
| 14 | Učesnici | Da li kupci u trgovini vide jedni druge i ukupnu prijavljenu količinu? | Animacija udruživanja |  |
| 15 | Troškovi | Da li platforma naplaćuje proviziju ili članarinu, kome i koliko? Stranica o franšizi pominje udeo franšizanta od 1,5% po transakciji. | Poruka o ceni korišćenja |  |
| 16 | Ponuda | Koje kategorije robe su danas aktivne? Smemo li da prikažemo stvarne oglase? | Snimci ekrana, primer proizvoda |  |
| 17 | Ponuda | Da li se mogu nuditi i usluge, ili samo roba? | Obuhvat poruke |  |
| 18 | Platforma | Da li je sajt menjan od 2020. ili se redizajn planira pre snimanja? | Snimci ne smeju brzo da zastare |  |
| 19 | Platforma | Možete li otvoriti demo nalog kupca i prodavca i test-oglas za snimanje? | Autentičan prikaz toka |  |
| 20 | Kampanja | Glavni cilj: registracija kupaca, prodavaca ili oba? Koji je jedan glavni poziv na akciju? | Struktura i završetak videa |  |
| 21 | Kampanja | Gde će se video koristiti: sajt, YouTube, LinkedIn, sajmovi, prodajni sastanci? | Trajanje, titlovi, formati |  |
| 22 | Kampanja | Da li video pominje franšizu ili samo kupce i prodavce? | Obuhvat poruke |  |
| 23 | Kampanja | Treba li i engleska verzija? | Naracija, titlovi, grafika |  |
| 24 | Brend | Koji je zvanični oblik naziva (eBerza ili e-Berza) i da li je „pametna trgovina“ aktuelan slogan? | Grafika i naracija |  |
| 25 | Brend | Logo (SVG), zvanične boje (HEX), fontovi, brand book i postojeći materijali? | Vizuelna doslednost |  |
| 26 | Dokazi | Postoje li stvarni korisnici ili rezultati koje smemo da navedemo, uz njihovu saglasnost? | Kredibilitet bez izmišljanja |  |
| 27 | Pristup | Možete li dodati eberza.rs i eberza.com u dozvoljene domene okruženja, ili poslati tekst stranica FAQ i Pravila? | Provera svih nalaza na živom sajtu | Delimično: poslati su snimci registracije i link ka FAQ; FAQ i pravila još nisu otvoreni |

## Sledeći koraci

Faza 2 (kreativni koncept) čeka vašu potvrdu i odgovore na pitanja 5–10, 15 i 20. Do tada ne pravim koncepte, scenario, slike ni video.

**Odluke klijenta (16. 10. 2026.):**

- Video govori firmama i preduzetnicima (B2B), ne građanima.
- Produkcija ne koristi Remotion ni slične alate koji video prave iz koda. Montaža i animacija rade se u klasičnim alatima, a izbor alata dolazi u fazi 4.

* [x] Potvrditi publiku: firme i preduzetnici
* [ ] Omogućiti pristup: dodati eberza.rs i eberza.com u dozvoljene domene okruženja ili poslati tekst stranica FAQ i Pravila (link ka FAQ je stigao, ali stranica nije dostupna iz okruženja)
* [ ] Poslati materijal za referentne videe (YouTube u dozvoljenim domenima, transkript sa snimcima ekrana ili MP4 fajlovi)
* [ ] Odgovoriti na otvorena pitanja u sekciji 7
* [ ] Poslati logo, zvanične boje, fontove i postojeće materijale
* [ ] Otvoriti demo nalog kupca i prodavca za snimanje toka

Kada pristup bude omogućen, proveriću svaki citat iz ovog dokumenta na živom sajtu, dopuniti vizuelni identitet i analizirati reference.

## Izvori

- Snimci ekrana stranice za registraciju (od klijenta, 16. 10. 2026.): `assets/registracija-*.png`
- [Business rules on eBerza — pravila poslovanja, EN](https://eberza.com/api/documents/152/document) (posredno, izvodi preko pretrage)
- [eberza.rs/sr — početna strana](https://eberza.rs/sr) (posredno, preko indeksa pretraživača)
- [eberza.rs/sr/buyers — kupci](https://eberza.rs/sr/buyers) (posredno)
- [eberza.rs/en/sellers — prodavci, EN](https://eberza.rs/en/sellers) (posredno)
- [eberza.rs/en/franchise — franšiza, EN](https://eberza.rs/en/franchise) (posredno)
- [eberza.rs/en/faq — FAQ](https://eberza.rs/en/faq) (nije otvoren; nije u indeksu pretraživača)
- [Danas: „eBerza“ rešenje za ulazak srpskih firmi na globalno tržište (2018.)](https://www.danas.rs/vesti/ekonomija/eberza-resenje-za-ulazak-srpskih-firmi-na-globalno-trziste/)
- [Elektronsko bankarstvo: E-berza pomaže srpskim firmama da uđu na globalno tržište (27. 11. 2018.)](https://www.elektronskobankarstvo.rs/e-berza-pomaze-srpskim-firmama-da-udju-na-globalno-trziste/)
- [International Franchise Expo 2024 — profil izlagača eBerza](https://www.franchiseexpo.com/ife/exhibitors/afeja-belgrade)
- [Facebook: eBerza - pametna trgovina](https://www.facebook.com/eberza.rs/)
- [Justia: prijava žiga EB EBERZA, 79374476](https://trademarks.justia.com/793/74/eb-79374476.html)
- [Pravilnik o obrascu za odustanak, „Sl. glasnik RS“ 21/2022, na eberza.rs](https://www.eberza.rs/api/documents/166/document)

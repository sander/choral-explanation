[🏔️ Alkemio](https://welcome.alkem.io/) › [🏔️ TIP](https://alkem.io/tip/dashboard) › Kennisbank
# 📄 Wat kunnen we als TIP leren van OpenPeppol als raamwerk om gegevens uit te wisselen?
Om te komen tot een multi corner model voor uitwisseling is er een structuur nodig om elkaar te vinden en om met elkaar te verbinden. OpenPeppol heeft binnen en buiten Europa een dergelijke structuur voor het ontvangen en versturen van orders en facturen. Wat kunnen we daarvan leren?

***
Vraag oorspronkelijk gesteld door [🏔️ Sander Boer](https://alkem.io/user/sander-boer-499). [`🏔️ Origineel`](https://alkem.io/tip/collaboration/watkunnenwealsti-6516)

- ## <a id="besteenhoopov-1407"></a> 📌 Best een hoop.... over Peppol
  OpenPeppol is een eDelivery implementatie die gebruik maakt van de standaard AS4. Inmiddels zijn er vele landen aangesloten op dit netwerk; ook buiten Europa. Veel informatie is te vinden op hun site: [🌐 The Future Is Open - OpenPeppol. ](https://peppol.org/)Het huidige gebruik richt zich op het versturen en ontvangen van orders en facturen maar Peppol is zo opgezet dat er ook andere gegevenstromen mogelijk zijn. Daar wordt inmiddels ook mee geëxperimenteerd. Ook is Peppol geschikt om informatie uit te wisselen tussen natuurlijke personen als er maar een goede identifier beschikbaar is (zoals IBAN). Peppol is geschikt om naast factuurstromen de uitwisseling van medische informatie tussen zorgaanbieder en afnemer te organiseren: het bestaat nu alleen nog niet.
  
  Binnen Nederland zijn er diverse serviceproviders actief die onder toezicht staan van de Nederlandse Peppolautoriteit (zie [🌐 Peppol: dé internationale standaard voor digitaal zakendoen (](https://peppolautoriteit.nl/?gclid=EAIaIQobChMI7Mqv0M_XggMVi_J3Ch04BwJVEAAYASAAEgJxDfD_BwE)[🌐 peppolautoriteit.nl](http://peppolautoriteit.nl)[🌐 ). ](https://peppolautoriteit.nl/?gclid=EAIaIQobChMI7Mqv0M_XggMVi_J3Ch04BwJVEAAYASAAEgJxDfD_BwE)De gegevensuitwisseling vindt plaats in een four cornermodel: bedrijven kiezen zelf een (of meerdere) serviceprovider(s) om gegevens te sturen en ontvangen / de serviceproviders zetten hun klanten in een groot telefoonboek (SML en SMP)
  
  SMP staat voor Service Metadata Publisher. Een Peppol SMP is een partij die een register bijhoudt van de adresinformatie van elke ontvanger op het Peppol netwerk, welk Access Point zij gebruiken en welke berichten zij kunnen ontvangen. SML staat voor Service Metadata Locator. De Peppol SML bevat de identificatienummers van alle ontvangers aanwezig op het netwerk, alsook in welke SMP de detailinformatie kan gevonden worden. Deze bronnen zijn alleen te raadplegen en aan te passen via een erkende serviceprovider.
  
  Het is mogelijk om binnen Openpeppol een structuur neer te zetten om de communicatie tussen QTSP's mogelijk te maken. Dit kan helpen bij het realiseren van een interoperabiliteitsframework tussen verschillende QERDS aanbieders (zie ETSI EN 319 522 1 daar staat geen gemeenschappelijke infrastructuur in en Peppol zou daar ook geschikt voor kunnen zijn) . Het is ook mogelijk om eisen te stellen op welk betrouwbaarheidsniveau een gebruiker (bedrijf of persoon) geïdentificeerd moet zijn. Peppol maakt hier nu nog geen gebruik van binnen factuur en orderstromen maar het ligt in de lijn van de verwachting dat dit er wel tzt gaat komen. Er bestaat nu nog geen implementatie waarbij een QERDS gecombineerd is met een Peppol uitwisselstroom maar dit is wel mogelijk. Verder zijn er binnen peppol ook mogelijkheden om berichten op inhoud te controleren en dat maakt het waarschijnlijk ook mogelijk om validatiefuncties in te richten.

  ***
  Antwoord oorspronkelijk geschreven door [🏔️ Sander Boer](https://alkem.io/user/sander-boer-499).  [`🏔️ Origineel`](https://alkem.io/tip/collaboration/watkunnenwealsti-6516/posts/besteenhoopov-1407)

<details><summary><code>Schrijf een antwoord</code></summary>

1. [Log in op Alkemio](https://identity.alkem.io/login).
2. Als je nog niet lid bent van de TIP-space, [vraag en wacht op toegang](https://alkem.io/tip/dashboard).
3. Ga naar de [vraag in Alkemio](https://alkem.io/tip/collaboration/watkunnenwealsti-6516).
4. Klik op (+).
5. Neem kennis van de placeholder-tekst en verwijder deze.
6. Verstuur je antwoord.

Je antwoord verschijnt direct op Alkemio. Na synchronisatie verschijnt het ook hier.

</details>

* * *
<small>Bijdragen zijn gelicenseerd onder [🌐 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.nl).</small>

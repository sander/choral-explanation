[Alkemio](https://welcome.alkem.io/) › [TIP](https://alkem.io/tip/dashboard) › Kennisbank
# [Wat is identity matching en discovery?](https://alkem.io/tip/collaboration/watisidentitymatc-4236)
Oorspronkelijk gevraagd door [Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912)
>Als lid werkgroep Techniek wil ik begrijpen __wat__ de domeinen van identity matching en discovery behelzen, zodat we hier een standaard op kunnen vaststellen. (Denk aan BSN, pseudoniemen en koppelcodes.)
## Antwoorden
>### [Scriptie TU Delft over identity matching in Europa op basis van het BRP](https://alkem.io/tip/collaboration/watisidentitymatc-4236/posts/scriptietudelft-196)
>Oorspronkelijk geantwoord door [Sander Dijkhuis](https://alkem.io/tip/collaboration/watisidentitymatc-4236/posts/scriptietudelft-196)
>>Zie scriptie [*Dutch Identity Matching: The Devil’s in the Details*](https://repository.tudelft.nl/islandora/object/uuid%3A5d52babb-c6b0-4c96-8f93-8f3129ba448d) door Anton Welling de Arruda.
>>
>>Hier wordt *identity matching* gedefinieerd als: het proces om te bepalen of een persoon al een account heeft bij de dienst waar deze zijn zich wil laten authenticeren. De scriptie verkent een Europese implementatie voor identity matching ondersteund door de Nederlandse Basisregistratie Personen (BRP).
>>
>>Dit onderwerp is voor TIP relevant aangezien elke deelnemer eigen dossiervorming doet, natuurlijke personen herkent op basis van Europees erkende middelen, en geen directe toegang heeft tot een centrale gebruikersdatabase.
>>
>>In de EU bestaat nog geen standaard methode voor identity matching bij grensoverschrijdend inloggen. In de praktijk wordt een set persoonsidentificatiegegevens (*person identification data*, PID) gebruikt, die niet altijd voldoende is. Deze PID is binnen eIDAS gedefinieerd voor centrale authenticatiediensten en wordt binnen EUDI uitgebreid voor decentrale wallets.
>>
>>De scriptie gaat in op de vraag hoe een Nederlandse gereguleerde of publieke partij die op een buitenlandse EUDI-wallet vertrouwt, identity matching kan uitvoeren met eigen opgeslagen dossiers. Deze buitenlandse wallet zal PID bevatten zonder BSN.
>>
>>Momenteel loopt een vergelijkbaar proces onder eIDAS via [BSNk PP](https://www.logius.nl/domeinen/toegang/bsnk-pp/hoe-werkt-het):
>>
>>1.  Het buitenlandse knooppunt authenticeert de burger.
>>
>>2.  Het buitenlandse knooppunt levert PID aan het Nederlandse knooppunt, inclusief een *eIDAS-identifier*: een uniek nummer voor de burger binnen de context van de relatie tussen de twee lidstaten.
>>
>>3.  Het Nederlandse knooppunt vraagt de burger om het BSN in te voeren en controleert bij het BRP of deze inderdaad bij de naam en geboortedatum in het PID past. Automatisch, en bij twijfel door een medewerker.
>>
>>4.  Het Nederlandse knooppunt vertaalt de eIDAS-identifier naar:
>>
>>    1.  een “PP-EU”: polymorf pseudoniem op basis van de eIDAS-identifier
>>    2.  een “PP-BSN”: polymorf pseudoniem op basis van het ingevulde BSN (moet PI-BSN zijn?)
>>
>>5.  Het Nederlandse knooppunt deelt, afhankelijk van autorisatie van de vertrouwende partij, de naam, geboortedatum, en een voor de Nederlandse vertrouwende partij specifiek afgeleide:
>>
>>    1.  “VI”: versleutelde identiteit op basis van PP-BSN (om BSN te verwerken), of
>>    2.  “VP”: versleuteld pseudoniem op basis van PP-EU of PP-BSN (zonder mogelijkheid om BSN te verwerken).
>>
>>6.  De vertrouwende partij gebruikt de versleutelde identifier, de naam en de geboortedatum om zelf matching uit te voeren. Schijnbaar mag deze niet vertrouwen op de matching die het Nederlandse knooppunt aanbiedt met de versleutelde identifier alleen.
>>
>>Bij deze vraag spelen tradeoffs rond privacy en betrouwbaarheid. Met name is de vraag of het Nederlandse knooppunt en bijbehorende diensten uit hun rollen van *single point of failure* en *privacy hotspot* kunnen worden gehaald. Specifiek voor identity matching kunnen zich twee typen falen rond betrouwbaarheid voordoen:
>>
>>*   false positives: match met een dossier gevonden, terwijl het om een andere persoon gaat
>>*   false negative: geen match met een dossier gevonden, terwijl het om dezelfde persoon gaat
>>
>>De auteur ziet deze oorzaken bijdragen aan deze problemen:
>>
>>*   verschillen in opgeslagen PID
>>*   homoniemen (verschillende namen hetzelfde opgeschreven)
>>*   verschillen in spelling en opmaak in PID
>>*   veranderende eIDAS-identifier voor een en dezelfde persoon
>>*   burger heeft PID vanuit verschillende lidstaten
>>*   veranderingen en fouten in PID
>>
>>De EUDI-wallet lost dit niet op, maar kan wel bijdragen: hij stelt vertrouwende partijen in staat om bij de burger zelf voldoende PID uit te vragen voor identity matching. Hiermee verkleint de rol en verantwoordelijkheid van het Nederlandse knooppunt. Dit knooppunt blijft wel noodzakelijk voor diensten die identity matching met de BRP vereisen. De auteur ziet verschillende oplossingsrichtingen voor wanneer straks iemand met een buitenlandse EUDI-wallet zaken wil doen met een Nederlandse vertrouwende partij:
>>
>>*   **Overheidsgericht**: de eIDAS-opzet, maar waar de wallet direct het Nederlandse knooppunt vraagt om na autorisatie van de vertrouwende partij een gewaarmerkte VI/VP op te halen voor een specifiek verzoek.
>>*   **Hybride**: de overheidsgerichte opzet, maar waarbij de wallet zelf autorisatie uitvoert en het VI/VP voor een vertrouwende partij kan hergebruiken.
>>*   **Wallet-aanbiedersgericht**: de hybride opzet, maar waarbij de wallet zelf het VI/VP genereert op basis van een eenmalig door de overheid uitgegeven PP-BSN en/of PP-EU en een door de wallet-aanbieder ingezette HSM.
>>
>>Let op dat het PP-EU in de context van de EUDI-wallet misschien helemaal niet meer relevant is.
>>
>>De auteur concludeert dat de wallet-aanbiedersgerichte oplossingsrichting het meest wenselijk is verband met de behoefte aan privacy en controle voor burgers.
>#### Reacties
>>##### [Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912) 2023-08-30 17:28 UTC
>>>[@Paul Staal](https://alkem.io/user/paul-staal-854) beter laat dan nooit: ik zou je nog eens inzichten op dit onderwerp sturen. Dit is een eerste stuk.
>>##### [Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912) 2023-08-30 17:29 UTC
>>>[@Nitesh Bharosa](https://alkem.io/user/nitesh-bharosa-5829) dank nog voor het delen. Ik heb mijn samenvatting hier geplaatst. Weet jij of dit onderwerp verder binnen TU Delft / Digicampus / BZK is opgepakt?
>### [Discovery van digitale identiteiten en adressen](https://alkem.io/tip/collaboration/watisidentitymatc-4236/posts/discoveryvandigita-8878)
>Oorspronkelijk geantwoord door [Sander Dijkhuis](https://alkem.io/tip/collaboration/watisidentitymatc-4236/posts/discoveryvandigita-8878)
>>In de [When Willeke can get rid of paperwork](https://repository.tudelft.nl/islandora/object/uuid%3A4c2005ea-9cfd-420f-80fb-e8714be0bdd5) introduceren we het vermogen van *discovery* (ontdekken, vinden): het kunnen **herkennen** en **adresseren** van andere identiteiten. Dit is voor TIP relevant: als straks iedereen een betrouwbare digitale identiteit heeft, hoe vind ik die dan zonder toegang tot een centraal telefoonboek?
>>
>>In de fysieke wereld kunnen we dit doen door te vertrouwen op fysieke eigenschappen zoals menselijke lichamen en thuis- of kantooradressen.
>>
>>In de digitale wereld hebben we te maken met representaties. We kunnen een digitale identiteit **herkennen** door de attributen ervan te vergelijken, vastgesteld met een zeker betrouwbaarheidsniveau, met een referentiemodel. We kunnen een digitale identiteit **ontdekken** door door iemand geïntroduceerd te worden en ons referentiemodel bij te werken, of door een toegankelijk referentiemodel te raadplegen.
>>
>>Deze referentiemodellen kunnen gecentraliseerd zijn (denk aan een register zoals KvK en BRP) of gedecentraliseerd (denk aan de contactenlijst op mijn telefoon).
>>
>>We hebben twee modellen gezien voor discovery:
>>
>>*   Zoals beschreven in [Scriptie TU Delft over identity matching in Europa op basis van het BRP](https://alkem.io/tip/collaboration/watisidentitymatc-4236/posts/scriptietudelft-196): personen halen een identiteitsverklaring op bij een centrale basisregistratie, om zich via een website-authenticatie kenbaar te maken.
>>*   Zoals beschreven in [Ontwerppatronen voor het koppelen van identiteiten](https://alkem.io/tip/collaboration/watisidentitymatc-4236/posts/ontwerppatronenvoor-2306): personen halen een identiteitsverklaring op bij een QTSP (op basis van een centrale basisregistratie), om zich via een out-of-band verkregen koppelcode kenbaar te maken via infrastructuur voor berichtuitwisseling.
>#### Reacties
>>##### [Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912) 2023-08-31 09:03 UTC
>>>[@Paul Staal](https://alkem.io/user/paul-staal-854) Gisteren deelde ik met je een samenvatting van de TU Delft-scriptie over identity matching. Bij deze ter info een korte algemenere inleiding op de concepten identity linking en discovery.
>### [Ontwerppatronen voor het koppelen van identiteiten](https://alkem.io/tip/collaboration/watisidentitymatc-4236/posts/ontwerppatronenvoor-2306)
>Oorspronkelijk geantwoord door [Sander Dijkhuis](https://alkem.io/tip/collaboration/watisidentitymatc-4236/posts/ontwerppatronenvoor-2306)
>>In de context van project HDN Goed IDee schreef ik *Design patterns for identity linking*, versie 2 van 2022-10-28.
>>
>>In dit stuk bedoel ik met *identity linking* ongeveer hetzelfde als de scriptie [Dutch Identity Matching](https://alkem.io/tip/collaboration/watisidentitymatc-4236/posts/scriptietudelft-196) bedoelt met *identity matching*: het koppelen van inkomende persoonsidentificatiegegevens (PID) uit andermans dossier aan een eigen dossier binnen een gegeven context.
>>
>>In de gegeven context van vastgoedtransacties zijn uitgangspunten:
>>
>>*   geen gebruik van BSN, want hiervoor bestaat geen grondslag;
>>*   geen gebruik van BRP, want hiervoor ontbreekt toegang tot bijbehorende voorzieningen;
>>*   geen matching op basis van namen;
>>*   een **intermediair** heeft al een dossier en out-of-band contact met de consument, bijvoorbeeld op kantoor of via een mijn-omgeving;
>>*   de consument heeft een **handelingsomgeving**;
>>*   beide zijn verbonden met een **platform** voor berichtuitwisseling.
>>
>>Het doel in deze context is om een betekenisvolle **connectie** tussen consument en meerdere dienstverleners te maken: zorgen dat alle dienstverleners een *lokaal unieke identifier* hebben voor de consument, op basis waarvan ze inkomende berichten kunnen koppelen. Denk bij deze dienstverleners aan de intermediair en aan een geldverstrekker.
>>
>>Hiermee is de context gemakkelijker dan in sommige andere ketens waarbij de identificatie globaal uniek moet zijn. Zulke ketens zullen een beroep doen op een centrale basisregistratie.
>>
>>Het stuk beschrijft drie ontwerppatronen:
>>
>>*   **Intermediair-beheerde connectie**: De intermediair maakt verbinding met de handelingsomgeving van de consument, en geeft de bijbehorende identifier direct door aan andere dienstverleners.
>>*   **Platform-beheerde connectie**: De intermediair vraagt het platform om een koppelcode; het platform maakt verbinding met de handelingsomgeving, en geeft de bijbehorende identifier direct door aan de intermediair en andere door de intermediair gemachtigde dienstverleners.
>>*   **Burger-beheerde connectie**: De burger beheert een polymorf pseudoniem BSN (PP-BSN) in haar EUDI-wallet, en initieert direct via het platform connecties met dienstverleners. De intermediair heeft in het identity matching geen rol.
>>
>>In elk van de drie patronen draagt de beheerder de verantwoordelijkheid om de koppeling integer te houden, en de identifier alleen vrij te geven aan bevoegde partijen.
>>
>>Zolang het PP-BSN niet beschikbaar is voor burger-beheerde connecties, raad ik aan om in te zetten op platform-beheerde connecties. Een intermediair-beheerde connectie legt onnodig veel verantwoordelijkheid bij de intermediair: het verbinden met verschillende handelingsomgevingen, het afdwingen van machtigingen, en het integer houden van de relatie tussen het eigen dossiernummer en de van de handelingsomgeving verkregen identifier. Hoewel een platform deze problemen niet wegneemt, kan het wel voor een generieke oplossing zorgen met hergebruik van de informatiebeveiligingsmaatregelen die al nodig waren voor berichtuitwisseling.
>>
>>Binnen HDN Goed IDee is dan ook gekozen voor platform-beheerde connecties. Deze zijn we nu aan het beproeven.
* * *
_Bijdragen zijn gelicenseerd onder [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.nl)._

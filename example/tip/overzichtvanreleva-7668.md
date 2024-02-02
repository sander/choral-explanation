[🏔️ Alkemio](https://welcome.alkem.io/) › [🏔️ TIP](https://alkem.io/tip/dashboard) › Kennisbank
# [🏔️ Analyse van gerelateerde initiatieven](https://alkem.io/tip/collaboration/overzichtvanreleva-7668)
Oorspronkelijk gevraagd door [🏔️ Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912)
>Er zijn verschillende initiatieven op wallets, kluisjes en uitwisseling. Deze inventariseren we langs vraag/antwoord in onze [kennisbank](https://alkem.io/tip/knowledge-base). Bijvoorbeeld:
>
>*   [Wat voor wallet-initiatieven zijn er in Nederland en wat is de impact op TIP?](https://alkem.io/tip/collaboration/watvoorwallet-init-2068)
>*   [Wat voor initiatieven zijn er voor de inzet van datakluizen in Nederland en wat is de impact op TIP?](https://alkem.io/tip/collaboration/watvoorinitiatieve-1713)
>
>Daarnaast ontwikkelen we met TIP Werkgroep Kennis een gestructureerd overzicht langs een aantal vragen. Deze vragenlijst herzien we continu op basis van voortschrijdend inzicht. We nodigen je graag uit om het formulier in te vullen voor relevante initiatieven.
>
>We richten ons op de implementatieplateaus voor TIP: (1) signatures en seals, (2) gegevensuitwisseling middels aangetekende bezorging, (3) brede toepassing TIP-afspraken. Dat betekent dat we in de gap-analyse van initiatieven langs deze prioritering naar de specificaties van basisfunctionaliteiten kijken. Zie ook: [Wat zijn de basisfunctionaliteiten van TIP?](https://alkem.io/tip/collaboration/watzijndebasisfun-743)
>
>De werkgroep Kennis verzorgt een formulier met controlevragen, coördineert de analyse, en communiceert hierover met TIP-partners en belanghebbenden. Aanspreekpunt voor de verschillenanalyse is [Ralph Verhelst](https://alkem.io/user/ralph-verhelst-6873). Om bij te dragen heb je een account bij Alkemio nodig: zie [Aanmelden bij Alkemio](https://alkem.io/login?returnUrl=https://alkem.io/tip).
## Antwoorden
>### [🏔️ DIIP](https://alkem.io/tip/collaboration/overzichtvanreleva-7668/posts/diip-7901)
>Oorspronkelijk geantwoord door [🏔️ Sander Dijkhuis](https://alkem.io/tip/collaboration/overzichtvanreleva-7668/posts/diip-7901)
>>## Beschrijving
>>
>>### Wat is het initiatief?
>>
>>DIIP is een technische standaard voor interoperabiliteit van attesteringen volgens het W3C-model, met de bedoeling om future-proof naar eIDAS2 / ARF te implementeren.
>>
>>## Belangen
>>
>>### Op welke sectoren is dit initiatief van toepassing?
>>
>>Cross-sectoraal, maar er wordt bewust gekozen voor de W3C-standaarden die in de private sector een groeiende rol spelen in plaats van voor de ISO-standaarden die in de publieke sector voor bijvoorbeeld rijbewijzen wordt gebruikt.
>>
>>### Wie doen er mee aan dit initiatief?
>>
>>De standaard wordt geschreven door:
>>
>>*   Animo Solutions
>>*   Sphereon
>>*   TNO
>>
>>## Gap-analyse
>>
>>### Worden er elektronische handtekeningen en zegels gemaakt? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Signing data?
>>
>>Nee.
>>
>>### Worden er elektronische handtekeningen en zegels gevalideerd? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Validating signatures?
>>
>>Nee.
>>
>>### Worden er elektronische handtekeningen en zegels bewaard? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Preserving signatures?
>>
>>Nee.
>>
>>### Zijn er andere basisfunctionaliteiten van TIP van toepassing? Hoe verhoudt dit initiatief zich tot die TIP-basisfunctionaliteit?
>>
>>*   Attestation of attributes: DIIP heeft een nadere uitwerking van enkele ARF-standaarden waar TIP naar verwijst als een van de mogelijkheden om attributen te attesteren. Daarbij is DIIP meer “opiniated” in haar keuze voor de W3C-standaarden in plaats van de ISO-standaarden. Voor toepassingen in TIP zullen ook andere standaarden relevant blijven.
>### [🏔️ Potential](https://alkem.io/tip/collaboration/overzichtvanreleva-7668/posts/potentialuc5-2150)
>Oorspronkelijk geantwoord door [🏔️ Sander Dijkhuis](https://alkem.io/tip/collaboration/overzichtvanreleva-7668/posts/potentialuc5-2150)
>>## Beschrijving
>>
>>### Wat is het initiatief?
>>
>>Potential is een Large Scale Pilot-consortium voor o.a. de EUDI-wallets. Binnen dit consortium richt Use Case 5 (UC5) zich op de toepassing van de wallet voor gekwalificeerde handtekeningen.
>>
>>## Belangen
>>
>>### Op welke sectoren is dit initiatief van toepassing?
>>
>>Cross-sectoraal.
>>
>>### Wie doen er mee aan dit initiatief?
>>
>>Vertegenwoordiging vanuit verschillende lidstaten en QTSPs. Namens Nederland: EZK en TIP. Deelname van TIP wordt inhoudelijk afgestemd in Werkgroep Techniek.
>>
>>## Gap-analyse
>>
>>### Worden er elektronische handtekeningen en zegels gemaakt? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Signing data?
>>
>>Ja, net als bij TIP gekwalificeerd op basis van het ESI-framework van ETSI, op een manier die past bij eIDAS1 en eIDAS2. De focus ligt op technische interoperabiliteit tussen wallet, vertrouwende partij en QTSP om de adoptie verder te vergroten.
>>
>>### Worden er elektronische handtekeningen en zegels gevalideerd? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Validating signatures?
>>
>>Ja, al heeft dit nog geen focus binnen UC5. Aangenomen wordt dat andere use cases deze basisfunctionaliteit conform het ESI-framework van ETSI implementeren. Wel staat gepland om in 2024 te onderzoeken hoe attesteringen kunnen worden meegenomen in de validatie.
>>
>>### Worden er elektronische handtekeningen en zegels bewaard? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Preserving signatures?
>>
>>Nee, dit heeft geen focus binnen UC5. Aangenomen wordt dat praktische use cases deze basisfunctionaliteit conform het ESI-framework van ETSI implementeren.
>>
>>### Zijn er andere basisfunctionaliteiten van TIP van toepassing? Hoe verhoudt dit initiatief zich tot die TIP-basisfunctionaliteit?
>>
>>*   Attestation of attributes: in 2024 kijkt UC5 naar welke attestering een QTSP nodig heeft om de sleutel voor handtekeningen/zegels te activeren, en eventueel om er een certificaat over uit te geven.
>### [🏔️ Peppol](https://alkem.io/tip/collaboration/overzichtvanreleva-7668/posts/peppol-6470)
>Oorspronkelijk geantwoord door [🏔️ Ralph Verhelst](https://alkem.io/tip/collaboration/overzichtvanreleva-7668/posts/peppol-6470)
>>## Beschrijving
>>
>>### Wat is het initiatief?
>>
>>Peppol" staat voor Pan-European Public Procurement Online. Het is een raamwerk dat digitale communicatie- en transactieprocessen tussen overheidsorganisaties en particuliere bedrijven mogelijk maakt. Het werd oorspronkelijk ontwikkeld door de Europese Unie als onderdeel van een initiatief om openbare aanbestedingsprocessen in heel Europa te stroomlijnen.
>>
>>Peppol biedt een reeks standaarden en technische specificaties om elektronische inkoopprocessen, zoals e-facturering, e-bestellingen en e-catalogi, te vergemakkelijken. Het is ontworpen om de interoperabiliteit te garanderen tussen verschillende inkoopsystemen en -processen die door verschillende organisaties worden gebruikt, waardoor naadloze en efficiënte grensoverschrijdende transacties mogelijk worden.
>>
>>Hoewel het in Europa begon, heeft het gebruik van Peppol zich internationaal uitgebreid, waarbij verschillende landen buiten Europa de normen hebben overgenomen.
>>
>><br>
>>
>>## Belangen
>>
>>### Op welke sectoren is dit initiatief van toepassing?
>>
>>Cross-sectoraal, maar de uitwisseling betreft financiële gegevens (facturering).
>>
>>### Wie doen er mee aan dit initiatief?
>>
>>Particuliere organisaties & overheidsorganisaties.
>>
>><br>
>>
>>## Gap-analyse
>>
>>### Worden er elektronische handtekeningen en zegels gemaakt? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Signing data?
>>
>>Peppol maakt gebruik van het AS4 profiel waarin handtekeningen gemaakt worden. Sommige lidstaten of partijen vereisen gekwalificeerde handtekeningen.
>>
>>Zie <https://joinup.ec.europa.eu/sites/default/files/document/2014-12/d1-1-part-1-background-and-scope_2.pdf>
>>
>>### Worden er elektronische handtekeningen en zegels gevalideerd? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Validating signatures?
>>
>>Zegels worden ook volgens het AS4 gevalideerd.
>>
>>### Worden er elektronische handtekeningen en zegels bewaard? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Preserving signatures?
>>
>>In het Peppol-netwerk worden doorgaans geen zegels of handtekeningen in de traditionele zin opgeslagen. Peppol is ontworpen om de uitwisseling van gestandaardiseerde elektronische documenten, zoals e-facturen, te vergemakkelijken. Deze documenten worden digitaal verstuurd en ontvangen via het Peppol-netwerk, dat gebruik maakt van strikte identificatie- en authenticatiemechanismen om de veiligheid en integriteit van de gegevens te waarborgen.
>>
>>Digitale handtekeningen kunnen echter wel een onderdeel zijn van de documenten die via Peppol worden verzonden. Deze digitale handtekeningen worden gebruikt om de authenticiteit en integriteit van een elektronisch document te garanderen. Ze zorgen ervoor dat het document niet is gewijzigd sinds het werd ondertekend en bevestigen de identiteit van de ondertekenaar.
>>
>>### Zijn er andere basisfunctionaliteiten van TIP van toepassing? Hoe verhoudt dit initiatief zich tot die TIP-basisfunctionaliteit?
>>
>>Later
>### [🏔️ Nuts (Zorg)](https://alkem.io/tip/collaboration/overzichtvanreleva-7668/posts/nutszorg-9315)
>Oorspronkelijk geantwoord door [🏔️ Ralph Verhelst](https://alkem.io/tip/collaboration/overzichtvanreleva-7668/posts/nutszorg-9315)
>>## Beschrijving
>>
>>### Wat is het initiatief?
>>
>>Het Nuts initiatief is een samenwerkingsproject binnen de Nederlandse gezondheidszorgsector, gericht op het verbeteren van de digitale communicatie en gegevensuitwisseling. Het doel van Nuts is om een gedecentraliseerde infrastructuur te creëren die zorgaanbieders in staat stelt om op een veilige en privacyvriendelijke manier informatie uit te wisselen.
>>
>><br>
>>
>>## Belangen
>>
>>### Op welke sectoren is dit initiatief van toepassing?
>>
>>Zorg
>>
>><br>
>>
>>### Wie doen er mee aan dit initiatief?
>>
>>Een verscheidenheid aan organisaties, waaronder softwareleveranciers, zorgaanbieders en adviesbureaus, die samenwerken om een gedecentraliseerd communicatienetwerk voor de zorg te realiseren. Daarnaast maken er zorgafnemers & toezichthouders gebruik van.
>>
>><br>
>>
>>## Gap-analyse
>>
>>### Worden er elektronische handtekeningen en zegels gemaakt? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Signing data?
>>
>><br>
>>
>>### Worden er elektronische handtekeningen en zegels gevalideerd? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Validating signatures?
>>
>>*…*
>>
>>### Worden er elektronische handtekeningen en zegels bewaard? Hoe verhoudt dit zich tot TIP-basisfunctionaliteit Preserving signatures?
>>
>>*…*
>>
>>### Zijn er andere basisfunctionaliteiten van TIP van toepassing? Hoe verhoudt dit initiatief zich tot die TIP-basisfunctionaliteit?
>>
>>*…*
>#### Reacties
>>##### [🏔️ Gijs van den Beucken](https://alkem.io/user/gijs-vandenbeucken-8950) 2024-02-02 11:31 UTC
>>>Algemene info
>>>https://nuts.nl
>>>
>>>In deze video wordt de roadmap, tijdlijn en migratiepad uitgelegd
>>>https://www.youtube.com/watch?v=lXcc0LJNahg
>>>
>>>Momenteel (voor de migratie) zijn de dit de docs:
>>>https://nuts-foundation.gitbook.io/v1/
* * *
<small>Bijdragen zijn gelicenseerd onder [🌐 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.nl).</small>

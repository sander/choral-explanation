[🏔️ Alkemio](https://welcome.alkem.io/) › [🏔️ TIP](https://alkem.io/tip/dashboard) › Kennisbank
# 📄 Kan een bank SCA delegeren aan een QTSP?
Als bank wil ik weten in hoeverre ik eisen aan *strong customer authentication* (SCA) kan delegeren aan een gekwalificeerd vertrouwensdienstverlener onder de eIDAS, met het oog op hergebruik van wallets en eventuele verplichtingen uit de herziening van eIDAS.

***
Vraag oorspronkelijk gesteld door [🏔️ Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912). [`🏔️ Origineel`](https://alkem.io/tip/collaboration/kaneenbankscadel-5381)

- ## <a id="toepassingvangekwa-1586"></a> 📌 Toepassing van gekwalificeerde certificaten en beperking van aansprakelijkheid
  [🌐 IANAL](https://en.wikipedia.org/wiki/IANAL) maar bij deze wat ik begrijp op basis van een aantal gesprekken.
  
  Banken zijn onder PSD2 Artikel 97(1) verplicht om SCA uit te voeren bij toegang, initiatie betaaltransacties, en andere riskante online acties. In Artikel 4(3) definieert PSD2 het concept SCA als multi-factor authenticatie van de gebruiker.
  
  Let op: SCA is onderdeel van een set aan risicogebaseerde maatregelen, en niet de kapstok waaronder ook alle andere risicogebaseerde maatregelen bij transacties vallen. Dus de vraag over SCA met een QTSP gaat niet over het geheel verleggen van de verantwoordelijkheid voor het maatregelenpakket, alleen over het delegeren van uitgifte en beheer van een authenticatiemiddel.
  
  Een gekwalificeerd certificaat (QC) is zo’n authenticatiemiddel, en wordt in de praktijk vaak aan een wallet uitgegeven. Daarbij aanvaardt de uitgevende QTSP aansprakelijkheid bij fouten in naleving van eIDAS bij identiteitsverificatie. De QTSP mag die aansprakelijkheid beperken. De beperking zal vaak samenhangen met de omzet die de QTSP maakt op die dienstverlening.
  
  Als de bank het risico op identiteitsfraude als hoog beoordeelt, is een mogelijke maatregel om een relatief vers QC te vereisen. Zo beperkt de bank het risico dat de wallet na uitgifte in handen is gekomen van een andere persoon. Er zijn ook andere maatregelen te bedenken.
  
  Stel de bank voert een betaaltransactie van €100M uit op basis van een vers QC uitgegeven door een QTSP die aansprakelijkheid beperkt tot €100k. Wat als de identiteit alsnog niet blijkt te kloppen, door het onvoldoende naleven van eIDAS door de QTSP, en daarmee de €100M naar de verkeerde rekening gaat?
  
  Nu is het nodig om naar twee bedragen te kijken:
  
  *   Onterecht verplaatst geld: €100M. Hier ligt voor de hand dat banken en/of partijen in de transactie aanvullende maatregelen treffen bovenop SCA. Denk aan verzekeringen of aanvullende procedures.
  *   Schade: denk aan herstelschade, bijvoorbeeld om de fraudeur te bereiken, en verminderde goodwill of winsten.
  
  In eIDAS is de aansprakelijkheid voor de schade rond vertrouwensdienstverlening geregeld. Deze zal in de praktijk veel lager liggen dan de onterecht verplaatste €100M. Daarmee lijkt de beperking in aansprakelijkheid door QTSPs geen barrière.

  ***
  Antwoord oorspronkelijk geschreven door [🏔️ Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912).  [`🏔️ Origineel`](https://alkem.io/tip/collaboration/kaneenbankscadel-5381/posts/toepassingvangekwa-1586)

    - #### 💬 Reactie van [🏔️ Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912) op 2024-01-10 18:56 UTC
          
      Zie ook deze gerelateerde vraag: [📄 Wat moet er geregeld worden rond de aansprakelijkheid zodra een PID geaccepteerd moet worden?](watmoetergeregeld-7715.md).
    - #### 💬 Reactie van [🏔️ Nitesh Bharosa](https://alkem.io/user/nitesh-bharosa-5829) op 2024-01-15 15:47 UTC
          
      👍
- ## 📌 Context waarin dit relevant is
  Automatisch verzameld op basis van verwijzingen:
  - [📌 Wat moet er geregeld worden rond de aansprakelijkheid zodra een PID geaccepteerd moet worden? Mogelijke rol voor QTSP](watmoetergeregeld-7715.md#mogelijkerolvoorq-9971)
<details><summary><code>Schrijf een antwoord</code></summary>

1. [Log in op Alkemio](https://identity.alkem.io/login).
2. Als je nog niet lid bent van de TIP-space, [vraag en wacht op toegang](https://alkem.io/tip/dashboard).
3. Ga naar de [vraag in Alkemio](https://alkem.io/tip/collaboration/kaneenbankscadel-5381).
4. Klik op (+).
5. Neem kennis van de placeholder-tekst en verwijder deze.
6. Verstuur je antwoord.

Je antwoord verschijnt direct op Alkemio. Na synchronisatie verschijnt het ook hier.

</details>

* * *
<small>Bijdragen zijn gelicenseerd onder [🌐 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.nl).</small>

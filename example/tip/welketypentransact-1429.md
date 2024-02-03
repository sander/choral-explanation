[🏔️ Alkemio](https://welcome.alkem.io/) › [🏔️ TIP](https://alkem.io/tip/dashboard) › Kennisbank
# 📄 Welke typen transacties zijn te ondertekenen?
Bij implementatie van de basisfunctionaliteit *Signing data* wil ik weten welke type transacties ik kan onderscheiden, zodat ik daarmee rekening kan houden in beleid.

***
Vraag oorspronkelijk gesteld door [🏔️ Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912). [`🏔️ Origineel`](https://alkem.io/tip/collaboration/welketypentransact-1429)

- ## <a id="pkioverheidauthent-6351"></a> 📌 PKIoverheid: authenticity, non-repudiation
  Onder PKIoverheid wordt onderscheid gemaakt tussen certificaten voor:
  
  *   authenticity
  *   non-repudiation
  
  Bron: [🌐 PKIo CPS v5.1 § 1.4.1 Permitted Certificate Usage](https://cps.pkioverheid.nl/pkioverheid-cps-unified-v5.1.html#141-permitted-certificate-usage)
  
  Het non-repudiation certificaat is een gekwalificeerd certificaat onder eIDAS.
  
  Het ligt voor de hand om het authenticity certificaat alleen te gebruiken binnen gesloten systemen waar externe erkenning niet nodig is, ook niet voor controle van vastgelegde verklaringen achteraf. Denk aan inloggen op een interne Windows-omgeving of bij een eHerkenning-authenticatiedienst.
  
  Het non-repudiation certificaat kan ook worden gebruikt voor authenticatie, met als kanttekening dat de ondertekende verklaring dan ook onweerlegbaar is.

  ***
  Antwoord oorspronkelijk geschreven door [🏔️ Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912).  [`🏔️ Origineel`](https://alkem.io/tip/collaboration/welketypentransact-1429/posts/pkioverheidauthent-6351)

    - #### 💬 Reactie van [🏔️ Sander Boer](https://alkem.io/user/sander-boer-499) op 2024-01-15 13:09 UTC
          
      [🌐 @Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912) :  kan je de laatste zinnen nog wat toelichten?  Die zijn voor mij wat te cryptisch.
- ## <a id="documentenenservic-8288"></a> 📌 Documenten en serviceberichten
  Je kunt onderscheid maken tussen het ondertekenen van **documenten** (rapportages, contracten, aangiftes, brieven) en van **serviceberichten** (verzoeken, opdrachten, antwoorden).
  
  In beide gevallen gaat het om “Claims about information” zoals beschreven in de paper [🌐 When Willeke can get rid of paperwork](https://repository.tudelft.nl/islandora/object/uuid%3A4c2005ea-9cfd-420f-80fb-e8714be0bdd5).
  
  Bij documenten is het formele standpunt ten opzichte van de informatie van belang. Deze kan ook lang na een service-interactie worden geraadpleegd. Denk aan langlopende contracten en verklaringen uit authentieke bronnen.
  
  Bij serviceberichten is vooral van belang dat de herkomst en integriteit van de informatie zijn beschermd. Deze worden gecontroleerd tijdens de service-interactie. Als deze na de service-interactie worden geraadpleegd, is dat typisch met het oog op kwaliteitscontrole van systemen of waarheidsvinding bij incidenten.
  
  Als een formeel document in een servicebericht wordt verstrekt, ligt het voor de hand om twee keer te ondertekenen en/of verzegelen.
  
  Het is raadzaam om het onderscheid expliciet te maken in een *signature policy* ([📄 Wat zijn signature policies en wat heb je er aan?](watzijnsignaturep-7232.md)) en bijvoorbeeld gebruik te maken van *commitment types* zoals beschreven in het ESI Framework.

  ***
  Antwoord oorspronkelijk geschreven door [🏔️ Sander Dijkhuis](https://alkem.io/user/sander-dijkhuis-3912).  [`🏔️ Origineel`](https://alkem.io/tip/collaboration/welketypentransact-1429/posts/documentenenservic-8288)

<details><summary><code>Schrijf een antwoord</code></summary>

1. [Log in op Alkemio](https://identity.alkem.io/login).
2. Als je nog niet lid bent van de TIP-space, [vraag en wacht op toegang](https://alkem.io/tip/dashboard).
3. Ga naar de [vraag in Alkemio](https://alkem.io/tip/collaboration/welketypentransact-1429).
4. Klik op (+).
5. Neem kennis van de placeholder-tekst en verwijder deze.
6. Verstuur je antwoord.

Je antwoord verschijnt direct op Alkemio. Na synchronisatie verschijnt het ook hier.

</details>

* * *
<small>Bijdragen zijn gelicenseerd onder [🌐 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.nl).</small>

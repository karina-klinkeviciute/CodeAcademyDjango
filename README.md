# Projekto su Django pavyzdys
repozitorija, skirta Django pavyzdžiams dėstant

# Įrankių nuoma 

## Trumpas aprašymas

Web puslapis įrankių nuomai. Naudotojai gali kelti savo įrankius, o kiti naudotojai gali ieškoti jiems reikiamų įrankių ir juos išsinuomoti. 

(jei toks projektas iš tikro būtų įgyvendinamas, reikėtų labai apgalvoti atvejus, kai įrankiai neveiks, bus nekokybiški, ar išsinuomojęs naudotojas juos sugadins. Ar būtų kažkoks draudimas, kažkokia kompensacija ar kas)

## Duomenys 

- Vartotojas 
    - Vardas
    - Pavardė
    - telefonas
    - el. paštas
    - vietovė
    - jei tai įmonė, įmonės pavadinimas

- įrankis
    - pavadinimas
    - nuotrauka
    - kategorija 
    - jėgos šaltinis (mechaninis (rankinis, elektrinis, elektrinis akumuliatorinis, benzininis, kita)
    - galia
    - išmatavimai
    - kaina valandai
    - ar su pristatymu, ar reikia pasiimti
    - vietovė (gali būti kita, nei naudotojo vietovė)
    - kokiu laiku galima nuomotis (pvz. darbo dienomis nuo 8 iki 17, arba savaitgaliais nuo 12 iki 20)

- Nuomos faktas
    - įrankis
    - nuo kada
    - iki kada
    - bendra kaina
    - pastabos


    
## Procesai

- Įrankio įkėlimas
    - Naudotojas paspaudžia "Įkelti naują įrankį"
    - Naudotojas užpildo įrankio įvedimo formą (pagal aukščiau nurodytus duomenis)
    - Naudotojas paspaudžia mygtuką "Įvesti įrankį" ir įrankis išsisaugo. 
    - Naudotonas gali paspausti mygtuką "Peržiūrėti įrankį"

- Savo įkeltų įrankių peržiūra
    - Naudotojas paspaudžia mygtuką "mano įrankiai"
    - Naudotojui parodomi visi jo įkelti įrankiai su visais duomenimis 

- Įkelto įrankio redagavimas
    - Aukščiau aprašytam įrankių sąraše prie kiekvieno įrankio yra mygtukas "redaguoti"
    - Paspaudus mygtuką "redaguoti", atsidaro langas, identiškas įvedimo langui, bet jau su esamais duomenimis
    - Duomenis galima pakeisti
    - Paspaudus mygtuką "saugoti", duomenys išsaugomi. 

- Įrankių paieška
    - Pagridiniame puslapyje rodomas įrankių sąrašas
    - Sąrašą galima filtruoti pagal įvairius kriterijus: kategorija, jėgos šaltinis, kaina, pristatymas ir kita. 
    - Taip pat galima paieška pagal raktinius žodžius
    
- Įrankio išsinuomavimas
    - Naudotojas, norintis išsinuomoti įrankį, prie jo aprašymo paspaudžia mygtuką "nuomotis" 
    - Pasirenka datą ir laiką (rodomos galimos datos, tos datos, kuriomis įrankis jau išnuomotas, neaktyvios)
    - Pasirinkęs laiką (nuo - iki)naudotojas paspaudžia mygtuką "nuomos užklausa"
    - Užklausa nueina įrankio nuomotujui. 
    - Įrankio nuomotojas gauna naują nuomos pranešimą
    - Atsidaręs puslapį, nuomotojas mato nuomos užklausą, kurią gali patvirtinti arba atmesti
    - Jei užklausa patvirtinama, nuomotojas susisiekia su nuomininku dėl įrankio atsiėmimo ir grąžinimo detalių bei apmokėjimo.
    
## Naudotojai ir rolės

1. Nuomotojas/nuomininkas. Gali matyti ir redaguoti savo paskyros duomenis. Gali kelti įrankius nuomai. Gali patvirtinti jam skirtą nuomos užsakymą. Gali išsinuomoti įrankius. 
2. Sistemos administratorius. Gali matyti visų vartojų duomenis. Gali trinti įrankių įrašus. Gali atšaukti užsakymus. Gali panaikinti naudotojų paskyras. 

## Dizainas

Dizainas minimalus, funkcionalus
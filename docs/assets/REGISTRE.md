# REGISTRE DES ASSETS GRAPHIQUES

> Prévu par `07_DIRECTION_ARTISTIQUE.md` §6 : **aucun asset n'entre dans le projet sans sa ligne ici** (source + licence). C'est aussi la checklist de production de la partie visuelle — un lot = une issue GitHub.

## Règles (rappel de la DA)
- **Juridique** : aucun asset du Tales of Magic original (propriété CRATR.games GmbH) — les fichiers de référence restent dans `asset/` local, gitignoré, jamais intégrés. Interdits aussi : personnages sous IP, packs « fantasy » sans licence claire.
- **Licences** : game-icons.net = CC BY 3.0 → créditer dans les mentions légales. Toute génération IA : vérifier les conditions commerciales de l'outil et consigner outil + version + prompt dans ce registre.
- **Formats** : SVG minifié pour icônes/ornements ; WebP/AVIF ≤ 150 Ko pour les illustrations ; recoloration par tokens CSS (`currentColor`/masques), jamais de couleur en dur.
- **Statuts** : `à produire` → `en cours` → `produit` → `intégré` (intégré = présent dans `static/` et utilisé par un écran).

---

## Lot I — Icônes (~88, source : game-icons.net sauf mention)

### Attributs (5)
| Asset | Usage | Format | Statut |
|---|---|---|---|
| Puissance magique | fiche perso, entraînement, potions | SVG 24 px | à produire |
| Concentration | idem | SVG 24 px | à produire |
| Résistance | idem | SVG 24 px | à produire |
| Vitalité | idem | SVG 24 px | à produire |
| Sagesse | idem | SVG 24 px | à produire |

### Stats et ressources (7)
| Asset | Usage | Format | Statut |
|---|---|---|---|
| PV (cœur/goutte) | barres, rapports | SVG 16 px | à produire |
| Mana | barres, coûts de sorts | SVG 16 px | à produire |
| Initiative | fiche perso, rapports | SVG 16 px | à produire |
| XP | barre d'XP, récompenses | SVG 16 px | à produire |
| Or (pièce) | header, boutique, ledger | SVG 16 px | à produire |
| Gemme | header, boutique cosmétique | SVG 16 px | à produire |
| Énergie (gemme de jauge) | jauge d'actions du header | SVG 16 px | à produire |

### Écoles de magie (4)
| Asset | Usage | Format | Statut |
|---|---|---|---|
| Feu | badges, grimoire, création de perso | SVG 24 px | à produire |
| Givre | idem | SVG 24 px | à produire |
| Arcane | idem | SVG 24 px | à produire |
| Nature | idem | SVG 24 px | à produire |

### Actions et navigation (16)
| Asset | Usage | Format | Statut |
|---|---|---|---|
| Chasser | action rapide, nav | SVG 24 px | à produire |
| Quêtes | idem | SVG 24 px | à produire |
| Donjon | idem | SVG 24 px | à produire |
| Duel PvP | idem | SVG 24 px | à produire |
| Entraînement | idem | SVG 24 px | à produire |
| Travail à l'école | idem | SVG 24 px | à produire |
| Banque | idem | SVG 24 px | à produire |
| Alchimie / transmutation | idem | SVG 24 px | à produire |
| Boutique | idem | SVG 24 px | à produire |
| Grimoire | idem | SVG 24 px | à produire |
| Cercle (guilde) | idem | SVG 24 px | à produire |
| Forum | idem | SVG 24 px | à produire |
| Messagerie | idem + badge non-lus | SVG 24 px | à produire |
| Classements | idem | SVG 24 px | à produire |
| Profil | idem | SVG 24 px | à produire |
| Notifications (cloche) | header | SVG 24 px | à produire |

### Équipement — les 8 emplacements (7 icônes)
| Asset | Usage | Format | Statut |
|---|---|---|---|
| Bâton | inventaire, fiche perso | SVG 24 px | à produire |
| Chapeau | idem | SVG 24 px | à produire |
| Robe | idem | SVG 24 px | à produire |
| Bottes | idem | SVG 24 px | à produire |
| Gants | idem | SVG 24 px | à produire |
| Amulette | idem | SVG 24 px | à produire |
| Anneau (×2 slots) | idem | SVG 24 px | à produire |

### Objets et consommables (7)
| Asset | Usage | Format | Statut |
|---|---|---|---|
| Potion (fiole) | boutique, inventaire — recolorée par attribut | SVG 24 px | à produire |
| Ingrédient : herbe | inventaire, alchimie | SVG 24 px | à produire |
| Ingrédient : cristal | idem | SVG 24 px | à produire |
| Ingrédient : essence | idem | SVG 24 px | à produire |
| Ingrédient : poudre | idem | SVG 24 px | à produire |
| Coffre / butin | rapports, donjons | SVG 24 px | à produire |
| Parchemin (quête) | quêtes, tutoriel | SVG 24 px | à produire |

### États et divers (10)
| Asset | Usage | Format | Statut |
|---|---|---|---|
| Victoire (laurier) | rapports | SVG 24 px | à produire |
| Défaite | rapports | SVG 24 px | à produire |
| Bouclier de protection | protection PvP, bouclier de novice | SVG 24 px | à produire |
| Verrou (banque / thread) | banque, forum | SVG 24 px | à produire |
| Sablier / minuteur | timers en cours | SVG 24 px | à produire |
| Récolter (main ouverte) | bouton fin de minuteur | SVG 24 px | à produire |
| Partager | lien public de rapport | SVG 24 px | à produire |
| Épingler | forum | SVG 24 px | à produire |
| Rang de sort (étoile) | grimoire (rangs 1–5) | SVG 16 px | à produire |
| Buff actif | fiche perso, pré-combat | SVG 16 px | à produire |

### Sorts (32 — après le seed de la Phase 2)
| Asset | Usage | Format | Statut |
|---|---|---|---|
| 8 icônes sorts de Feu | grimoire, séquence, rapports | SVG 24 px | en attente du seed |
| 8 icônes sorts de Givre | idem | SVG 24 px | en attente du seed |
| 8 icônes sorts d'Arcane | idem | SVG 24 px | en attente du seed |
| 8 icônes sorts de Nature | idem | SVG 24 px | en attente du seed |

---

## Lot II — Illustrations de créatures (24, génération IA via `PROMPTS.md`)

> **Bestiaire validé par le porteur de projet le 10/07/2026** (décision actée, voir 05) — c'est la base du seed de la Phase 2. Couvre les exemples du GDD (rats, zombies, gobelins, esprits, golems, dragons) sur les 50 niveaux, plus les 4 boss des 2 donjons V1. Format 3:4, WebP ≤ 150 Ko. En attendant : silhouettes SVG monochromes (07 §8).

| Créature (validée) | Tranche de niveau | Statut |
|---|---|---|
| Rat des cryptes | 1–5 | à produire |
| Limon d'encre | 1–5 | à produire |
| Zombie affamé | 1–5 | à produire |
| Chauve-souris spectrale | 1–5 | à produire |
| Gobelin chapardeur | 6–10 | à produire |
| Squelette d'apprenti | 6–10 | à produire |
| Esprit frileux | 6–10 | à produire |
| Araignée des réserves | 6–10 | à produire |
| Goule de la crypte | 11–15 | à produire |
| Feu follet | 11–15 | à produire |
| Harpie des tours | 11–15 | à produire |
| Golem d'argile | 16–25 | à produire |
| Spectre du bibliothécaire | 16–25 | à produire |
| Chimère naissante | 16–25 | à produire |
| Golem de pierre runique | 26–35 | à produire |
| Liche mineure | 26–35 | à produire |
| Élémentaire déchaîné | 26–35 | à produire |
| Wyverne des orages | 36–45 | à produire |
| Jeune dragon | 36–45 | à produire |
| Dragon ancien | 46–50 | à produire |

### Boss de donjon (4, validés 10/07/2026)
| Boss | Donjon — étage | Statut |
|---|---|---|
| Gardien de la Crypte | Crypte de l'Académie — ét. 5 | à produire |
| Bibliothécaire spectral | Crypte de l'Académie — ét. 10 | à produire |
| Golem de foudre | Tour foudroyée — ét. 5 | à produire |
| Wyverne matriarche | Tour foudroyée — ét. 10 | à produire |

---

## Lot III — Avatars, skins et bannières (génération IA + SVG)

| Asset | Usage | Format | Statut |
|---|---|---|---|
| Avatar de base : Sorcière | création de personnage | carré, WebP | à produire |
| Avatar de base : Mage | création de personnage | carré, WebP | à produire |
| 10 skins d'avatar (5 sorcière / 5 mage) | boutique de gemmes + hauts faits | carré, WebP | à produire |
| 8 bannières de profil | boutique de gemmes | SVG (motifs abstraits palette) | à produire |
| Cadres de portrait (2–3) | cosmétique | SVG | à produire |

---

## Lot IV — Ornements, logo et hero (SVG maison + 1 illustration)

| Asset | Usage | Format | Statut |
|---|---|---|---|
| Coin gravé serti d'une gemme | Page de Grimoire, level-up, butin épique — SEULS usages | SVG | à produire |
| Texture de grain du parchemin | Page de Grimoire | filtre SVG | à produire |
| Logo Arcanum | header, page publique | SVG (Cinzel Decorative + gemme) | à produire |
| Favicon | navigateur | SVG/PNG 32 px | à produire |
| Hero de la page d'accueil | vitrine publique — la tour de l'école au crépuscule | WebP ≤ 150 Ko | à produire |

---

## Lot V — Maquettes d'écrans (captures dans `docs/assets/maquettes/`)

> Chaque écran clé est maquetté (HTML statique sur les tokens, ou image) **avant** sa phase d'implémentation ; la capture validée est déposée dans `docs/assets/maquettes/` et sert de référence à la PR de l'écran. Les gabarits tableau de bord et rapport de combat existent déjà en fil de fer dans 07 §5.

| Écran | Phase | Statut |
|---|---|---|
| Accueil public (vitrine + hero + classements) | 0/6 | à maquetter |
| Connexion / inscription | 1 | à maquetter |
| Création de personnage (archétype, école, pseudo) | 1 | à maquetter |
| Tableau de bord | 1 | à maquetter (fil de fer 07 §5) |
| Fiche personnage / entraînement | 1 | à maquetter |
| Grimoire + éditeur de séquence de combat | 2 | à maquetter |
| Bestiaire / chasse | 2 | à maquetter |
| **Rapport de combat (Page de Grimoire — la signature)** | 2 | à maquetter (fil de fer 07 §5) |
| Quêtes (minuteur, journalières, histoire) | 2 | à maquetter |
| Donjon (étages, progression) | 2 | à maquetter |
| Boutique de l'école | 3 | à maquetter |
| Inventaire / équipement (8 slots) | 3 | à maquetter |
| Banque | 3 | à maquetter |
| Alchimie (reroll + avertissement) | 3 | à maquetter |
| Profil public | 4 | à maquetter |
| Cercle (page, trésorerie, forum interne) | 4 | à maquetter |
| Forum global | 4 | à maquetter |
| Messagerie | 4 | à maquetter |
| PvP (recherche de cible, pré-combat) | 5 | à maquetter |
| Classements | 5 | à maquetter |
| Boutique de cosmétiques (gemmes) | 6 | à maquetter |

---

## Lot VI — Catalogue d'équipement (proposition pour le seed de la Phase 3)

> **Politique visuelle actée le 10/07/2026 (hybride)** : un objet = icône de son emplacement (Lot I) recolorée + bordure de rareté (DA §4 : commun gris, peu commun givre, rare or, épique grenat). **Aucune icône dédiée, sauf les 5 épiques de boss** — le butin épique garde son moment « waouh », fidèle au principe « rare donc précieux ». Les bonus d'attributs seront chiffrés au seed de la Phase 3 ; ici on fixe les noms, emplacements et raretés.

### Équipement de départ (acté GDD §1 — remis à la création)
| Objet | Emplacement | Rareté |
|---|---|---|
| Bâton d'apprenti | bâton | commun |
| Robe usée | robe | commun |

### Boutique de l'école — 5 tranches × 8 emplacements (40 objets, communs → peu communs)
| Emplacement | Apprenti (1–10) | Disciple (11–20) | Compagnon (21–30) | Maître (31–40) | Archimage (41–50) |
|---|---|---|---|---|---|
| Bâton | Bâton de coudrier | Bâton d'if noueux | Bâton ferré de runes | Bâton à orbe de cristal | Bâton de l'aube |
| Chapeau | Chapeau de feutre | Chapeau à large bord | Chapeau étoilé | Chapeau du conseil | Chapeau d'astronome |
| Robe | Robe de bure | Robe de laine teinte | Robe brodée d'argent | Robe d'examinateur | Robe de nuit étoilée |
| Bottes | Bottes de cuir souple | Bottes cloutées | Bottes de pas feutrés | Bottes du messager | Bottes de brume |
| Gants | Gants de chanvre | Gants de peau retournée | Gants d'archiviste | Gants d'incantateur | Gants de duelliste |
| Amulette | Amulette de verre filé | Amulette d'ambre | Amulette de pierre de lune | Amulette scellée | Amulette du recteur |
| Anneau 1 | Anneau de cuivre | Anneau d'argent | Anneau de grenat | Anneau d'or terni | Anneau de l'équinoxe |
| Anneau 2 | Anneau d'étain | Anneau de jaspe | Anneau de givre | Anneau des quatre écoles | Anneau du solstice |

### Butin rare (10 — chasse et étages de donjon, jamais en boutique)
| Objet | Emplacement | Source indicative |
|---|---|---|
| Bâton en nerf de dragon | bâton | Jeune dragon |
| Chapeau du croque-mitaine | chapeau | Goule de la crypte |
| Robe tissée de brume | robe | Esprit frileux |
| Robe du veilleur de crypte | robe | Crypte de l'Académie (étages) |
| Bottes du monte-en-l'air | bottes | Gobelin chapardeur |
| Gants du prestidigitateur | gants | Feu follet |
| Amulette de sang de golem | amulette | Golems |
| Anneau de feu follet | anneau | Feu follet |
| Chapeau de la harpie | chapeau | Harpie des tours |
| Anneau de la liche | anneau | Liche mineure |

### Épiques de boss (5 — les seuls objets à icône dédiée)
| Objet | Emplacement | Boss | Icône dédiée | Statut |
|---|---|---|---|---|
| Bâton du Premier Recteur | bâton | Bibliothécaire spectral | SVG 24 px | à produire |
| Cœur de la Crypte | amulette | Gardien de la Crypte | SVG 24 px | à produire |
| Anneau de foudre vive | anneau | Golem de foudre | SVG 24 px | à produire |
| Bottes de la Matriarche | bottes | Wyverne matriarche | SVG 24 px | à produire |
| Couronne du Dragon Ancien | chapeau | Dragon ancien (chasse, très rare) | SVG 24 px | à produire |

---

## Lot VII — Ingrédients et potions (contenu nommé, icônes du Lot I)

### Ingrédients d'alchimie (8 — récolte PvE, coût des rerolls)
| Ingrédient | Rareté | Icône (Lot I) |
|---|---|---|
| Herbe de lune | commun | herbe |
| Pétale de mandragore | commun | herbe |
| Poudre d'os | commun | poudre |
| Cristal de givre | commun | cristal |
| Essence spectrale | peu commun | essence |
| Larme de golem | peu commun | cristal |
| Écaille de wyverne | rare | poudre |
| Cendre de dragon | rare | essence |

### Potions de boost (5 — une par attribut, achat en or uniquement)
| Potion | Attribut | Visuel |
|---|---|---|
| Potion de Puissance | Puissance magique | fiole (Lot I) recolorée grenat |
| Potion de Concentration | Concentration | fiole recolorée or-terni |
| Potion de Résistance | Résistance | fiole recolorée ombre-violette-clair |
| Potion de Vitalité | Vitalité | fiole recolorée grenat-clair |
| Potion de Sagesse | Sagesse | fiole recolorée givre-arcane |

---

## Concepts d'exploration (10/07/2026 — `docs/assets/concepts/`)

> Premières générations IA du porteur de projet (rythme : ~5/jour, offre gratuite). Ce sont des **études de style**, pas des assets finaux. ⚠️ À consigner par le porteur : **nom et version de l'outil + prompt de chaque image** (obligatoire avant qu'un concept devienne un asset final) — et vérifier que l'offre gratuite autorise l'usage commercial, sinon regénérer les finaux sur un plan qui l'autorise.

| Fichier | Sujet | Lecture au regard de la DA |
|---|---|---|
| `concept-portrait-capuche.webp` | Sorcière à capuche, flamme d'or | Très proche de la palette (encre nocturne + or terni). Style peinture ✓. Signature IA en bas à droite à retoucher. |
| `concept-avatar-sorciere.webp` | Portrait sorcière, chapeau à gemme | Bon candidat de **style d'avatar** : buste 3/4, visage lisible en 64 px ✓. Fond gris à assombrir. |
| `concept-mage-feu-3d.webp` | Mage de feu, rendu 3D, cercle runique | **Écarté** (décision n°19 : direction picturale) — conservé en historique d'exploration. |
| `concept-mage-givre-3d.webp` | Mage de givre, rendu 3D | **Écarté** — idem. |
| `concept-hero-tour.webp` | Tour au crépuscule, corbeaux, cadre orné | **Candidat hero sérieux** : coche presque tout le gabarit (tour, crépuscule, corbeaux). Le cadre décoratif devra être retiré (le cadre est du ressort du CSS/SVG, pas de l'image). |
| `concept-zombie-bestiaire.webp` | Zombie, style peint | Bon trait, mais **fond blanc = hors gabarit** (fond neutre sombre requis) — à regénérer sur fond sombre. |

### ✅ Direction de style TRANCHÉE (10/07/2026, décision n°19)
**Picturale « type Arcane »** : peinture texturée, coups de pinceau visibles, éclairage théâtral. Le rendu 3D lisse est écarté. Gabarit v2 dans `PROMPTS.md` — règle : décrire les attributs du style, jamais citer la marque dans un prompt.

## File de concept art (à générer — ~5/jour, gabarit v2)

> Chaque pièce fixe un morceau du monde **et** servira de référence (ou d'illustration d'ambiance) à un écran réel — comme l'original illustrait chaque page (bibliothèque, marchand, duel, cf. 08 §4 bis). Ordre = priorité. À la livraison d'une pièce : outil + prompt consignés ici, fichier dans `asset/` → intégré en WebP dans `concepts/`.

### Vague 1 — les fondations du monde (à faire en premier)
| # | Pièce | Format | Sert à |
|---|---|---|---|
| 1 | **La bibliothèque de nuit** — immense bibliothèque circulaire, grimoire lumineux sur un pupitre | 16:9 | LA formule de la DA ; écran « travail à l'école » |
| 2 | **La tour de l'école au crépuscule, v2** — reprendre `concept-hero-tour` sans cadre, en pictural v2 | 21:9 | Hero de l'accueil public |
| 3 | **Portrait sorcière de base** | carré | Avatar de création (Phase 1) |
| 4 | **Portrait mage de base** | carré | Avatar de création (Phase 1) |
| 5 | **Zombie affamé, v2** — reprendre le concept sur fond sombre | 3:4 | Première créature du bestiaire ; teste le gabarit créature |

### Vague 2 — les lieux et PNJ des écrans
| # | Pièce | Format | Sert à |
|---|---|---|---|
| 6 | **Le marchand de la boutique** — PNJ au grand chapeau derrière son comptoir encombré | 3:4 | Écran boutique (l'original avait son marchand) |
| 7 | **Le bibliothécaire** — vieux mage sévère entre les rayonnages | 3:4 | Écran travail à l'école |
| 8 | **La salle d'alchimie** — cornues, athanor, ingrédients suspendus | 16:9 | Écran alchimie/reroll |
| 9 | **La banque de l'école** — chambre forte aux coffres runiques | 16:9 | Écran banque |
| 10 | **La Crypte de l'Académie** — escalier s'enfonçant sous l'école, lueur grenat | 16:9 | Donjon 1 |
| 11 | **La Tour foudroyée** — ruine frappée d'orage perpétuel | 16:9 | Donjon 2 |
| 12 | **Duel de mages** — feu contre givre, à distance | 16:9 | Écran PvP (écho au visuel d'époque) |

### Vague 3 — motifs et déclinaisons
| # | Pièce | Format | Sert à |
|---|---|---|---|
| 13 | **Les 4 bâtons élémentaires** — nature morte, écho assumé à l'artwork d'époque | 3:4 | Vitrine/boutique ; clin d'œil à `baton.jpg` |
| 14 | **Vignettes des 4 écoles** — Feu, Givre, Arcane, Nature (une main incantant chaque magie) | 4 × carré | Choix d'école à la création |
| 15 | **Le chat noir familier** | carré | Tease V2 / cosmétique de bannière |

---

## Références locales (jamais intégrées — voir 08 §4 bis)
| Fichier (local `asset/`, gitignoré) | Nature | Propriété |
|---|---|---|
| `home.jpg` | écran réel : page personnage (DE) | CRATR.games — référence seulement |
| `profil_which.png` | zoom fiche personnage | idem |
| `spell_house.jpg` | écran réel : grimoire | idem |
| `baton.jpg` | artwork promo : 4 bâtons élémentaires | idem |
| `character_3d.jpg` | artwork promo : mage 3D | idem |
| `icon.webp` | avatar/favicon d'époque | idem |

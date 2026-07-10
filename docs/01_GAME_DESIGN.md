# 01 — GAME DESIGN DOCUMENT

> Les valeurs numériques ci-dessous sont des valeurs de départ à équilibrer. Elles doivent être stockées en configuration (fichier ou table `game_config`), jamais codées en dur dans la logique.

---

## 1. Création de personnage

- Un compte = un personnage (V1). Prévoir le modèle de données pour plusieurs personnages plus tard.
- Choix à la création :
  - **Genre d'archétype** : Sorcière ou Mage (purement cosmétique en V1 : avatar et textes genrés).
  - **École d'affinité** (choix définitif, oriente la progression) : voir §3.
  - **Apodo** (pseudo) : unique, 3–20 caractères.
- Le personnage démarre : niveau 1, 100 pièces d'or, 0 gemme, équipement de novice (bâton d'apprenti, robe usée), 1 sort de base de son école.

## 2. Attributs

Cinq attributs principaux, entraînables contre de l'or + temps (voir §6) :

| Attribut | Effet principal |
|---|---|
| **Puissance magique** | Dégâts des sorts |
| **Concentration** | Précision, chance de coup critique |
| **Résistance** | Réduction des dégâts subis |
| **Vitalité** | Points de vie max (PV = 50 + Vitalité × 10) |
| **Sagesse** | Bonus d'XP gagnée, vitesse de régénération du mana |

Statistiques dérivées : PV, Mana (30 + niveau × 5 + bonus), Initiative (Concentration + bonus d'équipement).

## 3. Écoles de magie et sorts

Quatre écoles. L'école d'affinité donne −20 % sur le coût d'apprentissage de ses sorts et +10 % d'efficacité.

- **Feu** — dégâts directs élevés, effets de brûlure (dégâts sur la durée).
- **Givre** — dégâts moyens, effets de contrôle (ralentir/geler = l'ennemi perd un tour).
- **Arcane** — polyvalent : dégâts, vol de mana, boucliers magiques.
- **Nature** — soins, poisons, bonus de récolte d'ingrédients.

### Système de sorts
- Chaque sort a : école, niveau requis, coût d'apprentissage (or), coût en mana, dégâts/effet, temps de recharge (en tours de combat).
- Progression : chaque sort possède 5 rangs. Monter un rang = or + ingrédients + minuteur d'étude.
- Grimoire du joueur : liste des sorts appris. Le joueur définit sa **liste de sorts de combat** (ordre de priorité de 3 à 6 sorts). Le serveur l'exécute avec l'algorithme le plus simple : à chaque tour, premier sort de la liste dont le mana suffit et qui n'est pas en recharge ; sinon attaque de bâton.
- V1 : 6 à 8 sorts par école (24–32 sorts au total). Définis en données (seed), pas en code.

## 4. Combat (moteur commun PvE et PvP)

Fidèle à l'original : le joueur lance le combat (chasse, donjon ou duel) → **minuteur de 10 minutes** → le serveur résout automatiquement → le joueur découvre le rapport montrant l'ordre des sorts joués en auto. L'algorithme de choix des sorts est volontairement le plus simple possible (point 2).

Résolution au tour par tour, intégralement côté serveur :

1. L'initiative détermine qui commence.
2. À chaque tour, le combattant lance le premier sort disponible de sa séquence (mana suffisant + pas en recharge). Sinon : attaque de bâton (dégâts faibles, gratuit).
3. Dégâts = base du sort × (1 + Puissance/100) × modificateur critique − réduction (Résistance). Formule à équilibrer, centralisée dans un module `combat_engine` unique et testé unitairement.
4. Fin : un combattant tombe à 0 PV, ou 30 tours (match nul défensif : le défenseur "repousse" l'attaquant).
5. Sortie : **rapport de combat** persistant, tour par tour, lisible par les deux parties, avec un lien partageable.

## 5. PvE — chasse, donjons, quêtes (priorité n°2)

### 5.1 Chasse aux créatures
- Liste de créatures par tranche de niveau : rats des cryptes, zombies, gobelins, esprits, golems, jeunes dragons, dragons anciens…
- Chasser = choisir une créature accessible → minuteur de combat de 10 min → rapport de combat et récompenses (XP, or, ingrédients, objets rares).
- Coût : 1 énergie (voir §8).

### 5.2 Donjons
- Donjons thématiques à étages (ex. : « Crypte de l'Académie », 10 étages). Un étage = un combat contre un monstre de plus en plus fort.
- Un essai par jour et par donjon. La progression d'étage est persistante. Boss tous les 5 étages avec butin unique.

### 5.3 Quêtes
- **Quêtes à minuteur** (fidèle à l'original) : le joueur choisit une mission (courte 10 min / moyenne 1 h / longue 4 h), le personnage est occupé pendant la durée, récompense à la fin avec un petit texte narratif. Possibilité d'événements aléatoires en cours de mission (bonus ou embuscade → combat).
- **Quêtes journalières** : 3 objectifs simples par jour (ex. : chasser 3 zombies) → bonus.
- **Trame narrative légère** : chaîne de quêtes d'introduction (tutoriel déguisé) faisant visiter chaque système du jeu.

## 6. Progression et entraînement (priorité n°1)

- **XP et niveaux** : courbe XP(n) = 100 × n^1.8 (à équilibrer). Niveau max V1 : 50.
- **Entraînement d'attribut** : coût en or croissant (coût = base × 1.15^valeur_actuelle) + minuteur (durée croissante). Un seul entraînement à la fois.
- **Montée de niveau** : +2 points d'attribut à répartir librement, PV/mana restaurés.
- Règle de conception : il doit toujours y avoir au moins 3 « choses à faire progresser » en parallèle (un entraînement, une quête, une recharge d'énergie).

## 7. Économie, équipement, alchimie

### Monnaies
- **Or** : monnaie principale. Sources : chasse, quêtes, travail à l'école (« aider le bibliothécaire » : minuteur pur → or, sans risque). Puits : sorts, entraînement, équipement, transmutations (rerolls).
- **Gemmes** : monnaie premium **strictement cosmétique** (modèle Riot Games) : skins d'avatar, bannières de profil, cadres, titres. Aucun avantage de gameplay, jamais. V1 : obtenues uniquement en jeu (boss de donjon, journalières complètes, montées de niveau) ; la vente réelle est une option V2 qui ne change pas ce design.

### Équipement
- 8 emplacements : bâton, chapeau, robe, bottes, gants, amulette, 2 anneaux.
- Raretés : commun / peu commun / rare / épique. Bonus d'attributs, parfois effet spécial (ex. : +5 % dégâts de Feu).
- Boutique de l'école (stock par tranche de niveau, rotation quotidienne d'un objet rare) + butin PvE.
- Pas d'hôtel des ventes entre joueurs en V1 (V2 potentielle).

### Alchimie (transmutation / reroll) — fidèle à l'original
- L'alchimie sert à **relancer aléatoirement** (reroll) ce qu'on possède, pas à fabriquer des potions :
  - **Reroll d'objet** : relance les bonus d'attributs d'un objet, dans la fourchette de sa rareté.
  - **Reroll de sort** : relance l'effet secondaire d'un sort appris (ex. : la brûlure devient un vol de mana).
- Coût : ingrédients récoltés en PvE + or + minuteur de transmutation.
- **Décision actée** : le reroll est totalement aléatoire — le résultat peut être pire que l'existant (gamble fidèle à 2008). L'interface doit l'annoncer clairement avant confirmation.

### Potions (boosts temporaires)
- Achetables **uniquement en or** à la boutique de l'école — jamais en gemmes (les gemmes restent 100 % cosmétiques).
- Effet : bonus temporaire sur un attribut pendant une durée (ex. : +10 Puissance pendant 1 h). Les stats effectives d'un combat (équipement + buffs) sont **figées au lancement** : une fenêtre de pré-combat récapitule l'équipement et les buffs actifs, permet de boire une potion, puis le joueur confirme (décision actée 08/07/2026).
- Une seule potion active par attribut à la fois. Pas de potion utilisable en plein combat (pas de soin en duel) : le combat reste 100 % automatique.
- Définies en données (seed), prix et durées en configuration.

### Cosmétiques
- Types V1 : avatar de personnage (skins), bannière de profil, titre affiché, cadre de portrait.
- Boutique de gemmes dédiée ; certains cosmétiques rares sont des récompenses de hauts faits (non achetables).
- Visibles sur le profil public, les classements et les rapports de combat.

## 8. Énergie journalière et rythme — fidèle à l'original

- Quota d'**énergie par jour** : N points d'énergie, remis à zéro à 00:00 UTC. Pas de recharge continue dans la journée — le joueur voit une jauge « Énergie » qui ne remonte qu'au reset quotidien. Valeur de départ : 15/jour en `game_config` ; l'équilibrage final du quota est **délégué à l'implémentation** (décision actée), qui le justifiera par rapport au rythme visé.
- Coûts en énergie : chasse 1, donjon 2, attaque PvP 2. Les quêtes à minuteur, l'entraînement et la transmutation ne coûtent pas d'énergie (le temps EST le coût).
- **Rythme fidèle 2008** : progression volontairement lente (plusieurs jours par niveau à mi-parcours). Toutes les durées et courbes vivent en `game_config` sous un profil `pacing: classic`.
- Objectif de rythme : 2–3 sessions de 5–15 min par jour suffisent pour consommer son énergie et entretenir ses minuteurs.

## 9. Communauté (priorité n°3)

### Cercles (guildes)
- Création : niveau 10 + 1 000 or. Rôles : Archimage (chef), Officier, Membre. 30 membres max.
- Fonctionnalités V1 : page de cercle publique, trésorerie (dons d'or), forum interne du cercle, bonus passif faible pour les membres (+2 % XP).
- V2 (documenter mais ne pas coder) : guerres de cercles, boss de cercle.

### Forum et messagerie
- Forum global intégré : catégories (Annonces, Taverne, Commerce, Stratégies), threads, posts, modération basique (épingler, verrouiller, supprimer — rôle admin/modérateur).
- Messagerie privée entre joueurs (boîte de réception, non temps réel).
- Profil public de personnage : niveau, école, guilde, hauts faits, classement — consultable par tous (c'est l'âme sociale des PBBG).

## 10. PvP (priorité n°4, fidèle à l'original)

- **Duel asynchrone** : attaquer un joueur en ligne ou hors ligne. Le défenseur se bat avec sa séquence de combat et son équipement actuels.
- Cibles : recherche par pseudo ou liste de cibles suggérées (±20 % de puissance).
- Enjeux : le vainqueur vole 5 % de l'or **non banké** du perdant + gagne des points de classement (Elo simplifié). Le perdant ne perd jamais d'XP ni d'objets.
- **Banque de l'école** : l'or déposé est à l'abri du vol (frais de dépôt 5 %). Mécanique classique RedMoon, crée les décisions intéressantes.
- Protections : bouclier de novice (aucune attaque possible avant le niveau 8 dans les deux sens), 1 h de protection après avoir été vaincu, maximum 3 attaques reçues par jour par le même agresseur.
- **Classements** : général (points PvP), par école, par niveau, par or gagné en chasse. Pages consultables sans être connecté (vitrine du jeu).

## 11. Points à valider avec les souvenirs du porteur de projet
Voir `05_QUESTIONS_OUVERTES.md`. Toute réponse doit être reportée ici avant le début du code.

# 04 — ROADMAP D'IMPLÉMENTATION

> Ordre aligné sur les priorités du projet : Progression → PvE → Économie/Craft → Communauté → PvP. Chaque phase se termine par ses critères d'acceptation (CA) verts, tests inclus, avant de passer à la suivante.

## Phase 0 — Fondations
Stack décidée (voir `adr/ADR-001-stack.md`) et durcissement qualité (voir `adr/ADR-002-robustesse.md`) : squelette Django 5.2 LTS avec structure `domain/` vs `game/`, uv + lockfile, docker compose (web + db + scheduler), migrations initiales, i18n activé, seed de développement, pytest, pyright strict + django-stubs, ruff, import-linter, pre-commit, CI complète avec gates bloquants.
**CA :** `docker compose up` sert une page d'accueil ; migrations et seed s'exécutent ; la CI passe au vert sur les 5 gates (lint, types, architecture, tests, migrations) ; un test dans `domain/` tourne sans base de données.

## Phase 1 — Compte, personnage, progression (cœur)
Inscription/connexion, création de personnage (archétype, école, pseudo), page « Mon personnage », attributs, quota d'énergie journalier (reset à 00:00 UTC, sans recharge continue — décision actée n°4), entraînement d'attribut à minuteur (résolution lazy + job), montée de niveau avec répartition de points, travail à l'école (minuteur → or), gold_ledger.
**CA :** un joueur s'inscrit, crée son perso, lance un entraînement, revient après le minuteur et voit son attribut monté et son or débité ; le ledger reconstitue le solde ; tests unitaires sur XP, coûts, énergie, résolution des timers.

## Phase 2 — Moteur de combat + PvE
Module combat_engine (pur, seedé, testé), grimoire et apprentissage de sorts, séquence de combat, chasse aux créatures (minuteur → combat → rapport), rapports de combat consultables, quêtes à minuteur avec événements aléatoires, quêtes journalières, donjons à étages.
**CA :** boucle complète chasse → rapport → XP/or/butin ; un même seed rejoue exactement le même combat ; le donjon conserve la progression d'étage et limite à 1 essai/jour.

## Phase 3 — Économie et alchimie
Boutique avec stock par niveau + rotation quotidienne, équipement (8 slots, équiper/déséquiper, effets sur les stats), banque de l'école (dépôt/retrait avec frais), ingrédients et butin PvE, alchimie de **reroll** (objets et sorts, minuteur de transmutation, avertissement « le résultat peut être pire »), potions de **boost temporaire** (achat en or uniquement, buff appliqué en pré-combat — jamais en plein combat), boutique de cosmétiques en gemmes (100 % cosmétique).
**CA :** acheter/équiper modifie les stats de combat de façon vérifiable ; boire une potion de boost et voir le buff pris en compte dans un rapport de combat ; un reroll d'objet relance ses bonus dans la fourchette de sa rareté ; l'or banké est intouchable.

## Phase 4 — Communauté
Profils publics de personnage, cercles (création, rôles, trésorerie, forum interne, bonus passif), forum global (catégories, threads, posts, modération), messagerie privée, panneau admin minimal.
**CA :** deux comptes de test peuvent : rejoindre le même cercle, poster sur le forum, s'écrire en privé ; un modérateur peut verrouiller un thread ; tout contenu utilisateur est échappé (test XSS basique).

## Phase 5 — PvP et classements
Duel asynchrone (recherche de cible, suggestions ±20 %), vol d'or non banké, Elo simplifié, protections (bouclier de novice, 1 h post-défaite, 3 attaques/jour/même cible), classements publics (général, école, niveau, chasse).
**CA :** A attaque B hors ligne, B retrouve le rapport à sa connexion ; les trois protections sont testées ; les classements sont consultables sans connexion.

## Phase 6 — Polish et bêta
Chaîne de quêtes d'introduction (tutoriel), notifications en jeu (fin de minuteur, attaque subie, message reçu), équilibrage via game_config, pages vitrine (accueil avec classements), passe design finale (selon `07_DIRECTION_ARTISTIQUE.md` §8), audit sécurité (rate limits, injections, XSS), doc de déploiement VPS.
**CA :** un nouveau joueur va de l'inscription au niveau 5 guidé par le tutoriel sans aide externe ; revue de sécurité effectuée et consignée.

## V2 (documenté, non implémenté)
Guerres de cercles, boss de cercle, hôtel des ventes entre joueurs, événements saisonniers, monétisation réelle des gemmes, multi-serveurs, vérification email obligatoire, application des langues EN/ES/DE.

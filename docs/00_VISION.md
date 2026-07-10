# 00 — VISION DU PROJET

## Pitch
**Arcanum** est un remake fidèle de *Tales of Magic* (RedMoon Studios, 2007-2010) : un jeu de rôle multijoueur par navigateur, en mode texte/menus, où le joueur incarne un(e) apprenti(e) sorcier(ère) qui intègre une école de magie et progresse pour devenir le meilleur mage du monde.

L'esprit du jeu original doit être préservé : rythme lent basé sur des actions à minuteur, progression persistante, économie simple, communauté forte (guildes, forum). L'interface est modernisée (responsive, propre, rapide) mais reste une interface de menus et de pages — **pas** de rendu temps réel, pas de déplacement sur carte, pas de graphismes animés.

## Piliers de design (par ordre de priorité)
1. **Progression** — le cœur du jeu : montée en niveau, apprentissage de sorts, entraînement des attributs, équipement, économie. Chaque session (même 5 minutes) doit faire avancer le personnage.
2. **PvE / Quêtes** — chasse aux créatures (zombies, dragons…), donjons à étages, quêtes à minuteur. C'est la source principale d'or et d'XP.
3. **Communauté** — cercles (guildes), forum intégré, messagerie privée, classements consultables.
4. **PvP** — duels asynchrones entre joueurs avec vol d'or et classement. Présent et fidèle à l'original, mais non obligatoire pour progresser.

## Ce que le jeu EST
- Un PBBG (persistent browser-based game) asynchrone : le serveur vit en continu, les joueurs se connectent quand ils veulent.
- Un jeu à sessions courtes : lancer une action, revenir plus tard voir le résultat.
- Un jeu où le combat est **résolu par le serveur** et présenté sous forme de rapport de combat détaillé (tour par tour, en texte).
- Un jeu multilingue par conception (FR d'abord, architecture i18n dès le départ).

## Ce que le jeu N'EST PAS (hors scope)
- Pas de combat en temps réel ni d'action directe.
- Pas de graphismes 2D/3D en jeu (uniquement illustrations statiques et icônes).
- Pas d'application mobile native (le site doit être responsive, c'est suffisant).
- Pas de monétisation réelle en V1 : la monnaie premium (gemmes) s'obtient uniquement en jeu pour l'instant et n'achète **que du cosmétique** (avatars, bannières, titres — modèle Riot Games), jamais d'avantage de gameplay.
- Pas de fédération multi-serveurs en V1 : un seul monde/serveur.

## Boucle de jeu principale
1. Le joueur se connecte, dispose de son **énergie journalière** (quota remis à zéro chaque jour à 00:00 UTC).
2. Il lance des actions à minuteur : chasser une créature, partir en quête, s'entraîner, travailler à l'école (gagner de l'or).
3. Les résultats tombent à la fin du minuteur : XP, or, objets, ingrédients.
4. Il dépense : nouveaux sorts, équipement, potions, entraînement d'attributs.
5. Il interagit : guilde, forum, éventuellement attaque un autre joueur.
6. Il se déconnecte ; ses défenses (équipement, sorts passifs) le protègent pendant son absence.

## Critères de réussite de la V1
- Un joueur peut créer un compte, créer un personnage, jouer la boucle complète (chasse → récompense → achat → progression) sans bug.
- Deux joueurs peuvent interagir : duel PvP avec rapport de combat, messagerie, même guilde.
- Le serveur résout toutes les actions côté serveur (aucune logique de jeu critique côté client).
- Le jeu tourne avec `docker compose up` en local et est déployable sur un VPS simple.

## Références d'inspiration
- Tales of Magic (structure générale, thème école de magie, sorcière/mage).
- Autres jeux RedMoon : KnightFight, MonstersGame (mécaniques d'attaque asynchrone, entraînement à minuteur, clans).
- Shakes & Fidget (exemple de modernisation réussie d'un PBBG).

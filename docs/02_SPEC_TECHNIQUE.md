# 02 — SPÉCIFICATION TECHNIQUE

> La stack est **décidée** : Django 5 / PostgreSQL / HTMX — voir `adr/ADR-001-stack.md` pour le détail et la justification. Les contraintes ci-dessous restent non négociables et l'ADR doit être respecté.

## 1. Contraintes d'architecture

### Serveur autoritaire
- **Toute** la logique de jeu (combat, récompenses, minuteurs, coûts) est exécutée côté serveur. Le client n'envoie que des intentions (`POST /hunt`, `POST /train`), jamais de résultats.
- Le moteur de combat est un module pur (entrées → déroulé déterministe avec graine aléatoire loggée) pour être testable unitairement et rejouable (anti-triche, debug).

### Type d'application
- Backend : API HTTP (REST ou équivalent) + tâches planifiées. Pas de websocket requis en V1 (le jeu est asynchrone) ; un simple polling léger ou refresh suffit pour la messagerie.
- Frontend : SPA ou pages serveur, au choix, mais responsive (mobile-first acceptable) et léger. Esthétique : dark fantasy, parchemins et ornements, inspirée de la capture d'écran de l'original mais épurée. La référence visuelle complète (tokens, composants, gabarits) est `07_DIRECTION_ARTISTIQUE.md`.
- Base de données **relationnelle** (le modèle de données de `03_MODELE_DONNEES.md` est relationnel par nature).

### Gestion du temps (cœur du genre PBBG)
- Les minuteurs (quêtes, entraînements, brassages) sont stockés comme `started_at` + `ends_at` en base. La résolution se fait **à la lecture** (lazy) : quand le joueur consulte, si `ends_at` est dépassé, le serveur résout et crédite. Un job périodique (toutes les minutes) résout aussi les actions expirées pour les notifications et les classements.
- L'énergie journalière est un simple compteur (`daily_energy_used` + `energy_date`) vérifié à la volée : si la date stockée n'est plus le jour UTC courant, le compteur repart à zéro. Pas de job par joueur.
- Les combats (chasse, donjon, PvP) sont créés en état « en cours » avec `ends_at = maintenant + 10 min`, puis résolus comme les autres minuteurs (lazy + job).
- Toutes les dates en UTC. Le « jour » de jeu (reset des quêtes journalières, tentatives de donjon) bascule à 00:00 UTC ; afficher l'heure du reset au joueur.

### Transactions et intégrité
- Toute opération économique (achat, vol d'or PvP, don à la guilde) est transactionnelle et journalisée dans une table `gold_ledger` (source de vérité auditable). Le solde affiché peut être dénormalisé mais doit être reconstructible depuis le ledger.
- Verrouillage optimiste ou transactions sérialisées sur les opérations concurrentes sensibles (deux attaques simultanées sur le même joueur, double-clic sur un achat).
- Idempotence des endpoints de résolution (rejouer la même résolution ne crédite pas deux fois).

## 2. Authentification et sécurité
- Comptes email + mot de passe (hachage moderne type argon2/bcrypt). Vérification d'email en V1.1, pas bloquante en V1.
- Sessions Django par cookie httpOnly (acté : auth Django native, cf. ADR-001).
- Rate limiting sur : login, création de compte, envoi de messages, posts de forum.
- Validation stricte de toutes les entrées côté serveur. Échappement systématique du contenu utilisateur (forum, messages, pseudos) — XSS est LE risque classique de ce genre de jeu.
- Rôles : `player`, `moderator`, `admin`. Panneau d'admin minimal : bannir, muter, ajuster l'or d'un joueur (avec journalisation), verrouiller un thread.

## 3. Internationalisation
- Tous les textes UI passent par un système i18n dès le premier écran. Langue V1 : français. Structure prête pour EN/ES/DE.
- Les contenus de jeu (noms de sorts, créatures, textes de quêtes) sont des données avec clés de traduction, pas des chaînes en dur.

## 4. Qualité et tests
- **Garde-fous de l'ADR-002 obligatoires** : Django 5.2 LTS, pyright strict + django-stubs, ruff, import-linter (le package `domain/` n'importe jamais Django), CI bloquante (lint, types, architecture, tests, migrations à jour), couverture ≥ 90 % sur `domain/`.
- Tests unitaires obligatoires sur : moteur de combat, formules de progression (XP, coûts d'entraînement), énergie journalière, ledger d'or, résolution de minuteurs (y compris cas limites : résolution en retard, double résolution).
- Tests d'intégration sur les parcours critiques : inscription → création de perso → première chasse → achat.
- Seed de données de développement : 20 joueurs factices, toutes les créatures, sorts et objets, pour tester immédiatement.

## 5. Exploitation
- `docker compose up` doit lancer l'ensemble (app + BDD) en local.
- Configuration par variables d'environnement, fichier `.env.example` fourni.
- Migrations de schéma versionnées dès le premier jour.
- Logs structurés ; toute résolution de combat logge sa graine aléatoire.
- Cible de déploiement : un VPS unique (2 vCPU / 4 Go). Dimensionner pour ~500 joueurs actifs/jour en V1 ; pas d'optimisation prématurée au-delà.

## 6. Conventions pour l'assistant IA de code
- Lire l'intégralité de `docs/` (y compris `adr/`) avant tout code.
- Ouvrir `05_QUESTIONS_OUVERTES.md` : si des questions bloquantes sont sans réponse, les poser avant d'implémenter la partie concernée.
- Travailler par phases selon `04_ROADMAP.md` ; ne pas commencer une phase avant que les critères d'acceptation de la précédente soient verts.
- Chaque décision structurante = un ADR court dans `docs/adr/` (ADR-001 est déjà écrit).
- Les valeurs d'équilibrage vivent dans des fichiers de données/seeds, jamais dans la logique.

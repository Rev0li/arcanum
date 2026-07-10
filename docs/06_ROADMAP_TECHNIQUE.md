# 06 — ROADMAP TECHNIQUE (plan d'exécution ingénierie)

> Ce document traduit la roadmap fonctionnelle (`04_ROADMAP.md`) en travail technique concret : modules, modèles, vues, services, tests. Il respecte les ADR-001 (stack) et ADR-002 (garde-fous). Chaque phase liste ses livrables techniques et sa *definition of done* (DoD). L'ordre des tâches à l'intérieur d'une phase est l'ordre recommandé d'implémentation.

## Principes d'exécution transversaux
- **Un commit = une tâche verte** : lint, types, architecture, tests, migrations à jour. Jamais de commit rouge.
- **Domaine d'abord** : pour toute mécanique, on écrit d'abord le module `domain/` (pur, testé), puis les modèles, puis les vues/templates. L'UI est toujours la dernière couche.
- **Services applicatifs** : les vues ne contiennent aucune logique — elles appellent des fonctions de service (`game/services/`) qui orchestrent domaine + ORM dans `transaction.atomic()`.
- **Convention de nommage** : anglais pour le code, français pour les textes joueurs (via i18n).
- **Git** : branche par phase, tags `phase-0` … `phase-6` à chaque DoD atteinte.

---

## Phase 0 — Fondations et outillage

### Arborescence cible du dépôt
```
grimoire/
  docs/                    # ce dossier
  src/
    domain/                # python pur, zéro import Django
    game/                  # apps Django
    config/                # settings, urls, asgi/wsgi
  tests/
    domain/                # tests sans BDD
    integration/           # tests avec BDD (pytest-django)
  compose.yaml
  Dockerfile
  pyproject.toml           # uv, ruff, pyright, import-linter, pytest
  .pre-commit-config.yaml
  .github/workflows/ci.yaml
```

### Tâches dans l'ordre
1. `uv init` ; dépendances : django==5.2.*, psycopg[binary], gunicorn, django-htmx, django-stubs, pytest, pytest-django, ruff, pyright, import-linter, pre-commit, argon2-cffi. Lockfile committé.
2. Projet Django : settings découpés (`base.py` / `dev.py` / `prod.py`), variables d'env via `os.environ` + `.env.example`, `PASSWORD_HASHERS` avec argon2 en premier, `LANGUAGE_CODE = "fr"`, `USE_I18N = True`, `TIME_ZONE = "UTC"`.
3. `compose.yaml` : services `web` (gunicorn, bind-mount en dev), `db` (postgres:16, volume nommé, healthcheck), `scheduler` (même image, commande de boucle cron — voir Phase 1 T6).
4. Configuration qualité dans `pyproject.toml` : ruff (règles par défaut + isort), pyright `strict` limité à `src/`, import-linter avec le contrat « `domain` ne peut pas importer `game`, `config`, ni `django` ».
5. `.pre-commit-config.yaml` : ruff check, ruff format, pyright.
6. CI GitHub Actions : jobs lint → types → architecture → tests (service postgres) → `makemigrations --check`. Badge dans le README du dépôt.
7. Page d'accueil placeholder (template de base `base.html` + `tokens.css` conformes à `07_DIRECTION_ARTISTIQUE.md`) + healthcheck `/healthz`.
8. Commande `seed_dev` vide (sera remplie phase par phase).

**DoD** : `docker compose up` sert l'accueil ; CI verte sur les 5 gates ; `pytest tests/domain` tourne sans BDD.

---

## Phase 1 — Compte, personnage, progression

### Modules domaine
- `domain/progression/xp.py` : `xp_required(level)`, `apply_xp(...) -> LevelUpResult` (dataclasses).
- `domain/progression/training.py` : `training_cost(attribute_value)`, `training_duration(...)`.
- `domain/economy/ledger.py` : types `GoldChange(reason, delta, reference)` ; règles d'invariants (jamais de solde négatif).
- `domain/actions.py` : calcul du quota journalier (reset UTC), `can_spend(actions_used, cost, today)`.

### Apps Django et modèles
- `game/accounts` : User custom (email login), inscription/connexion (vues Django auth), rate limiting simple (cache + middleware) sur login/register.
- `game/characters` : `Character` (cf. 03_MODELE_DONNEES), création de personnage (archétype, école, pseudo unique), page « Mon personnage ».
- `game/timers` : modèle `ActiveTimer` générique + **service de résolution** `resolve_due_timers(character=None)` : idempotent (`resolved_at` + verrou `select_for_update`), appelé (a) à chaque requête du joueur concerné — résolution lazy, (b) par la commande `run_scheduler` (boucle : résolution globale toutes les 60 s) du service `scheduler`.
- `game/economy` : modèle `GoldLedger` + service `credit/debit(character, reason, delta, ref)` — SEUL point d'écriture de l'or, dans `transaction.atomic()`.
- Fonctionnalités : entraînement d'attribut (un seul actif — contrainte d'unicité partielle en BDD), travail à l'école, montée de niveau avec répartition de points (formulaire HTMX).
- Admin : enregistrement de tous les modèles ; action admin « ajuster l'or » qui passe par le ledger avec reason `admin_adjust`.

### Tests clés
- Domaine : courbes XP/coûts (valeurs limites), reset des actions à minuit UTC, invariants du ledger.
- Intégration : double résolution d'un même timer (idempotence), deux requêtes concurrentes qui dépensent le même or (une seule passe), reconstruction du solde depuis le ledger == solde dénormalisé.

**DoD** : parcours inscription → perso → entraînement → résolution vérifié par un test d'intégration bout-en-bout ; couverture `domain/` ≥ 90 %.

---

## Phase 2 — Moteur de combat et PvE

### Modules domaine
- `domain/combat/` : `entities.py` (Combatant, SpellDef, Buff — dataclasses figées), `engine.py` (`resolve_combat(attacker, defender, seed) -> CombatResult` : boucle de tours, algorithme « premier sort disponible », journal de tours sérialisable), `formulas.py` (dégâts, critique, résistance). Déterminisme : `random.Random(seed)` injecté, aucun accès horloge.
- `domain/combat/loot.py` : tirage de butin depuis une table de loot (seedé).

### Côté Django
- `game/grimoire` : modèles `Spell`, `CharacterSpell`, `CombatSequence` ; écrans grimoire, apprentissage, éditeur de liste de sorts (HTMX : monter/descendre ; l'îlot Svelte drag-and-drop est un bonus de Phase 6).
- `game/bestiary` : `Creature`, fixtures des créatures ; `game/hunts` : service `start_hunt` (débite 1 action, crée un timer `combat` de 10 min) et résolution → appelle `domain.combat` → crée `CombatReport` (JSON des tours + seed) → crédite via ledger.
- `game/combat_reports` : page rapport (rendu tour par tour), URL publique par token.
- `game/quests` : quêtes à minuteur (occupation exclusive du personnage : contrainte de service), journalières (reset UTC), chaîne d'introduction en fixtures.
- `game/dungeons` : progression persistante, 1 essai/jour, boss.
- Seeds : 24–32 sorts, ~20 créatures, 2 donjons, quêtes d'intro.

### Tests clés
- Golden tests du moteur : même seed ⇒ même journal (fichiers de référence committés).
- Propriétés : le combat se termine toujours ≤ 30 tours ; jamais de PV négatifs dans le journal.
- Intégration : chasse bout-en-bout, quota d'actions décrémenté, limite donjon 1/jour.

**DoD** : rejouer un `CombatReport` depuis sa seed reproduit exactement son journal (test automatisé).

---

## Phase 3 — Économie, équipement, alchimie

- `game/items` : `Item`, `Inventory`, équiper/déséquiper (recalcul des stats via une fonction domaine `effective_stats(character, equipment, buffs)` — utilisée aussi par le moteur de combat).
- `game/shop` : stock par tranche de niveau, rotation quotidienne (choix seedé par date), achat transactionnel.
- `game/bank` : dépôt (frais 5 %) / retrait, via ledger uniquement.
- `domain/alchemy/reroll.py` : reroll d'objet (bonus retirés dans la fourchette de rareté) et de sort (effet secondaire), aléatoire total, seedé ; `game/alchemy` : ingrédients, minuteur de transmutation, écran avec avertissement explicite « le résultat peut être pire ».
- `game/potions` : `Potion`, `PotionInventory`, `ActiveBuff` (expires_at) ; achat en or ; `effective_stats` intègre les buffs actifs au moment de la résolution du combat.

**DoD** : test d'intégration « acheter → équiper → chasser » où le rapport de combat reflète les stats d'équipement et un buff de potion actif ; l'or banké est prouvé involable par test.

---

## Phase 4 — Communauté

- `game/profiles` : page publique de personnage (cosmétiques équipés, hauts faits).
- `game/guilds` : modèles, rôles, trésorerie (ledger reason `guild_donation`), forum interne (réutilise les modèles forum avec `guild_id`).
- `game/forum` : catégories/threads/posts, pagination, permissions modérateur (pin/lock/delete soft), échappement systématique (templates Django auto-escape — test XSS dédié).
- `game/messaging` : messagerie privée, compteur de non-lus dans le header (fragment HTMX pollé à intervalle long).
- Admin : vues modération (bannir avec durée, muter), toutes les actions journalisées dans un modèle `ModerationLog`.

**DoD** : scénario de test à deux comptes (guilde commune, post forum, MP) ; test XSS injectant `<script>` dans pseudo/post/MP.

---

## Phase 5 — PvP et classements

- `game/pvp` : recherche de cible (index sur une « puissance » précalculée ±20 %), service `start_attack` (2 actions, timer combat 10 min), résolution : vol de 5 % de l'or non banké via ledger (`pvp_steal_in/out` appairés), Elo simplifié (`domain/pvp/rating.py`).
- Protections en contraintes de service testées une à une : niveau < 8, `protection_until`, table `AttackLimit` (3/jour/cible).
- `game/rankings` : classements (général, école, niveau, or de chasse) — requêtes agrégées + cache (Django cache, TTL 5 min), pages publiques sans login.

**DoD** : matrice de tests des protections (chaque règle bloque, sa levée débloque) ; attaque hors-ligne bout-en-bout avec ledger équilibré (somme volée = somme reçue).

---

## Phase 6 — Polish, durcissement, déploiement

- Notifications en jeu (modèle `Notification`, badge HTMX) : fin de minuteur, attaque subie, MP reçu.
- Îlot Svelte n°1 : éditeur drag-and-drop de la liste de sorts (build Vite séparé → web component statique versionné dans `static/islands/`).
- Passe design (suivre `07_DIRECTION_ARTISTIQUE.md` §8) : Page de Grimoire complète, illustrations finales, audit contraste/clavier, cohérence écran par écran.
- Équilibrage : script de simulation (`scripts/simulate_progression.py`) qui joue N jours de progression type et sort des courbes — sert à calibrer `game_config` (dont le quota d'actions/jour).
- Sécurité : revue rate limits, en-têtes (SecurityMiddleware, CSP simple), `DEBUG=False` vérifié en CI pour la conf prod.
- Déploiement VPS : reverse proxy Caddy (TLS auto) ou nginx+certbot, `compose.prod.yaml`, script `backup_db.sh` (pg_dump quotidien, rotation 14 jours, cron), doc `docs/DEPLOIEMENT.md` pas-à-pas.

**DoD** : nouveau joueur → niveau 5 via le tutoriel sans aide ; déploiement réel effectué sur le VPS en suivant uniquement la doc.

---

## Risques techniques identifiés et parades
- **Concurrence sur l'or et les timers** → toute écriture via services atomiques + `select_for_update` ; tests de concurrence dédiés dès la Phase 1.
- **Dérive de l'équilibrage** → tout en `game_config`/fixtures + script de simulation (Phase 6, mais utilisable dès la Phase 2).
- **Résolution en retard des minuteurs** (scheduler down) → la résolution lazy à la lecture garantit qu'un joueur n'est jamais bloqué ; le scheduler n'est qu'un confort (notifications).
- **Croissance du JSON des rapports de combat** → cap à 30 tours + purge des rapports > 90 jours (commande de maintenance).
- **Montée de version Django** → fenêtre d'upgrade à chaque LTS uniquement, en suivant la release note, CI comme filet.

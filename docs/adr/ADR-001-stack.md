# ADR-001 — Choix de la stack technique

**Statut :** accepté (décidé en brainstorming le 07/07/2026)
**Contexte de décision :** développeur solo (profil 42, polyglotte JS/PHP/Python), infra personnelle (VPS), code écrit majoritairement par IA avec supervision humaine.

## Décision

| Couche | Choix |
|---|---|
| Langage / framework | **Python 3.12+ / Django 5.x** (monolithe) |
| Base de données | **PostgreSQL 16** |
| Frontend | **Templates Django + HTMX** + feuille CSS maison à tokens (`tokens.css`, voir `07_DIRECTION_ARTISTIQUE.md` — tranché post-ADR, pas de Tailwind) |
| Jobs planifiés | Commande de management `resolve_timers` exécutée chaque minute (cron/supercronic dans le conteneur) |
| Tests | pytest + pytest-django |
| Conteneurisation | Docker Compose : `web` (gunicorn), `db` (postgres), `scheduler` |
| Admin / modération | **Django Admin** natif (personnalisé au fil des phases) |
| i18n | Système de traduction natif Django (FR par défaut) |
| Auth | Django auth natif (argon2 comme hasher) |

## Justification

1. **Développement piloté par IA** : les conventions Django sont strictes et massivement documentées → l'IA a un minimum de décisions arbitraires à prendre, le code produit est prévisible, uniforme et facile à auditer par le superviseur humain.
2. **Minimiser le code généré** : auth, sessions, protections CSRF/XSS, migrations, i18n et panneau d'administration sont fournis par le framework. Moins de code écrit = moins de surface de bugs à superviser. Le Django Admin couvre à lui seul l'essentiel des besoins de modération (bannir, ajuster un solde avec journalisation, verrouiller un thread).
3. **Adéquation au genre PBBG** : jeu de pages et de menus, asynchrone, sans besoin temps réel → le rendu serveur + HTMX (fragments HTML à la demande) donne une UI moderne et réactive sans SPA, sans build front complexe, sans duplication de logique client/serveur.
4. **Exploitation solo sur VPS** : un seul langage, un seul processus applicatif, PostgreSQL, un cron. `docker compose up` et c'est en ligne.
5. **ORM + transactions** : l'ORM Django et `transaction.atomic()` couvrent naturellement les exigences du ledger d'or et des opérations concurrentes (spec §1).

## Alternatives écartées
- **Laravel (PHP)** : excellent fit également, mais admin auto-généré moins complet (nécessite Filament) et avantage Python pour la lisibilité en supervision.
- **Node.js/TypeScript (NestJS/Fastify)** : pertinent pour une SPA riche, mais tout est à assembler (auth, admin, i18n, ORM, jobs) → plus de code généré, plus de décisions d'architecture déléguées à l'IA, plus de dépendances à maintenir. Le cahier des charges ne demande pas de front riche.

## Conséquences
- Le moteur de combat est un module Python pur (`src/domain/combat/`, emplacement fixé par l'ADR-002), sans dépendance Django, testé unitairement, seedé (`random.Random(seed)`).
- Les valeurs d'équilibrage vivent dans la table `game_config` + fixtures de seed.
- Si un besoin d'interactivité dépasse HTMX, ajouter des **îlots Svelte** ciblés (compilés en web components autonomes, un îlot = un widget, ex. : éditeur drag-and-drop de la liste de sorts) plutôt que migrer vers une SPA. Svelte est retenu comme techno d'îlots : compilation légère sans runtime embarqué, et compétence existante du porteur de projet. Règle : un îlot ne contient jamais de logique de jeu, uniquement de l'interface ; le serveur reste autoritaire.

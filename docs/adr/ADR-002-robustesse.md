# ADR-002 — Durcissement : robustesse, stabilité, upgradabilité

**Statut :** accepté (challenge de l'ADR-001 mené le 07/07/2026)
**Contexte :** le code est écrit majoritairement par IA. L'exigence est : robuste sous itération, stable dans le temps, upgradable sans douleur. L'ADR-001 (Django/PostgreSQL/HTMX) est confirmé mais complété par les garde-fous suivants, tous **non négociables**.

## 1. Versions et dépendances
- **Django 5.2 LTS** (support 3 ans) — on ne suit pas les versions non-LTS. Upgrade LTS → LTS uniquement, en suivant la release note officielle.
- **Python 3.12**, **PostgreSQL 16**.
- Gestionnaire de dépendances : **uv** avec lockfile committé. Politique : le moins de dépendances possible ; toute nouvelle dépendance doit être justifiée en une ligne dans le PR/commit.
- Renovate ou Dependabot activé sur le dépôt : mises à jour de sécurité automatiques, mineures groupées, majeures manuelles.

## 2. Typage statique strict (filet de sécurité n°1 pour le code écrit par IA)
- **pyright en mode `strict`** (ou mypy `--strict`) sur tout le code, avec **django-stubs**.
- Aucune fonction sans annotations. `Any` interdit sauf commentaire justificatif.
- Objets métier passés entre couches : **dataclasses ou pydantic**, jamais des dicts anonymes.

## 3. Architecture en couches : le domaine ignore le framework
```
src/
  domain/          # PYTHON PUR — aucune importation de Django
    combat/        # moteur de combat (seedé, déterministe)
    progression/   # formules XP, coûts d'entraînement
    economy/       # règles du ledger, banque, vol PvP
    alchemy/       # règles de reroll
  game/            # apps Django FINES : modèles, vues, admin
                   # elles appellent domain/, jamais l'inverse
  config/          # settings, urls, i18n
```
- Règle d'or : `domain/` est testable sans base de données ni Django. C'est ce qui rend les upgrades de framework indolores et l'itération IA sûre : on peut réécrire une vue sans risquer le moteur, et inversement.
- Un test d'architecture (import-linter) fait échouer la CI si `domain/` importe Django.

## 4. CI : quality gates bloquants (la boucle d'itération de l'IA)
Pipeline (GitHub Actions ou équivalent) exécuté sur chaque commit, **tout doit être vert** :
1. `ruff check` + `ruff format --check` (lint/format)
2. `pyright` strict (types)
3. `import-linter` (frontières d'architecture)
4. `pytest` avec couverture : **≥ 90 % sur `domain/`**, ≥ 70 % global
5. `python manage.py makemigrations --check` (aucune migration oubliée)
- Localement : pre-commit reproduit 1–3. L'IA itère jusqu'au vert avant toute livraison ; l'humain ne relit que du code déjà vert.

## 5. Base de données et migrations
- Migrations toujours réversibles quand c'est possible ; les migrations de données sont séparées des migrations de schéma.
- Interdiction de modifier une migration déjà appliquée en prod.
- Sauvegarde automatique (pg_dump quotidien) dès la mise en ligne — script fourni dans le repo.

## 6. Itération et évolutivité
- Toute évolution de gameplay = d'abord une mise à jour de `docs/01_GAME_DESIGN.md`, puis le code (les docs restent la source de vérité).
- Feature flags simples via `game_config` pour activer/désactiver une mécanique sans déploiement.
- Les seeds (sorts, créatures, objets) sont des fixtures versionnées : ajouter du contenu = un commit de données, zéro code.

## Conséquences
- La Phase 0 de la roadmap inclut désormais : CI complète, pyright strict, structure `domain/` vs `game/`, pre-commit, lockfile uv.
- Coût accepté : la Phase 0 est un peu plus longue. Gain : chaque phase suivante s'itère plus vite et plus sûrement — c'est l'arbitrage explicitement voulu.

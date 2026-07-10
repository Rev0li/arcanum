# Workflow du projet

Ce repo suit un workflow **issue-driven** : tout changement passe par une issue, une branche et une PR. Aucun commit direct sur `main`.

## Cycle de vie d'un changement

```
Issue ouverte → Branche créée depuis l'issue → Commits → PR ("Closes #N")
→ Merge (squash) sur main → l'issue se ferme automatiquement, la branche est supprimée
```

### 1. Créer une issue

Toute tâche commence par une issue, via l'un des templates. L'issue décrit le **quoi** et les critères d'acceptation.

**Syntaxe des titres** — le préfixe est pré-rempli par le template, le titre décrit l'action :

| Template | Préfixe du titre | Exemple |
|----------|------------------|---------|
| ✨ Feature | `[Feat]` | `[Feat] Système de combat au tour par tour` |
| 🐛 Bug | `[Bug]` | `[Bug] Crash à l'ouverture de l'inventaire` |
| 📝 Documentation | `[Docs]` | `[Docs] Lore des royaumes du Nord` |

**Labels de domaine** — en plus du label de type posé par le template (`enhancement`, `bug`, `documentation`), ajouter le ou les domaines concernés :

| Label | Domaine |
|-------|---------|
| `front` | Interface / côté joueur |
| `back` | Serveur / logique métier |
| `bdd` | Base de données |
| `game-design` | Règles du jeu, équilibrage, lore |
| `infra` | Outils, CI, hébergement |

### 2. La branche est créée automatiquement 🤖

À l'ouverture de l'issue, une GitHub Action ([branche-auto.yml](.github/workflows/branche-auto.yml)) crée la branche, la lie à l'issue (section Development) et poste en commentaire la commande pour la récupérer.

Convention de nommage (appliquée par l'Action selon le label de l'issue) :

| Type | Format | Exemple |
|------|--------|---------|
| Feature | `feat/N-description-courte` | `feat/12-systeme-de-combat` |
| Bug | `fix/N-description-courte` | `fix/23-crash-inventaire` |
| Documentation | `docs/N-description-courte` | `docs/8-lore-royaumes-du-nord` |

En local :

```bash
git fetch origin
git switch feat/12-systeme-de-combat
```

### 3. Commiter

Messages de commit au format [Conventional Commits](https://www.conventionalcommits.org/fr/) :

```
feat: ajoute le sort boule de feu
fix: corrige le crash à l'ouverture de l'inventaire
docs: met à jour le README
```

### 4. Ouvrir une PR

- Cible : `main`
- La description doit contenir **`Closes #N`** (pré-rempli par le template de PR) : c'est ce qui ferme l'issue automatiquement au merge.
- ⚠️ Ne jamais fermer l'issue à la main avant le merge — c'est le merge de la PR qui la ferme.

### 5. Merger

- Mode de merge : **Squash and merge** (un commit propre par PR sur `main`)
- Titre du squash : `feat: description (#N)` — c'est le titre de la PR par défaut
- La branche est supprimée automatiquement après le merge.

## Règles du repo

- `main` est protégée : pas de push direct, tout passe par une PR.
- Une issue = une branche = une PR. Pas de PR fourre-tout.
- Le board GitHub Projects suit l'avancement : `Todo → In Progress → In Review → Done`.

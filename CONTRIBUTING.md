# Workflow du projet

Ce repo suit un workflow **issue-driven** : tout changement passe par une issue, une branche et une PR. Aucun commit direct sur `main`.

## Cycle de vie d'un changement

```
Issue ouverte → Branche créée depuis l'issue → Commits → PR ("Closes #N")
→ Merge (squash) sur main → l'issue se ferme automatiquement, la branche est supprimée
```

### 1. Créer une issue

Toute tâche (feature ou bug) commence par une issue, via les templates ✨ Feature ou 🐛 Bug. L'issue décrit le **quoi** et les critères d'acceptation.

### 2. Créer la branche depuis l'issue

Sur la page de l'issue, utiliser le bouton **"Create a branch"** (section Development, colonne de droite) — cela lie automatiquement la branche à l'issue.

Convention de nommage :

| Type | Format | Exemple |
|------|--------|---------|
| Feature | `feat/N-description-courte` | `feat/12-systeme-de-combat` |
| Bug | `fix/N-description-courte` | `fix/23-crash-inventaire` |

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

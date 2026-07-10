# Devlog — 2026-07-10 : Mise en place du workflow GitHub

**Issues/PR concernées** : #2 (automatisation), #3 (PR), #4 (test), #5 (cette doc)

Ce jour-là, le repo est passé d'un simple README à un workflow complet : issue → branche auto → PR → squash merge, avec `main` protégée. Toute la mise en place a été faite **à distance en ligne de commande** avec le CLI GitHub (`gh`). Cette entrée documente chaque script utilisé, pour pouvoir rejouer la configuration sur un autre repo ou vérifier l'état de celui-ci.

---

## 1. Prérequis : installer et authentifier `gh`

### Installation (Windows)

```powershell
winget install --id GitHub.cli --accept-source-agreements --accept-package-agreements
```

> ⚠️ Après installation, `gh` n'est pas dans le PATH des terminaux déjà ouverts.
> Sous Git Bash : `export PATH="$PATH:/c/Program Files/GitHub CLI"`

### Authentification

Deux options :

**Option A (propre)** — login interactif une fois pour toutes :

```bash
gh auth login   # choisir GitHub.com → HTTPS → navigateur
```

**Option B (sans interaction)** — réutiliser le jeton que git a déjà en mémoire (celui du Git Credential Manager, qui sert aux push). Utile en session non interactive :

```bash
export GH_TOKEN=$(printf "protocol=https\nhost=github.com\n" | git credential fill | grep '^password=' | cut -d= -f2)
```

> ⚠️ Limite de l'option B : ce jeton couvre les scopes `repo`/`workflow` mais **pas
> `project`** — impossible de créer/gérer des GitHub Projects avec. Pour ça, option A.

Vérifier que ça marche :

```bash
gh repo view Rev0li/tales-of-magic-Resurect --json visibility,isPrivate
```

---

## 2. Configuration du repo : squash merge + auto-delete

Un seul mode de merge autorisé (squash), titre du commit = titre de la PR, corps = description de la PR, et suppression automatique des branches après merge :

```bash
gh api -X PATCH repos/Rev0li/tales-of-magic-Resurect \
  -F allow_squash_merge=true \
  -F allow_merge_commit=false \
  -F allow_rebase_merge=false \
  -F delete_branch_on_merge=true \
  -f squash_merge_commit_title=PR_TITLE \
  -f squash_merge_commit_message=PR_BODY
```

---

## 3. Protection de `main` (ruleset)

Crée le ruleset `protect-main` : PR obligatoire (0 approbation requise — on est deux, on ne peut pas s'auto-approuver), pas de suppression de la branche, pas de force-push, squash seul mode de merge autorisé.

```bash
cat > /tmp/ruleset.json <<'EOF'
{
  "name": "protect-main",
  "target": "branch",
  "enforcement": "active",
  "conditions": { "ref_name": { "include": ["~DEFAULT_BRANCH"], "exclude": [] } },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": false,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false,
        "allowed_merge_methods": ["squash"]
      }
    }
  ]
}
EOF
gh api -X POST repos/Rev0li/tales-of-magic-Resurect/rulesets --input /tmp/ruleset.json
```

Vérifier / lister les rulesets existants :

```bash
gh api repos/Rev0li/tales-of-magic-Resurect/rulesets --jq '.[] | {id, name, enforcement}'
```

> 💡 Les rulesets sont gratuits sur les repos **publics**. Sur un repo privé, il faut un plan payant.

---

## 4. Labels de domaine

```bash
gh label create front       --color 1d76db --description "Interface / côté joueur"
gh label create back        --color 0e8a16 --description "Serveur / logique métier"
gh label create bdd         --color 5319e7 --description "Base de données"
gh label create game-design --color d876e3 --description "Règles du jeu, équilibrage, lore"
gh label create infra       --color f9d0c4 --description "Outils, CI, hébergement"

gh label list   # vérification
```

---

## 5. Le cycle complet en ligne de commande

Le workflow (voir [CONTRIBUTING.md](../../CONTRIBUTING.md)) peut se dérouler entièrement au CLI. Exemple réel (issue #5, celle de cette doc) :

### a. Créer l'issue

```bash
gh issue create --title "[Docs] Devlog : mise en place du workflow" \
  --label documentation --label infra \
  --body "..."
# → renvoie l'URL avec le numéro : .../issues/5
```

### b. Attendre la branche créée par l'Action et basculer dessus

L'Action [branche-auto.yml](../../.github/workflows/branche-auto.yml) crée la branche en ~10 s. Pour l'attendre en script :

```bash
for i in 1 2 3 4 5 6; do
  branch=$(git ls-remote --heads origin "docs/5-*" | awk '{print $2}' | sed 's|refs/heads/||')
  [ -n "$branch" ] && break
  sleep 10
done
git fetch origin && git switch "$branch"
```

### c. Travailler, commiter, pousser

```bash
git add . && git commit -m "docs: ajoute l'entrée devlog du 2026-07-10"
git push -u origin "$branch"
```

### d. Ouvrir la PR (avec `Closes #N` !)

```bash
gh pr create --title "docs: devlog mise en place du workflow" \
  --body "## Description
...

## Issue liée

Closes #5"
```

### e. Merger en squash

```bash
gh pr merge <numéro-PR> --squash
git switch main && git pull origin main && git fetch --prune
```

Le merge ferme l'issue (grâce à `Closes #5`) et supprime la branche distante automatiquement.

---

## 6. Scripts de vérification

### L'Action a-t-elle tourné ?

```bash
gh run list --workflow=branche-auto.yml --limit 5
# statut attendu : completed / success
```

### La branche liée existe-t-elle ?

```bash
git ls-remote --heads origin | grep "5-"
```

### L'issue est-elle bien fermée après merge ?

```bash
gh issue view 5 --json state --jq .state   # → CLOSED
```

### État général du repo

```bash
gh issue list                 # issues ouvertes
gh pr list                    # PR ouvertes
gh repo view --json deleteBranchOnMerge,squashMergeAllowed,mergeCommitAllowed
```

### Nettoyage après un test (issue #4 par exemple)

```bash
gh issue close 4 --comment "Test concluant ✅" --reason "not planned"
git push origin --delete docs/4-test-de-l-automatisation-de-branche
```

---

## Récap de ce qui a été mis en place ce jour-là

| Élément | Où |
|---------|-----|
| Templates d'issues ✨ 🐛 📝 | `.github/ISSUE_TEMPLATE/` |
| Template de PR (`Closes #N` pré-rempli) | `.github/pull_request_template.md` |
| Action branche auto par issue | `.github/workflows/branche-auto.yml` |
| Doc du workflow | `CONTRIBUTING.md` |
| Ruleset `protect-main` | Settings → Rules (via API) |
| Squash only + auto-delete | Settings → General (via API) |
| Labels front/back/bdd/game-design/infra | Issues → Labels (via CLI) |

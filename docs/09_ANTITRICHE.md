# 09 — ANTITRICHE : MODÈLE DE MENACES ET MESURES

> **Statut : propositions à valider par le porteur de projet** (à valider au plus tard avant la Phase 5 — PvP, là où le risque devient réel). Dimensionné pour la cible V1 : un serveur, ~500 joueurs actifs/jour. Beaucoup de mesures sont déjà des exigences de `02_SPEC_TECHNIQUE.md` ; ce document les relie aux menaces qu'elles couvrent.

## Pourquoi tricher ici ?
Un PBBG compétitif a trois choses à voler : **l'or** (économie), **le classement** (prestige PvP) et **le temps** (contourner les minuteurs et le quota d'énergie). Tout le modèle de menaces découle de ces trois cibles.

## Menace 1 — Multi-comptes et « pushing » PvP
Créer des comptes sacrifiables pour les attaquer et siphonner leur or, ou gonfler son Elo.

**Mesures :**
- Un compte = un personnage (V1) ; rate limiting sur la création de compte (par IP).
- Le vol PvP est plafonné à 5 % de l'or **non banké** : un compte poire fraîchement créé n'a presque rien à voler.
- Suggestions de cibles à ±20 % de puissance + maximum 3 attaques/jour sur la même cible : le farming d'un compte précis est mécaniquement limité.
- Pas de transfert d'or direct entre joueurs en V1 (pas d'hôtel des ventes, pas d'échange) ; seul canal : don à la trésorerie de guilde, journalisé dans le ledger (`guild_donation`) donc auditable.
- Vue admin « comptes corrélés » (proposition) : mêmes IP de connexion récurrentes + interactions PvP répétées = signalement manuel, pas de bannissement automatique.

## Menace 2 — Bots et automatisation
Scripts qui consomment l'énergie, relancent les minuteurs et travaillent à l'école 24 h/24.

**Mesures :**
- La conception limite déjà le gain : quota d'énergie journalier fixe, minuteurs incompressibles, occupation exclusive pendant les quêtes. Un bot parfait ne gagne que quelques minutes de latence par jour sur un humain assidu — le rythme `pacing: classic` est en soi une défense.
- Rate limiting global sur les endpoints d'action (en plus de login/register/messages déjà exigés par 02).
- Journal d'activité par compte (horodatage des actions) pour l'analyse manuelle en cas de doute.
- **Pas** de CAPTCHA par défaut (friction inutile pour 500 joueurs/jour) ; en réserve comme feature flag `game_config` si un abus avéré apparaît.

## Menace 3 — Exploitation de bugs économiques
Doubles crédits (double-clic, requêtes concurrentes), soldes négatifs, duplication d'objets.

**Mesures (déjà exigées par 02/ADR-002, rappelées ici comme mesures antitriche) :**
- `gold_ledger` = source de vérité auditable ; le solde dénormalisé est reconstructible.
- Idempotence de toute résolution de minuteur (`resolved_at` + verrou) ; transactions atomiques + `select_for_update` sur les opérations concurrentes ; tests de concurrence dès la Phase 1.
- Proposition : commande de maintenance `check_economy` (job quotidien) qui recalcule chaque solde depuis le ledger et alerte sur tout écart — détection au plus tôt d'un exploit passé inaperçu.

## Menace 4 — Triche au temps et au client
Manipuler l'horloge, forger des requêtes, soumettre des résultats.

**Mesures :**
- Serveur autoritaire absolu (02 §1) : le client n'envoie que des intentions, jamais de résultats ; tous les horodatages sont pris côté serveur en UTC.
- Les minuteurs vivent en base (`started_at`/`ends_at`) : il n'existe aucun état côté client à falsifier.

## Menace 5 — Triche au combat
Relancer un combat jusqu'à obtenir un résultat favorable, ou contester un résultat.

**Mesures :**
- La graine aléatoire est fixée **à la création** du combat et loggée ; le rapport est immuable une fois résolu.
- Tout combat est rejouable depuis sa seed par le moteur déterministe (golden tests de la Phase 2) : en cas de litige ou de soupçon, l'admin rejoue et compare.

## Menace 6 — Abus du contenu utilisateur et du social
XSS via pseudo/forum/MP (LE classique du genre), harcèlement via PvP.

**Mesures :**
- Échappement systématique + tests XSS dédiés (déjà exigés : 02 §2, 06 Phase 4).
- Protections PvP par conception : bouclier de novice (< niveau 8), 1 h post-défaite, 3 attaques/jour/agresseur.
- Outils de modération journalisés (`ModerationLog`) : bannir avec durée, muter, verrouiller.

## Ce qu'on ne fait PAS en V1 (hors scope assumé)
Fingerprinting navigateur, anti-bot comportemental, obfuscation client, détection automatisée avec sanctions automatiques. Coût/complexité disproportionnés pour la cible ; la conception (serveur autoritaire + ledger + seeds rejouables) couvre l'essentiel, l'humain fait le reste.

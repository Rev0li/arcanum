# 07 — DIRECTION ARTISTIQUE ET DESIGN SYSTEM

> Ce document définit l'identité visuelle du jeu et son système de design. Il fait référence pour toute production d'interface (Phase 0 → 6) et d'assets. Règle juridique absolue : **aucun asset de Tales of Magic original ne doit être réutilisé** (illustrations, logo, ornements scannés) — on recrée une identité originale dans le même esprit.

## 1. Intention

L'original (2008) : cadre baroque sombre, gemmes serties, sorcière et tour au crépuscule, panneaux de parchemin. On garde cette **âme** — un objet magique précieux et sombre — mais on l'exécute avec la discipline d'une interface moderne : hiérarchie claire, espaces généreux, ornement rare donc précieux.

Formule de la DA en une phrase : **« un grimoire précieux ouvert dans une bibliothèque de nuit »** — l'interface est sombre et calme (la bibliothèque), le contenu important est lumineux et texturé (les pages du grimoire).

Trois interdits (les tics du design générique) : pas de fond noir pur avec un accent vert acide, pas de dégradés violets « gaming » saturés, pas d'ornement partout (si tout est enluminé, rien n'est précieux).

## 2. Tokens — la source de vérité visuelle

Implémentés en **CSS custom properties** dans `static/css/tokens.css`. Aucune couleur ou taille en dur dans les templates : tout passe par les tokens.

### Palette (6 couleurs nommées)
| Token | Hex | Rôle |
|---|---|---|
| `--encre-nocturne` | `#191627` | Fond global — un noir bleuté profond, jamais #000 |
| `--ombre-violette` | `#252038` | Surfaces : cartes, panneaux, navigation |
| `--parchemin` | `#E9DEC3` | Pages de contenu (rapports, grimoire) + texte principal sur fond sombre |
| `--or-terni` | `#C9A24B` | Accent principal : titres, boutons primaires, bordures actives, XP |
| `--givre-arcane` | `#7BA7C9` | Magie/mana, liens, école de Givre et Arcane, états d'info |
| `--grenat` | `#A93A5B` | PV, danger, PvP, erreurs — la gemme rouge de l'original |

Déclinaisons autorisées : chaque couleur en variantes `-clair` / `-sombre` (±12 % de luminosité) générées une fois dans tokens.css. Les 4 écoles de magie mappent sur la palette : Feu → grenat-clair, Givre → givre-arcane, Arcane → givre-arcane-sombre, Nature → un vert mousse dérivé `#6E7F4E` (7e token, usage restreint aux écoles).

### Typographie (3 rôles, polices Google Fonts auto-hébergées)
| Rôle | Police | Usage |
|---|---|---|
| Display | **Cinzel** (600/700) | Titres de pages, noms propres du monde, boutons majeurs. Avec parcimonie : jamais en paragraphe. |
| Corps | **Vollkorn** (400/600 + italique) | Tout le texte courant, récits de quêtes, rapports. Serif de livre, très lisible en petit corps. |
| Utilitaire | **Alegreya Sans** (400/700) | Labels d'interface, stats, tableaux, badges — avec `font-variant-numeric: tabular-nums` pour tous les chiffres. |

Échelle de type : 12 / 14 / 16 (base) / 20 / 26 / 34 px. Interligne 1.6 pour le corps, 1.2 pour le display.

### Espacement, formes, élévation
- Échelle d'espacement : 4 / 8 / 12 / 16 / 24 / 40 px. Rien en dehors.
- Rayons : 2 px par défaut (le grimoire a des angles, pas des bulles), 6 px pour les avatars et gemmes.
- Bordures : 1 px `--ombre-violette-clair` par défaut ; 1 px `--or-terni` = élément actif/sélectionné.
- Ombres : une seule, discrète (`0 2px 12px rgb(0 0 0 / 0.4)`), réservée aux surélévations réelles (modales, menus).

## 3. La signature visuelle : la Page de Grimoire

L'élément que le jeu sera le seul à avoir : **les rapports de combat et les textes de quêtes sont rendus comme des pages de grimoire manuscrites** — fond `--parchemin` texturé (grain SVG léger), encre `#3A2F22`, lettrine Cinzel en tête, chaque tour de combat comme un paragraphe daté dans la marge, les dégâts soulignés à l'encre grenat, les soins à l'encre nature. Le contraste page claire / bibliothèque sombre fait de chaque combat un moment.

Corollaire de discipline : **c'est le seul endroit orné**. Le reste de l'interface (menus, boutiques, formulaires) est sobre, sombre et rapide. Un seul motif ornemental existe — un coin gravé serti d'une gemme, en SVG — et il n'apparaît que sur : la page de grimoire, les montées de niveau, et le butin épique. Nulle part ailleurs.

## 4. Composants (bibliothèque à construire au fil des phases)

- **Barres de ressources** : PV (grenat), Mana (givre), XP (or) — hauteur 8 px, fond ombre, valeur en tabular-nums à droite. Composant unique paramétré.
- **Jauge d'actions journalières** : rangée de gemmes (pleines/vides), le compteur central du header.
- **Minuteur** : temps restant en tabular-nums + fine barre de progression or ; à zéro, remplacé par un bouton « Récolter » (HTMX).
- **Carte de personnage** (la sienne, un adversaire, un membre de guilde) : avatar 64 px, nom en Cinzel, niveau + école en badge, barres.
- **Bouton primaire** : fond ombre-violette, bordure et texte or-terni, hover : fond or-terni / texte encre. Bouton danger (attaquer) : même logique en grenat.
- **Tableaux** (classements, inventaire) : lignes zébrées à 4 % d'opacité, en-têtes Alegreya Sans 12 px majuscules espacées, tri par en-tête.
- **Badges d'école et de rareté** : rareté par couleur de bordure uniquement (commun gris, peu commun givre, rare or, épique grenat) — jamais par fond plein.
- **Toast/notification** : bandeau discret en haut, icône + une phrase, voix active (« Entraînement terminé — Puissance +1 »).
- États vides et erreurs : toujours une direction (« Aucun sort appris — visite la bibliothèque de l'école »), jamais un constat sec.

## 5. Gabarits d'écrans clés (wireframes de référence)

### Tableau de bord (après connexion)
```
┌──────────────────────────────────────────────────────┐
│ GRIMOIRE      [gemmes ◆◆◆◇◇ actions]   or | gemmes | ✉ │  header fixe
├───────────┬──────────────────────────────────────────┤
│ Avatar    │  MINUTEURS EN COURS                       │
│ Nom       │  ⏳ Entraînement Puissance   12:41 ▓▓▓░   │
│ Nv 12     │  ⏳ Quête « Les rats »        03:12 ▓▓▓▓  │
│ PV ▓▓▓░   │──────────────────────────────────────────│
│ Mana ▓▓░  │  ACTIONS RAPIDES                          │
│ XP ▓▓▓▓░  │  [ Chasser ] [ Quêtes ] [ Donjon ] [ PvP ]│
│───────────│──────────────────────────────────────────│
│ Nav :     │  DERNIERS ÉVÉNEMENTS                      │
│ Grimoire  │  • Rapport : victoire contre Zombie  →    │
│ Boutique  │  • MP de Kaelis                       →   │
│ Guilde    │  • Classement : +3 places             →   │
│ Classemts │                                           │
└───────────┴──────────────────────────────────────────┘
```
Mobile : la colonne gauche devient un header compact + nav en tiroir.

### Rapport de combat (la signature)
```
┌────────────[ fond bibliothèque sombre ]───────────────┐
│   ┌────────[ PAGE PARCHEMIN, coin gravé ◆ ]─────────┐ │
│   │  𝕮hronique du duel — Aluna c. Zombie affamé     │ │
│   │  Tour 1 — Aluna incante Trait de givre (−14 PV) │ │
│   │  Tour 2 — Le zombie frappe (−6 PV)              │ │
│   │  ...                                            │ │
│   │  ✦ Victoire — 34 or, 120 xp, Fiole de brume     │ │
│   └─────────────────────────────────────────────────┘ │
│        [ Rejouer une chasse ]   [ Partager la page ]  │
└───────────────────────────────────────────────────────┘
```

## 6. Assets graphiques : besoins et production

### Inventaire des besoins (V1)
- **Icônes** (~80) : sorts, attributs, objets, actions. Source : **game-icons.net** (licence CC BY 3.0 — créditer dans les mentions légales), recolorées aux tokens via CSS `currentColor`/masques SVG. Zéro dessin à produire.
- **Illustrations de créatures** (~20, format 3:4) et **avatars/skins** (~12 pour lancer le cosmétique) : production par génération d'images IA avec un prompt-gabarit unique versionné dans `docs/assets/PROMPTS.md` (style : peinture numérique sombre, palette du jeu, fond neutre) pour garantir la cohérence. Vérifier les conditions commerciales de l'outil choisi.
- **Bannières de profil** (~8) : motifs abstraits dérivés de la palette (dégradés encre + constellation de gemmes), réalisables en SVG — pas besoin d'illustration.
- **Ornements** : le coin gravé + gemme (1 SVG), la texture de grain du parchemin (1 SVG filter), le logo (typographie Cinzel Decorative + gemme — pas d'illustration complexe en V1).
- **Hero de la page d'accueil publique** : 1 seule illustration ambitieuse (la tour de l'école au crépuscule — clin d'œil à l'original sans le copier).

### Règles
- Tout asset est optimisé (SVG minifié, WebP/AVIF pour les illustrations, ≤ 150 Ko par illustration).
- Un fichier `docs/assets/REGISTRE.md` liste chaque asset, sa source, sa licence — obligatoire avant intégration.
- Interdits : assets ToM originaux, personnages sous IP, packs « fantasy » sans licence claire.

## 7. Qualité, accessibilité, mouvement
- Contraste AA minimum partout (le parchemin sur encre-nocturne et l'or-terni sur ombre-violette passent — vérifier chaque nouvelle combinaison).
- Focus clavier visible (anneau or-terni 2 px), navigation complète au clavier.
- Mouvement : une seule animation orchestrée — l'ouverture de la page de grimoire (fondu + léger dépliage, 300 ms). Micro-transitions ≤ 150 ms ailleurs. `prefers-reduced-motion` respecté (tout devient instantané).
- Responsive : mobile-first, breakpoints 640 / 960 px. Le jeu doit être entièrement jouable au pouce.
- Budget performance : page < 300 Ko hors illustrations, aucune police > 2 graisses chargées.

## 8. Roadmap graphique (alignée sur 06_ROADMAP_TECHNIQUE)
- **Phase 0** : `tokens.css`, `base.html`, header/nav, boutons, typographie — le squelette est déjà « dans le thème ».
- **Phases 1–5** : chaque écran est livré avec les composants de ce document (pas de placeholder gris) ; les illustrations de créatures peuvent être des silhouettes SVG temporaires monochromes.
- **Phase 6** : production des illustrations finales (créatures, avatars, hero), la Page de Grimoire dans sa version complète (texture, lettrine, animation d'ouverture), passe de cohérence écran par écran avec captures comparées, audit contraste/clavier.

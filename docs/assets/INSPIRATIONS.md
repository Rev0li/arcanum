# MOODBOARD — INSPIRATIONS UI

> Références visuelles pour les maquettes (Lot V du `REGISTRE.md`) et la production d'assets. **Règle absolue : inspiration seulement, jamais de copie** — ces pages sont les œuvres d'autres artistes. Les captures récoltées vont dans `asset/inspirations/` (dossier local **gitignoré**, jamais commité), avec pour chaque capture une ligne : URL source + ce qui plaît dedans.

## Comment on s'en sert
1. **Récolte** (porteur de projet) : parcourir les pages ci-dessous, capturer les écrans/détails intéressants → `asset/inspirations/`, une ligne de contexte par fichier (ex. : `hollow-whispers-inventaire.png — la grille d'inventaire à bordures fines`).
2. **Analyse** (assistant) : rapprocher chaque capture de notre DA (tokens, composants du §4, gabarits du §5) et en tirer des choix concrets pour les maquettes.
3. On ne reprend jamais un élément tel quel : on note le **principe** (hiérarchie, rythme, forme) et on le réexécute avec nos tokens.

## Les références (déposées le 10/07/2026)

| Référence | Lien | Ce qu'on y regarde (rapporté à notre DA) |
|---|---|---|
| Set of dark fantasy elements for UI (Adobe Stock, kit vectoriel) | [stock.adobe.com](https://stock.adobe.com/fr/images/set-of-dark-fantasy-elements-for-user-interface-poster-video-fantasy-magic-hud-template-for-rpg-game-interface-vector-illustration-eps10/876349277) | Formes de cadres, boutons ornés, jauges. ⚠️ Kit **commercial** : s'il est acheté pour de vrai (pas seulement regardé), sa licence doit être consignée au `REGISTRE.md` avant toute intégration — sinon référence de formes uniquement. |
| Hollow Whispers — Game UI (Behance) | [behance.net](https://www.behance.net/gallery/213346975/Hollow-Whispers-Game-UI) | Ambiance sombre disciplinée : comment rester « dark fantasy » sans surcharge d'ornements — proche de notre interdit n°3 (si tout est enluminé, rien n'est précieux). |
| King & Dawn — User Interface (Behance) | [behance.net](https://www.behance.net/gallery/193050941/King-Dawn-User-Interface) | Hiérarchie des panneaux et typographie display/corps — à comparer à notre duo Cinzel/Vollkorn. |
| Map System — Fantasy game concept (Dribbble) | [dribbble.com](https://dribbble.com/shots/20968681-Map-System-Fantasy-game-concept) | Traitement « parchemin » d'une surface de contenu — nourrit la Page de Grimoire (notre signature), même si Arcanum n'a pas de carte. |
| HWADAM — Chosun Fantasy UI/UX (Behance) | [behance.net](https://www.behance.net/gallery/250322119/HWADAM-Chosun-Fantasy-UIUX-(-Personal-ArtWorks-)) | Élégance non-occidentale : espaces généreux, ornement rare — exactement notre discipline §1. |
| Dark RPG Game UI Concept (Behance, 1/2) | [behance.net](https://www.behance.net/gallery/243502249/Dark-RPG-Game-UI-Concept-Design) | Cartes de personnage, barres de ressources, badges de rareté — nos composants §4. |
| Dark RPG Game UI Concept (Behance, 2/2) | [behance.net](https://www.behance.net/gallery/248294903/Dark-RPG-Game-UI-Concept-Design) | Variante du précédent — comparer les traitements de tableaux/classements. |

## Bibliothèques d'assets libres — sources candidates (déposées le 10/07/2026)

> ⚠️ Deux garde-fous avant d'utiliser quoi que ce soit d'ici : **(1) licence** — OpenGameArt et itch.io hébergent des licences différentes par pack (CC0, CC-BY, GPL, « free » ambigu…), chaque pack utilisé doit avoir sa ligne au `REGISTRE.md` avec sa licence exacte ; **(2) cohérence DA** — la plupart de ces packs sont du **pixel art**, ce qui n'est pas notre direction (icônes SVG gravées + illustrations peintes). Usage légitime : **placeholders de prototypage** pendant les Phases 1–5, ou dépannage ponctuel recoloré. Si le pixel art te tente comme vraie direction, c'est une remise en cause de la DA §1 à acter dans `05`, pas un choix d'asset.

| Pack | Type | Usage envisageable |
|---|---|---|
| [Wyvern elemental skins](https://opengameart.org/content/wyvern-elemental-skins) (OGA) | sprites wyverne | référence de silhouette pour nos wyvernes |
| [Aeon Monsters I](https://opengameart.org/content/js-monsters-aeon-monsters-i) (OGA) | monstres | placeholders bestiaire en attendant les illustrations |
| [OSARE weapon icons](https://opengameart.org/content/osare-weapon-icons) (OGA) | icônes d'armes | dépannage icônes bâtons |
| [Armor icons by equipment slot](https://opengameart.org/content/armor-icons-by-equipment-slot) (OGA) | icônes par emplacement | ⭐ le plus pertinent : colle à notre système à 8 slots |
| [Medieval props textured](https://opengameart.org/content/medieval-props-textured) / [Rocks](https://opengameart.org/content/rocks-0) (OGA) | props 3D | décor de scènes 3D si pipeline rendu-3D retenu |
| [Necromancer free](https://creativekind.itch.io/necromancer-free) (itch) | sprite animé | hors DA (animation) — référence visuelle nécromancie (V2) |
| [Pixel magic spell effects 32×32](https://foozlecc.itch.io/pixel-magic-sprite-effects) (itch) | effets pixel | hors DA — le jeu n'a pas d'effets animés |
| [48 magic potions pixel icons](https://free-game-assets.itch.io/48-free-magic-potions-pixel-art-icons) (itch) | icônes potions | placeholder potions (nos 5 fioles finales : SVG) |
| [RPG items 16×16 : staves, books](https://pixelcreations.itch.io/rpg-items-16x16) (itch) | icônes objets | placeholder inventaire |
| [BloodMoon Tower GIF](https://creativekind.itch.io/gif-bloodmoon-tower-free) (itch) | tour animée | référence d'ambiance pour le hero (statique chez nous) |
| [Flame FX](https://binbun3d.itch.io/flame-fx) / [Elemental magic FX](http://binbun3d.itch.io/elemental-magic-fx) (itch) | effets Godot | hors scope (pas de moteur temps réel) |
| [TTRPG legacy rings (2000+ combinaisons)](https://ddant1100.itch.io/ttrpg-legacy-rings-1) (itch) | icônes d'anneaux | dépannage pour nos 10 anneaux nommés |
| [The art of scrolls 16×16](https://bigwander.itch.io/the-art-of-scrolls) (itch) | parchemins pixel | placeholder quêtes |

## Note de production : rendus 3D (Three.js, Blender…)

Les artworks du Tales of Magic original étaient eux-mêmes des **rendus 3D exportés en images** (cf. `asset/character_3d.jpg`, `asset/baton.jpg` — 08 §4 bis). Reproduire ce pipeline est donc légitime et même fidèle :

- ✅ **Autorisé V1** : modéliser/éclairer une scène 3D (Blender, Three.js…) et **exporter des images statiques** (WebP) pour les avatars, créatures, bâtons, hero — c'est une technique de production comme la génération IA, même règle : outil + source consignés au `REGISTRE.md`, palette et gabarits de `PROMPTS.md` respectés.
- ❌ **Hors scope V1** : de la 3D **en jeu** (viewer Three.js temps réel, avatar qui tourne…) — la vision l'exclut explicitement (`00_VISION.md` : « pas de graphismes 2D/3D en jeu, uniquement illustrations statiques et icônes »). Si l'envie se confirme, c'est une question à rouvrir dans `05` + un ADR, pas une décision d'asset.

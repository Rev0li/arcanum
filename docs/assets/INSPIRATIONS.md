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

## Note de production : rendus 3D (Three.js, Blender…)

Les artworks du Tales of Magic original étaient eux-mêmes des **rendus 3D exportés en images** (cf. `asset/character_3d.jpg`, `asset/baton.jpg` — 08 §4 bis). Reproduire ce pipeline est donc légitime et même fidèle :

- ✅ **Autorisé V1** : modéliser/éclairer une scène 3D (Blender, Three.js…) et **exporter des images statiques** (WebP) pour les avatars, créatures, bâtons, hero — c'est une technique de production comme la génération IA, même règle : outil + source consignés au `REGISTRE.md`, palette et gabarits de `PROMPTS.md` respectés.
- ❌ **Hors scope V1** : de la 3D **en jeu** (viewer Three.js temps réel, avatar qui tourne…) — la vision l'exclut explicitement (`00_VISION.md` : « pas de graphismes 2D/3D en jeu, uniquement illustrations statiques et icônes »). Si l'envie se confirme, c'est une question à rouvrir dans `05` + un ADR, pas une décision d'asset.

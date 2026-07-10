# PROMPTS DE GÉNÉRATION D'ILLUSTRATIONS

> Prévu par `07_DIRECTION_ARTISTIQUE.md` §6 : **un prompt-gabarit unique, versionné**, pour que toutes les illustrations générées (créatures, avatars, hero) appartiennent au même monde. Toute évolution du gabarit = nouvelle version datée ici, jamais de modification silencieuse.
>
> Avant toute production : vérifier que les conditions de l'outil autorisent l'usage commercial, et consigner **outil + version + prompt exact (+ seed si disponible)** dans la ligne de l'asset du `REGISTRE.md`.

## Gabarit de base — v2 (10/07/2026, direction picturale actée — décision n°19)

Référence d'intention : la facture peinte des séries d'animation type Fortiche (*Arcane*). ⚠️ **Ne jamais écrire « Arcane », « Riot » ou « Fortiche » dans un prompt** : on décrit les attributs du style (meilleure qualité, et zéro risque de ressemblance à une IP).

```
Illustration peinte, style peinture numérique texturée de série d'animation
moderne : coups de pinceau visibles, textures picturales façon gouache/huile,
traits de construction assumés, PAS de rendu 3D lisse, PAS de photoréalisme,
PAS de cel-shading plat. Éclairage théâtral très contrasté : une source de
lumière magique colorée + contre-jour (rim light), profondeur atmosphérique,
grain pictural. Palette imposée : fonds bleu-noir profond (#191627, #252038),
lumières or terni (#C9A24B), accents givre (#7BA7C9) et grenat (#A93A5B),
touches parchemin (#E9DEC3). Fond neutre sombre ou vaporeux.
Aucun texte, aucun logo, aucune signature, aucun filigrane.
```

Interdits (rappel DA §1) : vert acide, dégradés violets « gaming » saturés, esthétique néon, pixel art. Et évidemment : aucune imitation des artworks du Tales of Magic original, aucun personnage sous IP (ni ToM, ni Arcane).

## Déclinaison Créature (Lot II)
Gabarit de base +
```
Portrait de créature : [NOM + description en une phrase, ex. « un zombie
affamé, chairs grises, robe d'apprenti en lambeaux »]. Cadrage en pied ou
buste, format portrait 3:4, la créature regarde légèrement hors champ.
Menaçante mais lisible en vignette de 120 px de large.
```
- Une créature = une génération réussie + retouches éventuelles ; pas de mélange de styles entre créatures.
- Export : WebP, 600×800 max, ≤ 150 Ko.

## Déclinaison Avatar / skin (Lot III)
Gabarit de base +
```
Portrait de [sorcière / mage], buste de trois quarts, format carré,
chapeau pointu et attributs d'école [feu/givre/arcane/nature] discrets.
Expression déterminée, visage lisible en 64 px.
```
- Deux archétypes de base sobres ; les skins déclinent tenues et ambiances de couleur (une école dominante par skin).
- Export : WebP carré 512×512, ≤ 100 Ko.

## Déclinaison Hero (Lot IV — un seul asset)
Gabarit de base +
```
Paysage panoramique : la tour d'une école de magie au crépuscule orangé,
fenêtres éclairées, corbeaux dans le ciel, premier plan sombre. Ambiance
« un grimoire précieux ouvert dans une bibliothèque de nuit ». Format 21:9.
```
- Clin d'œil à l'original (tour au crépuscule) **sans en copier la composition** — vérifier visuellement contre la capture de référence avant adoption.

## Déclinaison Concept art / scène (file du REGISTRE)
Gabarit de base +
```
Scène d'ambiance : [SUJET, ex. « une immense bibliothèque circulaire la
nuit, un grimoire ouvert et lumineux sur un pupitre, chandelles »].
Composition cinématographique, plan large ou moyen, un point focal
lumineux unique. Format paysage 16:9 (ou 3:4 pour un PNJ en pied).
```
- Le concept art sert à **fixer le monde** avant les assets finaux : lieux des écrans, PNJ, donjons. Une scène validée devient la référence de son écran.

## Journal des versions
| Version | Date | Changement |
|---|---|---|
| v1 | 10/07/2026 | Gabarit initial (base + créature + avatar + hero) |
| v2 | 10/07/2026 | Direction picturale « type Arcane » actée (décision n°19) : attributs peints texturés, éclairage théâtral, interdiction de citer l'IP dans les prompts ; + déclinaison Concept art |

# 08 — RÉFÉRENCES : LE TALES OF MAGIC ORIGINAL

> Compilation de tout ce qui reste documenté en ligne sur le jeu original (recherches effectuées le 07/07/2026). Sert de référence de fidélité pour le remake et de mémoire du jeu. Rappel : ces sources servent à comprendre l'original, **jamais** à en copier les assets ou les textes.

## 1. Fiche d'identité
- **Titre** : Tales of Magic — slogan du studio : « WE ENTERGAME YOU! »
- **Développeur/éditeur** : RedMoon Studios GmbH & Co. KG (Allemagne), devenu **CRATR.games GmbH** le 04/11/2020. Studio des jeux KnightFight, MonstersGame, Dig'n'Fight, FreedomResist, PiratesAssault, BananaKing, TechWarrior, RumbleRace, et du portail de comptes MoonID.
- **Période d'exploitation** : copyright « © 2007 - 2010 » sur le site (capture de référence) ; sortie France datée 2008 par jeuxvideo.com ; la fiche ModDB indique 2005 (probablement la version d'origine ou une erreur). Le jeu est aujourd'hui fermé (date de fermeture non documentée publiquement).
- **Genre** : MMO/RPG par navigateur, textuel à menus (PBBG), gratuit avec monnaie premium.
- **Portée internationale** : domaines connus — talesofmagic.de, .fr (dont **world2.talesofmagic.fr** : preuve de mondes/serveurs multiples par pays), .us, .co.uk, .it, .ru, talesofmagic.jogos.sapo.pt (Portugal). La capture de référence montre 10 drapeaux de langues (DE, UK, ES, FR, IT, PL, PT, RO, RU, US).
- **Serveurs datés** : le sélecteur de la capture montre « Serveur 1 (07.12.2009) » — les serveurs affichaient leur date d'ouverture.

## 2. Le jeu tel que décrit à l'époque (synthèse des descriptions officielles et fiches)
Le joueur devient **sorcière ou mage**, intègre « la plus grande école de sorciers du web », apprend des sorts, attaque d'autres sorciers avec des **boules de feu et des attaques de glace**, et combat des **zombies et des dragons** pour devenir le plus puissant magicien. Le jeu était comparé à l'époque à « un Harry Potter » à l'école de magie (fiche italienne GDR-online). Avec l'expérience gagnée, on remplissait son **grimoire** de sorts et on achetait une **robe** plus résistante et d'autres objets mystiques.

## 3. Mécaniques originales documentées (faits, pas reconstructions)
- **Choix d'une voie magique à la création** (description officielle allemande) : trois orientations — les **arts noirs**, la **maîtrise des éléments**, ou la **magie blanche** (soins). Le jeu évoquait aussi un positionnement « bon ou mauvais ».
- **Cercles** (« Zirkel ») : groupes de sorciers alliés menant des batailles ensemble — l'équivalent des clans/guildes, et l'origine du terme « cercles » repris dans notre GDD.
- **PvP central** : attaquer d'autres sorciers était l'argument n°1 de toutes les descriptions commerciales.
- **PvE** : zombies et dragons cités dans toutes les langues ; « dominer des créatures puissantes » (description allemande).
- **Monnaie premium échangeable contre de l'or** : les descriptions portugaise (« trocar rubis por ouro ») et italienne (« ticket-gemme pour obtenir encore plus d'or ») confirment que les **rubis/gemmes s'échangeaient contre de l'or** — un modèle pay-for-advantage classique de l'époque. ⚠ Voir §6 : notre remake s'en écarte volontairement.
- **Jeu textuel** : les fiches spécialisées le classent explicitement comme « text-based browser game ».

## 4. La capture d'écran de référence (source primaire du projet)
Fournie par le porteur de projet : page de connexion en **espagnol** sur un **serveur français** (Serveur 1, 07.12.2009), preuve du portail multilingue. Éléments visuels notables ayant inspiré la direction artistique (07) :
- Cadre baroque sombre ceinturant tout l'écran, serti de **gemmes rouge/rose** aux angles et de lierre.
- À gauche : sorcière au chapeau pointu, bâton et orbe de magie bleue ; à droite : tour de l'école au crépuscule orangé ; corbeau et chandelle en haut de cadre.
- Panneau central de connexion sur fond sombre : champs Serveur / Apodo (pseudo) / Contraseña, boutons ornés « ENTRAR » et « REGISTRARSE », accroche : traverser les portes de l'école de magie et devenir le meilleur mage du monde.
- Quatre vignettes de présentation en bas (aperçus du jeu : interface, baguettes/sorts, parchemin de stats, personnage).
- Footer : © 2007-2010 RedMoon Studios GmbH & Co. KG, mentions légales, et liens croisés vers les autres jeux du studio.

## 4 bis. Captures et artworks d'époque fournis par le porteur de projet (10/07/2026)

Six fichiers d'origine (Exif : Photoshop CS2, juillet 2007) conservés dans le dossier local `asset/`, **gitignoré — jamais commités, jamais intégrés** (propriété CRATR.games, cf. §7). C'est la plus riche source primaire du projet : deux écrans internes réels, ce que les archives en ligne n'avaient pas livré.

- **`home.jpg` — écran réel de la page personnage** (« Charakterseite », version allemande) : navigation principale à 5 entrées — **Mein Charakter / Mein Zauberbuch / Meine Schatztruhe / Mein Turm / Accountdaten** (personnage / grimoire / coffre au trésor / **tour** / compte) ; rangée d'icônes d'action serties dans des orbes de verre sous le logo ; fiche : Level, Zirkel, **Gesinnung : « neutral »**, Gold, **Status : « Bereit »** ; portrait dans un cadre baroque flanqué d'un orbe bleu et d'un orbe rouge avec barre de progression ; programme de parrainage (250 or par filleul).
- **`profil_which.png` — zoom de la même fiche** (« mariposa », niveau 1) : libellé exact **« Gold / Edelsteine : 50 / 0 »** → l'or de départ était 50, or et gemmes affichés côte à côte.
- **`spell_house.jpg` — écran réel du grimoire** (« Mein Zauberbuch ») : livre ouvert sur parchemin, **onglets-marque-pages colorés par famille de magie (7 visibles)** ; règle affichée en toutes lettres : *l'ordre des sorts détermine leur utilisation en combat — au 1er tour le 1er sort, au 2e tour le 2e, etc. ; les sorts désactivés ne sont pas utilisés* ; chaque sort affiche : effet typé (« Kampf Luft 1–2 », « Kampf Wasser 1–2 », « Heilung 1–1 »), coût en mana, **niveau « 1 / 3 » (rang max 3)** et des commandes monter / descendre / activer / désactiver. Sorts attestés : **Rauch** (fumée, air), **Kälte** (froid, eau), **Leichte Heilung** (soin léger).
- **`baton.jpg` — artwork promo** : quatre bâtons aux magies rouge, verte, bleue et violette — écho direct à nos quatre écoles.
- **`character_3d.jpg` — artwork promo** : mage en robe bleue ornementée, bâton à orbe lumineux, cercle runique au sol.
- **`icon.webp`** : avatar/favicon d'époque (visage de sorcière, 32 px).

**Mécaniques nouvellement attestées** (jusqu'ici seulement déduites du marketing) : l'axe d'alignement existait comme champ de la fiche (« Gesinnung », avec état **neutre** par défaut) ; le personnage avait un **statut d'occupation** (« Bereit ») — notre occupation exclusive est donc fidèle ; les sorts avaient des **rangs** (max 3) et une **activation/désactivation** ; l'exécution en combat suivait **strictement l'ordre de la liste** ; il existait une section « Ma tour » (piste V2 à creuser : demeure du joueur ?).

## 5. Sources (vérifiées le 07/07/2026)
| Source | Contenu utile |
|---|---|
| jeuxvideo.com — fiche Tales of Magic (`jeuxvideo.com/jeux/web/00022221-tales-of-magic.htm`) | Fiche FR : éditeur RedMoon, sortie France 2008, genre MMO/Web |
| ModDB (`moddb.com/games/tales-of-magic`) | Pitch anglais (école de sorciers, boules de feu/givre, zombies, dragons), style RPG/Fantasy/MMO |
| browsergames.de (`browsergames.de/talesofmagic`) | La description la plus riche : 3 voies magiques, Zirkel, grimoire, robe, bon/mauvais |
| newrpg.com (`newrpg.com/browser-games/tales-of-magic/`) | Confirmation « text-based », sorcière ou mage, échange gemmes→or |
| gdr-online.com (`gdr-online.com/tales_of_magic.asp`) | Fiche italienne datée 01/10/2008, comparaison Harry Potter, duels de mages |
| Wikis KnightFight & MonstersGame (`kfwiki.arcadewelten.eu`, `mgwiki.arcadewelten.eu`) | Histoire du studio : liste des jeux RedMoon, transition vers CRATR.games (04/11/2020), portail MoonID |
| webstatsdomain.org (`webstatsdomain.org/d/world2.talesofmagic.fr`) | Preuve des domaines par pays et du monde 2 français ; slogans FR/PT/IT d'époque |
| urlm.co (`urlm.co/www.talesofmagic.co.uk`) | Domaine UK, hébergement Hetzner, slogan « WE ENTERGAME YOU! » |
| Capture d'écran du porteur de projet | Source primaire : interface réelle, serveur daté, identité visuelle |

### Pistes d'archives complémentaires (à explorer manuellement)
- **Wayback Machine** (`web.archive.org`) sur talesofmagic.de / .fr / world2.talesofmagic.fr : snapshots probables de la page d'accueil et peut-être de pages de jeu — la meilleure chance de retrouver des écrans internes (grimoire, combat, boutique).
- Communautés nostalgiques des jeux RedMoon (forums KnightFight/MonstersGame encore actifs, Discord CRATR) : d'anciens joueurs de ToM peuvent confirmer les mécaniques fines (noms des stats, économie).
- Vidéos YouTube d'époque (recherches « Tales of Magic RedMoon » 2008-2010) : rares mais possibles.

## 6. Écarts assumés entre l'original et le remake
| Sujet | Original (documenté) | Remake (décidé) | Justification |
|---|---|---|---|
| Monnaie premium | Rubis/gemmes échangeables contre de l'or (pay-for-advantage) | Gemmes 100 % cosmétiques | Décision actée (05) : modèle moderne type Riot, plus sain |
| Orientations magiques | 3 voies : arts noirs / éléments / magie blanche | 4 écoles : Feu, Givre, Arcane, Nature | Décision actée : « comme des écoles mais plus moderne » ; les 4 écoles couvrent les 3 voies (Nature ≈ magie blanche/soins) |
| Axe bon/mauvais | **Attesté en jeu** : champ « Gesinnung » de la fiche, défaut « neutral » (cf. §4 bis) | Absent de la V1 | ACTÉ (05, décision n°15) : idée V2 purement cosmétique |
| Nom, assets, textes | Propriété RedMoon/CRATR.games | Identité 100 % originale | Obligation légale (voir 05 et 07) |
| Algorithme de combat | Tour N = sort n° N de la liste, sorts désactivables (attesté, grimoire §4 bis) | Premier sort de la liste dont le mana suffit et hors recharge | Écart mineur assumé : évite les tours morts quand le mana manque |
| Rangs de sorts | Max 3 (attesté, grimoire §4 bis) | 5 rangs | Écart assumé : progression plus longue durée |
| Or de départ | 50 (attesté §4 bis) | 100 | Valeur d'équilibrage en `game_config`, ajustable |

## 7. Avertissement
Les marques, textes et visuels de Tales of Magic appartiennent à leurs ayants droit (CRATR.games GmbH). Ce document est une compilation de faits publics à but de recherche et de design. Le registre des assets du remake (`docs/assets/REGISTRE.md`, cf. 07) garantit qu'aucun élément protégé n'entre dans le projet.

# Arcanum — Remake de Tales of Magic
## Dossier de spécifications pour développement assisté par IA

Ce dossier contient le cahier des charges complet du projet. À placer dans `docs/` à la racine du dépôt. Utilisable avec n'importe quel assistant IA de code (Claude, etc.) ou en développement manuel.

## Ordre de lecture
1. `00_VISION.md` — le quoi et le pourquoi, les piliers, le scope.
2. `01_GAME_DESIGN.md` — toutes les mécaniques de jeu (toutes les décisions sont actées).
3. `02_SPEC_TECHNIQUE.md` — contraintes d'architecture non négociables.
4. `adr/ADR-001-stack.md` — la stack décidée : Django 5.2 LTS / PostgreSQL / HTMX, et pourquoi.
5. `adr/ADR-002-robustesse.md` — garde-fous non négociables : typage strict, architecture `domain/`, CI bloquante.
6. `03_MODELE_DONNEES.md` — modèle conceptuel des données.
7. `04_ROADMAP.md` — phases d'implémentation avec critères d'acceptation.
8. `06_ROADMAP_TECHNIQUE.md` — plan d'exécution ingénierie : modules, modèles, services et tests, phase par phase.
9. `07_DIRECTION_ARTISTIQUE.md` — identité visuelle, design system (tokens), signature « Page de Grimoire », plan des assets.
10. `05_QUESTIONS_OUVERTES.md` — journal des décisions actées et des questions de spec à trancher pendant le ticketing (le nom est acté : **Arcanum**).
11. `08_REFERENCES_ORIGINAL.md` — tout ce qui est documenté sur le Tales of Magic original : sources, mécaniques attestées, écarts assumés du remake.
12. `09_ANTITRICHE.md` — modèle de menaces et mesures antitriche (statut : propositions à valider par le porteur de projet).

## Prompt de démarrage suggéré pour l'assistant IA

```
Lis l'intégralité de docs/ dans l'ordre indiqué par docs/README.md.
docs/adr/ADR-001-stack.md fixe la stack (Django 5.2 LTS / PostgreSQL / HTMX)
et docs/adr/ADR-002-robustesse.md fixe les garde-fous qualité :
ces deux ADR ne sont pas rediscutables.
Implémente la Phase 0 en suivant docs/06_ROADMAP_TECHNIQUE.md
tâche par tâche, dans l'ordre indiqué.
N'annonce une tâche comme terminée que si les 5 gates de la CI
sont verts (lint, types, architecture, tests, migrations).
Ne passe jamais à une phase suivante sans que les critères
d'acceptation de la phase courante soient satisfaits.
À chaque décision structurante non couverte par les docs,
propose un ADR court dans docs/adr/ et attends ma validation.
```

## Règles d'or (rappel)
- Serveur autoritaire : aucune logique de jeu côté client.
- Moteur de combat : module Python pur, seedé, testé, rejouable, sans dépendance Django.
- Toute variation d'or passe par le ledger, dans la même transaction (`transaction.atomic()`).
- Équilibrage en données (`game_config` + seeds), jamais en dur.
- i18n dès le premier écran (FR d'abord).
- Une phase = critères d'acceptation verts avant la suivante.

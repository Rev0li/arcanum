# 03 — MODÈLE DE DONNÉES (conceptuel)

> Modèle conceptuel : l'implémenteur choisit les types exacts et peut ajouter des colonnes techniques (timestamps, index). Les noms sont indicatifs mais la structure des relations doit être respectée.

## Comptes et personnages
- **users** : id, email (unique), password_hash, role (player/moderator/admin), locale, created_at, banned_until, last_login_at.
- **characters** : id, user_id (unique en V1), name (unique), archetype (sorciere/mage), school (feu/givre/arcane/nature), level, xp, gold_on_hand, gold_banked, gems, daily_energy_used, energy_date, hp_current, attributes (puissance, concentration, resistance, vitalite, sagesse), protection_until, created_at.

## Contenu de jeu (données seedées, pas créées par les joueurs)
- **spells** : id, school, name_key, min_level, learn_cost, mana_cost, base_damage, effect_type, effect_params (JSON), cooldown_turns, max_rank.
- **creatures** : id, name_key, level_range, stats (JSON), timer_minutes, energy_cost, loot_table_id.
- **loot_tables** : id, name ; **loot_table_entries** : loot_table_id, reward_type (gold/item/ingredient/gems), reference_id (nullable), chance, min_qty, max_qty.
- **ingredients** : id, name_key, rarity, description_key.
- **achievements** (hauts faits) : id, name_key, description_key, condition (JSON), reward (JSON nullable : cosmétique, gemmes, titre).
- **dungeons** : id, name_key, floors_count ; **dungeon_floors** : dungeon_id, floor_number, creature_id, is_boss.
- **items** : id, slot, rarity, min_level, name_key, price, attribute_bonuses (JSON), special_effect (JSON nullable).
- **transmutation_rules** : id, target_type (item/spell), rarity_or_school, ingredients_required (JSON), gold_cost, duration_minutes — règles de coût des rerolls.
- **cosmetics** : id, type (avatar/banniere/titre/cadre), name_key, gem_price (nullable si récompense de haut fait), unlock_condition (JSON nullable).
- **potions** : id, name_key, boosted_attribute, bonus_value, duration_minutes, gold_price.
- **quest_templates** : id, type (timed/daily/story), name_key, duration_minutes, rewards (JSON), story_order (nullable), random_events (JSON).
- **game_config** : key, value — toutes les constantes d'équilibrage.

## État du joueur
- **character_spells** : character_id, spell_id, rank.
- **combat_sequences** : character_id, position, spell_id (la liste de sorts définie par le joueur, exécutée automatiquement).
- **character_cosmetics** : character_id, cosmetic_id, equipped (bool).
- **potion_inventory** : character_id, potion_id, quantity.
- **active_buffs** : character_id, potion_id, expires_at — le moteur de combat lit les buffs actifs du personnage au moment de la résolution.
- **inventory** : character_id, item_id, equipped (bool), quantity.
- **ingredients_inventory** : character_id, ingredient_id, quantity.
- **active_timers** : id, character_id, type (training/quest/transmutation/combat), payload (JSON : quoi précisément), started_at, ends_at, resolved_at (nullable), result (JSON, rempli à la résolution). *Une seule table pour tous les minuteurs simplifie la résolution lazy + job.*
- **dungeon_progress** : character_id, dungeon_id, current_floor, last_attempt_date.
- **daily_quests** : character_id, date, objectives (JSON), completed (bool).

## Combat et PvP
- **combat_reports** : id, type (pve/pvp/dungeon), attacker_character_id, defender_character_id (nullable) ou creature_id, seed, turns (JSON), winner, gold_stolen, xp_gained, loot (JSON), created_at, public_token (lien partageable).
- **pvp_ratings** : character_id, rating, wins, losses.
- **attack_limits** : attacker_id, defender_id, date, count (application de la règle des 3 attaques/jour).

## Économie
- **gold_ledger** : id, character_id, delta, balance_after, reason (enum : hunt_reward, quest_reward, purchase, training, pvp_steal_in/out, bank_deposit/withdraw, guild_donation, admin_adjust…), reference_id, created_at. *Source de vérité auditable.*
- **shop_rotation** : date, item_id (l'objet rare du jour).

## Communauté
- **guilds** : id, name (unique), tag, description, leader_character_id, treasury_gold, created_at.
- **guild_members** : guild_id, character_id, role (archimage/officier/membre), joined_at.
- **forum_categories** / **forum_threads** (category_id ou guild_id nullable pour les forums de cercle, author_id, title, pinned, locked) / **forum_posts** (thread_id, author_id, body, created_at, deleted_by).
- **private_messages** : id, sender_id, recipient_id, subject, body, read_at, created_at.

## Relations clés à respecter
- Un `combat_report` référence toujours sa `seed` → tout combat est rejouable par le moteur pour audit.
- `characters.gold_on_hand` et `gold_banked` sont dénormalisés mais chaque variation crée une ligne `gold_ledger` dans la même transaction.
- `active_timers` : contrainte « un seul timer de type training actif par personnage » ; les quêtes occupent le personnage de façon **exclusive** : pas de chasse, donjon ni attaque PvP pendant une quête ; entraînement et transmutation restent autorisés (décision actée 10/07/2026, voir 05).

# IAmLegionReborn
For Dying Light 2

Update 1.5c

New Chaos system implemented
This is the first phase of my new spawn system that is meant to bring random "epic moments" to the world. I want your feedback on your experiences and if this system has any immersion breaking moments. There are currently 9 new AI chaos agents added to the game that spawn randomly and then they will summon new enemies and allies to the world. This system is meant to mirror the behavior of the Valve AI Director from Left 4 Dead, and it still has a ways to go but I'm really excited about this new system. You may occasionally spot enemies spawning in near you, I'm still working on some of the code for this so stay tuned for future updates.

Volatile fixes and improvements to difficulty balancing
I have removed the always start a chase code with Volatiles, thank you for your patience, and have attempted to properly balance Volatiles in the world again for all difficulties so that you get Volatiles who start chases and ones who summon additional volatiles.

The IALR loot system is restored
1.13 has been a pain in the ass to clean up all the bugs but the Loot system is back online and working well! The Mod config will now be able to properly balance the world loot again and you should find the additional items in the world. As a reminder, you can disable the new IALR items in the Loot system and trader system in the Mod config if you don't want these items dropped.

Fixes for audio events
After the 1.13 update, the audio events have had some bugs and I've been slowly working them out. You should see some improvements though all of the bugs may not be done just yet. Please report in ⁠ialr-dl2-bug-reporting which as many details as possible so I can replicate.

Warzones Refactor
Using the new Chaos system, I have made some drastic improvements to the warzones systems. The new spawn system will allow squads or groups of enemies to spawn and band together, resulting in much larger enemy forces around the world and new enemy patrols.
Warzones now features: Bandits, Renegades, PK, PK Commandos, Colonel's Men, Colonel's Commandos, the Wolves Faction, the WorldBurner's faction, the Survivors, with the ability for packs of Volatiles, Hives, Demolishers, Goons, and Hordes to spawn into the world for the ultimate clash.

Difficulty improvements
Using the new chaos systems I have worked to rebalance Survivor, Ultimate, and Insanity to make the world feel vastly more alive and dangerous. Survivor received a few improvements while Ultimate and Insanity will now bring a great mix of chaos and rewarding moments.

Human AI overhaul
Many improvements to the AI's ability to detect and interact with the world and each other, fixes for aggression and blocking.
Launcher Updates:
Updated launcher to be able to pull the latest update prior to installing the mod for the first time. This will ensure that for all future updates and versions of the mod, you can always immediately grab the latest version before installing.

New Multiplayer/Coop tools
A large number of players have reported the Data mismatch issue when attempting to play coop, so I wrote some code into the launcher to help with that!
Head into the new "Launch Multiplayer Pack" and select the role you are trying to play with Coop: "Host, Player 2, Player 3, Player 4". So for example if you are the host then leave it on host but if you're trying to join someone set yourself to Player 2 in the Launcher.
All players and the host should press the "Generate Validation File" once you have set your role from the dropdown, which will get all of the file sizes for all the files under "Engine" and "Ph" in your Dying Light 2 directory.
Once your validation file is generated, you can press the "Create Coop Pack" button to "Bundle" the validation file and all of the extra Data .Paks in your ph/source folder to immediately send to your host or any players looking to join you. This file is located in your Dying Light 2 Root/IALR_Coop folder: "Coop_pack_date.zip"
Send this over to the other players and extract the ialr_coop folder in the Coop_pack_date.zip into your Dying Light 2 root folder. If you are hosting, you do not need to copy the ph/source folder into your DL2 root, only if you are a player to ensure the same files exist between both host and players. Once that's been done, you can press "Validate Player Files" and it will let you know which players match the host, and if any players do not match the host, it will tell you which files are different between your systems. This should help you repair or update the mod accordingly.
This should speed up the process of sending your Coop files but will also let you know if there are different mods installed or files that shouldn't be on your game compared to the host

Improved the flow for detecting the mod
This should be a lot cleaner when you launch for the first time and each time after

Checking for updates
This will only happen if you have the mod activated
Note you can easily toggle the Mod on and off by clicking the IALR Logo or then the DL2 logo

Added a DL2 Shortcut to the main menu
This should make it easier to change, modify, or get access to the IALR_Coop folder



Update 1.5b
Update to 1.13.0.0
IALR Launcher is about to be officially launched! Thanks for your feedback so far, I'm working to update the launcher based on your feedback prior to launching on the Nexus.
The IALR Halloween event is live with new Killer clowns and Vampires that can be found in the world! There are 2 tiers of vampires, you'll know them by their red eyes and speeds when attacking!
Insanity and Ultimate now feature more Volatiles, Insanity has increased their ability to spot and track you during chases.
Fix for Heavy armor skills causing movement to be poor when moving side to side or inverted with the combination of multiple heavy armor pieces.
A fix for the NG+ crash has also been released

Human AI overhaul
Many improvements to the AI's ability to detect and interact with the world and each other, fixes for aggression and blocking.

Difficulty Balancing
Started fresh on re-balancing every difficulty, your feedback is appreciated

Volatiles now always start chases/Hunt
I'm going to set this up to be a toggle in the Mod Config next update

Removal of visual effects from Biters and Infected
Feedback is always appreciated on the mod, especially if it's something that is causing players frustration

Fix for crash
Found and removed a crash due to changing the inventory size, I would not recommend adjusting this currently in the mod config. This happens every other update for whatever reason, maybe something on Techlands end

Loot system Mod config options currently disabled due to bug from 1.13.0 update
Reported issue with the noise system/Daystalker and Night stalker spawn system, not a major bug and the game should be playable until I figure out why it's broken again
Some invisible zombies may have returned

Everything appears to be stable and running well, the bugs that Techland fixed were not in the mod because they were super easy to spot o.0 they had like 4 syntax errors hidden in the official code they just fixed


Update 1.5pre
Updated to 1.12.2
Release of IALR Armorer and armor update
⦁    This first release features new custom Torsoaddon (Bracer slot) and helmet armors, complete with weight system (Light, Medium, and Heavy armor). 
⦁    1.5pre features: 240 new gold tier armors and 100 Platinum tier armors each with their own skills. 
⦁    Armor can now be purchased from the IALR Armorer which will show up with the other traders in your stash for now.
⦁    Armor has also been added randomly to the world, the Gold tier and Platinum armors have not been added to the loot system yet.
A new stat system is release that shows a quick summary of the armors skills and unique perks. Each armor has it's own stat summary
A new scaling system has been added for all armor
⦁    White armor does not scale
⦁    All Green armor scales late in the game
⦁    All Blue armor scales Mid-Late game
⦁    All Violet armor scales Mid game
⦁    All Gold tier armor scales early game
⦁    All Platinum tier armor scales early game
Release of the new Horde system into the Mod config

⦁    Make sure to check out the new tab in the "World Spawns" Section, which now features a new "Performance" tab and "Horde" Tab
⦁    The performance tab can be used to change the number of enemies that spawn on the map, their distances, and the physics used on the spawned enemies. This should help you find a new balance for all the Mod players across all the different tiers of systems running it (including steam deck)
⦁    The Horde tab will let you set how many zombies spawn in the day into the horde groups. To adjust this you need to first set the amount of spawns in performance (make sure they are somewhat relative (don't set min = 1 and max = 1100 if max spawns is 120)). You can now set a min and a max on each spawn group that spawns on the map during the day. This will let you make MASSIVE hordes on the map. If you increase the size of the horde, I would recommend increasing the density so those hordes spawn further apart.
⦁    Reduced the number of global gas tanks that spawn and can explode, these guys make hordes death traps.
⦁    I have included 2 new local configs with this release that quickly set Medium tier spawn increases and add the horde and then a High tier spawn and very large horde. You can easily merge these into your configs or merge them into the different difficulties if you want. Feel free to delete if you don't want them.
Updated the Mod Config application to support smaller text so it's easier to scale the interface for the 1080p users
Overhauled the Mine explosives to do more damage to limbs and body parts when exploding and they also do more damage to enemies


Mod Config tool released!
Modify the game how you want without having to know how to modify the .pak files.
⦁    The Mod Config tool can create custom configs (custom difficulties) that are easy to share and update. 
⦁    The Mod Config tool uses version control on it's data so in the future all your configs will be backed up and then updated when a change is detected.
⦁    The Mod config is included in the Installer and will be installed into your Dying Light 2 game root when you install IALR, a desktop shortcut will also be added (you'll need to select the Dying Light 2 root path the first time you run the Tool).
⦁    Easily save immediately inside the game files for quick testings and injection.
IALR Save Game Tool is now included with the Installer!

⦁    Quickly and easily backup your savegames for Dying Light 2.
⦁    You will need to select your Savegame location the first time you run the Tool (...STEAMDIR\userdata\YouruserID\534380\remote\out\save)
⦁    Add a tag to your vanilla games and for your modded games so you can ensure you have good backups available for when the official updates roll out.
Added new options to the Vanilla Loot section of the Mod config for setting the amounts of specific items including crafting, plants, and valuables.

Fix for Casual spawns and Volatiles, better balancing compared to Vanilla.

Reduced the number of Volatiles that spawn in Casual Survivor and Survivor at night
The goal here is not to remove Volatiles from interiors and crawling through the world, but to reduce the amount compared to the Good Night, Goodluck update for the casual players out there.
Added a new "Merge Config" button to the Mod Config Tool
This new feature will allow you to set a baseline difficulty for the merge from the drop down and then either merge with a single local config or multiple local configs to try to import as many "unique" values from your configs as possible into a config.
This should be an easy way to create a specific mod setting that you like, such as disabling lock picking or increasing weapon durability, and then being able to quickly change the difficulty of the mod and merge in this change so you can apply these settings to the mod without having to "re-create" these specific settings.
The interface will not show both being selected but if you select multiple configs in the Left and Right panel, it will try to merge both of the selected configs or individually either/or with the baseline difficulty config.
Added a new "Delete Configs" buttons
Allows you to quickly remove the selected local configs
Improved the code for upgrading your custom local config files to the latest version of the mod configs. This latest version is 1.6 and so all your configs should create backups and upgrade your config when launching the new mod config.
Please let me know if you get an error in this process in the Mod Config Console so I can improve the code for this system.
Added a Color Picker feature to the mod config to better support creating new colors inside the mod.
Click the Color Picker color box to open the color picker.
Currently this only works on the color picker but you can copy the values from the R, G, B boxes in the color picker into the values below and then once you save you can reload your data2.pak or ial_setting.mth to confirm your colors for now.
Added an increased ability for the Mod config to prevent syntax errors by forcing values to be Float (0.0), INT (1,2,3,..), String (""), and true and false values.
Based on the common errors reported so far by the community, when apply your config make sure to check the "Changed to >" values to see if you spot syntax errors, especially if you're crashing after modifying the config.
Make sure to check out the Documents/Dying Light 2/out/logs folder for the latest Crash logs if you have a crash to make sure you don't have a common "syntax" error.
Added a new Survival Sense upgrade to the Mod Config to allow you to set colors, opacity, duration, and colors to every major infected in the game
This system will allow you to properly deploy a diverse set of visuals to each group of infected and biters in the world to improve immersion and to remove the old outline system.
Make sure to check out the new "Survivor Sense" tabs for more information.
Each difficulty has been balanced to better support this new feature, the higher the difficulty, the less survivor sense capability you will have (until the 1.5 Armor release adds the new goggles and legendary gear).
Added new options for setting the UI Map, HUD, and objective icon colors in the "UI Setting" section.
This feature will allow you to create your own unique HUD and map colors that can be saved as part of your configuration in the Mod Config tool so you can easily add features or toggle the HUD as you modify the values.

Update 1.4i
- Updated to 1.12.1
- IALR Mod Config Tool is released!
⦁ Modify the game how you want without having to know how to modify the .pak files.
⦁ The Mod Config tool can create custom configs (custom difficulties) that are easy to share and update.
⦁ The Mod Config tool uses version control on it's data so in the future all your configs will be backed up and then updated when a change is detected.
⦁ The Mod config is included in the Installer and will be installed into your Dying Light 2 game root when you install IALR, a desktop shortcut will also be added (you'll need to select the Dying Light 2 root path the first time you run the Tool).
⦁ Easily save immediately inside the game files for quick testings and injection.
- IALR Save Game Tool is now included with the Installer!
⦁ Quickly and easily backup your savegames for Dying Light 2.
⦁ You will need to select your Savegame location the first time you run the Tool (...STEAMDIR\userdata\YouruserID\534380\remote\out\save)
⦁ Add a tag to your vanilla games and for your modded games so you can ensure you have good backups available for when the official updates roll out.
- Added new options to the Vanilla Loot section of the Mod config for setting the amounts of specific items including crafting, plants, and valuables.
- Fix for Casual spawns and Volatiles, better balancing compared to Vanilla.
- The IALR Syntax Debug tool has been written and helped fixed a lot of small bugs left over!
- Updated Pathways to now work with Skip Prologue
- Added more support for "clearing" areas, enemies are less likely to respawn until you run away from that area a good ways. Let me know how this affects performance.
- Updated the Density system to have better balancing for Casual and Survivor Difficulty having less zombies during the day
- Added 47 new Swamp biome zombies and infected visuals
- Added Bloater/Vomit zombies to swamp region
- Added Swamp GRE Volatile that can start a chase to the swamp biom
- Fix for Swamp Biome zombies and infected having weird texture issues after latest update
- Fix for Swamp Goons not attacking and weapons not loading
- Updated all language supports for French, German, Italian, Polish, Portuguese, and Spanish
- Special characters are still not added, please review the International Language Excel to give your feedback on ways to improve the badly translated names! I appreciate the support!
- Fix for more invisible zombies
- FIx for Volatile Tyrants not attacking and glitching
- Fix for Resting Volatiles
- Fix for Hazmat and Worldburner Virals being affected by sunlight, they are now immune
- Fix for Chargers not being immune to sunlight
- Fix for Volatiles and enemies spawning into darkzones due to noise glitch
- Fix for Screamers and enemies not called out the players location
- Fix for Safezone bugs including not being able to sleep in beds and enemies spawning within the walls. You may be forced to walk in some bases for now but I'm aware of this and looking into it.
- Fix for the Renegade bowman firing very rapidly, they should increase speed based on their level now.
- Update to Custom Map Optional, this may have fixed the reported bugs with Sofie quest and the Windmill quest, please let me know if this is not the case.

Known bugs:
-Armor visual clipping: this can't be solved for due to how the Devs setup the materials on the models =( still looking for ways to fix it with 1.5 Armor update
-Archers standing around and not attacking in a quest: Please send me a savegame for this bug if you encounter it before that quest is completed so I can fix this.




Update 1.4h
New Feature Release: Trader Item Config
- Added new feature block to the Mod Config "TRADER ITEM AMOUNT MODIFIERS"
You can now set the the number of items you can find in the world at all the traders by setting a Min and Max value on the "IAL_Trader_item" values in the mod Config. Doing so will increase the amount of items overall that you can find at the traders. If you want to decrease the amount of items found in the world you can also now reduce the "max" values for your prefered world difficulty and gameplay balancing.
- Added all IALR content to the traders
You can now purchase the content from the mod from all the traders around the world. New unique traders will be coming in the future but for now they are all randomly blended in. You can increase or reduce the amount of items that show up from the mod using the config.
- Vanilla + IALR Content mod
This version of the mod gives you the Mod Config, the new infected models (DiverseZ's), and all the new weapons and armors without the detection and AI changes. This feature will need feedback so please let me know what you run into!
- Added bows, crossbows, and flamethrowers to the traders
You can randomly find the flamethrower at traders around the world. You can find Crossbows at the PK traders, and bows at the survivors.
- Added ammo, explosives, tools, fuel, and other useful goodies to the traders
Added useful tools and ammo to the traders to help give you a reason to use that hard earned cash.
- Reduced the overall price of the mod content to help reduce price bloating from selling mod content.
- Insanity now has a better mix of Runners and Walkers based on the Mod Config. The most choas and the most fun for sure =)
- Ultimate survivor now has biters running at night (Nightwalkers) with some weak zombies moving slow as a mix. Daytime has a mix of runners and walkers. More Volatiles that are not Pack Leaders who start minichases and bring more enemies down on the player based on the Mod Config Volatiles noise system. Ultimate is now where this system is first implemented for Day time, night will use the Night_Hunter system for Survivor, Ultimate, and Insanity.
- Survivor difficulty reduced, damages reduced, better spawn tables. Reduced the number of volatiles at night, less roaming volatiles without the icon indicator (pack leaders who start the hunt). Survivor difficulty no longer uses the Day_Hunter system so new players can enjoy exploring without the chaos.
- Casual Survivor brought back from the Vanilla only version, better balancing for an easier game for those of you who enjoy the world changes and slight chaos without the intensity.
- Fix for invisible arms on female PKs from the mod
- Reduced the likehood for Volatile Camo to drop by half.
- Fix for 1 shot damages for all difficulties, fix for bow damages
- Fix for Renegade Sniper feeling, better chances of missing the player
- Fix for Biters walking with miss leg visuals, should only be crawlers now
- Better damage scaling for humans, they will do more damage with higher levels
- Fixes and improvements to the new Spawn system when running, rebalancing across all levels.
- Fix for the issue with not being able to set Runners and Walkers in the Mod Config for Ultimate and Insanity
- Fix for blob zombies
- Fix fo more invisible zombies- Fix for the issue with not being able to set the Climbers in the Mod Config for Ultimate and Insanity
- Ultimate difficulty no longer results in all biters running, there is now a better balance for a combination of walkers and runners.
- Removed running Biters from Casual Survivor
- Lowered the amount of running biters in Survivor difficulty
- Rebalancing of all spawn pools for Survivor, Ultimate, and Insanity to include more volatiles at night and more screamers. Ultimate and Insanity now have a higher chance to spawn Hives and other special infected into interiors during the day
- Insanity now has a minimum hit count for Volatiles (6), Tyrants (8), Demolishers (8), and Goons (6). Normal health should still apply here, this should only make sure that even when you are max lvl and loaded with high level gear you still have a challenge.
- Fix for Virals randomly spawning when running around the map, this was a mistake on my part and has been fixed, sorry about the bug!
- Added more demolishers, goons, volatiles to the world at day and night using sound spawn system. Make sure to check out the Mod Config Day Hunter and Night Hunter settings for your own balancing preferences.

PATREON CONTENT:
New Feature: Never work again Bundles released
- New XP Boost system
The new XP boost system allows you to select from a low tier 1 hour XP boost, 2 hour XP boost, a full 24 hour XP boost, and a perminant XP boost for your savegame (cannot be undone). This system will allow you to quickly obtain all your skills from the start of the game if you so choose.
- New Trophy Bundle, Valuable Bundles, Money Bundles, Crystal Bundles, Military Tech Bundle, Boost Bundle
I wouldn't recommend using most of these as they make the need for getting money and valuables no longer required, but they have been added if you want to enjoy! You can now spawn millions of $ if you so choose. You only need to redeem the Money options once, as you can then retrieve an infinite amount of this item from your stash.
- Fix for the Walking dead bundle not working

Update 1.4g
New Feature Release: 7 New Custom Infected
- New Banshee Stalker
A new custom AI designed to follow and track the player from the rooftops, calling out the players position and spitting at the player and other human AI. This enemy is considered an early tier Banshee meant to help make the world come to life around the player.
- Refactored Enraged crawlers - Visual damage (damaged legs)
A new custom AI with a recent update to the more basic crawlers with improved logic and visuals that have damaged or destroyed legs. Enraged biters now screamer and lash out and crawl around the world prior to spotting the player.
- Venom Enraged Crawlers
A new custom AI that are enraged crawlers but have the visuals of burnt or damaged infected enemies (screamers, banshees, bolters) that have been disabled and have a venomous bite if they grab you. The damage can be controled with the Mod Config with the same damage value as the crawlers with additional Poison damages (IAL_Biter_Leg_Chomp_DMG_Percent)
- New Biter thugs
A new custom Biter AI that contained 3 new attacks, deep growling voices, more health, and heavy attacks. Their visuals currently use the same visuals as the normal male biters.
- Enraged Spitters
An updated version of the Spitters that is less defensive and can be identified as a spitter who is screaming and attacking without the player in view. This Spitter does faster and more damage attacks than most of the spitter variants.
- Boomers/Vomit infected
A new custom AI that has the visuals of the exploding zombies but will be vomiting, their only main attack is toxic vomit and if they attack the player with the vomit it will mark the map where you are located and enemies have a chance to spawn.
- Screamer code update (Chasing screamers)
Screamers will now run towards the player and attempt to shove them, this will lead to more intense chases, as the screamers will follow the player and call out your position. They also have the chance at shoving you off a rooftop into the arms of the waiting horde. Increased the frequency for the Screamer to scream and alert your location.
- Banshee improvements
Reduced the "autoaim" chances of the Banshee leap from above.
- Update for Infected inside interiors
Improvements to interior infected to be able to search and move through the interior spaces to attack the player or raiding human AI.
- Increased the number of Screamer pools by 10 in the Mod config for when the screamer screams and alerts your position.
- Increase the number of Day Hunter pools by 10 in the Mod Config to help increase world diversity.
- Improved chances to run into the World Burner faction in the world.
- Added 10 new unique encounters to the world that include Goons, Demolishers, the new Banshee Stalker, the Enraged Spitters, Vomit Infected, Biter Thugs, Enraged Crawlers, and mixes of all the above.

Update 1.4f
- Updated to 1.11.4
- New Feature Release: Trophy Exchange
- Added a new blueprint to the Stash > Extra section for all player to redeem if you would like the ability to convert Uncommon (5) > Rare (1), Uncommon (20) > Epic (1), Rare (3) > Epic (1), Epic (1) > Rare (3), Epic (1) > Uncommon (20), Rare (1) > Uncommon (5).
- Added some festive fireworks to the Stash > Extra section for all players to enjoy the hot summer with.
- Removed some code that could potentially be causing the Outpost Redeem issue, this is still not something I can directly fix, as the mod doesn't modify that system.
- 157 new custom biter visuals added to the world
- Recreated all 863 custom biters to attempt to eliminate the invisible biters that appear after the official updates. If you find biter visuals that don't look correct make sure to report with pictures on the Discord Channel.
- Added Viral Children with a chance to spawn them into the world using the Nighthunter system.
- Added an additional 10 slots to the Night Hunter pools in the Mod Config to add additional diversity to night infected spawning.
- Added back the ability to use weapons in safezones
- Added back the spawning of gasoline containers in the world
- Added more Gasoline to the world, you are more likely to find it inside Darkzones, homes, and infected areas where humans are less likely to be commonly roaming.
- Reduced the amount of Human damage done in Survivor Difficulty
- Fix for the Female outfits glitching, you can now enable the the outfits inside the stash, don't forget to **remove your helmet and/or gloves and press "X" while in the inventory to see the change.
- Changed the PK Reinforcement icons to be a walkie talkie for Reinforcements.
- Improvements to the visuals for the new screamer variants
- Removed all custom containers from the mod that were added to the world to in order to get rid of the grey cube bug introduced with the new update...not sure why this happened but I've had to remove all custom fuel containers and other containers added to the world for now.
- Honor the Fallen event has ended. Sadly it had to be ended due to the above glitch/bug, as the reward system was based off the container logic.
- Reduced Volatile spawns on Survivor difficulty.
- Better screamer and volatile balancing for all difficulties
- Added the new "nerfed" volatiles to the Casual Survivor difficulty.
- Implemented a better ranged health system for Volatiles in Survivor, Ultimate, and Insanity. You'll need the GUI on to see their health but some may be tankier than others, this should go well with their different size scales :slight_smile: no there is not a minimum number of hits implemented in the mod for volatiles.
- Boosted the health of Volatile hives to help make them harder to take down and give them more time to call for aid.
- Fix for Human AI always dodging thrown weapons.
- Fix for Human faces disappearing from Ultimate and Insanity from a bad push for that bug.
- Fix for the "Grey cube"
- Fix for the invisible head with custom helmets
- Fixed the new Fresh Viral Women using the male animations and noises in the Mod
- Fixes for missing arms with the virals
- Fix for Shrieker tool not causing a noise event when thrown
- added 25 new visuals for virals
- Fix for redeeming the Trophy Exchange System disappearing
- Fixes to the colliders on the larger special infected to help them through doorways

Known bugs:
- Armor clipping glitch through other armor still an issue, no known fix as this is a material setting the dev's must set on specific models.
- Random glitched biter blob due to loading so many presets of zombies. Sadly the only time I don't get this happening is when reducing the number of custom infected/biters presets to the world spawn system.
- Custom Map Optional will cause windmill glitches for now for some quests, along with other random quest glitches, just remove the data5.pak if you run into a glitch with a quest you can't turn in or floating NPCs.


Update 1.4e
Updated to 1.11.1c
- Added a supporting feature that when reinforcements are called during the day, more are likely to show up than at night.
- The same is true for infected, Virals, Banshees, Demolishers, and Chargers are more likely to show up in the day, while all the above and more will show up during night.
- Added improved noise detection for all the specitial infected when loud noises are caused for both the day and night, night being a more brutal response.
- Screamers will still be present in IALR, I see no reason to swap them out for Volatiles, as Volatile patrollers were already a thing in the mod.
- Make sure to check out the New Chase System and Howlers in the 1.4 release notes if you don't know why Screamers aren't immediately causing chases.
- Increased Volatile spawns at night to match density of new update.
- Bug fix for human damage, now increased with each mod difficulty and by enemy level
- Bug fix for infected spawns
- Reduced glowstick and flare loot chance for zombies
- Fix for Virals with missing arms
- Volatiles that start chases will have the GUI indicator over their heads, they will begin the "Hunt". All other Volatiles will begin Mini chases where they summon random packs of Volatiles when the scream.
    - Added a new VOLATILE Spawn list under "SPAWN LOGIC" in the mod config where you can choose what enemies Volatiles have a chance of spawning.

Update 1.4d
New feature release: Throwing Weapons
- Small and Large Throwing Stones: added that can be used for distractions or for crushing the skulls of your enemies. Great for luring large groups together and then picking off your enemies.
- 6 New Throwing Hammers added - 3 tiers each:
- Ball-Pin Hammer, Pick-End Hammer, Wrench Hammer, Meat Tenderizer, Welded Butt-End Hammer, Double-Sided Industrial Hammer added to the traders and enemies of the world.
- 9 New Throwing Axes added - 3 tiers each:
- Scavenger's Hatchet, Mountaineer's Hatchet, Valhalla's Horn Axe, Utility Tri-Axe, Veteran Firefighter's Hatchet, Butcher's Retort Hatchet, Tactical Broadblade Axe, Metal Marauder Cleaver, Fireman's Savior Axe added to the traders and enemies of the world.
- 3 New Heavy Throwing Axes added - 3 tiers each:
Barbaric Pipe Axe, Barricade Breaker Axe, Zombie Reaper Axe added to the traders and enemies of the world.
- You can equip all throwing weapons in your equipment the same as throwing knives, your primary weapon will be traded out for the throwing weapon until you release the equipment button.
- Each tier increases the attributes for each type of weapon and can randomly found in the world for now, rather than using crafting, stay tuned for more and please give your feedback.
- Added an optional to disable them in the MOD CONFIG, set = 0 to disable: IAL_Loot_AI_Throwing_Min_Amount_0, IAL_Loot_AI_Throwing_Max_Amount_3

New feature release: New Flares and Glowsticks added to the game
- 2 New Glowsticks added:
- Blue and Green, glowsticks have been added to the world and traders, use these to light paths through the dark and provide leave behind visual indicators of pathways and darkzones.
- 4 New Signal Flares added:
- Red, Blue, Green, and White flares have been added to the world and traders, use these to light paths through the dark and provide leave behind visual indicators of pathways and darkzones.
- Added an optional to disable them in the MOD CONFIG, set = 0 to disable: IAL_Loot_AI_Lighting_Min_Amount_1, IAL_Loot_AI_Lighting_Max_Amount_3

New feature release: New Weapon Mods
- 6 New Weapon Shaft Reinforcement mods added:
Leather Binding, Fiber Wrap, Resin Infusion, Rubber Coating, Metal Core, Steel Reinforcement added to the game to improve your weapons using world crafting items. This currently doesn't include visual indicators.
- Improvements to Patreon Content and naming/icon systems


Update 1.4c
New feature release: Honor the Fallen Update
- The Honor the Fallen mod event/update brings 22 new military infected and 36 new Colonels to the wasteland. This update is meant to bring the Colonels back to the wasteland with Colonel Patrols and various Colonel spawns around the wasteland. Undead Military biters and Undead Gasmask military biters have been added to the world as well to create diversity but also add a new reward system.
New feature release: Honor the Fallen Reward system
- A new reward system has been created so players can turn in the dogtags of the fallen military members found around the world for "Care Packages" that come in 4 tiers.
- Wooden Care Package, Metal Care Package, Military Care Package, Legendary Care Package have been added to the world and their crafting recipe can be purchased by the new Military Trader that can be summoned from the stash. The Military Trader will fight nearby enemies and continue to look for fellow Colonels after you are done shopping. These items summon a box to your feet when thrown that will give you a random selection of vanilla rewards and the new custom weapons, armor, items, ammo, and valuables.
New feature release: New Colonel Companion
- Added another companion to your stash that allows you to summon the new Colonel militia and Gasmask militia to your side.
New feature release: IALR Custom Biters, Infected, Special Infected visual overhaul
- Over 800+ models were updated with improved visuals. Biters appearances now appear worn and dirty. Virals and special infected will be a mix of blood covered and dirty. The Volatile Venom variant will no longer have the jet black with Red crest, instead they are black scorched and bloody with glowing red eyes.
New feature release: Warzones Optional
- The city has been called to war and all human factions will now be fighting it out on the streets. This is not meant to be Lore friendly, this is meant to be a fun new way to engage with the map and try to stay alive. Ultimate and Insanity have weapon drops for humans turned on by default so heads up, there will be a lot of weapons hitting the deck (you can disable in the mod config). This only applies to daytime, and your place in the game. If you are playing from the start you won't see as many enemies in the first city. When you reach the city you should start to see more Human enemy types. NG+ will have the most Human enemies so heads up.
- Added ability for crawlers to be affected by UV bars and Sun
- Reduced the Damage and added new damage value to MOD CONFIG to set "Biter_Leg_Chomp" damage.
- Crawlers do less damage when they grab you but they will take a chunk out of you and make you bleed for a short time, careful of the tall grass.
- Reduced overall number of PlagueBearers in Warzones Optional
- Disabled the new Noise and Chase systems in Casual Survivor, the goal of Casual Survivor is to provide the new content and Mod Config options without all of the new difficulty systems to keep the game closer to vanilla for certain players who have a specific vanilla playstyle but want more content.
- Added merge support for Stash system for easy merge
- Improvements to interior infected to make them less likely to flood interiors
- Removed Special infected Volatiles, Tyrants, Goons, Chargers, and custom infected from spawning in interiors on Casual Survivor.
- Fix for Survivor Sense on Casual Difficulty
- Fix for Dynamic Music not working
- Fix for PK Reinforcements using PK Dog tags instead of Fallen Hero dog tags
- Fix for GRE Anomalies jumping out of arenas
- Fix for 7 Invisible Virals
- Fix for Stash system possible causing issues with Pilgrim Outpost
- Various improvements to the installer to make things easier to select and follow the descriptions

Update 1.4b
New feature release: Initial Damage/Initial Enemy Health
- A new variation system has been added to where every enemy will now receive health based on a range rather than a set number. This will allow the enemies of the world to have some initial damage applied to them but also give them more or less health overall. This system is paired with the visuals of the creatures to help provide an immersive experience with each enemy.
New feature release: Randomized/Ranged Damage system
- This new feature has been added to help create unique fights against your enemies and damage dealt to the player. With each hit, a random damage amount is applied from a range created for each tier and difficulty of enemy. This should help create unique strikes against enemies that create unique combat experiences when taking on the wasteland.
Mod Config Overhaul
- The mod config has been re-released with new features and new documentation.
- The start of the mod config now has a breakdown that pairs with the Mod Manual to provide more information about systems in the Mod Config and they are now sorted by category. The list is very long and I won't add it to the changelog to help keep things clean.
New Mod Config feature released: Economy Settings
- Added the ability to set the world item values based on their category. The overall world prices have been reduced for Survivor, Ultimate, and Insanity. A balancing has been applied to the categories to help create more economic need for resources and buying and selling items. Let me know your thoughts on this balancing! Feel free to set these values yourself and let me know what you prefer.
New Mod Config feature released: Difficulty Settings
- Added a new section in the config that allows the players to quickly modify the overall damage resistance, buffs, Daytime and Nighttime damage, and Singleplayer, and new Coop settings to better balance the game to your playstyle within the config.
New Mod Config feature released: Loot Settings
- Added 9 new sections in the Mod config for setting the Loot values, including setting Trophy drops, cash, items dropped by enemies, and valuables.
New Mod Config feature released: Disable MOD custom loot
- Added the ability to turn off the Mod Content by category if you prefer to play without it. Check out the new "LOOT SYSTEM" in the Mod Config and the "IALR" section, you can set the MAX number of items to 0 to turn off the chance for those items to drop in the world. You can now disable overall Mod items, Alcohol, Camouflage, and the custom IALR armors.
New Mod Config feature released: Weapon Physics Settings
- Added a section for setting the Physics applied to specific weapon types. These have been set for the mod but feel free to change them to blast your enemies around the map.
New Mod Config feature released: Weapon Durability
- Added additional Features to set the weapon overall durability by the color of the weapon.
New Mod Config feature released: Arrows/Bolts attaching to Objects
- Added the ability to set the chance for arrows/Bolts attaching to objects to the Mod Config
- Restored alot of the prefabs removed on an earlier update after confirming they are working as expected.
- Increased the Item stacks to 999 and added the ability to set the stacks in the config under 2. Inventory and Economy
- Fix for Infected Bandit models showing up as invisible. 
- Decreased the chance of finding the generic Urban Armors
- Increased the chance to encounter Companions in the world for all difficulties

Update 1.4
- Updated to support 1.10.3c
New feature release: Insanity Difficulty
- A new difficulty has been added to the mod that will bring new levels of challenges utilizing all of the below systems. This version of the mod is meant for the players that want to see all the new enemies added by the mod while also receiving a constant stream of enemy attackers while running. You can set your Walk Toggle in the games settings to avoid awakening the Infected and Daytime hunters. You can get more loot by default while using this version of the mod and there is a greater mix of Walkers vs. Runners found in this version for balancing. Ultimate Survivor still contains the most climbers and runners but with better balancing for the experienced player looking to play Ultimate Survivor through the main quests. Please let me know if you manage to beat the compaign with Insanity difficulty, it can absolutely be done, just not highly recommended for new comers. IALR Veterans recommended.

New Gameplay balancing: Casual Survivor
- Thank you for your continued feedback on Casual Survivor. This version of the mod has been re-balanced to focus on providing all of the new features without the difficulty. Please continue to give feedback on this version as it is meant to allow everyone to enjoy the mod without all of the difficulty features.

New feature release: Camouflage
- Camouflage: You can now find various substances on the different infected of the world that will allow you to musk your scent and move through the city without being detected. You can run with camouflage but it will go away faster, walking is your best option! (Setting in Options to toggle). You cannot attack with weapons or throw things without being detected, but takedowns will work in most cases. This new phase of the mod moves into "Harvesting" the parts of the undead to turn into tools for survival
-     Volatile Putrid Potion, Volatile Tyrant Putrid Essence, Demolisher Putrid Disguise, Viral Putrid Vapor, Goon Putrid Grime, Banshee Putrid Perfume, Charger Putrid Paste, Drowner Putrid Decoction, Scortched Howler Putrid Smoke, Weakened Howler Putrid Miasma, Howler Putrid Haze, Bomber Putrid Brew, Biter Putrid Blend, Bolter Putrid Balm, Spitter Putrid Slime, GRE Anomaly Putrid Elixir 

New feature release: New Chase System and Howlers
- Howlers and Chase System: There are now 3 different types of Howlers: Scortched Howlers, Weak Howlers, and the Howler in the world and a new GRE Volatile. Howlers now gather all the nearby infected to their position to form a moving horde on the map. When the Howlers spots the player, they will target the player instead and send the horde to your position. When the Howlers scream they no longer immediately start a chase, rather they call to all nearby infected to come to their aid. The infected summoned by their scream can be set inside the Mod Config. On Ultimate Survivor and Insanity the icon is turned off for the screamers in the Mod Config, so you'll need to rely on the sound indicators on your screen to know when you are getting near a screamer.
-     The Scorched Howlers are burnt out husks of screamers that roam Old Villador. These screamers can taken down with a stealth takedown. This form of the screamer puts out a weaker sound than the Screamer so less infected will gather around it. These screamers also do not glow in the dark so be careful running through the dark.

-     The Weak Howlers are a smaller form of the Howler that are able to nearby Screamers . These screamers can taken down with a stealth takedown.

-     The Howler now puts out a loud sound that will gather all nearby infected to it's position. 

-     The GRE Anomaly Volatiles now has a chance to spawn when the Howler Screams. If one arrives and spots the player, they can start a chase which will start the standard chase system but will also spawn a new list of Infected that can be set inside the Mod Config.

-     Volatiles now have the chance of summoning packs of Volatiles when they begin pursuing you. (Disabled on Casual Survivor)
To Remove: If you want the original Chase system started by the Howlers, you only need to open the mod Data2.pak and navigate to AI/modulepresets/ and delete "module_Screamer.scr". This will allow Howlers to start a Chase when Screaming.

New feature release: New Day and Night Random Spawn system
- The new Spawn System utilizes the Mod Config to spawn pools of up to 10 enemies/allies during the day or night. This system uses the sound generated by the player when you run. Each difficulty has been balanced to randomly cause enemies to spawn to the players location after a period of time. This is where the new Camouflage system can really come in handy, so the more you gather during the day the better you can survive the night.
Casual Survivor: 
-     Day - Every 3 minutes while running, 
-     Night - Every 2 minutes and 5 seconds while running. 
- The spawn list is comprised of mainly Biters and Virals with occasionally the new Volatile DayStalker during the day. At night the spawn list is mainly comprised of Biters, Virals, and the occational Howler and Volatile.
Survivor: 
-     Day - Every 1 minute and 30 seconds while running, 
-     Night - Every 1 minutes and 5 seconds while running. 
- The spawn list is comprised of mainly Biters and Virals with occasionally the new Volatile DayStalker during the day. At night the spawn list is mainly comprised of Biters, Virals, and the occational Howler and Volatile.
Ultimate Survivor: 
-     Day - Every 1 minute and 30 seconds while running, 
-     Night - Every 45 seconds while running. 
- The spawn list is comprised of mainly Biters, Virals, Demolishers, Goons,  and a few of the new Volatile DayStalkers during the day. At night the spawn list is mainly comprised of Virals and Special Infected.
Insanity: 
-     Day - Every 20 seconds while running, 
-     Night - Every 15 seconds while running. 
- The spawn list is comprised of mainly Virals, Demolishers, Goons, a few of the new Volatile DayStalkers, and the occational Renegade Summoner during the day. At night the spawn list is mainly comprised of Virals, Special Infected, the new Chemical Volatiles, and the occasional new GRE Anomaly Volatile.
- To Remove: Simply set each of the "SpawnType" field to "" without a name in the "SPAWN LOGIC"section of the Mod Config. This will remove the spawning of enemies based on your running. 
New feature release: World Diversity
- The new world diversity system drives forward new interactions as you travel around the open world. You are more likely to run into the new factions The WorldBurners, The Wolves, The PK Commandos, and The Plague Bearers (The original Renegades have been restored to Hag Mounds). 
New Enemies Released: Viral WorldBurners
- The Viral WorldBurners can be found around the world and provide the additional chance to find Flamethrowers and Fuel.
- New Enemies Released: Hazmat Virals
- The Hazmat Virals can now spawn into the world and will contain Hazmat supplies along with the occational purging flamethrower fuel.

New feature release: Companions
New Companions released: 

- Brecken and Rahim can now be summoned or found in the world to aid the player on their journey. Both use Melee weapons.
- Randomly you can now run into fellow travelers armored with the same player armor you have been wearing since the start of the game. These fellow travelers will randomly come to your aid. There is a mix of 18 new companions, with 9 using Melee weapons and 9 using bows.
- 2 new PK Commando companions can be randomly found when traveling near PK bases. While they have their own agendas, they are happy to assess your skills and learn a Pilgrims technique as long as you watch their back.
- The Companions can now be found while traveling around the world and will randomly be found assisting other groups. Most Companions are more likely to spawn closer to their faction side or bases.

New feature release: More dead bodies and XP
- Dead infected and humans alike should remain on the ground for longer. You can also now receive more XP for assisting with kills and you may receive a small amount of XP for continuing to damage the dead.

- Fix for a damage bug with the Swiftshot bows
- Fix for a glitch with the Bowmen attacking and stuttering.
- Fix for the NPCs being able to attack enemies. This code has been updated to where Human NPCs should advance on the zombies and shove them to the ground before attacking. 
- Various other bug fixes and balancing added based on your feedback! 
Sorry for the long changelog, took over 2 hours to write all the details and as always it's probably missing several things. I hope you enjoy this new update, it really does make the world feel very different


Update 1.3h
Updated to support 1.10.2c
- New feature release: Pathways
- Pathways: Added 4 new optionals to the installer (Data6.pak) that allows you to select a starter kit when starting a new game.

Keeper of the Peace
- Peacekeeper Armor Set
- Peacekeeper 1 Handed Axe
- Weak Sharpshooter Crossbow and bolts, 
- 15 tier 1 UV flares, 
- 10 Blue Glowsticks, 
- 2 Clean Bandages,
- 6 Tiers of Crafting PeaceKeeper Reinforcements Recipes
- 1 Tier 1 Peacekeeper Reinforcements

Road Warrior
- Mixed Renegade and Bandit Armor Set
- Renegade 1 Handed Blade,
- Renegade 2 Handed Axe,
- 5 tier 1 Molotovs, 
- 2 Basic Bandages,
- Rage and Damage potions,

The Veteran
- Tier 1 Military Armor Set
- 1 Handed Club,
- Renegade 2 Handed Axe,
- 5 tier 1 Molotovs, 
- 2 Basic Bandages,

The DoomsDay Prepper
- This version is for those of you who want to get to the good stuff already
- Unlocks all skills from the start of the game
- 6 starting weapons including a Bow and Crossbow
- A custom paraglider that can be equiped to boost your current paraglider
- $5000 starting cash, several potions, crafting items, grenades and other explosives, and crafting mods.

The Apex Predator (Patreon Only)
- Full Legendary Tier Skinner Tyrant Armor Set
- Includes 5 Legendary weapons, along with a new Legendary Crossbow and Bow
- A Legendary Tier custom paraglider that can be equiped to boost your current paraglider
- $25000 starting cash, several potions, crafting items, grenades and other explosives, and crafting mods.

- Updated the core mod to have new items when starting a fresh game. Now you will start with: a Starter bow and arrows, Random craft loot, 2 tier 1 UV flares, 2 tier 1 Molotovs, 10 green glowsticks, and 2 Clean Bandages
- (MOD CONFIG Update) Added a Global Condition multiplier to all weapons in the game "IAL_Weapon_Durability_Global_Multiplier". Increase this over "1" as a whole number only to increase the worlds weapon conditions, IE: 2,3,4,5,etc.. (Don't use Float values 1.0).
- (MOD CONFIG Update) Replaced the Dismemberment System with the newer Damage System. This feature isn't completed but an early start on modifying the new damage system. Currently features modifying the damage to humans.
- (MOD CONFIG Update) Added a Trading System to the Mod config and removed the difficulty differences with the traders so you should be able to sell your items when playing on higher difficulty. Use the config to balance how you want!
- (MOD CONFIG Update) Added a Lockpick System to the Mod config so you can now apply any changes you would like within the mod such as making it easier to pick locks or breaking locks.
- (MOD CONFIG Update) Added a Loot System to the Mod config so you can now increase the amount of loot gathered in the world.
- Fix for Prologue quest bug when using Pathways
- Fix for Bows being broken on the 1.3h release
- Fix for Infected spawns inside Interiors and at night
- Added a crafting option for a new Basic Bow recipe for creating new weak bows
- Fix for the Prologue Zombies not running in Ultimate Survivor
- Fix for excess crafting items showing up in the crafting list.
- Fix for some of the clipping when using Custom armor! More coming soon.
- Fix for electrical damage not matching Vanilla
- Boosted the healing ability of the medkits

[size=4]Update 1.3g
- Updated to support 1.10.2e
- Over 800+ custom models updated with the new damage system
- Infected and special infected custom models updated to work with the custom damage system
- Updated the traders to now have a chance to sell the bows and crossbows around the world.
- Bug fix for the lootable cubes in the world
- Bug fix for volatile arms update
- Bug fix for empty inventory
[size=4]
Update 1.3f
- RUN FILE VERIFICATION AND REINSTALL THE MOD. If you run Steam file verification you only need to run the installer again, don't use the Uninstaller for this. Added better stability support for the core mod by removing all custom map content to the optional. This should help prevent glitches and issues on the map with objects and quests. If you want the more experiemental map content you can install the optional, but this should help ensure stability for everyone and rule out some bugs. If you're experiencing bugs on the map, you can run file verification and remove the custom Maps Data5.pak and it will probably fix the issue. If it doesn't? Then it's maybe a vanilla bug or will need more time to research.
- Over 800+ custom models updated with the new damage system
- Infected and special infected custom models updated to work with the custom damage system
- Updated the traders to now have a chance to sell the bows and crossbows around the world.
- Bug fixes for multiple crashes caused by updating the PK infected and NPCs, not sure why yet but I have repaired the files.
- Bug fix for the lootable cubes in the world
- Bug fix for volatile arms update
- Bug fix for empty inventory


[size=4]Update 1.3e
Currently with the Easter Event, the new loot system is affected by the event and some of the world spawns. To get the full mod experience make sure to play with Steam in Offline mod.
- 63 new custom Bows added to the world!  3 new playstyles of bows:
- 23 Swiftshot Bows, 4 Legendary SwiftShot Bows (Relentless Storm, Ruins Whisper, Unyielding Tempest, Apocalypse's Fury) - Designed for rapid arrow firing. It sacrifices some power for a quicker draw time, enabling archers to rapidly loose arrows and maintain consistent pressure on their foes. Ideal for those who prefer a fast-paced combat style. Benefits: Faster bullet speed and shorter charge time. Weaknesses: Lower stamina damage and headshot damage multiplier.
- 23 Powerdraw Bows, 4 Legendary SwiftShot Bows (Piercing Wind, Reckonings Might, Far-Reaching Gale, Devastation's Grasp) - Engineered to deliver devastating blows at the cost of a slower draw time. This bow rewards patient archers with increased damage, particularly when landing headshots. Perfect for those who prioritize accuracy and damage over speed. Benefits: Higher stamina damage and headshot damage multiplier. Weaknesses: Slower bullet speed and longer charge time.
- 9 Balanced Bows - strikes a harmonious balance between power and speed. Suitable for archers who want a reliable weapon capable of adapting to various combat situations. A solid choice for beginners and experienced archers alike. Benefits: Balanced performance in terms of speed, stamina damage, and charge time. No specific strengths compared to other Bow variations
Each bow has a Condition that is either Weak, Used, or New/Legendary, this effect the overall condition and quality of the weapon. Legendary weapons have unlimited condition and cannot break.
- 42 new custom Crossbows added to the world!  3 new playstyles of crossbows:
- 10 IronClad Crossbows, 2 Legendary IronClad Crossbows (Ironclad Annihilator, Titanium Piercer) - These sturdy crossbows are made of high-quality iron, providing superior durability and strength. Their unique characteristics include a reinforced stock that reduces recoil and allows for more accurate shots.
- 10 Marksman Crossbows, 2 Legendary Marksman Crossbows (Deadshot, Hawks Eye) - The Marksman Crossbows lives up to their name with their precise aim and deadly accuracy. Their unique characteristics include a custom-designed sight that enables the wielder to make accurate shots from long distances.
- 10 Rapidfire Crossbows, 2 Legendary Marksman Crossbows (Thunderbolt, Vulcan Fury) - The Marksman Crossbows lives up to their name with their precise aim and deadly accuracy. Their unique characteristics include a custom-designed sight that enables the wielder to make accurate shots from long distances.
- 6 new custom PK standard issue crossbows (Damaged Basic PK Crossbow, Standard PK Crossbow, Reinforced PK Crossbow, Automatic PK Crossbow, Automatic PK Crossbow Prototype B, PK Assassin Class Crossbow) - Each Crossbow can be found in the world on fallen PK soldiers and Military camps, Darkzones
- Added new Broken Arrow shafts that can be looted around the world. These can be used to craft "Makeshift Arrows" in the crafting section.
- New Optional in the Installer (DATA5) for Bazaar Map update! This includes 5 new traders found in the Bazaar, New wall defenses and Guards/Guard towers, Cleaned up and improved Player sleep area.
- Loot overhaul allowing 46 new  custom containers to be looted around the world.
- Fixes for Damages done by the Flamethrowers.
- Fixes for the basic Arrow crafting

Update 1.3d
- Created a basic crossbow bolt recipe that can be received on a new game crossbow bundle or from traders for everyone else. This creates a new way to provide ammo for your new crossbow. Broken crossbow bolts can now be found in the world and used for crafting new bolts with the recipe.
- Name and description overhaul for all items in the game, it's time we got a bit more immersive before the upcoming Armor and Loot overhaul release. This includes every item for IALR, with improvements to the capitalization system. These have not been translated yet but coming soon!
- New icons and descriptions for the companions
- Fix for Armor perks and classes, specifically for PK armor (Tank) leather (Healer)
- Removed alternative costs from several of the items, as the balancing was way off.
- Fix for flamethrower upgrade causing issues, now you can find the craft recipe for the flamethrower in the world and at traders
- Fix for spawn issue for Zombies on the first map, please continue to report this glitch with the Region code found on the map in the install zip.
- Fix for external and interior spawn bug
- Overhaul to the Navmesh agents (AI pathing) to improve movement around the world by faction and creature type. There should no longer be humans super-jumping to building rooftops, but rather pathing properly between connecting buildings and ledges.
- Fix for Zombie appearance bugs, female zombie with human face, zombie with missing legs.
- Fix for Urban Outfit names
- Removed food items for now, survival optional coming soon!

Update 1.3c
- Updated and finalized a large amount of the lower case custom items, they should all now properly show with proper capitalization!
- Added optional Languages to the installer for: French, German, Italian, Polish, Portuguese, and Spanish. (WIP) Sadly the custom characters aren't working yet but I hope this helps a bit in the meantime!
- Improvements to Human AI and their abilities across the different groups.
- Improved AI detection for Survivors, Colonels, and PlagueBearers
- Created custom profiles for the Opera DLC top help reduce enemies from retreating
- Potential fixe for Zombie female with human like face
- Disabled dismember to human arms by default until I can get the retreat and bleed out code working properly
- Attempted to fix paraglider skills messing up default skills

Update 1.3b
- Added support for latest hotfix 1.9.3p
- Added 6 new crossbows to the world: Weak Basic Crossbow (Part of the Starter bundle in the Stash), Basic Crossbow, Reinforced Crossbow, Automatic Crossbow, Automatic Crossbow Prototype B (New model), and the Assassin Crossbow.
- Patreon supporters will get immediate access to the Crossbow bundles, only Ultimate get access to Prototype B and Assassin Crossbow with unlimited ammo.
- Make sure to upgrade your Weak Basic Crossbow before it breaks!
- Improved Companions, detection and fighting
- Fix for "Loyal Wolf Companion"
- Added "Restore Paraglider" potions to the stash, if your savegame has the paraglider glitch you can use the potion to restore to the tier you were previously, sorry for the bug!
- Fix for Paragliders using a new skillset so its less likely to get confused with vanilla skillsets, added an additional restore feature that should fix the paraglider on specific savegames. I noticed that the icon stays disabled but the paraglider itself works!
- Added unique factions for relationships in the open world for the companions, Wolves, and Worldburners
- Companions will now attack Renegades and other hostile groups. Wolves Faction are hostile towards most groups, and the World Burners hate everything and everyone (angst).
- Added the chance to find Ranged weapons, arrows, crossbows, and bolts on the fallen PK (crossbows/bolts), survivors (bows/arrows), and Renegades (mix)
- Restore for repair broken flamethrower craft recipe
- Increased higher tier biter health slightly
- Increased the ability to encounter The World Burner faction and The Wolves Faction in the world
- Increased the spawn chance for the custom Hazmat Virals
- Fix for Cutscene bug, thanks for reporting on the discord
- Reduced spawn frequency for lower tiered custom armor
- Increased the chance of running into The Wolves and Worldburners factions
- Improved Polish translation for Main menu
- Potential fix for PK Aggression
- Fix for Lower case items in inventory! Huge shoutout to pittbull3r666 on the Nexus for helping me get this working.
- Some improved naming and identifiers for armors and weapons
- Slightly increased the Inventory size for Accessories, Consumables, and Stash.
- Improved consumable descriptions, thank you discord community!


Update 1.3a
- Updated to support 1.9.2p
- Two new companions added to the stash: Survivor Bowmen and Survivor Melee Fighter. Both are set to a lower cooldown than Crane
- Added the ability to find a "Wolf" companion when fighting and killing the Wolf Faction.
- Fix for a health bug for the biters making them overly spongy.

Update 1.3
- Updated to support 1.9.0p
- 7 New Legendary Companions join the world: Aitor, Barney, Crane, Frank, Hakon, Lawn, and Spike
- As a thank you for your support for the mod, Companion Kyle Crane has been added to everyone's Stash on a cooldown.
- The Wolves Faction can be found in the world through encounters (Rais's men)
- The World Burners factions can be found in the world through encounters (Flamethrower loot).
- PK Shield Bearers join the world
- Balancing for the PK Engineers, now can be found with different tiers of gear and can place different tiers of UV lights in the world. (Base building loot).
- PK Bowmen now throw UV Flares as well.
- Added a playable Crane outfit that allows you to wear armor and play as Crane both First person and third.
- Additional improvements to the DLC Opera humanAI content.
- Bowmen now move and fire instead of standing around waiting to die.
- Survivor Bowmen return from a bug causing their bows not to spawn
- Expanded the crafting menu to better show all new loot and crafting materials.
- Made ALL armor and weapons able to be dropped.
- Made the shop easier to get all random custom items, instead of mainly PK as before.
- Fixed the additional crash issue by removing all Inventory settings from the Config, this was causing a savegame crash.
- Known bugs:
- PK Random Aggression is still a thing, was able to make it happen even without the mod so still potentially a vanilla bug only seen more in the mod.
- Event: Due to the current event "1.9.0P", custom loot, spawns, and a few other systems may be buggy or not working while playing online. The easiest way to confirm or test this is to go offline on steam and launch the game.

Update 1.2i:
- Updated to support 1.9.0p
- Massive changes to the Main Menu approach, this reduces the mod by 160mbs. This was only essential to make sure people didn't mess up their savegames with the mod version not matching the vanilla game version. Please use the new banner to check compatibility.
- A lot of fixes for the Human AI and tweaking to help make combat against between Humans and Biters feel more natural based on difficulty.
- Glider has been restored by default, the custom gliders will only boost the current default glider when worn
- PK Engineers join the world and will travel with PK patrols to establish Tier 2 UV lights along their path. These can come in handy at night and will stick around until you close out the game. (May not sync on Coop).
- 5 new tiers of UV lights have been added to the IALR Trader
- 5 new summon-able Companions have been added to the IALR Trader
- Fix for running in shallow water bug
- Fully Restored Glider back to default for now
- Reduced number of PK in patrols
- Fix for weather effects being outdated with update
- Added NPC water avoidance (seeing how it insta-deaths AI, can't seem to turn that off still).
- Minor fixes for possible causes of 1.9.0 savegame brick with new Community Update2, still not sure what's causing the issue but hoping this helps with minor bugs.
⦁ Known bug: PK random aggression is still an issue, wasn't able to fix it in time with this hotfix, needs more work.
⦁ Anniversary event: Currently the event is disabling Spawns, Custom Loot, and the Player_Variables.scr which impacts a good amount of the config. If you see a "P" at the end of the game version, know that event may cause the mod not be fully working or have strange bugs. To test you can switch Steam to "Offline" mod and play the mod without the current event for the full experience.
- Fixes for some of the Biter Scaling
- Minor QOL fixes added based on feedback

Update 1.2H:
- Added the ability to summon the new Custom IALR trader on a cooldown to everyones stash (extras to redeem).
- This will give you access to base building content as well as all new custom content but at a limited and random compacity for now.
- I'm working at getting more custom traders into the world itself, ran out of time for this update.
- Restricted the "Push" attack from human AI to now be targeted against infected and zombies specifically and less the player. This will help keep them alive vs. the infected. Yay realism.
- Fix for Armor having WAY too many perks on each custom piece. Warning some of you may drop stats pretty severely. More balancing coming soon.
- Minor QOL fixes.Update 1.2g:



IAL_SETTINGS CONFIG UPDATE
- A complete overhaul to the Config! This should make it easier to follow and find things, along with better documentation and formatting. Sorry to everyone who has a config already 😦
- Updated the interiors amounts to better balance out daytime play with the mod for Survivor and Ultimate

- World Burners Content is available! Thank you everyone for your support of IALR, I hope this brightens your play.
- 4 new FlameThrowers enter the world. Everyone will receive the starter flamethrower (For now) in their stash. This comes with a blueprint on how to repair and upgrade each version of the flamethrower!
- Broken Flamethrower -You can tell your flames just aren't that powerful yet - This is the starter flamethrower and it does work but chokes out, you'll need to upgrade it for more fun.
- Damaged Flamethrower - Now we're starting to cook - This is the next tier for the flamethrower, you're able to shoot much further and without as much "jerk" to your shots. Your fuel also does more damage. This one can sometimes spit flames out to the side, you may set your allies on fire...RUN!
- Flamethrower - We're finally burnin' - This is the next standard tier for the flamethrower, use this to help purge the world of the infected, and humans if you so choose, but be warned, this one can sometimes spit out to the side so be careful.
- Perfected Flamethrower - Break out the BBQ - This is the best tier for the flamethrower, this one does the most damage, has some great visuals, and does solid damage to your enemies with less drift fire.
- World Burner Flamethrower - Burn Baby Burn - This is the Legendary tier for the flamethrower, this one does the ultimate damage, has the best flame visuals, and lights everything in sight on fire. This one is currently only available to Patreon supporters until I can find a way to bring it into the world.
- Flamethrower Ammo/Fuel - You'll recieve two types of craftable fuel in the Starter Flamethrower Bundle in your Stash. One uses "Accelerants" and takes more of it to make less Flamethrower fuel. The other uses "Gasoline" and makes a good amount of fuel. This is more likely to now be found on Gas Tank Biters and Gas Tank Virals (NEW). Ammo can also be found in the world in hand picked locations and traders.
- Fuel Bomb - This is a gasoline based grenade and it will light your hair on fire so stand back. This one does a lot of damage is best for blocking off large paths for the enemy infected. This requires Gasoline to make and the blueprint can be found at Traders around the world
- Fire Bomb - This is a accelerant based grenade and it will light up a good area with deadly flames. This one does a lot of burning damage but less than the Fuel Bomb and is best for blocking off large paths for the enemy infected. This requires accelerant to make and the blueprint can be found at Traders around the world
- Gasoline can now be found in the world. There is a chance to find empty gas containers and ones with some gas still inside! Later these will become part of the ongoing IALR story efforts but for now it is only used for crafting "Full Tank of Gas" which can be sold as a valuable, used for crafting Fuel Bombs, or turned into Fuel for your Flamethrower. Gasoline can also be found in the world in hand picked locations.
- Accelerant can also now be found in the world and is a weaker form of crafting material for making Fire Bombs and Fuel for your flamethrower. Accelerant can also be found in the world in hand picked locations.
- A Full Tank of Gas is a craftable valueable and it's blueprint can be found at local traders.

- Features:
- Viral Gas Tanks have now entered the world. They don't explode, because you need at precious Fuel they carry.
- Fixed the blob zombie...I found him and killed him.
- Fix for the rest of the invisible zombies (god I hope).
- Fix for Swamp Biters showing up in Old Villador (AIPresetPool_IALR.scr)

- PATREON UPDATE:
- Patreon supporters now get immediate access to all World Burner content, Thank you for your support!
- Fix for Safezones and Basebuilder content not working after the last update.
- Mobile Safezones now should keep enemies from respawning, so you can setup temporary bases for now and clear the city!
- Ultimate Patreons will get all content along with Unlimited ammo (practically) for all flamethrowers. Ultimate Patreons will also get access to additional content such as the new EasterEgg bundles, which include lots of Techland hidden secrets.
- Survivor Patreons will get access to all content
- Casual Patreons will now get access to all non-legendary content.

Update 1.2f:
IAL_SETTINGS CONFIG UPDATE
- Updated the damage for falling zombies by type
- Additionally, most of the IALR code is going exclusive with it's own version of scripts so there is less crossover for mod compatibility. This means you'll need to refer to the top of each script to see if that script is referencing IALR scripts. I'll have more details coming soon!

Features:- Biters can now fall down and also can fall off ledges. This can vary with different building types but does work for the most part.
- Biters no longer wait for your to be done getting chomped on by a single biter, they will overwhelm you.
- Biters now use attacks normally reserved for the player on NPCs
- A new type of biter joins the world, the Enraged Crawler. These guys don't know when to stay down and will crawl after you and take more hits than a normal crawler, you can tell them a part from the normal crawler by their constant screams.- Humans can now get knocked to the ground and pinned down by infected. If you so choose, It's up to you to get them off before they die.
- Lots of fixes for invisible zombies, I really messed up on that last release after having to remove more zombies to make room for the virals.
- Fix for more invisible virals.
- Fix for the special infected spawn glitch (ended up having to turn off special infected for now until I figure out a better way).
- Large update to base building and the release of the first part of base building is coming soon for everyone, but you can now clear out interiors and areas using building, so actually purging large areas is possible.
- Added Sandbags for rough defenses, more content coming soon.
- The problem I'm running into now is that the game doesn't properly store things like prefabs in the savegame data, it can store a State change such as turning something on but not that something has been placed or thrown into a specific area (does make sense especially for a multiplayer game). Which means the base building would sadly only be each session you play, so I'm looking into ways that it can be more about popup bases rather than permanent installations for now. This will also play well with defenses being overrun while you're gone but we'll see.
- Fix for the banshee armor having a FOV glitch
- Fix for Volatiles detecting UV flares while roaming.
- Slight increase to dogtag drops

Update 1.2e:
- Refactored the spawn system for the game by zone IDs, releasing a new custom spawn table that allows easy modification and adding any vanilla infected and custom infected easily to the map. See video tutorial.- These new zones bring more realism and set the stage for a lot of future updates for the Bandit overhaul and the zone specific encounters.
- Currently the new zones are balanced to be easier for the zones claimed by Survivors or PK, while the Renegade and Unclaimed zones are considered "wild" zones with more enemy spawns and diversity.
- PK zones have more PK undead in interiors and exteriors (Dog tags)
- Completely rebalanced the Biters in the game to make faction specific biters contain faction specific loot.
- Added more diversity for Weak, Biter, and Fresh biter variants.
- Fix and return of the Biter Nightwalker to the game, which allows the user to make biters run during the night and walk during the day through the config, this is disabled by default still.
- Added 80 unique virals to the spawn tables, currently there is a rogue invisible viral in the world but I'll get him next update, sorry about that.
- Fix for the volatiles acting strange and not attacking the player. There is still a vanilla bug that causes them to react like they are in the sunlight at night.
- Overhaul for most of the common IALR scripts for better mod compatibility and long term support.
- Fix for the skinner armor not showing in First person! This includes Volatile legs

Update 1.2d:
There are several features that were already added to the code that were not active due to the holiday event but now you should have:
- Added a very large amount of diversity to the Flooded City, new Virals, new biters, and the New Swamp Volatile.
- DayStalker Volatiles and Swamp Volatiles have been added to the world during the day! These are rare spawns and are built off the idea that the volatiles are covered in Mud or Swamp Chemicals to allow them to be out during the day.
- Fix for Bandits and Renegades not attacking, running up to player glitch
- Fix for Volatiles acting strange during Chase, they still have this odd vanilla bug where they run away if they spawn so only a certain number can actually chase you.
- Fix for the Virals acting weird during chases, they definitely hurt again
- Fix for the Swamp Volatile, which has a chance to spawn in the Sunken City. These Volatiles have been covered in thick chemical mud which allows them to creep around during the day and night.
- Added Swamp Goons, which have a chance to spawn normally into the Swamp biom. Swamp Goons slowly shamble but pack a mean punch
- Fix for Volatiles acting strange during Chase, they still have this odd vanilla bug where they run away if they spawn so only a certain number can actually chase you.- Fix for the Virals acting weird during chases, they definitely hurt again
- Fix for the Swamp Volatile, which has a chance to spawn in the Sunken City. These Volatiles have been covered in thick chemical mud which allows them to creep around during the day and night.
- Added Swamp Goons, which have a chance to spawn normally into the Swamp biom. Swamp Goons slowly shamble but pack a mean punch
- Reduced the HumanAI watching the player more than anything else in the world. This still happens but they pay much more attention to the world than before.
- Fix for Chargers walking around the city and not attacking in the day
- New volatiles Chemical and Venom variants out in the world and during events.
- New "Fresh" biters that run and climb mixed into the common zombies that are not "Virals".
- The ability to turn on "Nightwalkers" in the config to make all night time zombies runners and climbers while daytime zombies are walkers
- Crawling zombies should also be found in the world now with a much higher diversity to the types of crawlers
- "Swamp" zombies should be found in the flooded city, which hiss and are completely covered in swamp mud.
- Dog tags should be found on dead PK, viral PK, and zombie PK
- All armor drops and new loot should be back with better spawn rates
- Drastically improved Human AI for detecting zombies and attacking other enemies. This fix should address the HumanAI standing around until attacked. It's like they have woken up.- Survivor now has a few "Fresh Dead" that can run and climb added to the mix. This can be toggled in the config.
- Fix for the "blob" zombie in the world at night- Fix for the PK attacking the player
- Fix for Bandits not attacking
- Improved world loot system for the custom content but also for more expansion on the very simple loot system.
- Reduced Crawlers in interiors
- Removed Money and valuables from drops from infected (Goons, Chargers, Demolishers, volatiles, corruptors...) we can do better, increased the amount of glands and samples and increased the chances of "Play the Zombie" drops.
- Added unique loot to the custom biters, infected.
- Added unique loot to the volatiles and volatile tyrants
- Fix for the prologue zombies not properly resting
- Fix for Xray effect not showing
- Fix for missing spawn tables for a large number of HumanAI, they should now get faction specific loot.
- Colonels now have their own loot, based on military
- HumanAI have received a higher chance at spawning useful survivor tools such as Decoys, Mines, and UV Flares
- Reduced the number of Virals spawning inside interiors to better allow the player to sneak through areas.
- Added back special infected to interior zones
- Reduced the number of Venom and Chemical Volatile Variants
- Confirmed Swamp zombies are working!! They look great.
- I attempted to re-create the "warzone" spawns out in the world for the different groups of HumanAI, and currently the whole world turns on you due to their relationships haha, one group will be neutral but will auto side with another because they spotted you. Continuing to look into how to make the player less "detected immediately" by the HumanAI, a problem that has been there for a while.
- Ultimate now has a mix of walkers as well to keep things diverse
- Added the ability to toggle Weapon bounce by weapon class, so if you want sticks to bounce you can turn that on. // ------ WEAPONS --------\
- Added the ability to toggle Goon running to the Config //- Goon Movement Settings -\
- Drastically reduced the Zombie "Grab" attack
- Added more infected Chase options to the config! Now you can pick who has a chance to spawn when a chase starts, this includes, Virals, Goons, Chargers, Spitters, Banshees, Demolishers, GRE Anomalies. Each one has been balanced by difficulty.
- Fix for a bad update for the Survivor Config
- Drastically improved Companion logic for following the player and attacking enemies. Still not officially released to public but update should work for Patreon supporters.
- Added Biter attack damage and grab bite attack damage to the config: //- Infected Damage -\
- Fix for Perfume being a craft item, returned to valuable
- Added additional new zombies to the spawns

Update 1.2c:
- Updated for 1.8.3c (starts tomorrow)
- Fix for new medkits and healthkits not properly showing up at traders
- Fix for Smoke effect for reinforcements not being the proper color by Faction
- Fix for Casual Difficulty bug (sorry about that!)
- Fix for Restore glider optional, you'll now get your icon back, sorry about that.
- Fix for a bug with "No Kid Zombies" Optional, this should work as expected now!
- Patreon Supporters now have immediate access to over 1,200 new custom items from IALR including Base building, Companions, and Spawn system
- Companions Hakon, Spike, Lawan, and Companion Scavengers have been added to the world.
- To Activate a Companion you currently use the same approach as the PK Reinforcements, find and use summon Beacons to bring a companion to your location.
- All Custom items and Armor now have names and descriptions.
- The PK armor sets have been given unique and custom name for each piece of armor.
- The Hazmat Armor has been given unique names and descriptions for each set of armor.
- The Play the Zombie content has been given better names and descriptions.
- A ton of code cleanup was done to allow for IALR to have standalone code to make updating the Mod much much faster.
- Fixed a bug with the Survivors being neutral to Renegades, they should now attack them
-  Bandages and Clean Bandages have a new icon for health

Update 1.2b:
- Added working backpacks into the world with Stats displayed for each! Each does a varying degree of increased slots for Weapons, Equipment, and Consumables.
- Wearing a Medium or Larger backpack (Blue or greater) can cause effects to your gliding.
- Added the ability to change your inventory size overall and with your Weapons, Equipment, and Consumables in the Config.
- IAL_Inventory_Weapon_Slots, IAL_Inventory_Equipment_Slots, IAL_Inventory_Consumables_Slots
- Consumables have been increased to support carrying the new custom content.
- Investigated the detection of the player inside interiors, this is also being caused by the Winter Event, they are pretty much all Virals during the day, and those alert biters to your location. This should be better balanced after the event.
- Added 8 variations of female Gas Tanks to the world
- Added 14 new zombies to the world that represent fallen "players" and "scavengers" with backpacks that contain goodies.
- 2 new variants of Zombies join the world 
- The Fresh Dead, and the Nightwalker. (Sadly these are disabled until the Winter Event has finished...). The Fresh Dead have been added to the spawns at different amounts to balance Survivor and Ultimate (again not currently working with the event), and Nightwalkers are disabled by Default for Survivor for now but are available to be turned on and off in the config.
- The Fresh Dead now show up in Survivor and Ultimate difficulty and have the ability to run and climb to a limited degree.
- The Nightwalker variant is a setting that can be turned on to make all biters run at night and walk during the Day similar to DL1
- The ability to make the new biters walk and toggle climb has been added to the config.
- Improved visuals for all the biters to fix large amount of the texture tearing.
- Fix for various crashes reported
- Added a full suite of options for Survival Sense to the mod and added this system back to Survivor and Ultimate Survivor
- Added interior densities to the config and made this much better to balance for stealth
- Fix for ziplines not working
- Fix for Stamina Regen bug
- Fixed Takedowns in interiors, this will not alert other zombies unless they are too close to each other.

Update 1.2a:
1.2 Warzones is officially released with new features and content. This release won't have all the discussed features on the Stream but coming shortly it will also include:
- Companions
- Base Building
- Custom Bandit Factions
- Updated for 1.8.2p
- Cleaned up and improved over 500 biters, removed additional "invisible" zombies
- Added 25 custom new biters for Swamp areas (not working during holiday event).
- Added e3 styled coloring to the PK to help setup the world for the new custom Factions being worked on.
- Added 38 new variants for Male and female PK commanders
- Added the ability for PK Commanders to occasionally summon more troops.
- Added the ability for Renegades to summon more renegades
- PK guards now use Bows in the bases and will fire down on enemies outside of the walls.
- Base raids will sometimes occur in the PK Metro Hub at night in the first city.
- Removed a lot of the Blue color added to the PK from the last release
- Added 38 new variants for Male and female PK commanders
- Added the ability for PK Commanders to occasionally summon more troops.
- Added the ability for Renegades to summon more renegades
- Improved the overall Renegade AI to be more aggressive and to try to box in the player as more get summoned to the location.
- Fixed some issues with the Renegade Molotov spitters and throwers, they should work properly now.
- Removed a large amount of the food items from the common world spawns and made them more rare or completely removed until Survival optional is added, thanks for your feedback!
- Removed Chemical and Venom volatiles from the Casual Survival world spawns, they may appear is random encounters.
- Improved the overall Renegade AI to be more aggressive and to try to box in the player as more get summoned to the location.
- Added 5 new variations of Volatiles, 2 new types of Volatiles - Chemical and Venom variants you'll encounter in the world.
- All bases should now be online, meaning the AI should move around and attack the player if provoked (also attack zombies and infected). The only ones turned off right now are the traders due to custom code needing to be written to keep them around after battle.
- Metro Hub can be raided at night time.
- Bowmen have been added to the PK Base walls that fire down at enemies.
- The PK now reward you by giving you the ability to summon 6 tiers of PK reinforcements, including the new custom PK Commandos.
- Fixes for Spawn locations reported by users.
- Fix for crash caused by syntax error
- Fix for a large number of invisible zombies due to a reference error
- Fix for alcohol buff reducing damage
- Increase the healing of the basic bandages and clean bandages based on feedback
- Added the ability to find Tier 1 reinforcements by rescuing Hostage PK
- Fix for Damage bug reported on Nexus
- Fix for Viral visuals
- Fix for IALR Optionals being outdated after various hotfixes
- Added rewards for PK Reinforcements to story line and side quests for PK

Hotfix 1.1c:
- Custom and unique interior spawns and densities by difficulty and region
- Less spawns in the interiors at night, especially at starter zones.
- Some zones may have more or less, this is by design, come prepared for a fight.
- Improved zone spawning for more realistic warzones! City areas are ready to take on the horde during the day or have fully retreating inside their walls.
- Fixes for overpowered bow and arrows
- Created unique bows for the PK, they should be able to pack a punch now.
- Fixes for Volatile AI, some behavior improvements after Halloween update
- Explosions now have a chance to spawn virals, biters, and banshees
- Fix for visual glitch on Banshee
- Fix for visual glitch on Biter/Infected reported in the world.
- Improved Warzone spawn system so when you make a zone belong to a group, they will take over the area and continue to fight to take it back.
- Fix for detection glitch in the logic
- Zombies now move in a random speed, which will help the diversity.
- AI Improvements for detection and groupwork, they will now band together to take out enemies.
- Improvements to Bowmen logic and behavior.
- Survivors now use lower quality UV Flares
- PK now drop UV Flares with their loot


Hotfix 1.1b
- Weapons now drop from specific groups of human enemies
- Humans now are more intelligent and use grenades, flares, and decoys (took so long but FINALLY got it).
- Currently working on them throwing actual weapons (works but damage isn't working!!)
- Colonels men are added to the world with a new conflict matrix, before they were considered bandits but now they will work together and not attack the player unless attacked first, they will attack bandits and renegades.
- Added human PK commandos to the world. Added PK summoners to the world
- Fixes for spawns from previous release.
- 10 new goon visuals added to the world at random
- Fix for the random bandit model that is stuck in place
- Lowered the amount of interior spawns at night
- 12 new banshee appearances in the world
- 1 new look for the screamer
- Added proper red Biomarkers for zombie horde
- Added proper mouth textures to the zombie horde

I Am Legion 1.1
Features:
- DiverseZ's: Over 1000+ new custom enemies added to the game
- Armor overhaul: Over 200 new custom armors added to the game and loot tables
- Play the zombie Update:
- Find Platinum loot drops added to the world that will allow you to get a full armor set for the Banshee along with weapons and a booster to play the game like never before!
- The Play the Goon update isn't complete but is also in the game and can be found.
- The Play the Volatile and Volatile Tyrant isn't complete but is also in the game and can be found hidden in the world.
- Character Selection: Over 40 custom playable characters found in your stash- New weapons have been hidden in the world included a Doom's day plague bomb to end a city block
- A completely overhauled loot system has been added
- Hundreds of new updates from 1.0 to 1.1 with the communities feedback!

- Implemented the Hazmat Armor Sets (13 Armors), balanced and hidden in the world. This class of armor gives you increased time
in darkzones and night. There are 5 variants of helmets, 4 torsos, 3
sets of pants, and an air tank, each provides different perks for longer
time in the dark.
- Implemented the PK Armor Sets (21 Armors), balanced and hidden in the world. There are 6 Legendary sets, 3 helmets, 6 torso
pieces, 1 set of gloves, 5 armor plates, and 6 pants. All armors have
been balanced to include 6 versions with scaled perks.
- Implemented the Leisure Armor Sets (6 Armors), balanced and hidden in the world. I'm still working on their unique
skills but there is one Gold torso piece, 1 helmet, 3 torso pieces, and 2
pants. All armors have been balanced to include 6 versions with scaled
perks.
- Implemented the Brawler Armor Sets (14 Armors), balanced and hidden in the world. This set is built off the arena DLC
and is focused on melee fighters. There are 2 torso pieces, 4 additional
armor pieces, 5 pants, and 2 shoes. All armors have been balanced to
include 6 versions with scaled perks.
- Implemented the Runner Armor Sets (9 Armors), balanced and hidden in the world. This armor set has unique perks that allow you
to move faster in the world and run along walls for a longer time based
on the tier of armor. There are 4 torso pieces and 5 pants. All armors
have been balanced to include 6 versions with scaled perks.- More
information on spawn locations and hints will be given at 1.1's full
release.
- Implemented the Bandit Armor Sets (26 Armors), balanced and hidden in the world. This armor is centered around
melee combat and is considered "Medium Armor", more coming soon about
the "Light" "Medium" and "Heavy" armor classifications and what they
mean for gameplay. There are 4 legendary armors for this set, 7 helmets,
4 torso pieces, 8 armor addon pieces, 1 set of gloves, and 4 pants. All
armors have been balanced to include 6 versions with scaled perks.
- Rebalancing for loot across the world, I ended up spending a good chuck of the day testing and trying to be
playful with how this armor shows up in the world. Outfits can now be
found more likely in containers that should contain clothing, along with
darkzones, GRE, and military containers. I've also continued to
rebalanced how loot is spawning into the world, where you can find
different ingredients etc. based on your feedback.
- Added the ability to sell all my custom armor in the shops, let me know how this goes!
- Implemented the Renegade Armor Sets (15 Armors), balanced and hidden in the world. This armor is centered
around melee combat and is considered "Medium Armor", more coming soon
about the "Light" "Medium" and "Heavy" armor classifications and what
they mean for gameplay. There are 6 Legendary pieces, 8 helmets, 1
torso, 5 additional armor pieces, and 1 pair of pants.
- Improvements to Leather sets - Leather has now been fully balanced into the world with each of the 5
conditions (white, green, blue, violet, and orange) along with 5 new
legendary pieces. This armor is considered "Light" armor and focuses as a
healer set.
- Improvements to Military sets - Military has now been fully balanced into the world with each of the 5
conditions (white, green, blue, violet, and orange) along with 5 new
legendary pieces. This armor is considered "Heavy" armor and focuses
mainly as a Tank set.- Improvements to Medical sets
- The legendary medical set - has been improved and new versions have been created that can be
found at a lower level but very rarely. There are 3 versions of the
legendary set and all should highly boost a healers playthough, you'll
need to be 20+ to start finding this hidden armor.
- Improvements to inventory crashes - Found several issues with the code and made
improvements to stabilize the new armor systems
- There are now 1097 new armor pieces implemented ingame with 107 new unique pieces!
- Armor has been hidden in the world and loot systems, more details are coming with 1.1!
- Finally fixed the chrome bug (sorry for the delay on that)
- Implementation of "Heavy" Armor concept on Renegade armor set, Torso's have the most effects:

    Heavy armor slows down the player based on how many pieces they have equipped.
    Glider stamina and gravity drop MUCH higher when using heavy armor, use it to save your fall or a quick escape.
    Heavy Armor greatly reduces damage the more you have on and the higher the quality, this allows biters and arrows to be less of a factor with heavy armor.
    Heavy Armor reduces your jump height and fall damage the more pieces you wear.
    Heavy Armor Reduces the time you can wall run.
    Heavy Armor makes more noise when you move around the world.

- AI Improvements:- Greatly improved biters ability to follow the player and seek them out when spotted.
- Biters will now chase the player when a "Chase" begins on all difficulties.
- Added Colonel custom encounters
- Added more supporting "Rooftop" code for all versions for infected and bandits
- Added more diversity to the world encounters
- Improved Volatile code inside Darkzones
- Improved spawns inside interiors and Darkzones, welcome back special infected.
- Volatiles now properly search rooftops and interiors at night (mainly Survivor and Ultimate survivor, rare in Casual)
- Volatile combat fixes from 1.0f2
- Character selection has been largely completed, you can access these new character skins through your stash!
9 new male character skins, 10 female character skins, 5 male story
character skins, 5 male legendary skins, 6 female story character skins,
and 6 legendary female character skins.
- If you select a different race or gender, your first person view now shows the appropriate gender/ethnicity.
- Banshees have been fixed and should be behaving properly from 1.0f2.
- I've increased all ranged weapon headshot damage
- Added back new improved Renegades to the city
- Added back new improved Colonel troops to the city
- Improved spawn density system to better flood the cities.
- Weapons now have a chance for dropping from NPCs
- Loot has been rebalanced for better realism and based on feedback
- Improved damage from fire and Blasts in the game
- Better balancing for physics
- A lot of improvements to the biters AI, made them move faster at night and slower in the day
- Added rooftop spawns during the day and night
- More improvements to the AI Sensors and memory systems
- Volatiles and Screamers spawns balanced
- Fix for spawn bug, this was due to my volatile mini chase logic so that's been pulled back out for now (volatiles summoning other volatiles).
- Fix for Charger spawn bug, the world spawns should be working correctly now.
- Fix for "Chase" logic randomly spawning special infected when a screamer first screams. This is random and based on your selected Casual, Survivor, or Ultimate difficulty.



I Am Legion - Reborn 1.0
- Redesigned Nexus page coming soon!
- Improved Human AI climbing and fighting
- Fixed weapon glitching with Human AI
- Fix for missing weapons on Human AI
- Better balanced Bowmen and Melee fighters
- New zombie visuals including custom Virals, Armored, Renegade Zombies
- New PK visuals, better loadout and armor
- Fix for Banshee logic, no more infinite running
- Added some hidden content for the encounters and events, helps set a much darker tone
- Screamers now more likely to follow and chase player after a chase has started
- Improved Volatile logic, should no longer hang out in the sunlight- Improved biters for Ultimate, fix for the taunt loop where the zombies keep stopping and screaming, improved detection and world exploration
- Improved detection for screamers, the target is now at the players location, not the vanilla screamers feet (fixes so much for intensity)
- Mini-chase system added back to the volatiles, if a volatile spots you in Survivor and Ultimate versions they have a chance to call for more volatiles (RUN).
- Fix for Spitters not being able to target the player
- Fix for Banshees getting stuck in patrol, not attacking humans and player
- Fix for "Blue" viral glitch
- Fix for volatiles more likely to investigate firecrackers, players reported them always detecting the player, this is due to a higher alert from the noise of the firecracker and they will spot you if you are within their FOV.
- Fix for Remnant waves including a spawning volatile
- Removal of custom GUI color
- Added back the ability to toggle enemy health bars

HOTFIXES (1.0d)
- Updated to work with 1.4.0c
- Found various issues while updating so the AI should now have more fixes, including physics glitching, spawn issues, and more.
- Decreased the amount of health for volatiles after lvl 6, this will present a challenge at higher levels but not be impossible to kill.
- Rebalanced the screamers and volatiles for the 3 difficulties.
- Fixes for Syntax errors with collectables
- Fixes for missing loot from update
- Updated the Hive spawns modified back in Feb, 2022 to better reflect the current status of the game. This will probably need more balancing.
- Fix for Humans reacting to kicks, vaults, grapple
- Fix for dodge on humans happening too often
- Fix for volatile logic and attack patterns
- Fix for values error happening due to changed value types, causing the configuration to feed in the wrong type of values. Removed the values for now, configuration update is coming soon.

__**- Casual Survivor:**__
- Removed minichases for Casual version

__**- Survivor:**__
- Removed additional GUI elements to support more immersive gameplay

__**- Ultimate Survivor:**__
- Removed even more additional GUI elements to support more immersive gameplay
- Better balancing for zombies, improved detection and chasing



Updates to I Am Legion - Reborn 0.99pre Update 16a
- Updated to work with 1.3.0
- Added NG+ logic to the mod!
- Improved interior night time spawns, early areas will spawn survivors and bandits, high level can spawn all human groups.
- Fix for Climbing zombies in Casual
- Fix for Volatile fall damage
- This also includes better weapon physics reactions with blunt weapons mainly
 The 3 difficulties have been added! This is for feedback and early phase for the overhaul to the config and difficulties for 1.0.

__**- Casual Survivor:**__
- All the AI enhancements without as much intensity, Less Volatiles, Screamers, and Banshees.
- Less density throughout the world.
__**- Survivor:**__
- This is largely where the previous "Casual survivor" was in difficulty, the cities are intense and the spawns are higher than Casual. This version is for Lore players with the added intensity and realism.
__**- Ultimate Survivor:**__
- This version contains the running biters, more spawns, and more intensity!

- Volatiles now creep through the city looking for the player and other humans
    - This is sight based and should allow stealth to work again for Volatiles
- Screamers now crawl through the city seeking out the player as well, they can climb low objects and mid level city objects.
- Banshees now patrol the city and are frantically searching for targets
- Improved loot systems with better loot based on location.
- Improved Bowmen to help prevent falling down when climbing and attacking (Still falling but working on it).
- Added additional bug fixes for AI detection and UV reactions

Updates to I Am Legion - Reborn 0.99pre Update 1 - 15

    Fix for stamina- Fix for all runners
    Fix for Banshee glitch
    Fix for Biter glitch
    Fixed the spawn code! Actually found why people are sometimes seeing different special zombies scattered throughout the city and now howlers should be fixed for all areas.
    !!Removed!! the glitched howler? Please let me know if this killed him dead.
    Added back demolishers to night spawn exterior lists
    Added a Romero edition of the mod which features "Walking Dead"styled zombies that slowly shuffle around the map towards you and then attack when close enough to strike.
    Fixed Goons running around the map randomly
    Fixed Banshee's running away, disabled hunting mod for now to continue to develop code.Update 4:- Weather system
    New weather events unique to IAL
    Dynamic lighting and sun rays
    Darker nights and interiors
    Reduced saturation of color in the world without effecting GUIs
    Improved bowmen
    Removed Spitter footprints
    Fixes for Volatile code to improve stalking and hunting at night
    Fixes for a glitch with the Banshee
    Fixes for zombies not spawning with explosions
    Fixes for special zombies not spawning with Chase start
    Added bowmen dodge, step back, fire while moving
    Continued work on weather system to decrease fog brightness at night.
    Fix for crash, audio glitching
    Fix for spawn pools in metro and a few other locations
    Improved AI Pool for Lore based Bandits and Renegades at day
    Added Mini Chases to Volatiles, if spotted at night they will call other volatiles towards your location (NOT A FULL CHASE EVENT)
    Fixed Arrow swap
    Fixed day spawn glitches with Specials
    Fixed daytime running Volatiles
    Responsive AI, AI will now attack zombies and don't have to wait to be attacked
    Restore Immunity Timer
    Bowmen now added to Survivors and Bandit class
    Bowmen dodge and are more aggressive
    Fix for patrolling Volatiles, they now actually explore again at night
    Better balanced FOV for humans, hearing system
    Removed a large amount of chatter from AI, they will no longer constantly speak (as much).
    Fix for a crash reported by discord community.
    Fix for throw always for NPCs
    Fix for detection for volatiles and virals reduced unless they scream, then they hunt
    Fix for npc stutter glitch on movement
    More banshees and specials during the day
    Increase day densities in "ial_settings.mth" for more zombies during day on the streets
    Removed HumanAI stutter bug from update 10
    Improved spawn balance for daytime

    Removed HD and Color settings from main mod, they are now optionals
    Added logic for more interactions on rooftops, let me know how this goes
    Reduced sighting possibilities for Volatile and virals
    Fix for Hydrant explosions blasting NPC's into space randomly
    Fix added for config crash (Arrow penetration)
    Rebalanced loot system, less loot overall with higher chance at empty
    Lowered $ loot amounts and most valuable loot amounts
    Lowered Tokens received by Biters and special infected
    You're more likely to get glands with different types of special infected: Screamers and Demolishers have the highest chance.
    Early stage - Unique Medkits, Lockpicks, Molotovs, Remote Explosives, Shotgun, Grenades
    - Improved Human combat, more dangerous interactions and knowledge base for HumanAI.
    - AI will now switch between bows and melee weapons based on distance to the enemy (sometimes glitches)
    - Weapon offset can sometimes be seen when a bowmen also uses a melee weapon, I'm currently investigating.
    - Humans now group together and explore together, they investigate nearby threats and will stack up to take on enemies.
    - Sometimes zombies are still not detected right away
    - Bowmen now climb on objects and buildings to get a better line of sight on enemies
    - this can sometimes cause them to fall off ledges, still working on edge detection
    - Improved UV detection for special infected, should help with new chase system
    - larger special infected not affected by UV but I've tried to make them walk off after a period of time.
    - Fix for chrome effect on Fog, Rain, and storm weathers.

- Improved Human combat, more dangerous interactions and knowledge base for
- Rebalanced Human AI to support retreat and climbing system
- Human AI now run around the city and climb
- Better human reactions to zombies, dodging, and survival, gives them a fighting chance vs. Zombies.
- HumanAI will now scale multiple floors of buildings to fire down on enemies.
- Reduced rainy and stormy weather probability.
- Continued weapon balancing
- Reduced NPC chatter more than previous reduction
- Improved AI damages versus zombies
- Biters now move around the city when they don't detect a target



_____________________________________Change log:_____________________________________
Updates to I Am Legion - Reborn 0.99pre
Update 1 - 11
- Fix for stamina- Fix for all runners
- Fix for Banshee glitch
- Fix for Biter glitch
- Fixed the spawn code! Actually found why people are sometimes seeing different special zombies scattered throughout the city and now howlers should be fixed for all areas.
- !!Removed!! the glitched howler? Please let me know if this killed him dead.
- Added back demolishers to night spawn exterior lists
- Added a Romero edition of the mod which features "Walking Dead"styled zombies that slowly shuffle around the map towards you and then attack when close enough to strike.
- Fixed Goons running around the map randomly
- Fixed Banshee's running away, disabled hunting mod for now to continue to develop code.Update 4:- Weather system   
     - New weather events unique to IAL 
- Dynamic lighting and sun rays 
- Darker nights and interiors
- Reduced saturation of color in the world without effecting GUIs 
- Improved bowmen 
- Removed Spitter footprints
- Fixes for Volatile code to improve stalking and hunting at night
- Fixes for a glitch with the Banshee
- Fixes for zombies not spawning with explosions
- Fixes for special zombies not spawning with Chase start
- Added bowmen dodge, step back, fire while moving
- Continued work on weather system to decrease fog brightness at night.
- Fix for crash, audio glitching
- Fix for spawn pools in metro and a few other locations
- Improved AI Pool for Lore based Bandits and Renegades at day
- Added Mini Chases to Volatiles, if spotted at night they will call other volatiles towards your location (NOT A FULL CHASE EVENT)
- Fixed Arrow swap
- Fixed day spawn glitches with Specials
- Fixed daytime running Volatiles
- Responsive AI, AI will now attack zombies and don't have to wait to be attacked
- Restore Immunity Timer
- Bowmen now added to Survivors and Bandit class
- Bowmen dodge and are more aggressive
- Fix for patrolling Volatiles, they now actually explore again at night
- Better balanced FOV for humans, hearing system
- Removed a large amount of chatter from AI, they will no longer constantly speak (as much).
- Fix for a crash reported by discord community.
- Fix for throw always for NPCs 
- Fix for detection for volatiles and virals reduced unless they scream, then they hunt
- Fix for npc stutter glitch on movement 
- More banshees and specials during the day 
- Increase day densities in "ial_settings.mth" for more zombies during day on the streets
- Removed HumanAI stutter bug from update 10
- Improved spawn balance for daytime

Update 12
- Removed HD and Color settings from main mod, they are now optionals
- Added logic for more interactions on rooftops, let me know how this goes
- Reduced sighting possibilities for Volatile and virals
- Fix for Hydrant explosions blasting NPC's into space randomly
- Fix added for config crash (Arrow penetration)
- Rebalanced loot system, less loot overall with higher chance at empty
- Lowered $$$ loot amounts and most valuable loot amounts
- Lowered Tokens received by Biters and special infected
- You're more likely to get glands with different types of special infected: Screamers and Demolishers have the highest chance.
- Early stage - Unique Medkits, Lockpicks, Molotovs, Remote Explosives, Shotgun, Grenades

Updates to I Am Legion - Reborn 0.9b
- Fixed issues with ragdoll on drop kick and normal kick
- Fixed and improved grapple pull on zombies
- Fixed chemical zone timer bug
- Added full changelog to the link below

Updates to I Am Legion - Reborn 0.9a
- Fixed issue with the new chase spawn system where only demolishers were spawning.
- Raised the density back to 3.0 for day (8x as many zombies and specials) and 2.0 for night (15x as many zombies and specials), remember lower means high number of zombies and you can edit in the config file, see above videos for information on the configuration. (Density now makes a HUGE difference in difficulty with the volatiles on the map at night so make sure to tweak to your ideal settings).
- Added new chase spawn table to the "ial_setting.mth" config! Under Chase section.
- Fixed infection timer bug

Updates to I Am Legion - Reborn 0.9
- New chase system, special zombies included in the chase logic: Banshee's, Goons, Demolishers
- New persistence system, if you die in a location with special zombies spawned in during Chase, they may remain in the area to begin chasing you again after respawn.
- Banshee's reworked to stalk the player after they have been summoned during a chase.
- Demolishers reworked, they now climb and hunt down the player, throwing everything they can and charging the player.
- Improved grenades, explosive arrows, do alot more damage even at low levels.
- Faster walkers, variation to speeds
- Improved zombie reactions, pathing, and logic.
- Configuration settings added for the HUD, new color scheme
- Added timescale to the configuration files, added HUD options and easy access to color variables to design your own maps and HUD colors.
- Increased time for infection, currently working on rebalancing infection system based on bites and other factors in the game.
- Better trading prices, improved for different types of weapons and their color.


Updates to I Am Legion - Reborn 0.9a
- Fixed issue with the new chase spawn system where only demolishers were spawning.
- Raised the density back to 3.0 for day (8x as many zombies and specials) and 2.0 for night (15x as many zombies and specials), remember lower means high number of zombies and you can edit in the config file, see above videos for information on the configuration. (Density now makes a HUGE difference in difficulty with the volatiles on the map at night so make sure to tweak to your ideal settings).
- Added new chase spawn table to the "ial_setting.mth" config! Under Chase section.
- Fixed infection timer bug

Updates to I Am Legion - Reborn 0.9
- New chase system, special zombies included in the chase logic: Banshee's, Goons, Demolishers
- New persistence system, if you die in a location with special zombies spawned in during Chase, they may remain in the area to begin chasing you again after respawn.
- Banshee's reworked to stalk the player after they have been summoned during a chase.
- Demolishers reworked, they now climb and hunt down the player, throwing everything they can and charging the player.
- Improved grenades, explosive arrows, do alot more damage even at low levels.
- Faster walkers, variation to speeds
- Improved zombie reactions, pathing, and logic.
- Configuration settings added for the HUD, new color scheme
- Added timescale to the configuration files, added HUD options and easy access to color variables to design your own maps and HUD colors.
- Increased time for infection, currently working on rebalancing infection system based on bites and other factors in the game.
- Better trading prices, improved for different types of weapons and their color.

Updates to I Am Legion - Reborn 0.8c
- New zombie types including Zombie and Viral kids, new female zombies.
- Merged in updated spawn list, should help with large number of the special infected glitches, large armies of goons and demolishers.
- Improved Biter logic, added scaling values as you level up for the biter difficulty.

Updates to I Am Legion - Reborn 0.8b
- Updated to work with 1.2.0
- Another fix added to reduce bandit spawn glitch
- Includes Techlands physics updates while keeping some of my own, there weren't that many.
Updates to I Am Legion - Reborn 0.8a
- Insta spawning for bandits
- Extended day time and nighttime cycles
- Cleaned up some of the spawning and added Demolishers to the lists of the special infected spawns (goodluck)
Updates to I Am Legion - Reborn 0.8
-New AI Behaviors for Goon, Banshee, Screamer, and Spitter.
 - Banshee will track you from above, she will no longer hang out on the ground but will only attack from pouncing on the ground and from above
    - Removed Sparkles
 - Goon will now run towards you at high speed. Cooldowns reduced so the goon attacks more frequently
 - Screamer can now climb and track the player, they can be drawn towards noise and will come investigate your noise.
 - Spitter will now climb and track the player, they sprint close enought to spit and will try to keep up with the player and shove them.

- Removed Zombies drowning

- New configuration system, documentation update coming soon with more details but for now a single config file
    - Can be added externally
    - Store your settings for future IALR updates
    - Made AutoAim a toggle feature in Configs
        - Configuration Catergories:
        - GAMEPLAY
            -INTERFACE
            -CAMERA
            -SLOWMO
            -XRAY
            -ZIPLINE
            -LOOTING
            -INVENTORY
        - PLAYER Settings
            -Stamina
            -Running
            -Jump
            -COMBAT
            -Survivor Sense
            -Camoflage
        - WEAPON Settings
            -GENERAL
            -Bow
            -NIGHT Experience
        -SPAWN AND DENSITY
            -DENSITY
            -SPAWN LOGIC
        -AI DIFFICULTY
            -Infected Damage
            -BITER
            -Grouping System
        -AI ENCOUNTER Settings
            -GENERAL SPAWN LEVELS
            -AI SPAWN SETTINGS BY ZONE
            -INFECTED Difficulty Tiers
            -INFECTED ENDGAME Difficulty Tiers
            -HUMAN GANG Difficulty Tiers
        -DISMEMBER SYSTEM
            -Humans
            -INFECTED
        -CHASE SYSTEM
            -All conditions for chase
            -Chase Damage
        -DAMAGE MODIFIERS
            -GENERAL MODIFIERS
            -ARMOR
            -WEAPONS
        -HEIGHT (FALL) Settings
        -EXPLOSIVES
        
- Better map spawning due to improved spawn maps for Infected (I have seen a few glitches here and there)
- Improved hitboxes for all weapons and projectiles
- Fixed bug with Chase, should be back to normal intense chase system (part of config options)
- Improved noise detection, added ability to wake up interior zombies
- Improved Stealth systems, turned down some of my increased sensors, hopefully this will work better than before
- Fix for Toxic and Chemical Zombie damage
- Fixed Humans hyper focusing on Player
- Fixed? respawning reinforcements
- Increased spawn variety to cut down on boss death hacking
- Increased all damage systems
    - Biters do serious damage with a single bite
Updates to I Am Legion - Reborn 0.7
- Overhaul to Human AI and spawn numbers for the gangs, survivors, and PK
- Created new types of human AI, currently this is mainly Survivors, giving them the ability to have bows.
- All humans have been updated to use more bows for clearing the streets
- Survivors have received better weapons if they are spawning out in the cities.
- PK Watch towers are now maned 24hrs.
- Update to the human sensors to make stealth easier for missions.
- Increased toxic and chemical biter effect areas by level
- Update to human climbing and jumping, they should now behave more realistically.
- Removed daytime special infected
- Removed virals that looked like humans that were spawning in the daytime
- Added rooftop Volatiles, street volatiles are also working
- Fixed spawning floating cages in the world

Updates to I Am Legion - Reborn 0.6c
- Fixed issue where survivors were scared of the player.
- Fixed special infected spawning during the day.

Updates to I Am Legion - Reborn 0.6b
- Fixed issue where physics system and weapons caused 1 hit ragdolls, this is now conditional based on your weapon.
- Fixed a bug on the howlers that may have been causing zombies to flock to them and also spawn glitch? Please let me know.
- Fixed issue where volatiles were immune to UV and could run into bases.
- Balanced the AI tweaks released in 0.6.

Updates to I Am Legion - Reborn 0.6
- This version includes my latest physics improvements, which fixes weapon based physics for the zombies! I have not implemented this yet with the Human AI as that will need a lot of balancing.
- This update focused on the Human AI and balancing along with the special AI. Alot of improvements have been made to their cool downs, reactions, reinforcements, and intensities.
- This update also includes a rework to the noise system I added at the start of the mod, infected and humans alike will use new methods of inspecting, detecting, and sensing when you're nearby. You should be able to clear areas now by bringing the dead out of the interiors.

Updates to I Am Legion - Reborn 0.5c
- Made the GRE Corruptors very rare spawns, I haven't removed them from the common spawns as I think they force players to get out of the area, but let me know what you're experiencing!
- Made a new comparison video﻿ to help players decide their difficulty setting for 0.5 and also showcase some of the new features

Updates to I Am Legion - Reborn 0.5b
- Fixed issue with Zombies not awakening inside of interiors until bumped
- Glitched Howlers still occasionally spawn on the rooftops, still working on finding why this is.
- For notes on how to change the spawn amounts, see my 0.5 gameplay video at 07:50﻿

Updates to I Am Legion - Reborn 0.5
- Recreated the mod from the ground up to remove howler glitches and errors.
- Implemented new intensity system for both daytime and nighttime
- Special zombies now spawn in the world
- human detection reduced to support stealth

0.4c I Am Legion - Reborn
Updates to I Am Legion - Reborn 0.4c
- minor fixes mentioned by the discord community
- Human dismemberment didn't kill enemies
- Minor tweaks to improve other mod support, see blow list of compatible mods

Updates to I Am Legion - Reborn 0.4b

    - Continued support for spawn logic for more intense quests, story lines, interiors.
    - Continued game play mechanic updates such as the AI intelligence. Currently testing and working on updates to the special infected and their intensities.

Updates to I Am Legion - Reborn 0.4

    - Fixed audio for running biters, this now mimics the virals running sounds. Testers please keep an ear out for glitches.
    - Increased spawns and groups of zombies
    - Night Patrols for Peace Keepers
    - Volatiles spawn and patrol at night
    - Zombie patrollers now spawn during the day.
    - Interiors are more dangerous, specials may spawn in the interiors
    - Specials can now spawn during the day and night
    - Night balance is more intense, more zombies are in clusters and howlers bring down the whole map.
    - I've gotten weird results with the weather, it sometimes works? Still investigating where they have blocked it for the main map.
    - Physics are still the same as 1.2, I will need more time to release my updates for the weapons system. For all weapon related physics glitches, delete the Scripts/Damage folder for now should allow you to complete the quest. If that doesn't work then delete AI/Ragdoll as well.
    - The walker edition is all the of the updates for the mod but without the running biters.
    - Difficulty options will be coming with 0.5 (stamina, damage, health, etc)

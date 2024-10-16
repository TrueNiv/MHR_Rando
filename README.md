# Monster Hunter Rise Quest Rando

This is a simple quest rando using the REFramework custom quest feature. The rando allows you to swap out the monsters in any given quest.
**This is currently in beta. Please feel free to report crashes or bugs on this github. If you do report a bug, please attach a link to your quest file.**

Most of the info for custom quests was taken from the custom quest editor. You can find it here:
https://github.com/Fexty12573/RiseQuestLoader


## Setup
First set up the quest loader through REFRamework as described here:
https://www.nexusmods.com/monsterhunterrise/mods/1061

Once you're done use the quest loader to export either all quests or just the ones you want the program to edit. Once you're done start the program and enter the path to all of your quests. Next up enter a path to output the files to. It is recommended to have the input and output folders be subfolders of the folder the program is in. There is currently no checking in place to determine whether the program has read/write permissions to the folder. **If the input and output folder are the same your exported files will be overwritten! There should be no other files in your input folder!**

Next, select the settings you want to use. Once you're done the application will close and the output folder will be filled with questfiles of all the entered quests. These quests go into your Monster Hunter Rise installation under "MonsterHunterRise/reframework/quests". Next, take the spawn files in the SpawnFiles directory (or from the ZIP attached to the latest release) and put them into your Monster Hunter Rise installation under "MonsterHunterRise/reframework/quests/spawn/stage". These files are needed so that the monsters can spawn correctly in the changed terrain. 

Crashes are most likely connected to issues within the spawn file used for that quest. Should a mission repeatedly crash upon loading simply remove the questfile from your quests folder, play the vanilla quest and move on.

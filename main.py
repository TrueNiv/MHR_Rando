import os

import JsonHandler
from Settings import RandoSettings
from RandomizeData import RandomizeData


ImportPath = input("Enter quest file directory:\n")
if not os.path.isdir(ImportPath):
    print("Directory does not exist")
    exit(0)

ExportPath = input("Enter output directory:\n")
if not os.path.isdir(ExportPath):
    print("Directory does not exist")
    exit(0)

print(f'Taking files from "{ImportPath}" and exporting into "{ExportPath}"')
print("\n"
      "How do you want your monster placement to be? The monsters stats will be scaled to the rank of the respective mission.\n"
      "Split Base and Master rank - Monsters that are only in the base game will stay there while Master rank has every monster\n"
      "Shuffle Everything - Every Quest can have every monster\n\n"
      "0 = Split base and Master rank (Default)\n1 = Shuffle Everything")
inp = input("Enter a number: ").strip(' ')
try:
    MonsterPlacement = RandoSettings.RankCrossover(int(inp))
except:
    MonsterPlacement = RandoSettings.RankCrossover.SplitBaseAndMaster

print("\n"
      "Quests can either be updated to show the new monster or if you want to keep it a surprise, they can also show nothing.\n"
      "Show Monster - Replaces the quest logo and goal with the new target(s)\n"
      "Hide Monster - Replaces the quest logo and goal with placeholder texts\n\n"
      "0 = Show Monster (Default)\n1 = Hide Monster")
inp = input("Enter a number: ").strip(' ')
try:
    QuestDetails = RandoSettings.QuestInfo(int(inp))
except:
    QuestDetails = RandoSettings.QuestInfo.ShowMonster

print("\n"
      "A quest can have up to 5 targets. The amount can be changed to a random or a fixed number.\n"
      "Always One - Every quest will only have one monster to fight.\n"
      "Always Multiple - Every quest will have a random amount between 2 and 5 monsters to fight.\n"
      "Random Weighted - Quests are most likely to have one monster and each extra monster gets exceedingly more rare\n"
      "Random Completely - The quest will have a completely random amount of monsters\n"
      "Hunter Madness - EVERY quest will always have 5 monsters\n\n"
      "0 = Always One (Default)\n1 = Always Multiple\n2 = Random Weighted\n3 = Random Completely\n4 = Hunter Madness")
inp = input("Enter a number: ").strip(' ')
try:
    MonsterAmount = RandoSettings.MonsterAmount(int(inp))
except:
    MonsterAmount = RandoSettings.MonsterAmount.AlwaysOne

print("\n"
      "Monsters that are meant to be fought after Gaismagorm can sometimes be a lot stronger, even on lower ranks There monsters can be excluded.\n"
      "Include Monsters - Enables all monsters available only after defeating Gaismagorm\n"
      "Exclude Monsters - Disables all monsters available only after defeating Gaismagorm\n\n"
      "0 = Include (Default)\n1 = Exclude")
inp = input("Enter a number: ").strip(' ')
try:
    PostgameMonsters = RandoSettings.InlcudePostgame(int(inp))
except:
    PostgameMonsters = RandoSettings.InlcudePostgame.Include



print("Generating for the following settings:")

if MonsterPlacement == RandoSettings.RankCrossover.SplitBaseAndMaster:
    print("DLC Monsters only in DLC")
if MonsterPlacement == RandoSettings.RankCrossover.ShuffleEverything:
    print("Every monster in every quest")

if QuestDetails == RandoSettings.QuestInfo.ShowMonster:
    print("Showing monster info in advance")
if QuestDetails == RandoSettings.QuestInfo.HideMonster:
    print("Hiding monster info in quest description")

if MonsterAmount == RandoSettings.MonsterAmount.AlwaysOne:
    print("Single monster fights only")
if MonsterAmount == RandoSettings.MonsterAmount.RandomWeighted:
    print("Random weighted amount of monsters")
if MonsterAmount == RandoSettings.MonsterAmount.AlwaysMultiple:
    print("Random amount of more than one monster")
if MonsterAmount == RandoSettings.MonsterAmount.RandomCompletely:
    print("Completely random amount of monsters")
if MonsterAmount == RandoSettings.MonsterAmount.HunterMadness:
    print("Always 5 monsters")

if PostgameMonsters == RandoSettings.InlcudePostgame.Include:
    print("Including postgame monsters")
if PostgameMonsters == RandoSettings.InlcudePostgame.Exclude:
    print("Excluding postgame monsters")


print("Generating files...")
for filename in os.listdir(ImportPath):
    f = os.path.join(ImportPath, filename)

    if os.path.isfile(f):
        data = JsonHandler.ImportQuest(f)
        try:
            data = RandomizeData(data, MonsterPlacement, QuestDetails, MonsterAmount, PostgameMonsters)
        except Exception as e:
            print(f"Skipping quest {data["QuestID"]} due to an error in generation")
        JsonHandler.ExportQuest(os.path.join(ExportPath, filename), data)
print("Generation finished.")
print(f"Saved files in {ExportPath}")

import random
from Values import MonsterIDs
from Settings import RandoSettings
from Values import MonsterIDs


def RandomizeData(jsonData, monsterPlacement, questDetails, monsterAmount, postgameMonsters):
    enemyLevel = jsonData["QuestData"]["EnemyLevel"]
    questText = "Hunt:"

    amount = -1

    # Set the target to hunting all monsters
    jsonData["QuestData"]["TargetTypes"] = [5, 0]

    try:
        mapId = jsonData["QuestData"]["Map"]
        map = MonsterIDs.Maps[mapId]
    except Exception as e:
        print(f"Skipping quest {jsonData["QuestID"]} due to map {mapId} not being a known id.")
        return jsonData

    # Pick the amount of monsters to fight
    if monsterAmount == RandoSettings.MonsterAmount.AlwaysOne:
        amount = 0
    elif monsterAmount == RandoSettings.MonsterAmount.AlwaysMultiple:
        amount = random.randint(2, 4)
    elif monsterAmount == RandoSettings.MonsterAmount.RandomWeighted:
        amount = random.randint(1, 100)
        if amount < 70:
            amount = 0
        elif amount < 80:
            amount = 1
        elif amount < 90:
            amount = 2
        elif amount < 95:
            amount = 3
        else:
            amount = 4
    elif monsterAmount == RandoSettings.MonsterAmount.RandomCompletely:
        amount = random.randint(0, 4)
    elif monsterAmount == RandoSettings.MonsterAmount.HunterMadness:
        amount = 4

    if amount == -1: return jsonData

    # Pick a random monster based on user settings and adjust the spawn
    for i in range(7):
        if enemyLevel < 3 and monsterPlacement == RandoSettings.RankCrossover.SplitBaseAndMaster:
            monster = random.choice(list(MonsterIDs.PreMRIds.items()))
        elif postgameMonsters == RandoSettings.InlcudePostgame.Exclude:
            monster = random.choice(list(MonsterIDs.NoPostgameId.items()))
        else:
            monster = random.choice(list(MonsterIDs.MonsterId.items()))

        # Adjust monster spawn conditions
        jsonData["QuestData"]["Monsters"][i]["Id"] = monster[1]
        if i <= amount:
            questText += f" {monster[0]}"
            if i < 3:
                jsonData["QuestData"]["Monsters"][i]["SpawnCondition"] = MonsterIDs.SpawnAlways
            else:
                jsonData["QuestData"]["Monsters"][i]["SpawnCondition"] = MonsterIDs.Slot3Free
        elif mapId in MonsterIDs.Arenas:
            # Disable extra monsters if in an arena
            jsonData["QuestData"]["Monsters"][i]["SpawnCondition"] = MonsterIDs.NeverSpawn
        else:
            jsonData["QuestData"]["Monsters"][i]["SpawnCondition"] = MonsterIDs.Optional

        jsonData["QuestData"]["Monsters"][i]["SpawnParam"] = MonsterIDs.SlotParameter[i]

        # Move monster into correct area
        spawnArea = random.randrange(1, map[0] + 1)
        jsonData["EnemyData"]["Monsters"][i]["SetName"] = f"{map[1]}{spawnArea}"

        # Adjust stats so that extra monsters in arena quest that normally have less monsters also work
        jsonData["EnemyData"]["Monsters"][i]["HealthTable"] = jsonData["EnemyData"]["Monsters"][1]["HealthTable"]
        jsonData["EnemyData"]["Monsters"][i]["AttackTable"] = jsonData["EnemyData"]["Monsters"][1]["HealthTable"]
        jsonData["EnemyData"]["Monsters"][i]["StaminaTable"] = jsonData["EnemyData"]["Monsters"][1]["StaminaTable"]



    # Adjust Monster Text
    if questDetails == RandoSettings.QuestInfo.ShowMonster:
        jsonData["QuestText"]["QuestInfo"][1]["Target"] = questText
        # Set Monster Icons to random icons
        jsonData["QuestData"]["Icons"] = [random.randrange(0, 120), random.randrange(0, 120), random.randrange(0, 120),
                                          random.randrange(0, 120), random.randrange(0, 120)]
    else:
        jsonData["QuestText"]["QuestInfo"][1]["Target"] = f"Hunt {amount+1} Monsters"
        jsonData["QuestData"]["Icons"] = [999, 999, 999, 999, 999]

    return jsonData


def RandomMonster(enemyLevel, monsterPlacement):
    if monsterPlacement == RandoSettings.RankCrossover.SplitBaseAndMaster and enemyLevel < 3:
        return random.choice(list(MonsterIDs.PreMRIds.items()))
    return random.choice(list(MonsterIDs.MonsterId.items()))

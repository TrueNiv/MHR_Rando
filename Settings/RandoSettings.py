from enum import Enum


class RankCrossover(Enum):
    SplitBaseAndMaster = 0
    ShuffleEverything = 1


class RandomSizes(Enum):
    NormalSizes = 0
    CompletelyRandom = 1


class QuestInfo(Enum):
    ShowMonster = 0
    HideMonster = 1


class MonsterAmount(Enum):
    AlwaysOne = 0
    AlwaysMultiple = 1
    RandomWeighted = 2
    RandomCompletely = 3
    HunterMadness = 4


class InlcudePostgame(Enum):
    Include = 0
    Exclude = 1

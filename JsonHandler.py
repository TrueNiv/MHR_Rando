import os
import json

def ImportQuest(path):
    with open(path, 'r', encoding="utf-8") as j:
        data = json.load(j)
    return data

def ExportQuest(path, data):
    with open(path, 'w') as j:
        json.dump(data, j)
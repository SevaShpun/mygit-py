import crud
import json
import os


class Functions(object):

    def __init__(self, user_id):
        self.user_id = user_id
        self.result_down = "└───────────────────────────"

    def count_files(self, dir="db"):
        return len([1 for x in list(os.scandir(dir)) if x.is_file()])

    def Pretty_Json(self, inputdata):
        with inputdata as complex_data:
            data = complex_data.read()
            z = json.loads(data)
        return json.dumps(z[inputdata], indent=4, sort_keys=True)

    def Informer(self):
        os.system('cls')
        user = crud.mCRUD(self.user_id)
        return f"""
┌───────────────────────────
│      шахты : {user.json_load()["lvl"]["gold"]}
│  лесопилки : {user.json_load()["lvl"]["wood"]}
│каменоломня : {user.json_load()["lvl"]["stone"]}
│      ферма : {user.json_load()["lvl"]["food"]}
├───────────────────────────
│     золото : {user.json_load()["res"]["gold"]}
│  древесина : {user.json_load()["res"]["wood"]}
│     камень : {user.json_load()["res"]["stone"]}
│        еда : {user.json_load()["res"]["food"]}
├───────────────────────────
│ 1. Добыть золото
│ 2. Добыть дерево
│ 3. Добыть камень
│ 4. Собирать урожай
│ 5. Улучшить шахту
│ 6. Улучшить лесопилку
│ 7. Улучшить каменоломню
│ 8. Улучшить ферму
│
│ 0. Закрыть игру
{self.result_down}"""

    def Mining(self, mine=""):
        db = crud.mCRUD(self.user_id)
        user = db.json_load()
        res = 0
        food = 0
        if mine == "gold":
            res = 2
            food = user["lvl"][mine] + 3
        elif mine == "wood":
            res = 2
            food = user["lvl"][mine] + 1
        elif mine == "stone":
            res = 2
            food = user["lvl"][mine] + 2
        elif mine == "food":
            res = 2
            food = 0

        if user["res"]["food"] - food > 0:
            user["res"]["food"] -= food
            user["res"][mine] += user["lvl"][mine] * res
            db.json_save(user)
            self.result_down = "└───────────────────────────"
        else:
            self.result_down = """├───┬───────────────────┬──┐
│   │ недостаточно еды  │  │
└───┴───────────────────┴──┘"""
        return ""

    def Building(self, build=""):
        db = crud.mCRUD(self.user_id)
        user = db.json_load()
        res_gold = user["res"]["gold"]
        res_wood = user["res"]["wood"]
        res_stone = user["res"]["stone"]
        res_food = user["res"]["food"]
        build_need = {
            "gold": {"gold": 1000, "wood": 700, "stone": 800, "food": 200},
            "wood": {"gold": 700, "wood": 400, "stone": 500, "food": 120},
            "stone": {"gold": 800, "wood": 600, "stone": 700, "food": 150},
            "food": {"gold": 600, "wood": 300, "stone": 400, "food": 100}
        }
        need_res_gold = build_need[build]["gold"] * user["lvl"][build]
        need_res_wood = build_need[build]["wood"] * user["lvl"][build]
        need_res_stone = build_need[build]["stone"] * user["lvl"][build]
        need_res_food = build_need[build]["food"] * user["lvl"][build]

        if res_gold >= need_res_gold and res_wood >= need_res_wood and res_stone >= need_res_stone and res_food >= need_res_food:
            self.result_down = "└───────────────────────────"
            user["lvl"][build] += 1
            user["res"]["gold"] -= need_res_gold
            user["res"]["wood"] -= need_res_wood
            user["res"]["stone"] -= need_res_stone
            user["res"]["food"] -= need_res_food
            db.json_save(user)
        else:
            self.result_down = """├───────────────────────────
│        требуется ресурсов
│золото:{} камень:{}
│дерево:{} еда:{}
└───────────────────────────""".format(str(need_res_gold), str(need_res_wood), str(need_res_stone), str(need_res_food))
        return

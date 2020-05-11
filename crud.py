import funcs
import json
import os

class mCRUD(object):

    def __init__(self, user_id):
        self.user_id = user_id
        logic = funcs.Functions(self.user_id)
        self.struct = '''{
    "id": uid,
    "res": {
        "gold": 0,
        "wood": 0,
        "stone": 0,
        "food": 1
    },
    "lvl": {
        "gold": 1,
        "wood": 1,
        "stone": 1,
        "food": 1
    },
    "state": "work"
}'''.replace('uid', str(self.user_id))

    def registration(self):
        logic = funcs.Functions(self.user_id)
        if os.path.exists("db/"+str(self.user_id)+".json"):
            hello =  'Выберите действие!'
        else:
            hello = "Вы успешно зарегистрированы!"
            with open("db/"+str(self.user_id)+".json","a+") as f:
                f.write(self.struct)
                f.close()
        return hello

    def json_load(self):
        try:
            with open("db/"+str(self.user_id)+".json") as complex_data:
                data = complex_data.read()
        except:
            self.registration()
            with open("db/"+str(self.user_id)+".json") as complex_data:
                data = complex_data.read()
        return json.loads(data)

    def json_save(self, json_loads):
        json_dumps = json.dumps(json_loads, indent=2)
        if os.path.exists("db/"+str(self.user_id)+".json"):
            with open("db/"+str(self.user_id)+".json","w+") as f:
                f.write(json_dumps)
                f.close()
        return ""

    def getData(self, userid=False):
        uid = False
        result = None;
        if userid==False:
            uid = self.user_id
            if os.path.exists("db/"+str(uid)+".json"):
                with open("db/"+str(uid)+".json") as complex_data:
                    result = json.dumps(json.loads(complex_data.read()), indent=4, sort_keys=True)
            else:
                result = f"Пользователь '{uid}' не найден"
        else:
            uid = userid
            if os.path.exists("db/"+str(uid)+".json"):
                with open("db/"+str(userid)+".json") as complex_data:
                    result = json.dumps(json.loads(complex_data.read()), indent=4, sort_keys=True)
            else:
                result = f"Пользователь '{uid}' не найден"
        return result

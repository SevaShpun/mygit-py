import json
import funcs
import crud
import os

if __name__ == "__main__":
    user_id = 1001

    logic = funcs.Functions(user_id)
    user = crud.mCRUD(user_id)

    state = user.json_load()["state"]

    run = True
    while run:
        print(logic.Informer())
        cmd = input("Введите команду: ")
        if cmd == "0": run = False
        if cmd == "1": print(logic.Mining('gold'))
        if cmd == "2": print(logic.Mining('wood'))
        if cmd == "3": print(logic.Mining('stone'))
        if cmd == "4": print(logic.Mining('food'))
        if cmd == "5": print(logic.Building('gold'))
        if cmd == "6": print(logic.Building('wood'))
        if cmd == "7": print(logic.Building('stone'))
        if cmd == "8": print(logic.Building('food'))

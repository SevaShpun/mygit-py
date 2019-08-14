import json

struct = {
    "name": "Dev",
    "age": 0,
    "city": "Moscow",
}

# Вывод данных
print(struct)
for x in struct:
    print(f"{x}: {struct[x]}")
print(struct['name'])

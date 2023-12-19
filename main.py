import defs as d

while True:
    d.gameLoop()

    if d.hp <= 0:
        if input("Хочешь начать сначала? (Да/Нет):").lower() == "да":
            d.initGame(6, 5, 2, 1)
        else:
            break
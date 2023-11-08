import random as r

hp = 0
coins = 0
damage = 0

def printParameters():
    print("У тебя {0} жизней, {1} монет и {2} урона.".format(hp, coins, damage))

def printHp():
    print(f"У тебя {hp} жизней.")

def printCoins():
    print(f"У тебя {coins} монет.")

def printDamage():
    print(f"У тебя {damage} урона.")

def meetShop():
    global hp
    global coins
    global damage

    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            return True
        else:
            print("Нужно больше золота!")
            return False

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5) * weaponLvl
    weapons = ["Эльфийский лук", "Меч паладина", "Дворфский топор", "Щит и булава"]
    weaponRarities = ["Старый", "Добротный", "Великолепный"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponCost = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)

    oneHpCost = 5
    threeHpCost = 12

    print("Ты встретил торговца...")
    printParameters()

    while input("Ты решаешь...\n Зайти/Уйти:").lower() == "зайти":
        print(f"1) Малый амулет здоровья(+1 hp) - {oneHpCost} монет.")
        print(f"2) Большой здоровья(+3 hp) - {threeHpCost} монет.")
        print("3) {0} {1} - {2} монет.".format(weaponRarity, weapon, weaponCost))

        choice = input("Что хочешь приобрести?\n")
        if choice == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
        elif choice == "2":
            if buy(threeHpCost):
                hp += 3
                printHp()
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        else:
            print("Я такое не продаю.")
        printParameters()
def initGame(initHp, initCoins, initDmg):
    global hp
    global coins
    global damage

    hp = initHp
    coins = initCoins
    damage = initDmg

    print("Ты отправился в странствие навстречу приключениям и опасностям. Удачного путешествия!")
    printParameters()

def gameLoop():
    situation = r.randint(0, 10)
    if situation == 0:
        meetShop()
    elif situation == 1:
        input("Monster")
    else:
        input("Блуждаю...")

initGame(3, 5, 1)

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала? (Да/Нет):").lower() == "да":
            initGame(3, 5, 1)
        else:
            break
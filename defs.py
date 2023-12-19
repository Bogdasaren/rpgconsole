import random as r

lvl = 0
hp = 0
coins = 0
damage = 0

def printParameters():
    print("У тебя {0} уровень, {1} жизней, {2} монет и {3} урона.".format(lvl, hp, coins, damage))

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
                damage = damage + weaponDmg
                printDamage()
        else:
            print("Я такое не продаю.")
        lvl_define()
        printParameters()

def meetMonster():
    global hp, coins, lvl

    monsterLvl = r.randint(1, 4)
    monsterHp = monsterLvl * r.randint(1, 2)
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Giant Firefly", "Chimera", "Young Ciclop", "Giant Spider", "Lurker"]
    monster = r.choice(monsters)

    print("""Ох чёрт... Ты нарвался на монстра!
    Враг --> {0} {1} уровня, у него {2} здоровья и {3} урона.""".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()

    while monsterHp > 0:
        choice = input("""Что решаешь?
        АТАКА/Тикаем -->""").lower()

        if choice == "атака":
            monsterHp -= damage
            print("""Отличный удар!
            У чудища осталось""", monsterHp, "жизней.")
        elif choice == "тикаем":
            chance = r.randint(0, 1)
            if chance == 0:
                print("Ты сбежал... Какой позор... Чтож, отделался лёгким испугом.")
                break
            else:
                print("Кажется на завтрак эта тварь съела Усэйн Болта. Ты станешь отличным вторым блюдом...")
                hp = -1
                break

        else:
            continue

        if monsterHp > 0:
            hp -= monsterDmg
            print("А он не промах! Атаковал тебя! Это было больно, у тебя", hp, "здоровья")

        if hp <= 0:
            break
    else:
        loot = r.randint(0,2) + monsterLvl
        coins += loot
        print("Ты завалил эту тварь! Заработал немного шекелей -->", loot)
        printCoins()
        lvl_define()

def meetBandit():
    global hp, coins, lvl

    banditLvl = r.randint(1, 3)
    banditHp = banditLvl * r.randint(1, 2)
    banditDmg = banditLvl * 2 - 1
    bandits = ["Robber", "Forest Bandit", "Asassin", "Looter"]
    bandit = r.choice(bandits)

    print("""На своём пути ты встретил разбойника...
    Враг --> {0} {1} уровня, у него {2} здоровья и {3} урона.""".format(bandit, banditLvl, banditHp, banditDmg))
    printParameters()

    while banditHp > 0:
        choice = input("""Что решаешь?
        АТАКА/Тикаем -->""").lower()

        if choice == "атака":
            banditHp -= damage
            print("""Отличный удар!
            У врага осталось""", banditHp, "жизней.")
        elif choice == "тикаем":
            chance = r.randint(0, 1)
            if chance == 0:
                print("Тебе удалось его оглушить! Ты скрылся в тени... Нужно перевести дух.")
                break
            else:
                print("Он кинул в тебя кинжал, ты упал на землю и враг догнал тебя. Ты казнён.")
                hp = -1
                break

        else:
            continue

        if banditHp > 0:
            hp -= banditDmg
            print("Неплохо дерётся для такого отброса! ТЫ пропустил удар! У тебя осталось", hp, "здоровья")

        if hp <= 0:
            break
    else:
        loot = r.randint(0,2) + banditLvl
        coins += loot
        print("""Враг повержен. Думаю это ему больше не понадобится.
        Обыскав его, ты нашёл немного золота -->""", loot)
        printCoins()
        lvl_define()

def find_item():
    global hp, coins, damage, lvl

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 2) * weaponLvl
    weapons = ["Длинный лук", "Железный меч", "Топор берсерка", "Копье королевского гвардейца"]
    weaponRarities = ["Старый", "Добротный", "Великолепный"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weapon = r.choice(weapons)


    print("""Что это там за деревом?
Ты подходишь ближе и видишь тело солдата...
Жалко конечно этого добряка...
Переведя взгляд в сторону ты видишь, что рядом лежит его оружие. Ему это явно больше не нужно.
Ты получаешь {0} {1}""".format(weaponRarity, weapon))

    damage = damage + weaponDmg
    lvl_define()
    printParameters()

def find_altar():
    global hp

    print("""На пути тебе попался каменный алтарь. Всё исписано древними рунами. Это язык древних народов, не прочесть.
Кажется, раньше маги проводили здесь свои обряды. 
В чаше алтаря налита какая-то жидкость. Стоит ли рисковать?""")

    choice = input("""Что будешь делать?
    Выпить/Уйти --> """).lower()

    if choice == "выпить":
        chance = r.randint(0, 2)
        if chance == 0:
            print("""Кажется делать этого не стоило. Что-то поплохело.""")
            hp -= 2
            printParameters()
        else:
            print("""Видимо это было мощное целебное зелье.
            Ты чувствуешь себя гораздо лучше.""")
            hp += r.randint(1, 3)
            printParameters()


def initGame(initHp, initCoins, initDmg, initLvl):
    global hp
    global coins
    global damage
    global lvl

    hp = initHp
    coins = initCoins
    damage = initDmg
    lvl = initLvl

    print("Ты отправился в странствие навстречу приключениям и опасностям. Удачного путешествия!")
    printParameters()

def trap_event():
    global hp
    global coins
    global damage
    global lvl
    
    print("Вы попали в ловушку!")
    
    # Генерация случайного события в ловушке
    trap_type = r.choice(["damage", "lose_coins",])
    
    if trap_type == "damage":
        damage_amount = 1
        hp -= damage_amount
        print(f"Вы потеряли {damage_amount} здоровья. Ваше текущее здоровье: {hp}")
    
    elif trap_type == "lose_coins":
        coins_loss = r.randint(1, 2)
        coins -= coins_loss
        print(f"Вы потеряли {coins_loss} монет. У вас осталось {coins} монет")
    
    else:
            print("У вас уже 0 уровень, поэтому ничего не произошло.")

    # Проверка на отрицательное здоровье
    if hp <= 0:
        print("Ваши здоровье закончилось. Игра окончена.")

printParameters()

def komar_event():
    
    print("Бродя по этому миру вы наткнулись на кота!")

    komar_choice = input('Чтобы погладить, введите "пат-пат"\n ---> ').lower()

    if komar_choice == 'пат-пат':
        print('Вы погладили Комара и духовно выросли')
    else:
        print('Вы ужасный человек.')

#Игровые события
def lvl_define():
    global damage, lvl
    lvl = int(damage**0.5)


def gameLoop():
    situation = r.randint(0, 15)
    if situation == 0:
        meetShop()
    elif situation == 1:
        meetMonster()
    elif situation == 2:
        meetBandit()
    elif situation == 3:
        find_item()
    elif situation == 4:
        find_altar()
    elif situation == 10:
        trap_event()
    elif situation == 11:
        komar_event()
    else:
        input("Блуждаю...")

initGame(6, 5, 2, 1)

# while True:
#     gameLoop()
#
#     if hp <= 0:
#         if input("Хочешь начать сначала? (Да/Нет):").lower() == "да":
#             initGame(6, 5, 2, 1)
#         else:
#             break
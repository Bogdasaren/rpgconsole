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

    monsterLvl = lvl + 1
    monsterHp = (damage + monsterLvl) * 1.5
    monsterDmg = monsterHp * 0.5
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
            dodge_chance = r.randint(1, 3)
            if dodge_chance == 1:
                print("Отличная реакция!! Уклонился от удара!")
            else:
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

    banditLvl = lvl + 1
    banditHp = (damage + banditLvl) * 1.5
    banditDmg = banditHp * 0.5
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
            dodge_chance = r.randint(1, 3)
            if dodge_chance == 1:
                print("Отличная реакция!! Уклонился от удара!")
            else:
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

def barricade():
    global hp

    choice = input("""Проходя между горами, на вашем пути попадается обвал.
    Обойти/Перелезть-->""").lower()
    if choice == "обойти":
        anoth_road = r.randint(1, 3)
        if anoth_road == 1:
            print("Вы нашли обходную дорогу, но что это там за звуки?..")
            meetMonster()
        else:
            print("Вы нашли обходную дорогу.")
    elif choice == "перелезть":
        injury = r.randint(1, 3)
        if injury == 1:
            print("Перелезая через обвалившиеся камни, вы запинаетесь и больно падаете. Но обвал преодолён")
            hp -= 1
            printParameters()
        else:
            print("Вы успешно преодолели преграду")

def victim():
    global hp, damage, lvl

    choice = input("""Вы находите алтарь для жертвоприношений и старинную книгу рядом.
    В книге написано, что это место священно и боги одарят силой каждого кто осмелится пожертвовать собой ради них.
        Рискнуть/Уйти-->""").lower()
    if choice == "рискнуть":
        chance = r.randint(1, 3)
        if chance == 1:
            print("""Проведя обряд, вы теряете сознание, но вскоре приходите в себя и чувствуете явный прилив сил.""")
            hp += r.randint(3, 5)
            damage += r.randint(3,5)
            lvl_define()
            printParameters()
        else:
            print("""Проведя обряд, вы теряете сознание... И больше не просыпаетесь.
            Кажется боги вам не благоволят""")
            hp = -1

def storm():
    global hp, coins
    choice = input("""Идя по горам вы попадаете в сильную бурю. 
    Вы можете рискнуть и пойти дальше или попытаться найти укрытие.
    Идти/Прятаться-->""").lower()
    if choice == "идти":
        chance = r.randint(1, 3)
        if chance == 1:
            print("""Вы перебрались через гору и выбрались из стихии.
            По пути вы нашли редкий цветок, который в ближайшей деревне продали алхимику, заработав немного денег.""")
            coins += r.randint(3, 5)
            printParameters()
        else:
            print("""Эх... Дурак и ветер... Битва со стихией прошла не в твою пользу.""")
            hp = -1
    elif choice == "прятаться":
        print("Ты успешно переждал бурю, можно идти дальше")

def wolf_trouble():
    global hp, coins, damage, lvl
    choice = input("""Вы слышите впереди крики и волчий вой. 
    Вы решаете:
    Помочь/Уйти-->""").lower()
    if choice == "помочь":
        print("""Вы бежите на звуки и видите парня и девушку. Перед ними разъярённый волк и труп растерзанный этим волком.
        Вы выхватываете меч и бросаетесь на волка!""")
        wolfLvl = lvl + 1
        wolfHp = (damage + wolfLvl) * 1.5
        wolfDmg = wolfHp * 0.5
        print("""У волка {0} уровень, у него {1} здоровья и {2} урона.""".format( wolfLvl, wolfHp, wolfDmg))
        printParameters()

        while wolfHp > 0:
            choice = input("""Что решаешь?
                АТАКА/Тикаем -->""").lower()
            if choice == "атака":
                wolfHp -= damage
                print("""Отличный удар!
                    У твари осталось""", wolfHp, "жизней.")
            elif choice == "тикаем":
                chance = r.randint(0, 1)
                if chance == 0:
                    print("Ты дал этим людям надежду и бросил их! Ты хуже люого чудовища в этом жестоком мире")
                    break
                else:
                    print("Не стоило бросать этих людей. Ты стал закуской")
                    hp = -1
                    break
            else:
                continue

            if wolfHp > 0:
                dodge_chance = r.randint(1, 3)
                if dodge_chance == 1:
                    print("Отличная реакция!! Уклонился от удара!")
                else:
                    hp -= wolfDmg
                    print("А он не промах! Атаковал тебя! Это было больно, у тебя", hp, "здоровья")
            if hp <= 0:
                break
        else:
            reward = input("""Девушка смотрит на тебя со слезами на глазах и не может произнести ни слова.
        Мужчина подходит к тебе, благодарит и протягивает кошель с золотом.
        Взять/Отказаться""").lower()
            if reward == "взять":
                coins += r.randint(3, 5)
                printParameters()
            elif reward == "отказаться":
                print("""Мужчина хвалит тебя за твой выбор, но говорит, что не может оставить тебя без награды.
                Он достаёт из-за пазухи амулет и даёт его тебе.
                Ты получаешь 3 здоровья""")
                hp += 3
            lvl_define()
            printParameters()
    else:
        print("Своя шкура дороже.")

def trap_event():
    global hp
    global coins
    global damage
    global lvl

    print("Вы попали в ловушку!")

    trap_type = r.choice(["damage", "lose_coins", ])

    if trap_type == "damage":
        damage_amount = 1
        hp -= damage_amount
        print(f"Вы потеряли {damage_amount} здоровья. Ваше текущее здоровье: {hp}")

    elif trap_type == "lose_coins":
        coins_loss = r.randint(1, 2)
        coins -= coins_loss
        print(f"Вы потеряли {coins_loss} монет. У вас осталось {coins} монет")

    printParameters()

def komar_event():
    global hp
    print("Бродя по этому миру вы наткнулись на кота!")

    komar_choice = input('Чтобы погладить, введите "пат-пат"\n ---> ').lower()

    if komar_choice == 'пат-пат':
        print('Вы погладили Комара и духовно выросли')
        inner_growth = r.randint(1, 2)
        hp += inner_growth
        print(f"Вы получили {inner_growth} здоровья")
        printParameters()
    else:
        print('Вы ужасный человек.')
def initGame(initHp, initCoins, initDmg, initLvl):
    global hp, coins, damage, lvl

    hp = initHp
    coins = initCoins
    damage = initDmg
    lvl = initLvl

    print("Ты отправился в странствие навстречу приключениям и опасностям. Удачного путешествия!")
    printParameters()

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
    elif situation == 5:
        barricade()
    elif situation == 6:
        victim()
    elif situation == 7:
        storm()
    elif situation == 8:
        wolf_trouble()
    elif situation == 9:
        trap_event()
    elif situation == 10:
        komar_event()
    else:
        input("Блуждаю...")

initGame(6, 5, 2, 1)

import random


def attack(monster_hp):
    damage = random.randint(10, 25)
    monster_hp -= damage
    if monster_hp < 0:
        monster_hp = 0
    print("Вы нанесли монстру", damage, "урона!")
    return monster_hp

def monster_attack(player_hp):
    damage = random.randint(5, 20)
    player_hp -= damage
    if player_hp < 0:
        player_hp = 0
    print("Монстр нанёс вам", damage, "урона!")
    return player_hp

def heal(player_hp):
    if player_hp == 100:
        print("Здоровье уже полное!")
    else:
        player_hp = min(player_hp + 15, 100)
        print("Вы восстановили здоровье!")
    return player_hp

def show_status(player_hp, monster_hp):
    print("\nВаше здоровье:", player_hp)
    print("Здоровье монстра:", monster_hp)

def main():
    player_hp = 100
    monster_hp = 100

    while player_hp > 0 and monster_hp > 0:
        print("\n===== БИТВА С МОНСТРОМ =====")
        print("1. Атаковать")
        print("2. Восстановить здоровье")
        print("3. Посмотреть состояние боя")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            monster_hp = attack(monster_hp)
        if monster_hp > 0:
            player_hp = monster_attack(player_hp)
        elif choice == "2":
            old_hp = player_hp
            player_hp = heal(player_hp)
        if player_hp > old_hp:
            monster_hp_check = monster_attack(player_hp)
            player_hp = monster_hp_check
        elif choice == "3":
            show_status(player_hp, monster_hp)
        elif choice == "4":
            print("Вы покинули игру")
            break
        else:
            print("Неверный пункт меню")

    if player_hp <= 0:
        print("\nВы проиграли! Монстр победил.")
    elif monster_hp <= 0:
        print("\nПоздравляем! Вы победили монстра.")


main()
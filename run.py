from lib.player import Player
import random

outcomes = {
    1: "You're bleeding everywhere.",
    2: "You're limping",
    3: "You both hit each other, but you're even",
    4: "You hit the monster in the chin and he sees stars in his eyes.",
    5: "The monster fell and is flailing.",
    6: "A direct hit!"
}

monsters=[
        ("BORG", "It wants you to join its commune", 6),
        ("GOLLUM", "Where's my precious ring!!!", 10),
        ("VAMPIRE", "I want to suck your life blood", 20), 
]



if __name__ == "__main__":
    player = Player(10)
    player_name = input("Hello! What is your name? ")
    player.set_name(player_name)
    print("* * * * * * * * * * * * * * * * * * * *")
    print("* * * * * * * * * * * * * * * * * * * *")
    print("* * * * * * * * * * * * * * * * * * * *")
    print(f"Welcome {player.name} to Dungeonville! You will face increasingly difficult monsters. Good luck!")
    print("* * * * * * * * * * * * * * * * * * * *")
    print("* * * * * * * * * * * * * * * * * * * *")
    print("* * * * * * * * * * * * * * * * * * * *")

    while player.in_game:
        message = input("Hit any to start game or type 'quit' to run away.\n")
        if message == "quit":
            print("Roger that, thanks for playing!")
            player.in_game = False
        else:
            for choice in monsters:
                if not player.in_game:
                    print("You died. Game over.")
                    break
                score = choice[2]
                monster = Player(score)
                monster_type = choice[0]
                print("A {} has appeared. {}".format(monster_type, choice[1]))
                while monster.in_game and player.in_game:
                    
                    attack_join = input("Attack or join? ")
                    if attack_join.lower() == 'attack':
                        die = random.choice(range(1,7))
                        print("You rolled a {}!".format(die))
                        print(outcomes[die])
                        monster.score -= die
                        player.score -= (6-die)
                        if player.score <=0:
                            player.in_game=False     
                        elif monster.score<=0:
                            monster.in_game=False
                            print("You killed the {}! Nice!".format(monster_type))
                        else:
                            pass
                    elif attack_join.lower() == 'join':
                        die = random.choice((range(1,7)))
                        if die == 6:
                            player.score += 1
                            print("The {} gave you food! Yum!".format(monster_type))
                        elif (1 < die) and (die < 6):
                            print("The {} sang you a song.".format(monster_type))
                        else:
                            player.score -= 1
                            print("The {} thinks you're liar You sustained 1 damage".format(monster_type))
                    else:
                        print("You must attack or join. Sorry.")
                        print("The {} is growling angrily.".format(monster_type))
                    print("monster",monster.score)
                    print("player",player.score)
                    print("\n\n")


            print(player.repeat(message))

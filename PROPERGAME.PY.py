import turtle
import random
from time import sleep

t = turtle.Turtle()


def playAgansitAI():
    # list start
    # player one list start
    player1 = {}
    player1["name"] = "oliver"
    player1Heath = 100
    player1Power = 10
    player1["health"] = player1Heath
    player1["power"] = player1Power
    print(player1)
    # AI list start/player one list end
    AI = {}
    aiHealth = 100
    aiPower = random.randint(1, 10)
    AI["name"] = "AI"
    AI["heatlh"] = aiHealth
    AI["power"] = aiPower
    print(AI)
    # list end
    # game loop start
    while aiHealth != 0 or player1heath != 0 or aiHealth > 0 or player1Heath > 0:
        aiPower = random.randint(1, 10)
        aiAttack = random.randint(1, 3)
        if aiAttack == 1:
            player1Heath -= aiPower
        if aiAttack == 2:
            player1Heath -= aiPower + 2
        if aiAttack == 3:
            aiPower = random.randint(1, 10)
        print("your helath = ", player1Heath)
        sleep(1)
        PlayerAttack = input("what attack would you like to do (slap, kick)?: ")
        if PlayerAttack == "slap":
            aiHealth = aiHealth - player1Power
            player1Power += 1
        if PlayerAttack == "kick":
            aiHealth = aiHealth - player1Power
            player1Power += 1
        if PlayerAttack == "win":
            aiHealth = aiHealth - aiHealth
        print("ai helth = ", aiHealth)

        if (
            aiHealth == 0
            or player1Heath == 0
            or player1Heath < 0
            or aiHealth < 0
            or player1Heath < 9
        ):
            break
    if player1Heath == 0 or player1Heath < 0:
        print("you lose")
    if aiHealth == 0 or aiHealth < 0:
        print("YOU WIN!!!!!!!!!")
        t.write("you win")


def play2Player():
    player1 = {}
    player1Health = 100
    askPlayer1 = input("what is your name player1?: ")
    player1["name"] = askPlayer1
    if askPlayer1 == "Oliver":
        player1Health = 10000
    player1Power = 10
    player2 = {}
    askPlayer2 = input("what is your name player2?: ")
    player2["name"] = askPlayer2
    player2Health = 100
    player2Power = 10
    while (
        player1Health != 0
        or player2Health != 0
        or player1Health < 0
        or player2Health < 0
    ):
        player1Attack = input(
            "what attack would player1 like to do (slap, kick, punch, double punch)?: "
        )
        if player1Attack == "slap":
            player2Health = player2Health - player1Power
            t.write("player1 slaps player2")
            sleep(2)
            t.reset()
        if player1Attack == "kick":
            player2Health = player2Health - 20
            t.write("player1 kicks player2")
            sleep(2)
            t.reset()
        if player1Attack == "punch":
            player2Health = player2Health - 5
            t.write("player1 punchs player2")
            sleep(2)
            t.reset()
        if player1Attack == "double punch":
            player2Health = player2Health - 25
            t.write("player1 double punches player2")
            sleep(2)
            t.reset()
        if player1Attack == "shoot":
            hitBody = random.randint(1, 6)
            if hitBody == 1:
                player2Health = player2Health - player2Health
                t.write("player1 shoots player2")
                sleep(2)
                t.reset()
        print("player2's health =", player2Health)

        sleep(1)
        player2Attack = input(
            "what attack would player2 like to do (slap, kick, punch, double punch)?: "
        )
        if player2Attack == "slap":
            player1Health = player1Health - player2Power
            t.write("player2 slaps player1")
            sleep(2)
            t.reset()
        if player2Attack == "kick":
            player1Health = player1Health - 20
            t.write("player2 kicks  player1")
            sleep(2)
            t.reset()
        if player2Attack == "punch":
            player1Health = player1Health - 5
            t.write("player2 punchs player1")
            sleep(2)
            t.reset()
        if player2Attack == "double punch":
            player1Health = player1Health - 25
            t.write("player2 double punches player1")
            sleep(2)
            t.reset()
        if player2Attack == "kill":
            killed = random.randint(1, 6)
            if killed == 1:
                player1Health = player1Health - player1Health
                t.write("player2 kills player1")
            sleep(2)
            t.reset()
        print("player1's health =", player1Health)
        if (
            player2Health == 0
            or player1Health == 0
            or player1Health < 0
            or player2Health < 0
            or player1Health < 9
        ):
            break
        if player1Health == 0 or player1Health < 0:
            print(askPlayer1, "lost")
            print(askPlayer2, "WINS")
    if player2Health == 0 or player2Health < 0:
        print(askPlayer2, "lost")

        print(askPlayer1, "WINS")


def play3Player():
    player1Health = 100
    player2Health = 100
    player3Health = 100
    if player1Health != 0 and player1Health > 0:
        player1Attack = input("what would you like to do  slap, kick, double punch?")
        player1AttackPlayer = input("which player would you like to hit")
        if player1Attack == "slap" and player1AttackPlayer == "player2":
            player2Health = player2Health - 10
            t.write("player1 slaps player2")
            sleep(2)
            t.reset()
        if player1Attack == "kick" and player1AttackPlayer == "player2":
            player2Health = player2Health - 10
            t.write("player1 kicks player2")
            sleep(2)
            t.reset()
        if player1Attack == "double punch" and player1AttackPlayer == "player2":
            player2Health = player2Health - 10
            t.write("player1 double punches player2")
            sleep(2)
            t.reset()
        if player1Attack == " " and player1AttackPlayer == "player2":
            player2Health = player2Health - 100
            t.write("player1  s player2")
            sleep(2)
            t.reset()
        if player1Attack == "slaps" and player1AttackPlayer == "player3":
            player3Health = player3Health - 10
            t.write("player1 kicks player3")
            sleep(2)
            t.reset()
        if player1Attack == "kick" and player1AttackPlayer == "player3":
            player3Health = player3Health - 10
            t.write("player1 kicks player3")
            sleep(2)
            t.reset()
        if player1Attack == "punch" and player1AttackPlayer == "player3":
            player3Health = player3Health - 10
            t.write("player1 kicks player3")
            sleep(2)
            t.reset()
        if player1Attack == "kick" and player1AttackPlayer == "player3":
            player3Health = player3Health - 10
            t.write("player1 kicks player3")
            sleep(2)
            t.reset()
        if player1Attack == " " and player1AttackPlayer == "player3":
            player2Health = player2Health - 100
            t.write("player1  s player3")
            sleep(2)
            t.reset()
    if player2Health != 0 and player2Health != 0:
        print('hello')



playGame = input("would you like to play agaisnt the ai or play with a freind (1/2)?: ")
if playGame == "1":
    playAgansitAI()
if playGame == "2":
    play2Player()

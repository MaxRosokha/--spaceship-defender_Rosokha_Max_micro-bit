def on_button_pressed_a():
    Player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def Shoot():
    global Missile, EnemyHealth
    Missile = game.create_sprite(Player.get(LedSpriteProperty.X),
        Player.get(LedSpriteProperty.Y))
    Missile.set(LedSpriteProperty.BRIGHTNESS, 25)
    for index in range(4):
        Missile.change(LedSpriteProperty.Y, -1)
        if Missile.is_touching(SpaceShip):
            EnemyHealth += -1
        basic.pause(100)
    Missile.delete()

def on_button_pressed_ab():
    Shoot()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def Summon_SpaceShip():
    global EnemyHealth, SpaceShip, KilledSpaceShips
    EnemyHealth = randint(1, 3)
    SpaceShip = game.create_sprite(0, randint(0, 2))
    SpaceShip.set(LedSpriteProperty.BRIGHTNESS, 60)
    for index2 in range(randint(0, 4)):
        SpaceShip.change(LedSpriteProperty.X, 1)
        basic.pause(500)
    while EnemyHealth > 0:
        if EnemyCanShoot == 1:
            basic.pause(randint(200, MaximumTime))
            EnemyAttack()
    SpaceShip.delete()
    KilledSpaceShips += 1
def EnemyAttack():
    global EnemyCanShoot, EnemyMissile, Health
    EnemyCanShoot = 0
    EnemyMissile = game.create_sprite(SpaceShip.get(LedSpriteProperty.X),
        SpaceShip.get(LedSpriteProperty.Y))
    EnemyMissile.set(LedSpriteProperty.BRIGHTNESS, 25)
    for index3 in range(4):
        EnemyMissile.change(LedSpriteProperty.Y, 1)
        basic.pause(100)
    if EnemyMissile.is_touching(Player):
        Health += -1
    EnemyMissile.delete()
    EnemyCanShoot = 1
EnemyMissile: game.LedSprite = None
KilledSpaceShips = 0
MaximumTime = 0
SpaceShip: game.LedSprite = None
Missile: game.LedSprite = None
EnemyCanShoot = 0
EnemyHealth = 0
Player: game.LedSprite = None
Player = game.create_sprite(2, 4)
Health = 3
EnemyHealth = 1
EnemyCanShoot = 1
Level = 1

def on_forever():
    basic.pause(randint(200, 3000))
    Summon_SpaceShip()
basic.forever(on_forever)

def on_forever2():
    global MaximumTime
    if Level == 1:
        MaximumTime = 3000
basic.forever(on_forever2)

def on_forever3():
    if Health < 1:
        game.set_score(KilledSpaceShips)
        game.game_over()
    if EnemyHealth < 1:
        SpaceShip.delete()
basic.forever(on_forever3)

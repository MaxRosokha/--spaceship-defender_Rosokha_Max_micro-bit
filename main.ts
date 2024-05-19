function Summon_SpaceShip () {
    EnemyHealth = randint(1, 3)
    SpaceShip = game.createSprite(0, randint(0, 2))
    SpaceShip.set(LedSpriteProperty.Brightness, 60)
    for (let index = 0; index < randint(0, 4); index++) {
        SpaceShip.change(LedSpriteProperty.X, 1)
        basic.pause(500)
    }
    while (EnemyHealth > 0) {
        if (EnemyCanShoot == 1) {
            basic.pause(randint(200, MaximumTime))
            EnemyAttack()
        }
    }
    SpaceShip.delete()
    KilledSpaceShips += 1
}
input.onButtonPressed(Button.A, function () {
    Player.change(LedSpriteProperty.X, -1)
})
function Shoot () {
    Missile = game.createSprite(Player.get(LedSpriteProperty.X), Player.get(LedSpriteProperty.Y))
    Missile.set(LedSpriteProperty.Brightness, 25)
    for (let index = 0; index < 4; index++) {
        Missile.change(LedSpriteProperty.Y, -1)
        if (Missile.isTouching(SpaceShip)) {
            EnemyHealth += -1
        }
        basic.pause(100)
    }
    Missile.delete()
}
input.onButtonPressed(Button.AB, function () {
    Shoot()
})
input.onButtonPressed(Button.B, function () {
    Player.change(LedSpriteProperty.X, 1)
})
function EnemyAttack () {
    EnemyCanShoot = 0
    EnemyMissile = game.createSprite(SpaceShip.get(LedSpriteProperty.X), SpaceShip.get(LedSpriteProperty.Y))
    EnemyMissile.set(LedSpriteProperty.Brightness, 25)
    for (let index = 0; index < 4; index++) {
        EnemyMissile.change(LedSpriteProperty.Y, 1)
        basic.pause(100)
    }
    if (EnemyMissile.isTouching(Player)) {
        Health += -1
    }
    EnemyMissile.delete()
    EnemyCanShoot = 1
}
let EnemyMissile: game.LedSprite = null
let Missile: game.LedSprite = null
let KilledSpaceShips = 0
let MaximumTime = 0
let SpaceShip: game.LedSprite = null
let EnemyCanShoot = 0
let EnemyHealth = 0
let Player: game.LedSprite = null
Player = game.createSprite(2, 4)
let Health = 3
EnemyHealth = 1
EnemyCanShoot = 1
let Level = 1
basic.forever(function () {
    basic.pause(randint(200, 3000))
    Summon_SpaceShip()
})
basic.forever(function () {
    if (Level == 1) {
        MaximumTime = 3000
    }
})
basic.forever(function () {
    if (Health < 1) {
        game.setScore(KilledSpaceShips)
        game.gameOver()
    }
    if (EnemyHealth < 1) {
        SpaceShip.delete()
    }
})

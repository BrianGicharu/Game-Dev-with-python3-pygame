import pygame as pg

x = pg.init()

game_W = pg.display.set_mode((800, 600))
pg.display.set_caption("Game Development")

exitGame = False
gameOver = False

while not exitGame:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exitGame = True

pg.quit()
quit()
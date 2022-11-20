import pygame as pg

BLACK = (0,0,0)

screen = pg.display.set_mode((1200,800))
screen.fill((255,255,255))

def drawCircle(screen, x, y):
    pg.draw.circle( screen, BLACK, ( x, y ), 5 )

isPressed = False
flag = True

while flag:
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type == pg.QUIT or keys[pg.K_q]:
            #se clicar em fechar, fecha o jogo
            pg.quit()
            flag = False
            #sys.exit() 
        elif event.type == pg.MOUSEBUTTONDOWN:
            isPressed = True
        elif event.type == pg.MOUSEBUTTONUP:
            isPressed = False
        elif event.type == pg.MOUSEMOTION and isPressed == True:               
            ( x, y ) = pg.mouse.get_pos()
            drawCircle(screen, x, y)
    if flag:
        pg.display.flip()
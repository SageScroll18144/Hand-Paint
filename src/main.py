import pygame as pg

BLUE = (0,0,255)

screen = pg.display.set_mode((500,500))

def drawCircle(screen, x, y):
    pg.draw.circle( screen, BLUE, ( x, y ), 5 )

isPressed = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            #se clicar em fechar, fecha o jogo
            pg.quit()
            sys.exit() 
        elif event.type == pg.MOUSEBUTTONDOWN:
            isPressed = True
        elif event.type == pg.MOUSEBUTTONUP:
            isPressed = False
        elif event.type == pg.MOUSEMOTION and isPressed == True:               
            ( x, y ) = pg.mouse.get_pos()
            drawCircle(screen, x, y)
    pg.display.flip()
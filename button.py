import pygame as pg
pg.init()
screen = pg.display.set_mode([1000]*2)

class button():
    def __init__(self,centerX,centerY,height,colour,text):
        self.centerX = centerX
        self.centerY = centerY
        self.height = height
        self.y = self.centerY - 0.5 * self.height
        self.colour = colour
        self.text = text
        self.click = 0
        self.active = True
        self.pos = pg.mouse.get_pos()
        self.font = pg.font.SysFont('Calibri', self.height, True, False)
        self.renderedText = self.font.render(self.text, True, (255,255,255))
        self.textWidth = self.renderedText.get_width()
        self.textHeight = self.renderedText.get_height()
        self.width = self.textWidth + 10
        self.x = self.centerX - 0.5 * self.width
        self.button = pg.rect.Rect([self.x,self.y,self.width,self.height])
        self.textX = self.x + 0.5 * self.width - 0.5 * self.textWidth
        self.textY = self.y + 0.5 * self.height - 0.5 * self.textHeight + 3

    def drawButton(self):
        pg.draw.rect(screen, self.colour, self.button)
        screen.blit(self.renderedText,[self.textX,self.textY])
        
    def isPressed(self):
        self.pos = pg.mouse.get_pos()
        self.click = pg.mouse.get_pressed()[0]
        if self.button.collidepoint(self.pos) and self.click == 1 and self.active == True:
            self.active = False
            return(True)
        elif self.click == 0:
            self.active = True
            return(False)
        else:
            return(False)
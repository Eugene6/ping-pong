import sys

from pygame import *
import json
import os


init()
window = display.set_mode((600, 400))
display.set_caption("Menu")
main_font = font.Font("Houseprotein-Regular.ttf", 30)

class Button:
    def __init__(self, x, y, width, height, color, text, text_color=(0, 0, 0)):
        self.rect = Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font.Font(None, 28)

    def draw(self):
       draw.rect(window, self.color, self.rect)
       text_surf = self.font.render(self.text, True, self.text_color)
       text_rect = text_surf.get_rect(center=self.rect.center)
       window.blit(text_surf, text_rect)

    def is_clicked(self, event):
        return event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

# --- Кнопки ---
play_button = Button(200, 125, 200, 50, (66, 123, 194), "Play")
exit_button = Button(200, 240, 200, 50, (66, 123, 194), "Exit")


def menu():
    bgmenu = transform.scale(image.load("PINGPANG.png"), display.get_surface().get_size())
    runnning = True
    mixer.music.load("gamemusic.mp3")
    mixer.music.play(-1)

    play_button.rect.x = display.get_surface().get_size()[0] // 2 - play_button.rect.width // 2
    play_button.rect.y = display.get_surface().get_size()[1] // 3 + 50
    exit_button.rect.x = display.get_surface().get_size()[0] // 2 - exit_button.rect.width // 2
    exit_button.rect.y = display.get_surface().get_size()[1] // 3 + 150

    while runnning:

        for i in event.get():
            if i.type == QUIT:
                quit()
                sys.exit()
            if play_button.is_clicked(i):
                runnning = False
                mixer.music.stop()
            if exit_button.is_clicked(i):
                quit()
                sys.exit()

        window.blit(bgmenu, (0,0))
        play_button.draw()
        exit_button.draw()

        diff_text = main_font.render("PONG" , True, (0, 0, 0))
        window.blit(diff_text, (display.get_surface().get_size()[0] // 2 -50,100))

        display.update()

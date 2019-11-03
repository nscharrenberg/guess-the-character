import sys, os
import pygame
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
stdout = sys.__stdout__
stderr = sys.__stderr__
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

sys.stdout = stdout
sys.stderr = stderr

class ink(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, (self.x, self.y, self.x + self.width, self.y + self.height))

class grid(object):
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.length = rows + cols
        self.lines = []
        self.generateLines()
        pass

    def draw(self, canvas):
        for row in self.lines:
            for col in row:
                col.draw(canvas)

    def generateLines(self):
        x_spacing = self.width // self.cols
        y_spacing = self.height // self.rows
        self.lines = []

        for row in range(self.rows):
            self.lines.append([])
            for col in range(self.cols):
                self.lines[row].append(ink(x_spacing * col, y_spacing * row, x_spacing, y_spacing))

    def clicked(self, pos):
        t = pos[0]
        w = pos[1]
        g1 = int(t) // self.lines[0][0].width
        g2 = int(w) // self.lines[0][0].height

        return self.lines[g2][g1]

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                clicked = g.clicked(pos)
                clicked.color = (0, 0, 0)

            if pygame.mouse.get_pressed()[2]:
                try:
                    pos = pygame.mouse.get_pos()
                    clicked = g.clicked(pos)
                    clicked.colors = (255, 255, 255)
                except:
                    pass

        g.draw(win)
        pygame.display.update()

pygame.init()
width = height = 560
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw a Number")
g = grid(28, 28, width, height)
main()

pygame.quit()
quit()









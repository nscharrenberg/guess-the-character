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
    def __init__(self, x, y, width, height, scale):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.scale = scale
        self.neighbors = []

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, (self.x, self.y, self.x + self.width, self.y + self.height))

    def getNeighbors(self, canvas):
        col = self.x // self.scale
        row = self.y // self.scale

        col_count = 5
        row_count = 5

        # Get Horizontal Neighbors
        if row < col_count - 1: # Right
            self.neighbors.append(canvas.lines[row + 1][col])
        if row > 0: # Left
            self.neighbors.append(canvas.lines[row - 1][col])

        # Get Vertical Neighbors
        if col < row_count - 1: # Up
            self.neighbors.append(canvas.lines[row][col + 1])
        if col > 0:  # Down
            self.neighbors.append(canvas.lines[row][col - 1])

        # Get Diagnal Neighbors
        if col > 0 and row > 0: # Top Left
            self.neighbors.append(canvas.lines[row - 1][col - 1])
        if col + 1 < row_count and row > -1 and row - 1 > 0: # Bottom Left
            self.neighbors.append(canvas.lines[row - 1][col + 1])
        if row_count > col - 1 > 0 and row < col_count - 1: # Top Right
            self.neighbors.append(canvas.lines[row + 1][col -1])
        if col < row_count - 1 and row < col_count - 1: # Bottom Right
            self.neighbors.append(canvas.lines[row + 1][col + 1])

class grid(object):
    def __init__(self, rows, cols, width, height, scale):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.length = rows + cols
        self.lines = []
        self.scale = scale
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
                self.lines[row].append(ink(x_spacing * col, y_spacing * row, x_spacing, y_spacing, self.scale))

        for row in range(self.rows):
            for col in range(self.cols):
                self.lines[row][col].getNeighbors(self)

    def clicked(self, pos):
        g1 = int(pos[0]) // self.lines[0][0].width
        g2 = int(pos[1]) // self.lines[0][0].height

        return self.lines[g2][g1]

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                clicked = canvas.clicked(pos)
                clicked.color = (0, 0, 0)

                for neighbor in clicked.neighbors:
                    neighbor.color = (0, 0, 0)

            if pygame.mouse.get_pressed()[2]:
                try:
                    pos = pygame.mouse.get_pos()
                    clicked = canvas.clicked(pos)
                    clicked.colors = (255, 255, 255)
                except:
                    pass

        canvas.draw(window)
        pygame.display.update()

pygame.init()
width = 720
height = 720
scale = 18
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw a Number")
canvas = grid(width // scale, height // scale, width, height, scale)
main()

pygame.quit()
quit()









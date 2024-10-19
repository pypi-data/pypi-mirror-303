import pygame as pg
import math

pg.init()
def vector(self, psx, psy, targetx, targety, speed):
    self.distance = [targetx - psx, targety - psy]
    self.norm = math.sqrt(self.distance[0] ** 2 + self.distance[1] ** 2)
    self.dx = self.distance[0] / self.norm
    self.dy = self.distance[1] / self.norm
    self.vector = [self.dx * speed, self.dy * speed]
    return self.vector

class Entity:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.rect = pg.Rect((self.x, self.y), size)

    def follow(self, x, y, targetx, targety, speed):
        self.dx = targetx - x
        self.dy = targety - y
        self.dist = (self.dx ** 2 + self.dy ** 2) ** 0.5
        if self.dist > 0:
            self.dx /= self.dist
            self.dy /= self.dist
            x += self.dx * speed
            y += self.dy * speed
        self.pos = [x, y]
        return self.pos
    
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.rect = pg.Rect((self.x, self.y), size)

    def controls(self, x, y, speed):
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_d]:
            x += 1 * speed
        if self.keys[pg.K_a]:
            x -= 1 * speed
        if self.keys[pg.K_w]:
            y -= 1 * speed
        if self.keys[pg.K_s]:
            y += 1 * speed
        return x, y

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        
class Bullet:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.rect = pg.Rect(self.pos, self.size)
    def update(self):
        self.rect.x, self.rect.y = self.pos
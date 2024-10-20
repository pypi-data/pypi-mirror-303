import pygame as pg
import math

pg.init()
def vector(psx, psy, targetx, targety, speed):
    distance = [targetx - psx, targety - psy]
    norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
    dx = distance[0] / norm
    dy = distance[1] / norm
    vector = [dx * speed, dy * speed]
    return vector

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

    def controls(self, x, y, speed, borders=False, right=0, left=0, top=0, bottom=0):
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_d]:
            if borders:
                if not self.rect.colliderect(right):
                    x += 1 * speed
            if borders == False:
                x += 1 * speed
        if self.keys[pg.K_a]:
            if borders:
                if not self.rect.colliderect(left):
                    x -= 1 * speed
            if borders == False:
                x -= 1 * speed
        if self.keys[pg.K_w]:
            if borders:
                if not self.rect.colliderect(top):
                    y -= 1 * speed
            if borders == False:
                y -= 1 * speed
        if self.keys[pg.K_s]:
            if borders:
                if not self.rect.colliderect(bottom):
                    y += 1 * speed
            if borders == False:
                y += 1 * speed
        return x, y

    def dash(self, x, y, length):
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_d]:
            x += length
        if self.keys[pg.K_a]:
            x -= length
        if self.keys[pg.K_s]:
            y += length
        if self.keys[pg.K_w]:
            y -= length
        return x, y
        
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        
class Bullet:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.rect = pg.Rect(self.pos, self.size)
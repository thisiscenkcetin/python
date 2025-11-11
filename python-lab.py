"""
the world is yours
"""

import pygame
import math
import random
from enum import Enum

pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The World Is Yours - Uçan Balonlar")
clock = pygame.time.Clock()
font_large = pygame.font.Font(None, 100)
font_medium = pygame.font.Font(None, 50)

class Balon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(15, 35)
        self.velocity_y = random.uniform(-3, -1)
        self.velocity_x = random.uniform(-2, 2)
        self.rotation = 0
        self.rotation_speed = random.uniform(-5, 5)
        self.color = random.choice([
            (255, 215, 0),      # Altın
            (255, 200, 0),      # Turuncu sarı
            (255, 240, 0),      # Parlak sarı
            (218, 165, 32),     # Goldenrod
            (255, 225, 53)      # Parlak sarı 2
        ])
        self.opacity = 255
        self.life_time = random.randint(120, 300)
        self.age = 0
        self.wobble = random.uniform(0, 2 * math.pi)
        self.wobble_speed = random.uniform(0.05, 0.15)

    def update(self):
        self.age += 1
        self.wobble += self.wobble_speed
        
        # Dalgalı hareket
        wobble_offset = math.sin(self.wobble) * 1.5
        self.x += self.velocity_x + wobble_offset
        self.y += self.velocity_y
        self.rotation += self.rotation_speed
        
        # Parlaklık azalması
        fade_start = self.life_time * 0.7
        if self.age > fade_start:
            progress = (self.age - fade_start) / (self.life_time - fade_start)
            self.opacity = int(255 * (1 - progress))
        
        return self.age < self.life_time

    def draw(self, surface):
        # Geçici yüzey
        temp_surface = pygame.Surface((self.size * 2 + 20, self.size * 2 + 20), pygame.SRCALPHA)
        
        # Ana balon (daire)
        color_with_alpha = (*self.color, self.opacity)
        pygame.draw.circle(temp_surface, color_with_alpha, 
                          (self.size + 10, self.size + 10), self.size)
        
        # İç parlaklik
        inner_color = (255, 255, 255, int(self.opacity * 0.4))
        pygame.draw.circle(temp_surface, inner_color,
                          (self.size + 5, self.size - 5), self.size // 3)
        
        # İp
        string_color = (*self.color, self.opacity)
        pygame.draw.line(temp_surface, string_color,
                        (self.size + 10, self.size * 2 + 10),
                        (self.size + 8, self.size * 2 + 20), 2)
        
        surface.blit(temp_surface, (int(self.x - self.size - 10), int(self.y - self.size - 10)))

class Para:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_y = random.uniform(-4, -0.5)
        self.velocity_x = random.uniform(-3, 3)
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-15, 15)
        self.opacity = 255
        self.life_time = random.randint(150, 350)
        self.age = 0
        self.size = random.randint(10, 20)
        self.wobble = random.uniform(0, 2 * math.pi)
        self.wobble_speed = random.uniform(0.08, 0.15)

    def update(self):
        self.age += 1
        self.wobble += self.wobble_speed
        
        wobble_offset = math.sin(self.wobble) * 2
        self.x += self.velocity_x + wobble_offset
        self.y += self.velocity_y
        self.rotation += self.rotation_speed
        
        fade_start = self.life_time * 0.6
        if self.age > fade_start:
            progress = (self.age - fade_start) / (self.life_time - fade_start)
            self.opacity = int(255 * (1 - progress))
        
        return self.age < self.life_time

    def draw(self, surface):
        temp_surface = pygame.Surface((self.size * 3, self.size * 2), pygame.SRCALPHA)
        
        # Para sembolü
        color_with_alpha = (255, 215, 0, self.opacity)
        pygame.draw.ellipse(temp_surface, color_with_alpha,
                          (self.size // 2, 0, self.size * 2, self.size * 1.5))
        pygame.draw.line(temp_surface, color_with_alpha,
                        (self.size + self.size // 2, 0),
                        (self.size + self.size // 2, self.size * 1.5), 2)
        
        surface.blit(temp_surface, (int(self.x - self.size), int(self.y - self.size)))

class Yildiz:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_y = random.uniform(-2, -0.5)
        self.velocity_x = random.uniform(-1, 1)
        self.size = random.randint(3, 8)
        self.opacity = 255
        self.life_time = random.randint(100, 200)
        self.age = 0
        self.pulse = 0
        self.pulse_speed = random.uniform(0.05, 0.15)

    def update(self):
        self.age += 1
        self.pulse += self.pulse_speed
        
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        fade_start = self.life_time * 0.5
        if self.age > fade_start:
            progress = (self.age - fade_start) / (self.life_time - fade_start)
            self.opacity = int(255 * (1 - progress))
        
        return self.age < self.life_time

    def draw(self, surface):
        pulse_size = self.size + math.sin(self.pulse) * 2
        color_with_alpha = (255, 255, 200, self.opacity)
        pygame.draw.circle(surface, color_with_alpha, (int(self.x), int(self.y)), int(pulse_size))

# Ana oyun döngüsü
running = True
baloons = []
coins = []
stars = []
text_alpha = 255
spawn_timer = 0

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Yeni balonlar ve para
    spawn_timer += 1
    if spawn_timer > 8:
        x = random.randint(50, WIDTH - 50)
        y = HEIGHT + 20
        baloons.append(Balon(x, y))
        coins.append(Para(x, y))
        stars.append(Yildiz(x + random.randint(-30, 30), y))
        spawn_timer = 0
    
    # Update
    baloons = [b for b in baloons if b.update()]
    coins = [c for c in coins if c.update()]
    stars = [s for s in stars if s.update()]
    
    # Çizim
    screen.fill((20, 20, 40))  # Koyu arka plan
    
    # Yıldızlar
    for star in stars:
        star.draw(screen)
    
    # Para
    for coin in coins:
        coin.draw(screen)
    
    # Balonlar
    for balon in baloons:
        balon.draw(screen)
    
    # Metin
    text_main = font_large.render("THE WORLD", True, (255, 215, 0))
    text_sub = font_large.render("IS YOURS", True, (255, 215, 0))
    
    text_rect1 = text_main.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
    text_rect2 = text_sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
    
    screen.blit(text_main, text_rect1)
    screen.blit(text_sub, text_rect2)
    
    pygame.display.flip()

pygame.quit()

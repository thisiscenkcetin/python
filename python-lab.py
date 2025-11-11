import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1400, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Code Quest - Python Öğrenme Oyunu")
clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 80)
font_medium = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 35)
font_tiny = pygame.font.Font(None, 25)

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.size = 30
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 7
        self.health = 100
        self.max_health = 100
        self.bullets = []
        self.level = 1
        self.experience = 0
        self.exp_to_level = 100
        self.color = (0, 255, 150)

    def handle_input(self, keys):
        self.velocity_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity_x = self.speed

    def update(self):
        self.x += self.velocity_x
        self.x = max(self.size, min(WIDTH - self.size, self.x))
        
        for bullet in self.bullets[:]:
            bullet['y'] -= bullet['speed']
            if bullet['y'] < 0:
                self.bullets.remove(bullet)

    def shoot(self):
        self.bullets.append({
            'x': self.x,
            'y': self.y - self.size,
            'speed': 12,
            'size': 8,
            'damage': 10
        })

    def add_experience(self, amount):
        self.experience += amount
        if self.experience >= self.exp_to_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.exp_to_level = int(self.exp_to_level * 1.2)
        self.max_health += 20
        self.health = self.max_health

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, [
            (self.x, self.y - self.size),
            (self.x - self.size, self.y + self.size),
            (self.x + self.size, self.y + self.size)
        ])
        
        for bullet in self.bullets:
            pygame.draw.circle(surface, (255, 255, 0), 
                             (int(bullet['x']), int(bullet['y'])), bullet['size'])

class Enemy:
    def __init__(self, x, y, enemy_type):
        self.x = x
        self.y = y
        self.size = 20
        self.velocity_x = random.uniform(-2, 2)
        self.velocity_y = random.uniform(0.5, 2)
        self.health = 30
        self.max_health = 30
        self.type = enemy_type  # "loop", "variable", "function", "list"
        self.colors = {
            "loop": (255, 100, 100),
            "variable": (100, 150, 255),
            "function": (150, 100, 255),
            "list": (100, 255, 200)
        }
        self.color = self.colors[enemy_type]
        self.lesson_text = {
            "loop": "for x in range(5):",
            "variable": "x = 10",
            "function": "def func():",
            "list": "arr = [1,2,3]"
        }
        self.time_alive = 0

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.time_alive += 1
        
        if self.x < 0 or self.x > WIDTH:
            self.velocity_x *= -1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, 
                        (self.x - self.size, self.y - self.size, self.size * 2, self.size * 2))
        
        text = font_tiny.render(self.lesson_text[self.type], True, (255, 255, 255))
        surface.blit(text, (self.x - self.size - 20, self.y - self.size - 40))
        
        health_width = self.size * 2 * (self.health / self.max_health)
        pygame.draw.rect(surface, (255, 0, 0), 
                        (self.x - self.size, self.y - self.size - 10, self.size * 2, 5))
        pygame.draw.rect(surface, (0, 255, 0), 
                        (self.x - self.size, self.y - self.size - 10, health_width, 5))

class Particle:
    def __init__(self, x, y, color, vx, vy):
        self.x = x
        self.y = y
        self.color = color
        self.vx = vx
        self.vy = vy
        self.life = 30
        self.size = 5

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.2
        self.life -= 1
        return self.life > 0

    def draw(self, surface):
        alpha = int(255 * (self.life / 30))
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = []
        self.particles = []
        self.wave = 0
        self.wave_timer = 0
        self.spawn_timer = 0
        self.score = 0
        self.game_over = False
        self.wave_text_timer = 0
        self.lessons = [
            "Variables: Veriyi depolamak için",
            "Loops: Tekrar eden işler için",
            "Functions: Kodu organize etmek için",
            "Lists: Birden fazla veriyi saklamak için",
            "Conditionals: Karar vermek için (if/else)",
            "Strings: Metinle çalışmak için"
        ]

    def spawn_wave(self):
        self.wave += 1
        self.wave_text_timer = 120
        enemy_count = 3 + self.wave
        enemy_types = ["loop", "variable", "function", "list"]
        
        for i in range(enemy_count):
            x = random.randint(50, WIDTH - 50)
            y = -50
            enemy_type = random.choice(enemy_types)
            self.enemies.append(Enemy(x, y, enemy_type))

    def update(self):
        if self.game_over:
            return

        self.player.handle_input(pygame.key.get_pressed())
        self.player.update()

        for enemy in self.enemies[:]:
            enemy.update()
            
            if enemy.y > HEIGHT:
                self.enemies.remove(enemy)
                self.player.health -= 10
                if self.player.health <= 0:
                    self.game_over = True
                continue

            for bullet in self.player.bullets[:]:
                dist = math.sqrt((enemy.x - bullet['x'])**2 + (enemy.y - bullet['y'])**2)
                if dist < enemy.size + bullet['size']:
                    enemy.health -= bullet['damage']
                    self.player.bullets.remove(bullet)
                    
                    for _ in range(8):
                        angle = random.uniform(0, 2 * math.pi)
                        vx = math.cos(angle) * 3
                        vy = math.sin(angle) * 3
                        self.particles.append(Particle(enemy.x, enemy.y, enemy.color, vx, vy))
                    
                    if enemy.health <= 0:
                        self.enemies.remove(enemy)
                        self.score += 50
                        self.player.add_experience(25)
                    break

        self.particles = [p for p in self.particles if p.update()]

        self.spawn_timer += 1
        if len(self.enemies) == 0:
            self.spawn_wave()
        
        self.wave_text_timer = max(0, self.wave_text_timer - 1)

    def draw(self):
        screen.fill((15, 15, 35))
        
        for particle in self.particles:
            particle.draw(screen)

        for enemy in self.enemies:
            enemy.draw(screen)

        self.player.draw(screen)

        # UI
        level_text = font_medium.render(f"Level: {self.player.level}", True, (0, 255, 150))
        score_text = font_medium.render(f"Score: {self.score}", True, (255, 255, 0))
        wave_text = font_medium.render(f"Wave: {self.wave}", True, (255, 150, 0))
        
        screen.blit(level_text, (20, 20))
        screen.blit(score_text, (20, 80))
        screen.blit(wave_text, (20, 140))

        # Health bar
        health_width = 300 * (self.player.health / self.player.max_health)
        pygame.draw.rect(screen, (200, 0, 0), (WIDTH - 320, 20, 300, 30))
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH - 320, 20, health_width, 30))
        health_text = font_small.render(f"HP: {self.player.health}/{self.player.max_health}", True, (255, 255, 255))
        screen.blit(health_text, (WIDTH - 310, 22))

        # Experience bar
        exp_width = 300 * (self.player.experience / self.player.exp_to_level)
        pygame.draw.rect(screen, (50, 50, 100), (WIDTH - 320, 70, 300, 20))
        pygame.draw.rect(screen, (0, 200, 255), (WIDTH - 320, 70, exp_width, 20))

        # Lesson
        if self.wave_text_timer > 0:
            lesson_idx = (self.wave - 1) % len(self.lessons)
            lesson_text = font_small.render(self.lessons[lesson_idx], True, (100, 255, 200))
            rect = lesson_text.get_rect(center=(WIDTH // 2, 100))
            screen.blit(lesson_text, rect)

        # Game Over
        if self.game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            
            game_over_text = font_big.render("AĞLAMA OYNA", True, (255, 0, 0))
            final_score = font_medium.render(f"Score: {self.score}", True, (255, 255, 0))
            final_level = font_medium.render(f"Level: {self.player.level}", True, (0, 255, 150))
            restart_text = font_small.render("Oynamak için SPACE, çıkmak için ESC", True, (255, 255, 255))
            
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 250))
            screen.blit(final_score, (WIDTH // 2 - final_score.get_width() // 2, 380))
            screen.blit(final_level, (WIDTH // 2 - final_level.get_width() // 2, 450))
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 580))

        pygame.display.flip()

# Main loop
game = Game()
game.spawn_wave()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.player.shoot()
            if event.key == pygame.K_ESCAPE:
                running = False
            if game.game_over and event.key == pygame.K_SPACE:
                game = Game()
                game.spawn_wave()

    game.update()
    game.draw()

pygame.quit()

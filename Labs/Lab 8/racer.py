import pygame
import random
import os

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Устанавливаем рабочую директорию
os.chdir(os.path.dirname(__file__))

# Проверяем существование файла звука
sound_path = 'coin_sound.wav'
if not os.path.isfile(sound_path):
    print("Ошибка: Файл coin_sound.wav не найден. Убедитесь, что он находится в папке с игрой.")
    exit()

# Загрузка звука сбора монеты
coin_sound = pygame.mixer.Sound(sound_path)

# Размеры экрана
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)

# Параметры машины
car_width, car_height = 50, 100
car = pygame.Rect(WIDTH//2, HEIGHT-150, car_width, car_height)

# Параметры монет
coin_size = 30
coins = []
coin_spawn_timer = 0
coin_spawn_interval = 1000  # Интервал появления монет - 1 секунда

# Счёт
score = 0
font = pygame.font.Font(None, 36)

# Скорость игры
speed = 7

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение машины
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.left > 0:
        car.x -= speed
    if keys[pygame.K_RIGHT] and car.right < WIDTH:
        car.x += speed

    # Генерация монет
    coin_spawn_timer += clock.get_time()
    if coin_spawn_timer >= coin_spawn_interval:
        coin_x = random.randint(0, WIDTH - coin_size)
        coins.append(pygame.Rect(coin_x, -coin_size, coin_size, coin_size))
        coin_spawn_timer = 0

    # Движение монет и проверка столкновений
    for coin in coins[:]:
        coin.y += speed
        if coin.colliderect(car):
            score += 1
            coin_sound.play()  # Воспроизведение звука при сборе монеты
            coins.remove(coin)
        elif coin.y > HEIGHT:
            coins.remove(coin)

    # Отрисовка объектов
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, car)
    for coin in coins:
        pygame.draw.ellipse(screen, YELLOW, coin)

    # Отображение счёта в правом верхнем углу
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

# Завершение игры
pygame.quit()

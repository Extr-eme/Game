import pygame
from sys import exit
from movement import Character_state

pygame.init()

# Constants
tile_size = 100
screen_width = 1400
screen_height = 900
fps = 60

# Game variables
game_over = 0
main_menu = True
level = 3
max_levels = 7
score = 0

# Setup
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mistey")
test_font = pygame.font.Font('text/Pixeltype.ttf', 100)
text_surface = test_font.render('Welcome', False, 'RED').convert()

# Load images
restart_img = pygame.image.load('img/restart_btn.png').convert_alpha()
start_img = pygame.image.load('img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('img/exit_btn.png').convert_alpha()

# Tree Class
class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('img/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

# Button Class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect)
        return action

# Exit sprite class
class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/exit.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# World Class
class World():
    def __init__(self, data):
        self.tile_list = []

        dirt_img = pygame.image.load('img/GRASS/grass_1.png')
        grass_img = pygame.image.load('img/GRASS/road_1.png')

        for row_index, row in enumerate(data):
            for col_index, tile in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    self.tile_list.append((img, pygame.Rect(x, y, tile_size, tile_size)))
                elif tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    self.tile_list.append((img, pygame.Rect(x, y, tile_size, tile_size)))

    def draw(self, offset):
        for image, rect in self.tile_list:
            screen.blit(image, rect.topleft - offset)

# Camera Group
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_width() // 2
        self.half_h = self.display_surface.get_height() // 2

    def center_target(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player, world):
        self.center_target(player)

        # Draw terrain first
        world.draw(self.offset)

        # Then draw sprites (player, trees, etc.)
        for sprite in sorted(self.sprites(), key=lambda s: s.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

# Level Data
world_data = [[1] * 20 for _ in range(20)]  # Replace with your own layout
world = World(world_data)

# Buttons
restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)

# Main Game Loop
def main():
    global main_menu
    frame_timer = 0

    camera_group = CameraGroup()
    character_state = Character_state(screen_width / 2, screen_height / 2, 0)

    # Only character and interactive sprites go in camera group
    camera_group.add(character_state)

    run = True
    while run:
        clock.tick(fps)

        if main_menu:
            if exit_button.draw():
                run = False
            if start_button.draw():
                main_menu = False
            screen.blit(text_surface, (600, 200))
        else:
            keys = pygame.key.get_pressed()
            character_state.character_movement(keys)
            frame_timer = (frame_timer + 1) % fps

            camera_group.update(frame_timer)
            screen.fill((0, 0, 0))
            camera_group.custom_draw(character_state, world)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
    exit()

# Run the game
if __name__ == "__main__":
    main()

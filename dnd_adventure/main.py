import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DnD Adventure")

FONT = pygame.font.SysFont("consolas", 24)
clock = pygame.time.Clock()

def draw_text(surface, text, x, y):
    rendered = FONT.render(text, True, (255, 255, 255))
    surface.blit(rendered, (x, y))

def main():
    running = True
    game_state = "main_menu"

    player_race = None
    player_class = None

    while running:
        # -----------------------------
        # EVENT HANDLING
        # -----------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # MAIN MENU INPUT
            if game_state == "main_menu":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_state = "race_select"

            # RACE SELECTION INPUT
            elif game_state == "race_select":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        player_race = "Human"
                        game_state = "class_select"
                    elif event.key == pygame.K_2:
                        player_race = "Orc"
                        game_state = "class_select"
                    elif event.key == pygame.K_3:
                        player_race = "Elf"
                        game_state = "class_select"
                    elif event.key == pygame.K_4:
                        player_race = "Dwarf"
                        game_state = "class_select"

            # CLASS SELECTION INPUT
            elif game_state == "class_select":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        player_class = "Rogue"
                        game_state = "roll_stats"
                    elif event.key == pygame.K_2:
                        player_class = "Fighter"
                        game_state = "roll_stats"
                    elif event.key == pygame.K_3:
                        player_class = "Wizard"
                        game_state = "roll_stats"

        # -----------------------------
        # DRAWING SECTION
        # -----------------------------
        WINDOW.fill((0, 0, 0))

        if game_state == "main_menu":
            draw_text(WINDOW, "DnD Adventure", 100, 200)
            draw_text(WINDOW, "Press SPACE to Start", 100, 260)

        elif game_state == "race_select":
            draw_text(WINDOW, "Choose your race:", 100, 100)
            draw_text(WINDOW, "1. Human", 100, 160)
            draw_text(WINDOW, "2. Orc", 100, 200)
            draw_text(WINDOW, "3. Elf", 100, 240)
            draw_text(WINDOW, "4. Dwarf", 100, 280)

        elif game_state == "class_select":
            draw_text(WINDOW, f"Race chosen: {player_race}", 100, 100)
            draw_text(WINDOW, "Choose your class:", 100, 160)
            draw_text(WINDOW, "1. Rogue", 100, 200)
            draw_text(WINDOW, "2. Fighter", 100, 240)
            draw_text(WINDOW, "3. Wizard", 100, 280)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
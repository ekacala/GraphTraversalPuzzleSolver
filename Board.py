from Puzzle import solve_puzzle
from Converter import *
import pygame

# Initialize Pygame
pygame.init()

# Set clock
clock = pygame.time.Clock()

# Set up game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Path Finder")

# Set background color
background_color = (255, 255, 255)
line_color = (0, 0, 0)
screen.fill(background_color)

# Set font for user
base_font = pygame.font.Font(None, 24)
start_space = ''
end_space = ''

# Establish board for solve_puzzle function
board = [
     ['-', '-', '-', '-', '-'],
     ['-', '-', '#', '-', '-'],
     ['-', '-', '-', '-', '-'],
     ['#', '-', '#', '#', '-'],
     ['-', '#', '-', '-', '-']
]

# Draw game board
pygame.draw.rect(screen, line_color, [210, 10, 380, 280], 2)
pygame.draw.line(screen, line_color, [210, 66], [588, 66], 1)
pygame.draw.line(screen, line_color, [210, 122], [588, 122], 1)
pygame.draw.line(screen, line_color, [210, 178], [588, 178], 1)
pygame.draw.line(screen, line_color, [210, 234], [588, 234], 1)
pygame.draw.line(screen, line_color, [286, 10], [286, 288], 1)
pygame.draw.line(screen, line_color, [362, 10], [362, 288], 1)
pygame.draw.line(screen, line_color, [438, 10], [438, 288], 1)
pygame.draw.line(screen, line_color, [514, 10], [514, 288], 1)

# Label squares
a1 = base_font.render('A1', True, (0, 0, 0))
textRect = a1.get_rect()
textRect.center = (248, 38)
screen.blit(a1, textRect)

a2 = base_font.render('A2', True, (0, 0, 0))
textRect = a2.get_rect()
textRect.center = (324, 38)
screen.blit(a2, textRect)

a3 = base_font.render('A3', True, (0, 0, 0))
textRect = a3.get_rect()
textRect.center = (400, 38)
screen.blit(a3, textRect)

a4 = base_font.render('A4', True, (0, 0, 0))
textRect = a4.get_rect()
textRect.center = (476, 38)
screen.blit(a4, textRect)

a5 = base_font.render('A5', True, (0, 0, 0))
textRect = a5.get_rect()
textRect.center = (552, 38)
screen.blit(a5, textRect)

b1 = base_font.render('B1', True, (0, 0, 0))
textRect = b1.get_rect()
textRect.center = (248, 94)
screen.blit(b1, textRect)

b2 = base_font.render('B2', True, (0, 0, 0))
textRect = b2.get_rect()
textRect.center = (324, 94)
screen.blit(b2, textRect)

b4 = base_font.render('B4', True, (0, 0, 0))
textRect = b4.get_rect()
textRect.center = (476, 94)
screen.blit(b4, textRect)

b5 = base_font.render('B5', True, (0, 0, 0))
textRect = b5.get_rect()
textRect.center = (552, 94)
screen.blit(b5, textRect)

c1 = base_font.render('C1', True, (0, 0, 0))
textRect = c1.get_rect()
textRect.center = (248, 150)
screen.blit(c1, textRect)

c2 = base_font.render('C2', True, (0, 0, 0))
textRect = c2.get_rect()
textRect.center = (324, 150)
screen.blit(c2, textRect)

c3 = base_font.render('C3', True, (0, 0, 0))
textRect = c3.get_rect()
textRect.center = (400, 150)
screen.blit(c3, textRect)

c4 = base_font.render('C4', True, (0, 0, 0))
textRect = c4.get_rect()
textRect.center = (476, 150)
screen.blit(c4, textRect)

c5 = base_font.render('C5', True, (0, 0, 0))
textRect = c5.get_rect()
textRect.center = (552, 150)
screen.blit(c5, textRect)

d2 = base_font.render('D2', True, (0, 0, 0))
textRect = d2.get_rect()
textRect.center = (324, 206)
screen.blit(d2, textRect)

d5 = base_font.render('D5', True, (0, 0, 0))
textRect = d5.get_rect()
textRect.center = (552, 206)
screen.blit(d5, textRect)

e1 = base_font.render('E1', True, (0, 0, 0))
textRect = e1.get_rect()
textRect.center = (248, 262)
screen.blit(e1, textRect)

e3 = base_font.render('E3', True, (0, 0, 0))
textRect = e3.get_rect()
textRect.center = (400, 262)
screen.blit(e3, textRect)

e4 = base_font.render('E4', True, (0, 0, 0))
textRect = e4.get_rect()
textRect.center = (476, 262)
screen.blit(e4, textRect)

e5 = base_font.render('E5', True, (0, 0, 0))
textRect = e5.get_rect()
textRect.center = (552, 262)
screen.blit(e5, textRect)

# Place icons to indicate impassable squares
hashtag = pygame.image.load('images/hashtag-svgrepo-com.svg')
screen.blit(hashtag, (390, 84))
hashtag = pygame.image.load('images/hashtag-svgrepo-com.svg')
screen.blit(hashtag, (238, 196))
hashtag = pygame.image.load('images/hashtag-svgrepo-com.svg')
screen.blit(hashtag, (390, 196))
hashtag = pygame.image.load('images/hashtag-svgrepo-com.svg')
screen.blit(hashtag, (466, 196))
hashtag = pygame.image.load('images/hashtag-svgrepo-com.svg')
screen.blit(hashtag, (314, 252))

# Create text instructions
instructions_text_1 = 'To find the shortest path between two spaces, please input a starting space,'
instructions_text_2 = 'an ending space, and hit GO. A # indicates an impassable space.'
start_instruct_text = 'Starting Space:'
end_instruct_text = 'Ending Space:'

# Render line 1
instructions_1 = base_font.render(instructions_text_1, True, (0, 0, 0))
textRect = instructions_1.get_rect()
textRect.center = (400, 310)
screen.blit(instructions_1, textRect)

# Render line 2
instructions_2 = base_font.render(instructions_text_2, True, (0, 0, 0))
textRect = instructions_2.get_rect()
textRect.center = (400, 330)
screen.blit(instructions_2, textRect)

# Render start_instruct
start_instruct = base_font.render(start_instruct_text, True, (0, 0, 0))
textRect = start_instruct.get_rect()
textRect.center = (200, 360)
screen.blit(start_instruct, textRect)

# Render end_instruct
end_instruct = base_font.render(end_instruct_text, True, (0, 0, 0))
textRect = end_instruct.get_rect()
textRect.center = (480, 360)
screen.blit(end_instruct, textRect)

# Create input fields
start_input_rect = pygame.Rect(270, 350, 100, 24)
end_input_rect = pygame.Rect(550, 350, 100, 24)
color_passive = pygame.Color((211, 211, 211))
color_active = pygame.Color((250, 167, 235))

# Create GO button
go_rect = pygame.Rect(250, 400, 100, 24)
go_color = color_passive

# Create Reset button
reset_rect = pygame.Rect(450, 400, 100, 24)
reset_color = color_passive

# Set start variables
start_color = color_passive
end_color = color_passive
start_active = False
end_active = False
go_active = False
reset_active = False
answer = False
path_printed = False

path = ''

pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_input_rect.collidepoint(event.pos):  # If starting point input box is clicked
                start_active = True
                end_active = False
            elif end_input_rect.collidepoint(event.pos):  # If ending point input box is clicked
                start_active = False
                end_active = True
            elif go_rect.collidepoint(event.pos):  # If Go button is clicked
                start_active = False
                end_active = False
                go_active = True

                # Get coordinates for start and end positions
                coordinates = letter_converter(start_space, end_space)
                start_position = coordinates[0]
                end_position = coordinates[1]

                # Check for incorrect coordinates
                if start_position == (-1, -1) or end_position == (-1, -1):
                    # Erase previously printed path if Reset button was not clicked
                    if path_printed is True:
                        pygame.draw.rect(screen, background_color, pygame.Rect(0, 430, 800, 100))

                    # Print error message
                    error_message = base_font.render('Please provide a set of coordinates listed on the board.', True, (0, 0, 0))
                    textRect = error_message.get_rect()
                    textRect.center = (400, 450)
                    screen.blit(error_message, textRect)

                    path_printed = True
                elif start_position == (4, 0) or end_position == (4, 0): # Check for impassable coordinates
                    # Erase previously printed path if Reset button was not clicked
                    if path_printed is True:
                        pygame.draw.rect(screen, background_color, pygame.Rect(0, 430, 800, 100))

                    # Print error message
                    error_message = base_font.render('Error. Coordinate unreachable.', True,
                                                     (0, 0, 0))
                    textRect = error_message.get_rect()
                    textRect.center = (400, 450)
                    screen.blit(error_message, textRect)

                    path_printed = True
                else:
                    # Call puzzle.py
                    path = solve_puzzle(board, start_position, end_position)
                    path = path[0]
                    answer = True
            elif reset_rect.collidepoint(event.pos):  # If reset button is clicked
                reset_active = True
                start_active = False
                end_active = False
                go_active = False
                answer = False
                path_printed = False
                start_space = ''
                end_space = ''
                path = ''
                pygame.draw.rect(screen, background_color, pygame.Rect(0, 430, 800, 100))
            else:
                start_active = False
                end_active = False

        # Get start and end coordinates from user
        if start_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    start_space = start_space[:-1]
                else:
                    start_space += event.unicode
        elif end_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    end_space = end_space[:-1]
                else:
                    end_space += event.unicode

        # Change colors of selected boxes/buttons
        if start_active:
            start_color = color_active
            end_color = color_passive
            go_color = color_passive
            reset_color = color_passive
        elif end_active:
            start_color = color_passive
            end_color = color_active
            go_color = color_passive
            reset_color = color_passive
        elif go_active:
            start_color = color_passive
            end_color = color_passive
            go_color = color_active
            reset_color = color_passive
            go_active = False
        elif reset_active:
            start_color = color_passive
            end_color = color_passive
            go_color = color_passive
            reset_color = color_active
            reset_active = False
        else:
            start_color = color_passive
            end_color = color_passive
            go_color = color_passive
            reset_color = color_passive

        if answer:
            # Erase previously printed path if Reset button was not clicked
            if path_printed is True:
                pygame.draw.rect(screen, background_color, pygame.Rect(0, 430, 800, 100))

            # Convert path from coordinates to letter/number pair
            path = coordinate_converter(path)
            path = str(path)
            print(path)

            # Render answer
            answer_prompt = base_font.render('Sortest path:', True, (0, 0, 0))
            textRect = answer_prompt.get_rect()
            textRect.center = (200, 450)
            screen.blit(answer_prompt, textRect)

            answer_path = base_font.render(path, True, (0, 0, 0))
            textRect = answer_path.get_rect()
            textRect.center = (500, 450)
            screen.blit(answer_path, textRect)

            # Update variables
            answer = False
            path_printed = True

        # Display start input box
        pygame.draw.rect(screen, start_color, start_input_rect)
        text_surface = base_font.render(start_space, True, (255, 255, 255))
        screen.blit(text_surface, (start_input_rect.x+5, start_input_rect.y+5))
        start_input_rect.w = max(100, text_surface.get_width()+10)

        # Display end input box
        pygame.draw.rect(screen, end_color, end_input_rect)
        text_surface = base_font.render(end_space, True, (255, 255, 255))
        screen.blit(text_surface, (end_input_rect.x + 5, end_input_rect.y + 5))
        end_input_rect.w = max(100, text_surface.get_width() + 10)

        # Display GO button
        pygame.draw.rect(screen, go_color, go_rect)
        go_text = base_font.render('GO', True, (0, 0, 0))
        textRect = go_text.get_rect()
        textRect.center = (300, 412)
        screen.blit(go_text, textRect)

        # Display Reset button
        pygame.draw.rect(screen, reset_color, reset_rect)
        reset_text = base_font.render('Reset', True, (0, 0, 0))
        textRect = reset_text.get_rect()
        textRect.center = (500, 412)
        screen.blit(reset_text, textRect)

        pygame.display.flip()

        clock.tick(60)

# Quit Pygame
pygame.quit()
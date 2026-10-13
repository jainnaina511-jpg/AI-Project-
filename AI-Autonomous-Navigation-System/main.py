import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI-Based Autonomous Navigation System")

# Robot
robot_x = 100
robot_y = 500
speed = 2

# Obstacle
obstacle = pygame.Rect(350, 450, 80, 80)

# Goal
goal = pygame.Rect(700, 500, 30, 30)

clock = pygame.time.Clock()

running = True

while running:

    screen.fill((255, 255, 255))

    # Simple obstacle avoidance
    if robot_x + 20 < obstacle.left and robot_y == 500:
        robot_x += speed
    elif robot_y > 380 and robot_x + 20 >= obstacle.left and robot_x < obstacle.right:
        robot_y -= speed
    elif robot_x < goal.x and robot_y <= 380:
        robot_x += speed
    elif robot_y < 500 and robot_x >= obstacle.right:
        robot_y += speed

    # Draw robot
    pygame.draw.circle(screen, (0, 0, 255), (robot_x, robot_y), 20)

    # Draw obstacle
    pygame.draw.rect(screen, (255, 0, 0), obstacle)

    # Draw goal
    pygame.draw.rect(screen, (0, 255, 0), goal)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()

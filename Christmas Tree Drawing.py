import pygame
 
pygame.init()
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (7, 150, 12)
RED = (255, 0, 0)
BROWN = (109, 73, 15)
YELLOW = (238, 242, 9)
 
PI = 3.141592653
 
size = (400, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Justin W's Drawing")
 
done = False
clock = pygame.time.Clock()
 
while not done:
 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    screen.fill(BLUE)
    
    pygame.draw.rect(screen, BROWN, [170, 220, 40, 600], 0)

    for y_offset in range(141, 300, 10):
        pygame.draw.line(screen, GREEN, [190, 50 + y_offset], [150, 100 + y_offset], 10)
        
    for y_offset in range(141, 300, 10):
        pygame.draw.line(screen, GREEN, [190, 50 + y_offset], [230, 100 + y_offset], 10)
        
    pygame.draw.ellipse(screen, RED, [200, 250, 20, 20], 0)
    pygame.draw.ellipse(screen, YELLOW, [160, 280, 20, 20], 0)
    pygame.draw.ellipse(screen, BLUE, [200, 310, 20, 20], 0)
    pygame.draw.ellipse(screen, RED, [160, 335, 20, 20], 0)
    pygame.draw.ellipse(screen, BLUE, [160, 225, 20, 20], 0)

    pygame.draw.polygon(screen, YELLOW, [[190, 160], [170, 185], [210, 185]], 0)
    pygame.draw.polygon(screen, YELLOW, [[190, 195], [170, 170], [210, 170]], 0)
 
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    text = font.render("Merry Christmas!!!", True, RED)
 
    screen.blit(text, [100, 100])
    
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()

 
rect_change_x = 5
rect_change_y = 5

while done == False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
 
    screen.fill(BLACK)
 
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
 
    rect_x += rect_change_x
    rect_y += rect_change_y
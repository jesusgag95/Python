import sys, pygame, time 

background_colour = (255,255,255)
black = (0,0,0)
(width, height) = (800, 400)

def stopwatch(beats):
    bpm = beats/60
    elapsed = 0
    counter = 1
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Metronomo')
    screen.fill(background_colour)
    font = pygame.font.Font('freesansbold.ttf', 50) 
    time.perf_counter() #just for reference, doesnt do anything
    start = time.time()
    time.sleep(1)
    while True:
        elapsed = time.time() - start #reference
        if counter < 4:
            print(f"loop cycle time: {time.perf_counter()}, seconds count: {elapsed}, Counter: {str(counter)}")
            counter += 1
        else:
            print(f"loop cycle time: {time.perf_counter()}, seconds count: {elapsed}, Counter: {str(counter)}")
            counter = 1
        draw_screen(counter,screen,font)
        time.sleep(1/bpm)


def draw_screen(number,screen,font):
    text = font.render(str(number), True, black, background_colour) 
    textRect = text.get_rect()  
    textRect.center = (width // 2, height // 2)     
    pygame.display.flip()

    while True:
        screen.blit(text, textRect) 
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                pygame.quit() 
                quit() 
        pygame.display.update() 
        return
             

def run():
    bpm = int(input("Ingresa los bpm: "))
    stopwatch(bpm)


if __name__ == "__main__":
    run()

import sys, pygame, time
def show(i_s, i,notes_all,half_steps,start):
    size = width, height = 1280, 720

    screen = pygame.display.set_mode(size)
    note_img = pygame.image.load(f'\\Users\\jesus\\OneDrive\\Documentos\\Python\\Notas\\ImgNotas\\{str(start)}\\{i_s}.png')
    note_imgRect = note_img.get_rect()
    note_imgRect.center = (width // 2, height // 2)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        for j in range(len(notes_all[i:i+(half_steps+1)])):

                note_img = pygame.image.load(f'\\Users\\jesus\\OneDrive\\Documentos\\Python\\Notas\\ImgNotas\\{str(start)}\\{i_s+j}.png')
                note_imgRect = note_img.get_rect()
                screen.blit(note_img,note_imgRect)
                note_imgRect.center = (width // 2, height // 2)
                pygame.display.flip()
                time.sleep(1)
        time.sleep(3)


def show_f(i_s, i,notes_all,half_steps,start):
    size = width, height = 1280, 720

    screen = pygame.display.set_mode(size)
    note_img = pygame.image.load(f'\\Users\\jesus\\OneDrive\\Documentos\\Python\\Notas\\ImgNotas\\{str(start)}\\{12+i_s}.png')
    note_imgRect = note_img.get_rect()
    note_imgRect.center = (width // 2, height // 2)

    if half_steps == 12:
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            for j in range(len(notes_all[:0:-1])+1):

                    note_img = pygame.image.load(f'\\Users\\jesus\\OneDrive\\Documentos\\Python\\Notas\\ImgNotas\\{str(start)}\\{(12+i_s)-j}.png')
                    note_imgRect = note_img.get_rect()
                    screen.blit(note_img,note_imgRect)
                    note_imgRect.center = (width // 2, height // 2)
                    pygame.display.flip()
                    time.sleep(1)
            time.sleep(3)
    else:
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            for j in range(len(notes_all[:i-(half_steps+2):-1])):

                    note_img = pygame.image.load(f'\\Users\\jesus\\OneDrive\\Documentos\\Python\\Notas\\ImgNotas\\{str(start)}\\{(12+i_s)-j}.png')
                    note_imgRect = note_img.get_rect()
                    screen.blit(note_img,note_imgRect)
                    note_imgRect.center = (width // 2, height // 2)
                    pygame.display.flip()
                    time.sleep(1)
            time.sleep(3)


def sharper(notes_all, start, half_steps,i_s):
    i = notes_all.index(start)
    print(notes_all[i:i+half_steps+1])
    print(f'{half_steps} Semitonos son : {half_steps/2} tonos')
    show(i_s, i, notes_all,half_steps,start)
    return 2


def flatter(notes_all, half_steps,i,start):
    end = len(notes_all)
    print(notes_all[:end-(half_steps+2):-1])
    # print(notes_all[:0:-1])
    print(f'{half_steps} Semitonos son : {half_steps/2} tonos')
    # note_img = pygame.image.load(f'\\Users\\jesus\\OneDrive\\Documentos\\Python\\Notas\\ImgNotas\\{str(start)}\\{(12+i_s)-j}.png')
    show_f(i,end, notes_all,half_steps,start )
    return 2


def tones():
    notes = ['C',['C#','Db'],'D',['D#','Eb'],'E','F', ['F#','Gb'],'G',['G#','Ab'],'A',['A#','Bb'],'B']
    start = str(input('Selecciona la nota con la que quieres comenzar: ').upper())
    if '#' in start:
        # start = start.strip('#')
        i = notes.index(start.strip('#'))+1
    elif 'B' in start:
        # start = start.strip('B')
        i = notes.index(start.strip('B'))-1
    else:
        i = notes.index(start) #index to know where to start printing
    
    notes_start_finish = notes[i:] #notes from the starting note given to end of list
    notes_finish_start = notes[i::-1] #notes from the bottom of the list to the start given
    notes_all = notes_start_finish + notes_finish_start[::-1] #sum of both list to create one with all notes, starting on the note given
    print(notes_all)
    x = 1
    while x == 1:
        half_steps = int(input('Ingresa los semitonos que te quieres mover: '))
        sharper_flatter = input('Quieres avanzar (más agudo) o regresar (más grave): ')
        if sharper_flatter == 'a':
            x = sharper(notes_all,start, half_steps,i)
        elif sharper_flatter == 'r':
            x = flatter(notes_all, half_steps,i, start )
        else:
            print('Por favor escribe a o r')

    
def run():
        tones()


if __name__ == "__main__":
    run()
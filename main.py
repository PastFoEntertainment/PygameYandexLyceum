import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
pygame.display.set_caption('NeonButtons')
icon = pygame.image.load('texturess/icon.png')
bg = pygame.image.load('texturess/img.png')
pygame.display.set_icon(icon)
x = screen.get_width()
y = screen.get_height()
font = pygame.font.Font('fonts/Jersey25-Regular.ttf', 35)
font1 = pygame.font.Font('fonts/Jersey25-Regular.ttf', 150)
pygame.mixer.music.load('sound/1191499_cosmochild---Bomberman.mp3')
menubg = pygame.image.load('texturess/img_1.png')
endscreenbg = pygame.image.load('texturess/endscreen.jpg')
#Уровень
lvl = open('Levels/Bomberman.txt', mode='r', encoding="utf8")
codes = [line.rstrip() for line in lvl.readlines()]
lvl.close()
g = len(codes)
class drawler:
    def screwdriver():
        pygame.draw.rect(screen, (0, 0, 255), (x / 3.25, y / 6, 125, 125))
        pygame.draw.rect(screen, (0, 150, 255), (x / 3.25, y / 6, 125, 125), 5)
        pygame.draw.rect(screen, (0, 0, 255), (x - x / 3.25 - 125, y - y / 6 - 125, 125, 125))
        pygame.draw.rect(screen, (0, 150, 255), (x - x / 3.25 - 125, y - y / 6 - 125, 125, 125), 5)
        pygame.draw.rect(screen, (0, 0, 255), (x - x / 3.25 - 125, y / 6, 125, 125))
        pygame.draw.rect(screen, (0, 150, 255), (x - x / 3.25 - 125, y / 6, 125, 125), 5)
        pygame.draw.rect(screen, (0, 0, 255), (x / 3.25, y - y / 6 - 125, 125, 125))
        pygame.draw.rect(screen, (0, 150, 255), (x / 3.25, y - y / 6 - 125, 125, 125), 5)

    def animW(c):
        pygame.draw.rect(screen, (0, 255, 0), (x / 3.25 - 25 + c, y / 6 - 25 + c, 175 - 2 * c, 175 - 2 * c), 5)

    def animE(c):
        pygame.draw.rect(screen, (0, 255, 0), (x - x / 3.25 - 150 + c, y / 6 - 25 + c, 175 - 2 * c, 175 - 2 * c), 5)

    def animD(c):
        pygame.draw.rect(screen, (0, 255, 0), (x - x / 3.25 - 150 + c, y - y / 6 - 150 + c, 175 - 2 * c, 175 - 2 * c), 5)

    def animS(c):
        pygame.draw.rect(screen, (0, 255, 0), (x / 3.25 - 25 + c, y - y / 6 - 150 + c, 175 - 2 * c, 175 - 2 * c), 5)

    def music():
        pygame.mixer.music.play()

def main():
    running = True
    clock = pygame.time.Clock()

    timer = 0

    #W
    w = 0
    kw = False

    #E
    e = 0
    ke = False

    #D
    dd = 0
    kd = False

    #S
    s = 0
    ks = False



    gp = False
    menu = True
    endscreen = False
    accuracy = [100]
    pts = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        if timer == 0:
            drawler.music()

# - - - - - - - - - - - - - - - - - - ИГРА - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


        if gp:
            screen.blit(bg, (0, 0))
            # Ноты
            if timer <= g - 1:
                timer += 1
                note = codes[timer - 1].split()
                if len(note) > 1:
                    for button in note[1:]:
                        if button == '1':
                            kw = True
                        if button == '2':
                            ke = True
                        if button == '3':
                            kd = True
                        if button == '4':
                            ks = True
            text = font.render(f'Points: {str(pts)}', False, [0, 255, 0])
            text1 = font.render(f'accuracy: {str(sum(accuracy) // len(accuracy))}', False, [0, 255, 0])
            drawler.screwdriver()
            keys = pygame.key.get_pressed()
            if timer == 1500:
                gp = False
                endscreen = True


    #------------------------------------------- Кнопка S ---------------------------------------------------------------

            if keys[pygame.K_LCTRL]:
                ks = True
            if keys[pygame.K_s]:
                pygame.draw.rect(screen, (0, 255, 0), (x / 3.25 + 5, y - y / 6 - 115 - 5 , 115, 115))
                if ks:
                    if s >= 22.5:
                        pts += 300
                        accuracy.append(100)
                    elif 17.5 <= s < 22.5:
                        pts += 100
                        accuracy.append(66)
                    elif 12.5 <= s < 17.5:
                        pts += 50
                        accuracy.append(50)
                    ks = False
            if ks:
                drawler.animS(s)
                s += 0.5
            else:
                s = 0
                ks = False
            if s > 25:
                s = 0
                ks = False

    #------------------------------------------- Кнопка D ---------------------------------------------------------------

            if keys[pygame.K_TAB]:
                kd = True
            if keys[pygame.K_d]:
                pygame.draw.rect(screen, (0, 255, 0), (x - x / 3.25 - 120, y - y / 6 - 120, 115, 115))
                if kd:
                    if dd >= 23:
                        pts += 300
                        accuracy.append(100)
                    elif 21 <= dd < 23:
                        pts += 100
                        accuracy.append(66)
                    elif 15 <= dd < 21:
                        pts += 50
                        accuracy.append(50)
                    kd = False
            if kd:
                drawler.animD(dd)
                dd += 0.5
            else:
                dd = 0
                kd = False
            if dd > 25:
                dd = 0
                kd = False

    # ------------------------------------------ Кнопка E ---------------------------------------------------------------

            if keys[pygame.K_RSHIFT]:
                ke = True
            if keys[pygame.K_e]:
                pygame.draw.rect(screen, (0, 255, 0), (x - x / 3.25 - 120, y / 6 + 5, 115, 115))
                if ke:
                    if e >= 23:
                        pts += 300
                        accuracy.append(100)
                    elif 21 <= e < 23:
                        pts += 100
                        accuracy.append(66)
                    elif 15 <= e < 21:
                        pts += 50
                        accuracy.append(50)
                    ke = False
            if ke:
                drawler.animE(e)
                e += 0.5
            else:
                e = 0
                ke = False
            if e > 25:
                e = 0
                ke = False


    #------------------------------------------ Кнопка W ---------------------------------------------------------------

            if keys[pygame.K_LSHIFT]:
                kw = True
            if keys[pygame.K_w]:
                pygame.draw.rect(screen, (0, 255, 0), (x / 3.25 + 5, y / 6 + 5, 115, 115))
                if kw:
                    if w >= 23:
                        pts += 300
                        accuracy.append(100)
                    elif 21 <= w < 23:
                        pts += 100
                        accuracy.append(66)
                    elif 15 <= w < 21:
                        pts += 50
                        accuracy.append(50)
                kw = False
            if kw:
                drawler.animW(w)
                w += 0.5
            else:
                w = 0
                kw = False
            if w > 25:
                w = 0
                kw = False
            screen.blit(text1, (10, 35))
            screen.blit(text, (10, 10))


# - - - - - - - - - - - - - - - - - - МЕНЮ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


        if menu:
            timer = 0
            screen.blit(menubg, (0, 0))
            pygame.draw.rect(screen, (0, 0, 255), (x / 2 - 125, y / 2 - 50, 250, 100))
            texts = font.render('START', False, [0, 255, 0])
            screen.blit(texts, (x / 2 - 45, y / 2 - 20))
            if event.type == pygame.MOUSEBUTTONDOWN:
                xc, yc = pygame.mouse.get_pos()
                if (x / 2 - 125) < xc < (x / 2 - 125 + 250) and (y / 2 - 50) < yc < (y / 2 - 50 + 100):
                    gp = True
                    menu = False
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


#- - - - - - - - - - - - - - - - - - - - - ЭНДСКРИН - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


        if endscreen:
            timer = 0
            screen.blit(endscreenbg, (0, 0))
            pygame.draw.rect(screen, (0, 0, 255), (x - x / 4, y - y / 2 - 250, 250, 100))
            pygame.draw.rect(screen, (0, 0, 255), (x - x / 4, y - y / 2, 250, 100))
            back = font.render('BACK', False, [255, 255, 255])
            restart = font.render('RESTART', False, [255, 255, 255])
            stats = font1.render('Stats', True, [255, 255, 255])
            points = font1.render(f'Points: {str(pts)}', True, [255, 255, 255])
            accur = font1.render(f'Accuracy: {str(sum(accuracy) // len(accuracy))}%', True, [255, 255, 255])
            screen.blit(points, (50, 100))
            screen.blit(accur, (50, 200))
            screen.blit(stats, (50, 1))
            screen.blit(restart, (x - x / 4 + 65, y - y / 2 - 215))
            screen.blit(back, (x - x / 4 + 90, y - y / 2 + 30))
            if event.type == pygame.MOUSEBUTTONDOWN:
                xc, yc = pygame.mouse.get_pos()
                if (x - x / 4) <= xc <= (x - x / 4 + 250) and (y - y / 2 - 250) <= yc <= (y - y / 2 - 150):
                    accuracy = [100]
                    pts = 0
                    endscreen = False
                    gp = True

                if (x - x / 4) <= xc <= (x - x / 4 + 250) and (y - y / 2) <= yc <= (y - y / 2 + 150):
                    accuracy = [100]
                    pts = 0
                    endscreen = False
                    menu = True

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()



        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
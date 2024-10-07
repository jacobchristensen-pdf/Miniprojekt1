import math
import pygame
from datetime import datetime

pygame.init()
screen_size = (800, 600) # Størrelsen af screen
screen = pygame.display.set_mode(screen_size) # Laver mit display
screen.fill((255, 255, 255)) # Display gøres hvid

center = (screen_size[0] / 2, screen_size[1] / 2) # Centrum i cirklen/uret
radius_cirkel = 250 # Radius af cirklen/uret


while True: # Får programmet til at gentage sig uendelig gange
    screen.fill((255, 255, 255)) # Farver skærmen hvid for hver gang programmet gentager sig
    pygame.draw.circle(screen, (0, 0, 0), center, radius_cirkel, width=3) # Tegner en sort cirkel - omridset af uret

    # Nu tegnes timerne på uret
    for i in range (12): # Loop der kører 12 gange
        angle_12_mark = math.radians(i * (360 / 12)) # Definerer vinklen for 12 lige store vinkler i cirklen - viser timer

        #x og y koordinater for hvor de 12 linjer slutter (Ændrer sig for gang loppet kører)
        hour_end_x_mark = center[0] + radius_cirkel * math.cos(angle_12_mark)
        hour_end_y_mark = center[1] + radius_cirkel * math.sin(angle_12_mark)

        #x og y koordinater for hvor de 12 linjer starter (Ændrer sig for gang loppet kører)
        hour_start_x_mark = (radius_cirkel - 40) * math.cos(angle_12_mark) + (screen_size[0] / 2)
        hour_start_y_mark = (radius_cirkel - 40) * math.sin(angle_12_mark) + (screen_size[1] / 2)

        # Tegner en linje
        pygame.draw.line(screen, (0, 0, 0), (hour_start_x_mark, hour_start_y_mark), (hour_end_x_mark, hour_end_y_mark), 5)

        # Her tegnes minutterne på uret. Samme koncept som før, nu bare med 60 vinkler og linjer
    for i in range (60):
        angle_60_mark = math.radians(i * (360 / 60))
        sec_end_x_mark = center[0] + radius_cirkel * math.cos(angle_60_mark)
        sec_end_y_mark = center[1] + radius_cirkel * math.sin(angle_60_mark)
        sec_start_x_mark = (radius_cirkel - 20) * math.cos(angle_60_mark) + (screen_size[0] / 2)
        sec_start_y_mark = (radius_cirkel - 20) * math.sin(angle_60_mark) + (screen_size[1] / 2)

        pygame.draw.line(screen, (0, 0, 0), (sec_start_x_mark, sec_start_y_mark), (sec_end_x_mark, sec_end_y_mark), 3)
    
    # Vinklerne til hhv. sekunder, minutter og timer
    angle_sec = math.radians(360/60) * datetime.now().second - math.radians(90)
    angle_min = math.radians(360/60) * datetime.now().minute - math.radians(90)
    angle_hour = math.radians(360/12) * (datetime.now().hour + datetime.now().minute / 60 + datetime.now().second / 3600) - math.radians(90)
    # Dette giver en flydende overgang for timerviseren - så den ikke tikker direkte fra eks. kl. 11 til kl. 12

    # Timeviser
    hour_end_x = center[0] + (radius_cirkel - 100) * math.cos(angle_hour)
    hour_end_y = center[1] + (radius_cirkel - 100) * math.sin(angle_hour)
    pygame.draw.line(screen, (0, 0, 0), (center), (hour_end_x, hour_end_y), 10)
    
    # Minutviser
    min_end_x = center[0] + (radius_cirkel - 15) * math.cos(angle_min)
    min_end_y = center[1] + (radius_cirkel - 15) * math.sin(angle_min)
    pygame.draw.line(screen, (0, 0, 0), (center), (min_end_x, min_end_y), 10)
    
    # Sekundviser
    sec_end_x = center[0] + (radius_cirkel - 15) * math.cos(angle_sec)
    sec_end_y = center[1] + (radius_cirkel - 15) * math.sin(angle_sec)
    pygame.draw.line(screen, (255, 0, 0), (center), (sec_end_x, sec_end_y), 3)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
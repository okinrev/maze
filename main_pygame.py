import pygame, time
import get_path
import sys
 
file = str(sys.argv[2])
block_img = pygame.image.load("imgs/block.png")
path_img = pygame.image.load("imgs/path.png")
pac_img = pygame.image.load("imgs/pacman.png")
end_img = pygame.image.load("imgs/reward.png")
yellow_key_img = pygame.image.load("imgs/yellow_key.png")
blue_key_img = pygame.image.load("imgs/blue_key.png")
yellow_door_img = pygame.image.load("imgs/yellow_door.png")
blue_door_img = pygame.image.load("imgs/blue_door.png")
red_door_img = pygame.image.load("imgs/red_door.png")
red_key_img = pygame.image.load("imgs/red_key.png")
green_door_img = pygame.image.load("imgs/green_door.png")
green_key_img = pygame.image.load("imgs/green_key.png")
ghost_img = pygame.image.load("imgs/ghost.png")
pink_img = pygame.image.load("imgs/pink_cell.png")

class winui(object):
    def __init__(self):
        self.position = None
        self.screen = None
        self.maze_data = None
        self.cell = None
        self.temp_pink_list = None
        self.count_ghost = None
        self.all_pink_cells = None
        self.not_valid_cells = None
        self.start = None
        self.end = None
        self.path = None
        self.test_list = None

        
    def find_pink_pattern(x, y):
        k = int(winui.cell)-1
        v = 0
        check_pos=[x,(y-1)]
        if check_pos in winui.not_valid_cells:
            up_full = False
        else:
            up_full = True
        check_pos=[x,(y+1)]
        if check_pos in winui.not_valid_cells:
            down_full = False
        else:
            down_full = True
        check_pos=[(x-1),y]
        if check_pos in winui.not_valid_cells:
            left_full = False
        else:
            left_full = True
        #print(winui.not_valid_cells)
        check_pos=[(x+1),y]
        if check_pos in winui.not_valid_cells:
            right_full = False
        else:
            right_full = True
        #print(right_full)
        check_pos=[(x-1),(y-1)]
        if check_pos in winui.not_valid_cells or ([(x-1),y] in winui.not_valid_cells and [x,(y-1)] in winui.not_valid_cells):
            up_left_full = False
        else:
            up_left_full = True
        check_pos=[(x+1),(y-1)]
        if check_pos in winui.not_valid_cells or ([(x+1),y] in winui.not_valid_cells and [x,(y-1)] in winui.not_valid_cells):
            up_right_full = False
        else:
            up_right_full = True
        check_pos=[(x+1),(y+1)]
        if check_pos in winui.not_valid_cells or ([(x+1),y] in winui.not_valid_cells and [x,(y+1)] in winui.not_valid_cells):
            down_right_full = False
        else:
            down_right_full = True
        check_pos=[(x-1),(y+1)]
        if check_pos in winui.not_valid_cells or ([(x-1),y] in winui.not_valid_cells and [x,(y+1)] in winui.not_valid_cells):
            down_left_full = False
        else:
            down_left_full = True

        for i in range(1, k+1):
            #down left
            check_pos=[(x-i),(y+i)]
            if check_pos not in winui.not_valid_cells and down_left_full==True :
                #print("True", check_pos)
                winui.temp_pink_list.append(check_pos)
                down_left_full = True
            else:
                down_left_full = False
                #print("False", check_pos)
            #up
            check_pos=[x,(y-i)]
            if check_pos not in winui.not_valid_cells and up_full==True:
                winui.temp_pink_list.append(check_pos)
                up_full = True
            else:
                up_full = False                       

            #right
            check_pos=[(x+i),y]
            if check_pos not in winui.not_valid_cells and right_full==True:
                winui.temp_pink_list.append(check_pos)
                right_full = True
            else:
                right_full = False

            #left
            check_pos=[(x-i),y]
            if check_pos not in winui.not_valid_cells and left_full==True:
                winui.temp_pink_list.append(check_pos)
                left_full = True
            else:
                left_full = False

            #down
            check_pos=[x,(y+i)]
            if check_pos not in winui.not_valid_cells and down_full==True:
                winui.temp_pink_list.append(check_pos)
                down_full = True
            else:
                down_full = False

            #up right
            check_pos=[(x+i),(y-i)]
            if check_pos not in winui.not_valid_cells and up_right_full==True:
                winui.temp_pink_list.append(check_pos)
                up_right_full = True
            else:
                up_right_full = False

            #up left
            check_pos=[(x-i),(y-i)]
            if check_pos not in winui.not_valid_cells and up_left_full==True:
                winui.temp_pink_list.append(check_pos)
                up_left_full = True
            else:
                up_left_full = False

            #down right
            check_pos=[(x+i),(y+i)]
            if check_pos not in winui.not_valid_cells and down_right_full==True:
                winui.temp_pink_list.append(check_pos)
                down_right_full = True
            else:
                down_right_full = False
        #print(winui.temp_pink_list)
        
    def init_positions():
        winui.all_pink_cells = []
        winui.temp_pink_list = []
        winui.path = []
        winui.position = winui.start
        winui.test_list = get_path.main_start(file)
    def load_maze():
        with open(file) as f:
            winui.maze_data = [list(line.strip()) for line in f]
        return winui.maze_data
    def maze_data_clean():
        for sub in winui.maze_data:
            for elt in sub:
                if elt==' ':
                    sub.remove(elt)
    # Définition de la taille de la fenêtre
    def set_window():
        window_size = (len(winui.maze_data[0])*53, len(winui.maze_data)*53)
        winui.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('The Crazy Maze Runner')
        return winui.screen

    def set_pink_cell():
        for pink_cell in winui.temp_pink_list:
            px=pink_cell[0]
            py=pink_cell[1] 
            if pink_cell not in winui.not_valid_cells:
                winui.screen.blit(pink_img, (px*53, py*53))

    def pink_zone(x, y):
        winui.find_pink_pattern(x, y)
        winui.set_pink_cell()

    def move(pos, next_pos, previous_pos):
        print("pos from liste :", pos, next_pos, previous_pos)
        pos_x = pos[0]
        pos_y = pos[1]
        nxt_pos_y = next_pos[1]
        nxt_pos_x = next_pos[0]
        if previous_pos!=None:
            previous_pos_x = previous_pos[0]
            previous_pos_y = previous_pos[1]
            winui.screen.blit(path_img, (previous_pos_x*53, previous_pos_y*53))
            print("pirnted free on", previous_pos_x, previous_pos_y)
        #print("pos from move :",(pos_x, pos_y), (nxt_pos_x, nxt_pos_y))
        if (pos_x, pos_y) == winui.start:
            #print(True)
            winui.screen.blit(pac_img, (pos_x*53, pos_y*53))
            pygame.display.update()
            time.sleep(1)
        time.sleep(1)
        winui.screen.blit(pac_img, (nxt_pos_x*53, nxt_pos_y*53))
        print("pirnted pac on", nxt_pos_x, nxt_pos_y)
        
        pygame.display.update()
        #time.sleep(1)

    def get_values():
        winui.count_ghost = 0
        winui.not_valid_cells = []
        for y, row in enumerate(winui.maze_data):
            for x, winui.cell in enumerate(row):
                coord=[y,x]
                if winui.cell.isnumeric()==True:
                    if int(winui.cell) > 1:
                        winui.count_ghost+=1
                if winui.cell == "s":
                    winui.start=coord
                if winui.cell == "e":
                    winui.end=coord
                coord=[x,y]
                if winui.cell != "0":
                    winui.not_valid_cells.append(coord)
    # Boucle principale
    def main_loop():
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Dessin de la grille
            for y, row in enumerate(winui.maze_data):
                for x, winui.cell in enumerate(row):
                    coord=[x,y]
                    img=pac_img
                    if winui.cell == "1":
                        img=block_img
                    if winui.cell == "0":
                        if coord in winui.all_pink_cells:
                            img=pink_img
                        else:
                            img=path_img
                    if winui.cell == "s":
                        img=pac_img
                    if winui.cell == "e":
                        img=end_img
                    if winui.cell == "a":
                        img=yellow_key_img
                    if winui.cell == "b":
                        img=yellow_door_img
                    if winui.cell == "i":
                        img=blue_door_img
                    if winui.cell == "h":
                        img=blue_key_img
                    if winui.cell == "g":
                        img=red_door_img
                    if winui.cell == "f":
                        img=red_key_img
                    if winui.cell == "c":
                        img=green_door_img
                    if winui.cell == "d":
                        img=green_key_img
                    if winui.cell == "2" or winui.cell == "3" or winui.cell == "4" or winui.cell == "5" or winui.cell == "6":
                        img=ghost_img
                        if  len(winui.temp_pink_list)==0:
                            winui.pink_zone(x, y)
                        for pink_cell_elt in winui.temp_pink_list:
                            if pink_cell_elt not in winui.all_pink_cells:
                                winui.all_pink_cells.append(pink_cell_elt)
                        winui.temp_pink_list=[]
                    if winui.cell == " ":
                        pass
                    winui.screen.blit(img, (x*53, y*53))
            if running == True:
                print("end", winui.end)
                for id, pos in enumerate(winui.test_list):
                    print(pos, id)
                    if pos != winui.test_list[-1]:
                        if winui.test_list[id-1]==winui.test_list[id+1]:
                            index_next=len(winui.test_list) - winui.test_list[::-1].index(pos)-1
                        else:
                            index_next=id
                        if pos != (winui.start[0], winui.start[0]):
                            previous_pos=winui.test_list[id-1]
                        else:
                            previous_pos=None
                        next_pos=winui.test_list[index_next]
                        winui.move(pos, next_pos, previous_pos)
                    if pos == winui.test_list[-1]:
                        print("Le chemin est résolu !!!!")
                        print(winui.test_list)
                        exit()
            pygame.display.flip()
            clock.tick(60)

# Initialisation de Pygame
pygame.init()


winui.load_maze()
winui.maze_data_clean()
winui.set_window()
winui.get_values()
winui.init_positions()
winui.main_loop()

# Nettoyage de Pygame
pygame.quit()




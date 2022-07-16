import copy
import pygame
from random import choice
from time import sleep
class Game():

    pygame.init()
    blue=(20,189,172)
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption("tic tac toe")
    screen.fill(blue)
   # sys.setrecursionlimit(150000)
    def __init__(self):
        self.board=[ [-1,-1,-1] for i in range(3)]
        self.player_number=0
    
    def show_board(self):
        for i in self.board:
            print(i)
    
    def can_draw(self,y,x):
        if self.board[x][y]!=-1 :
            return False
        return True

    def draw_circle(self,x,y):
        pygame.draw.circle(self.screen, (242,235,211), ((x*200)+100,(y*200)+100), 60,15)

    def draw_cross(self,x,y):
        pygame.draw.line(self.screen, (84,84,84), (x * 200 + 55, y * 200 + 200 - 55), (x * 200 + 200 - 55, y * 200 + 55), 25 )	
        pygame.draw.line(self.screen, (84,84,84), (x * 200 + 55, y * 200 + 55), (x * 200 + 200 - 55, y * 200 + 200 - 55), 25 )

    def get_possible_places(self,game_board):
        places=[]
        for i in range(len(game_board)):
            for j in range(len(game_board[i])):
                if game_board[i][j]==-1:
                    places.append((i,j))
        print(places)
        return places

    def random_play(self):
        sleep(0.2)
        return choice(self.get_possible_places(self.board))

    def MM(self, game_board, is_maximazing,player_number):
        won=self.check_win(game_board)
        if won==0:
            #P0 won -> maximazing
            return 1,0
        if won==1:
            #P1 won -> minimazing
            return -1,0
        
        elif self.is_full(game_board):
            #Tie ->  neutral
            return 0,0

        if is_maximazing:
            best_moove_number = float('-inf')
            best_move = (0,0)
            possibles_mooves = self.get_possible_places(game_board)

            for (line, col) in possibles_mooves:
                temp_board = copy.deepcopy(game_board)
                temp_board[line][col]='X' if player_number==0 else "O"
                MM_status = self.MM(temp_board, False,(player_number+1)%2)[0]
                print(MM_status)
                if MM_status > best_moove_number:
                    best_moove_number = MM_status
                    best_move = (line, col)

            return best_moove_number, best_move

        elif (is_maximazing)==False:
            best_moove_number = float('+inf')
            best_move = (0,0)
            possibles_mooves =self.get_possible_places(game_board)
            for (line, col) in possibles_mooves:
                temp_board = copy.deepcopy(game_board)
                temp_board[line][col]='X' if player_number==0 else "O"
                MM_status = self.MM(temp_board, True,(player_number+1)%2)[0]
                print(MM_status)
                if MM_status < best_moove_number:
                    best_moove_number = MM_status
                    best_move = (line, col)

            return best_moove_number, best_move

    def user_play(self):
        print(f"Player {self.player_number+1}, choose where do you place your piece (0,0)")
        #res=input(">>")
        while 1:
            has_played=False
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
                
                #played=self.random_play()
                #played=self.MM(self.board,False)

                ###ia vs ia = MM_status,moove=self.MM(self.board,False if self.player_number==1 else True,self.player_number)
                if self.player_number==1:
                    moove=self.MM(self.board,False,self.player_number)[1]
                    column=moove[0]
                    line=moove[1]
                    has_played=True
                    self.show_board()
                    print(f"Choosen : ({line},{column})")

                IAvsIA= """   if self.player_number==0:
                        #played=self.random_play()
                        #played=self.MM(self.board,False)
                        MM_status,moove=self.MM(self.board,True,self.player_number)
                        column=moove[0]
                        line=moove[1]
                        has_played=True
                        self.show_board()
                        print(f"Choosen : ({line},{column})")
                        """

                if event.type==pygame.MOUSEBUTTONDOWN or has_played:
                    if has_played==False:
                        mouseX=event.pos[0]
                        mouseY=event.pos[1]
                        column=int(mouseY//200)
                        line=int(mouseX//200)
                    if self.can_draw(line,column):
                        if self.player_number==1:
                            self.draw_circle(line,column)
                        elif self.player_number==0:
                            self.draw_cross(line,column)
                        return (int(column),int(line))
                    else:
                        print("Not here")
    
        

    def add_piece(self,player_number):
        new_piece=self.user_play()
        if player_number==0:
            self.board[new_piece[0]][new_piece[1]]="X"
        else:
            self.board[new_piece[0]][new_piece[1]]="O"

    def is_full(self,game_board=0):
        if game_board==0:
            game_board=self.board

        for i in game_board:
            if i.count(-1)!=0:
                return False
        return True

    def check_win(self,game_board=0):
        if game_board==0:
            game_board=self.board

        for i in game_board:
            if i.count("X")==3:
                return 0
            elif i.count("O")==3:
                return 1
        
        if (game_board[0][0]=="X" and game_board[0][1]=="X" and game_board[0][2]=="X") or (game_board[1][0]=="X" and game_board[1][1]=="X" and game_board[1][2]=="X") or (game_board[2][0]=="X" and game_board[2][1]=="X" and game_board[2][2]=="X"):
            return 0
        elif (game_board[0][0]=="O" and game_board[0][1]=="O" and game_board[0][2]=="O") or (game_board[1][0]=="O" and game_board[1][1]=="O" and game_board[1][2]=="O") or (game_board[2][0]=="O" and game_board[2][1]=="O" and game_board[2][2]=="O"):
            return 1

        if (game_board[0][0]=="X" and game_board[1][1]=="X" and game_board[2][2]=="X") or (game_board[0][2]=="X" and game_board[1][1]=="X" and game_board[2][0]=="X"):
            return 0
        elif (game_board[0][0]=="O" and game_board[1][1]=="O" and game_board[2][2]=="O") or (game_board[0][2]=="O" and game_board[1][1]=="O" and game_board[2][0]=="O"):
            return 1


        if (game_board[0][0]=="X" and game_board[1][0]=="X" and game_board[2][0]=="X") or (game_board[0][1]=="X" and game_board[1][1]=="X" and game_board[2][1]=="X") or (game_board[0][2]=="X" and game_board[1][2]=="X" and game_board[2][2]=="X"):
            return 0
        elif (game_board[0][0]=="O" and game_board[1][0]=="O" and game_board[2][0]=="O") or (game_board[0][1]=="O" and game_board[1][1]=="O" and game_board[2][1]=="O") or (game_board[0][2]=="O" and game_board[1][2]=="O" and game_board[2][2]=="O"):
            return 1

        if self.is_full():
            return 3
        return -1

def lines(screen):
    pygame.draw.line(screen,(23,145,135),(0,200),(600,200),15)
    pygame.draw.line(screen,(23,145,135),(0,400),(600,400),15)
    pygame.draw.line(screen,(23,145,135),(200,0),(200,600),15)
    pygame.draw.line(screen,(23,145,135),(400,0),(400,600),15)



play=Game()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    lines(play.screen)
    play.show_board()
    pygame.display.update()

    play.add_piece(play.player_number)  

    state=play.check_win()

    play.player_number=(play.player_number+1)%2
    my_font = pygame.font.SysFont('Comic Sans MS', 140)


    if state!=-1:
        print(f"Player {state+1} won !" if state!=3 else "Tie !")
        play.show_board()
        if state==0:
            text_surface = my_font.render('You won', False, (255, 255, 255))
        elif state==1:
            text_surface = my_font.render('AI won', False, (255,255,255))
        else:
            text_surface = my_font.render('Tie', False, (255, 255 ,255))

        Game.screen.blit(text_surface, (150,150))
        pygame.display.update()
        sleep(5)
        break

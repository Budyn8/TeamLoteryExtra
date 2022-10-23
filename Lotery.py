import random
Num = 1
text = '''
Enter:
0 - to Exit
1 - to make a new pool
2 - to take random teams from current pool
3 - to add new player
4 - to delete a player
5 - to change an ammount of teams
'''
def fTeams():
    global Players
    global Teams
    global PlayersInTeam
    Players = int(input('Enter how many players '))
    Teams = int(input('Enter how many teams '))
    PlayersInTeam = int(input('Enter the ammount of players in team '))
    if(Players == 0 or Teams == 0 or PlayersInTeam == 0):
            exit()
                
def TeamAdd():
    fTeams()
    while(Players>Teams*PlayersInTeam or Players<Teams):
        if(Players>Teams*PlayersInTeam):
            print("The ammount of players is too big")
            fTeams()
        else:
            print("The ammount of Teams, can not be grater than Players")
            fTeams()

def varAdd():
    global PlayerList
    PlayerList = []

def PlayerAdd():
    global PlayerList
    global SavedTeams
    SavedTeams = []
    i = 1
    while(i<=Players):
        print('Enter',i,'player')
        Player = [input()]
        if(Player == 'Exit'):
            exit()
        PlayerList += Player
        i += 1

def xPlayerAdd(x):
    global Players
    global PlayerList
    global PlayersInTeam
    i = 1
    Players += x
    if(x%2 == 0):
        PlayersInTeam += x/2
    else:
        PlayersInTeam += (x+1)/2
    while(i<=x):
        print('Enter',i,'player')
        Player = [input()]
        PlayerList += Player
        i += 1

def AddPlayer():
    c = Players
    d = Teams
    f = PlayersInTeam
    e = 1
    global PlayerList
    while((d*f)/c != 1):
        PlayerList+=[e]
        c+=1
        e+=1
    print(PlayerList)

def PlayeRead():
    i = 1
    for a in PlayerList:
        print(i,'. ',a)
        i+=1

def PlayerDeleat(x):
    global PlayerList
    global Players
    global PlayersInTeam
    i = 1
    Players -= x
    if(x%2 == 0):
        PlayersInTeam -= x/2
    else:
        PlayersInTeam -= (x+1)/2
    while(i<=x):
        print('Enter',i,'player')
        Player = input()
        if(Player in PlayerList):
            PlayerList.remove(Player)
            i+=1
        else:
            print('This player isn\'t on the player list')
                
def TeamRead():
    a = 1
    b = 1
    global SavedTeams
    SavedTeams += PlayerList
    while(a<=Teams):
        print(a,'team is:')
        while(b<=PlayersInTeam):
            Player = random.choice(SavedTeams)
            SavedTeams.remove(Player)
            print('-',Player)
            b+=1
        b-=PlayersInTeam
        a+=1

def TeamNumChange(x):
    global Teams
    global PlayersInTeam
    i = len(PlayerList)        
    if(i%x != 0):
        print('You dint have enought ammount of players')
        if(Players<x):
            print('You need to add',(PlayersInTeam*x)-i,'players')
        else:
            print('You need to remove',(i%x),'players or add',(PlayersInTeam*x)-i,'players')
    else:
        PlayersInTeam = i/x
        Teams = x

while(Num!=0):        
    if(Num == 1):
        TeamAdd()
        varAdd()
        AddPlayer()
        PlayerAdd()
    if(Num == 2):
        TeamRead()
    if(Num == 3):
        PlayeRead
        xPlayerAdd(int(input('Enter how many players you want to add ')))
        AddPlayer()
    if(Num == 4):
        PlayeRead()
        PlayerDeleat(int(input('Enter how many players you want to remove ')))
    if(Num == 5):
        TeamNumChange(int(input('Set the new number of teams ')))
    Num = int(input(text))

##############################################################################
#   Computer Project 10
# 
#   Algorithm
#
#   Program consists of 11 functions that allow user to play 'Baker's Game'\
#   by using provided cards class and implementing game rules as conditions.
#
#   setup_game: sets cells, foundations, and tableaus of game. 
#    Deals tabelaus from shuffled deck, left to right.
#    Returns cells, foundations, and tableaus.
#
#   display_game: prints formatted cells, foundations, and tableaus for player
#
#   valid_fnd_move: determines if foundation move entered by user is legal
#
#   valid_tab_move: determines if tableau move entered by user is legal
#
#   tableau_to_cell: using valid_tab_move and error checking, attempts\
#    to move tableau card to cell.
#
#   tableau_to_foundation: using valid_tab_move and error checking, attempts\
#    to move tableau card to foundation
#
#   tableau_to_tableau: using valid_tab_move and error checking, attempts\
#    to move tableau card to another row in tableau.
#
#   cell_to_foundation: using valid_fnd_move and error checking, attempts\
#    to move card in cell to row in foundation.
#
#   cell_to_tableau: using valid_tab_move and error checking, attempts\
#    to move cell card to row in tableau.
#
#   is_winner: determines if player has won game.
#
#   main: main function of program, executes each function and goes through\
#   each possible command.
##############################################################################




#import sys
#def input( prompt=None ):
    #if prompt != None:
       # print( prompt, end="" )
    #aaa_str = sys.stdin.readline()
    #aaa_str = aaa_str.rstrip( "\n" )
    #print( aaa_str )
    #return aaa_str

    
import string

import cards #This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""


MENU = """
    Game commands:
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game
"""
    
def valid_fnd_move(src_card, dest_card):
    '''
    Determines if foundation move entered by user is legal using if statements.
    '''
    # if cars is not an ace #
    if dest_card == '' and src_card.rank() != 1:
        # raise error #
        raise RuntimeError("Invalid move: Source card is not an Ace")
    # if card is ace #
    if dest_card == '' and src_card.rank() == 1:
        # proceed with move #
        return
    #if cards are not of same suit and source card is not one more than last#
    if not(dest_card.suit() == src_card.suit() and\
           src_card.rank() == dest_card.rank() + 1):
        # raise error #
        raise RuntimeError("Invalid move: Wrong suit or wrong rank")
    # if cards are of same suit and source card is one more than last #
    if dest_card.suit() == src_card.suit() and\
           src_card.rank() == dest_card.rank() + 1: 
        # proceed with move #
        return

        
def valid_tab_move(src_card, dest_card): 
    '''
    Determines if tableau move entered by user is legal using if statements.
    '''
    # if cards are not of same suit and rank of source card is not one less #
    if not(dest_card.suit() == src_card.suit() and\
           src_card.rank() == dest_card.rank() - 1):
        # raise error #
        raise RuntimeError("Invalid move: Wrong suit or wrong rank")
    # if cards are of same suit and source card is one less #
    if dest_card.suit() == src_card.suit() and\
           src_card.rank() == dest_card.rank() - 1: 
        # proceed with move #
        return
    
    
def tableau_to_cell(tabs, cells, tab, cell):
    '''
    Attempts moving tableau card to cell using if/else statements. 
    '''
    # if tableau row is empty #
    if len(tabs[tab-1]) == 0:
        # raise error #
        raise RuntimeError("Empty tab silly")
    else:
        card = tabs[tab-1].pop()
        # if cell is empty #
        if cells[cell-1] == []:
            cells[cell-1].append(card)
            # move card here #
            return
        else:
            tabs[tab-1].append(card)
            # if cell already has card, raise error #
            raise RuntimeError("Cell is not empty")
            
            
def tableau_to_foundation(tabs, fnds, tab, fnd):
    '''
    Attempts moving tableau card to foundation by if/else statements.
    '''
    # if tableau is empty #
    if tabs[tab-1] == []:
        # raise error #
        raise RuntimeError("Empty tab")
    # if foundation is empty #
    if fnds[fnd-1] == []:
        # assigns empty string to dest_card #
        dest_card = ''
        # assigns last value of tableau row to src_card #
        src_card = tabs[tab-1].pop()
        tabs[tab-1].append(src_card)
        
    # if foundation row already has cards #
    else:
        # assigns last value of foundation stack to dest_card #
        dest_card = fnds[fnd-1].pop()
        fnds[fnd-1].append(dest_card)
        # assigns last value of tableau row to src_card #
        src_card = tabs[tab-1].pop() 
        tabs[tab-1].append(src_card)
   
    # if move is deemed valid, proceed with move #    
    valid_fnd_move(src_card, dest_card)
    # appends src_card to foundation #
    fnds[fnd-1].append(src_card)
    # removes src_card from tableau #
    src_card = tabs[tab-1].pop() 
          
            
def tableau_to_tableau(tabs, tab1, tab2):
    '''
    Attempts moving tableau card to another row in tableau, using if/else\
    statements. 
    '''
    # assigns last value of tableau row to src card #
    src_card = tabs[tab1-1].pop()
    tabs[tab1-1].append(src_card)
    # if tableau row is empty #
    if tabs[tab2-1] == []:
        # move tableau card to row #
        tabs[tab2-1].append(src_card)
        src_card = tabs[tab1-1].pop()
    else:
        # last row of destination tableau assigned to dest_card #
        dest_card = tabs[tab2-1].pop()
        tabs[tab2-1].append(dest_card)
        # if move is deemed valid, proceed with move #
        valid_tab_move(src_card, dest_card)
        # src_card appended to end of destination tableau list #
        tabs[tab2-1].append(src_card)
        # source card removed from original row #
        src_card = tabs[tab1-1].pop()

        
def cell_to_foundation(cells, fnds, cell, fnd):
    '''
    Attempts moving cell card to foundation by using if/else statements.
    '''
    # if cell is empty #
    if cells[cell-1] == []:
        # raise error #
        raise RuntimeError("empty cell")
    # if foundation is empty #
    if fnds[fnd-1] == []:
        # assign empty string to dest_card #
        dest_card = ''
        # value of cell assigned to src_card #
        src_card = cells[cell-1].pop()
        cells[cell-1].append(src_card)
    # if foundation card already exists #
    else:
        # last value of foundation row (top card) assigned to dest_card #
        dest_card = fnds[fnd-1].pop()
        fnds[fnd-1].append(dest_card)
        # value of cell assigned to src_card #
        src_card = cells[cell-1].pop() 
        cells[cell-1].append(src_card)
    # if move is deemed vlid, proceed with move #
    valid_fnd_move(src_card, dest_card)
    # src_card is appended to foundation row #
    fnds[fnd-1].append(src_card)
    # src_card is removed from cell #
    src_card = cells[cell-1].pop() 

    
def cell_to_tableau(cells, tabs, cell, tab):
    '''
    Attempts moving cell card to tableau using if/else statements.
    '''
    # value of cell assigned to src_card #
    src_card = cells[cell-1].pop()
    cells[cell-1].append(src_card)
    # if tableau is empty #
    if tabs[tab-1] == []:
        # move card to tableau row #
        tabs[tab-1].append(src_card)
        # remove src_card from cell #
        src_card = cells[cell-1].pop()
    # if tableau is not empty #
    else:
        # last value of tableau row assigned to dest_card #
        dest_card = tabs[tab-1].pop()
        tabs[tab-1].append(dest_card)
        # if move is deemed valid, proceed with move #
        valid_tab_move(src_card, dest_card)
        # src_card appended to tableau row #
        tabs[tab-1].append(src_card)
        # src_card removed from cell #
        src_card = cells[cell-1].pop()
              
              
def is_winner(fnds):
    '''
    Determines if user won game using if/else statements. 
    '''
    # if there are 13 cards in every foundation row (full deck) #
    if len(fnds[0]) == 13 and len(fnds[1]) == 13\
           and len(fnds[2]) == 13 and len(fnds[3]) == 13:
               # True assigned to winner #
               winner = True
    else:
        # False assigned to winner #
        winner = False
    return winner


def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 

    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).

    This function will return a tuple: (cells, foundations, tableaus)
    """
    
    #You must use this deck for the entire game.
    #We are using our cards.py file, so use the Deck class from it.
    stock = cards.Deck()
    stock.shuffle()
    #The game piles are here, you must use these.
    cells = [[], [], [], []]                    #list of 4 lists
    foundations = [[], [], [], []]              #list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []] #list of 8 lists
    
    """ YOUR SETUP CODE GOES HERE """
    # counter initialized at 1 #
    card_count=1
    for j in range(7):
        for i in range(8):
            if card_count<53:
                    #deals cards left to right #
                   tableaus[i].append(stock.deal())
                   # one added to card count ( to change rows ) #
                   card_count+=1
    return cells, foundations, tableaus


def display_game(cells, foundations, tableaus):
    '''
    Displays cells, foundations, and tableaus of game.
    '''
    #Labels for cells and foundations
    print("     =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
    print("     ", end="")
    # formatting for cells #
    for i in range(len(cells)):
        print("{:^5s}".format(str(cells[i]).strip('[]')), end='')
    print("  ", end="") 
    # formatting for foundations #
    for i in range(len(foundations)):
        try:
            last_card=foundations[i].pop()
            foundations[i].append(last_card)
            print("{:^5s}".format(str(last_card)), end='')
        except:
            print("     ", end='')
    

    print()
    #Labels for tableaus
    print("    ================Tableaus=================")
    print("    --1----2----3----4----5----6----7----8---") 
    # formatting for tableau #
    j_int=0
    while j_int<12:
        i_int=0
        print("     ", end='')
        while i_int<8:
           try:
               print("{:^5s}".format(str(tableaus[i_int][j_int])), end='')
               i_int+=1
           except:
               print("     ", end='')
               i_int+=1
        print("")
        j_int+=1
 
#HERE IS THE MAIN BODY OF OUR CODE
def main():
    print(RULES)
    cells, fnds, tabs = setup_game()
    display_game(cells, fnds, tabs)
    print(MENU)
    command = input("prompt :> ").strip()
    # while user does not try to quit program #
    while command != 'q':
        try:
            # error checking #
            if command == '':
                raise RuntimeError("You hit Enter. Wrong command, try again.")
            # command entered split into list #
            command_list = command.split()
            command = command_list[0]
            # if there is more than 1 word in command #
            if len(command_list) == 3:
                x = command_list[1]
                y = command_list[2]
                # error checking #
                try:                
                    x,y = int(x), int(y)
                except: 
                    raise RuntimeError("One or both numbers are not integers.")
            # if certain command is called, error checking, calling of function#
            if command.lower() == 'tc':
                if x > 8 or y > 4:
                    raise RuntimeError("Integer out of range!")
                if x < 1 or y < 1:
                    raise RuntimeError("Integer out of range!")
                tableau_to_cell(tabs,cells,x,y)
            if command.lower() == 'tf':
                if x > 8 or y > 4:
                    raise RuntimeError("Integer out of range!")
                if x < 1 or y < 1:
                    raise RuntimeError("Integer out of range!")
                tableau_to_foundation(tabs,fnds,x,y)
            if command.lower() == 'tt':
                if x > 8 or y > 8:
                    raise RuntimeError("Integer out of range!")
                if x < 1 or y < 1:
                    raise RuntimeError("Integer out of range!")
                tableau_to_tableau(tabs,x,y)
            if command.lower() == 'cf':
                if x > 4 or y > 4:
                    raise RuntimeError("Integer out of range!")
                if x < 1 or y < 1:
                    raise RuntimeError("Integer out of range!")
                cell_to_foundation(cells,fnds,x,y)
            if command.lower() == 'ct':
                if x > 4 or y > 8:
                    raise RuntimeError("Integer out of range!")
                if x < 1 or y < 1:
                    raise RuntimeError("Integer out of range!")
                cell_to_tableau(cells,tabs,x,y)
            # commands that are only 1 character #
            if len(command_list) != 3:
                if command.lower() == 'h':
                    print(MENU)
                else:
                    if command.lower() == 'r':
                        print("Starting fresh (Game reset)!")
                        cells, fnds, tabs = setup_game()
                        print(MENU)
                    else:
                        if command.lower() == 'q':
                            break
                        else: 
                            print("Wrong command. Try again.")
        #Any RuntimeError you raise lands here #
        except RuntimeError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
        display_game(cells, fnds, tabs)                
        winner = is_winner(fnds)
        # checking for winner #
        if winner == True:
            print("You won the game!")
            break
        command = input("prompt :> ").strip()
        
        
        
if __name__ == "__main__": 
    main()
    
# Questions
#Q1: 4
#Q2: 6
#Q3: 6
#Q4: 6
#Q5: 7
    

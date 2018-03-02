##############################################################################
#
#   Computer Project 11
#
#   Algorithm
#
#   program consists of Matrix class and two functions: using adjacency matrix\
#   and inputed user txt file, finds least number of TAs necessary to help\
#   room (1 TA can work a room and the rooms adjacent to it)
#
#   open_file: attempts opening file if it exists 
#   
#   main: main function of program, using matrix class and three nested for\
#   loops, finds least number of TA's necessary to work the maximum amount of\
#   rooms.
#
##############################################################################


import itertools

class Matrix(object):
    '''Add your docstring here.'''
    
    def __init__(self):  # no modification is needed for this method, but you may modify it if you wish to
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):  #fp is a file pointer
        '''Build an adjacency matrix that you read from a file fp.'''
        n = fp.readline()
        # converts n to integer #
        n = int(n)
        self._rooms = n
        # for loop creating list of lists, depending on number of users #
        for i in range(n):
            self._matrix.append(set())
        # for loop iterating through lines of txt file #
        for line in fp:
            # assigns stripped/split string to a and b #
            a,b=line.split()
            # converts a and b to integers #
            a,b = int(a),int(b)
            # adds b to the set of a #
            self._matrix[a-1].add(b)
            # adds a to the set of b #
            self._matrix[b-1].add(a)

    def __str__(self):
        '''Return the matrix as a string.'''
        #
        j = 1
        s = ''
        # fornatting for printing adjacency matrix #
        for i in range(self._rooms):
                s += str(j)+': '+str(self._matrix[i]).strip('{}').replace(',','')+'\n'
                j+=1
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        # Hint: only one line, return something, is needed
        return self._matrix[index-1]

    def rooms(self):
        '''Return the number of rooms'''
        # Hint: only one line, return something, is needed
        return len(self._matrix)

def open_file():
    '''
    Using user's input, attempts to open file (try/except)
    Returns file pointer
       '''
    # driver loop for user's file input #
    while True:
        file_input = input("Enter a filename: ")
        try:
            # while file exists, attempt opening #
            fp = open(file_input)
            # return file pointer #
            return fp
        # if file does not exist, prints error statement #
        except FileNotFoundError:
            print("\nError: File does not exist!")
def main():
    # functions called #
    fp = open_file()
    M = Matrix()
    M.read_file(fp)
    rooms = M.rooms()
    room_list = []
    room_num = 1
    # 'done' initialized to break out of all loops #
    done = False
    #list constructed for each room #
    for i in range(rooms):
        room_list.append(room_num)
        room_num += 1
        
    for tas in range(1, rooms+1):
        # combinations found through itertools #
        for ta_combs in itertools.combinations(room_list, tas):
            ta_set = set(ta_combs)
            for j in ta_combs:
                # union of sets (to find rooms necessary) #
                ta_set = ta_set.union(M.adjacent(j))
                if len(ta_set) == rooms:
                    done = True
                    num_tas = tas
                    ta_rooms = ta_combs
                    break
                
                
                
            if done:
                break
        if done:
            break
        
    # (for printing lidt og roomd)   
    ta_rooms_str = ''
    r = False
    for i in ta_rooms:
        if r:
            ta_rooms_str += ', '
        r = True
        ta_rooms_str += str(i)
        
        
       
    print("TAs needed:", num_tas)
    print("TAs assigned to rooms:", ta_rooms_str)
    print("\nAdjacency Matrix")
    print(M)
    
    
main()

#Questions
#Q1: 5
#Q2: 4
#Q3: 6
#Q4: 6
#Q5: 7
            

    
    
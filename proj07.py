##############################################################################
#   Computer Project 7
#
#   Algorithm
#
#   Project uses 7 functions to take a network provided and suggests a friend\
#   to inputed user that has the most friends in common (not already friends).
#
#   open_file: attempts opening .txt file if file exists
# 
#   read_file: uses file pointer as an argument and creates list of lists -\
#   each user and their friends. 
#
#   num_in_common_between_lists: takes two lists as arguments. Finds greatest\
#   number of friends in common between the two lists.
#
#   init_matrix: creates empty matrix that is n x n in size 
#
#   calc_similarity_scores: takes network as an argument. Creates similarity\
#   matrix of network's size.
#
#   recommend: uses network, user_id, and similarity_matrix as arguments.
#   Finds friend in common with most mutual friends (not already friends).
#
#   main: main function of program, uses user's inputed file and user_id,\
#   to determine recommended friend (with most mutual friends)
##############################################################################



#import sys
#def input( prompt=None ):
    #if prompt != None:
        #print( prompt, end="" )
    #aaa_str = sys.stdin.readline()
    #aaa_str = aaa_str.rstrip( "\n" )
    #print( aaa_str )
    #return aaa_str


def open_file():
    '''
    Using user's input, attempts to open .txt file (try/except)
    Returns txt file
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


def read_file(fp):  
    ''' 
    Using inputed file, creates a list of lists - each user's friends
    Returns network
    '''
    # Read n and initialize the network to have n empty lists -- 
    #    one empty list for each member of the network
    # saves first line of file (network size) to n #
    n = fp.readline()
    # converts n to integer #
    n = int(n)
    # initializes network to an empty list #
    network = []
    # for loop creating list of lists, depending on number of users #
    for i in range(n):
        network.append([])
    # for loop iterating through lines of txt file #
    for line in fp:
        # assigns stripped/split string to a and b #
        a,b=line.strip().split()
        # converts a and b to integers #
        a,b = int(a),int(b)
        # adds b to the network of a #
        network[a].append(b)
        # adds a to the network of b #
        network[b].append(a)
    # returns network - list of lists #
    return network

def num_in_common_between_lists(list1, list2):
    ''' 
    Using two lists of user friends, finds greatest value of friends in common
    Returns common_friends (integer)
    '''
    # initializes friends in common to 0 #
    common_friends = 0
    # for loop iterating through first list #
    for i in list1:
        # if user in list1 also appears in list2 #
        if i in list2:
            # increment common friends by 1 #
            common_friends += 1
    # returns greatest number of friends in common between lists #
    return common_friends
            

def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    ''' 
    Creates matrix of friends in common between each user
    Returns similarity_matrix
    '''
    # similarity matrix created n x n - numbers of users in network #
    similarity_matrix = init_matrix(len(network))
    for a in range(len(network)):
        for b in range (len(network)):
            # defines common_friends as number of friends in common between 2\
            # indexes of network #
            common_friends = num_in_common_between_lists(network[a],network[b])
            # creates similarity matrix #
            similarity_matrix[a][b] = similarity_matrix[b][a] = common_friends
    return similarity_matrix
            
            
def recommend(user_id,network,similarity_matrix):
    '''
    Uses user, network, and similarity matrix to find user with most\
    friends in common that the user is not already friends with.
    
    Returns recommendation.
    '''
    # creates similarity matrix from network provided #
    similarity_matrix = calc_similarity_scores(network)
    # initializes maximum value to 0 to begin counter #
    maximum = 0
    # enumerate loop through index that is provided user id #
    for i, value in enumerate(similarity_matrix[user_id]):
        # if statement picking largest value that is not the user id and\
        # not in its network #
        if value > maximum and i != user_id and i not in network[user_id]:
            maximum = value
            recommendation = i
    # returns friend recommendation #
    return recommendation
   
def main():
    print("\nFacebook friend recommendation.\n")
    # prompts user for file and attempts to open #
    fp = open_file()
    # creates list of lists (user's and their friends) from file provided #
    network = read_file(fp)
    # creates similarity matrix from network #
    similarity_matrix = calc_similarity_scores(network)
    # acceptable range assigned to net_range #
    net_range = len(network)-1

    # driver loop for inputed user_id #
    while True:
        # while integer is entered, try #
        try:
            # prompts user for integer in network range #
            user_input = input("Enter an integer in the range 0 to "\
                               +str(net_range)+": ")
            # converts user_input to integer #
            user_id = int(user_input)
        # if non-integer entered, error message printed and loop restarted #    
        except ValueError: 
            print("Error: non-integer entered!")
            continue
        # if the user_id falls into the range of the network #
        if user_id in range (net_range):
            # recommendation found using recommend function #
            recommendation = recommend(user_id,network,similarity_matrix)
            # prints recommended friend #
            print("The suggested friend for", user_id, "is", recommendation)
            # continuation prompt #
            cont_loop = input("\nDo you want to continue? ")
            # if user inputs any form of 'yes', restart loop #
            if cont_loop.lower() == 'yes':
                continue
            # if user inputs any form of 'no', quit program #
            if cont_loop.lower() == 'no':
                break
        # if integer entered is out of range, error message printed #
        else:
            print("Error: input must be an int between 0 and ", net_range)
if __name__ == "__main__":
    main()
    
# Questions
# Q1: 7
# Q2: 4
# Q3: 6
# Q4: 6
# Q5: 7

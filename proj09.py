##############################################################################
#
#   Computer Project 9
#
#   Algorithm
#
#   Program uses 4 functions to iterate through words in provided .txt file\
#   and find co-occurance of words of user's choosing and display.
#
#   open_file: attempts opening file if it exists
#
#   read_data: iterates through file and creates dictionary with each word\
#   as a key and set of lines the word occurs on as value.
#
#   find_coccurance: using user's input, finds co-occurance between words - \
#   by finding intersection between sets.
#
#   main: main function of program, calls each function, prompts user for\
#   input, and displays co-occurance.
##############################################################################

import string

def open_file():
    '''
    Using user's input, attempts to open file (try/except).
    Returns file pointer.
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
            print("\nError -- ", end = '')
            
def read_data(fp):
    '''
    Using opened file, iterates through each line and creates a dictionary\
    with each word as a key and a set of each line the word occurs on\
    as the value.
    Returns dictionary.
    '''
    # dictionary initialized #
    D = {}
    # set initialized #
    line_num = set()
    # counter initialized at 1 (for first line) #
    counter = 1
    for line in fp:
        # lines of file iterated through and converted into list of words #
        line = line.strip()
        line = line.strip(string.punctuation)
        line = line.split()
        # all punctuation taken out of words in list #
        for i, word in enumerate(line):
            line[i] = word.replace("'","")
        for i, word in enumerate(line):
            line[i] = word.replace(",","")
        for i, word in enumerate(line):
            line[i] = word.replace(";","")
        for i, word in enumerate(line):
            line[i] = word.replace("/","")
        for i, word in enumerate(line):
            line[i] = word.replace("-","")
        # words in list converted to lowercase#
        for i, word in enumerate(line):
            word = word.lower()
            line[i] = word
        # words under 2 characters removed from list #
        for i, word in enumerate(line):
            if len(word) < 2:
                line.remove(word)
        for word in line:
            # if word not in dictionary, add to dictionary #
            if word.lower() not in D:
                line_num = set()
                # counter value added to set #
                line_num.add(counter)
                # value of dictionary key = set (containing line number) #
                D[word] = line_num
            # if word is in dictionary, add counter (line number) to set #
            elif word.lower() in D:
                value = D[word]
                value.add(counter)
        # counter goes up one after each line #        
        counter += 1
            
    return D
        
        

def find_cooccurance(D, inp_str):
    '''
    Using dictionary and user's input, finds co-occurance between words\
    (intersection of sets).
    Returns list.
    '''
    sets = []
    # creates list out of user's inputed words #
    inp_str = inp_str.lower()
    co_list = inp_str.split()
    co_list.sort()
    word_count = len(co_list)
    
    # loop for how many words there are inputed #   
    for i in range(word_count):
        # set (which is value in dictionary) appended to list #
        sets.append(D[co_list[i]])
    #inersection between all sets calculated and assigned #
    inter_sets = set.intersection(*sets)
    
    sets = []
    #set iterated through and turned into list: sets#
    for item in inter_sets:
        sets.append(item)
    
    return sets


def main():
    inp_str = ''
    
    fp = open_file()
    D = read_data(fp)
    
    #driver loop for re-prompting #
    while True:
        # if user doe not input 'q' #
        if inp_str.lower() != 'q':
            inp_str = input("\nEnter space separated words: ")
            # user's input turned into list #
            inp_list = inp_str.split()
            # punctuation taken out of input #
            exclude = set(string.punctuation)
            inp_str = ''.join(ch for ch in inp_str if ch not in exclude)
            inp_str = inp_str.lower()
            
            
            
            co_list = inp_str.split()
            # 'temp_str' created to satisy conditionals - ie symbol inputed #
            temp_str = ''.join(co_list)
            

            list_error = False
            
            # if input is not alphabetic #
            if temp_str.isalpha() == False:
                num_str = 'None'
                list_error = True
            # if input is not in dictionary #
            for i in co_list:
                if i not in D:
                    num_str = 'None'
                    list_error = True
           
            # if all words entered in dictionary and alphabetic #
            if all(key in D for key in co_list) and temp_str.isalpha() == True:

                sets = find_cooccurance(D, inp_str)
                sets.sort()
            
                num_list = []
                # turns integer list of sets into list of strings #
                for num in sets:
                    temp = str(num)
                    num_list.append(temp)
                
                
                # creates strings from lists, that will be displayed #
                co_str = ', '.join(inp_list)
                co_str = co_str.lower()
                num_str = ', '.join(num_list)
                
                # if words have no lines in common #
                if num_str == '':
                    num_str = 'None'
                print("The co-occurance for:", co_str )
                print("Lines:", num_str)
           
            # if user enters q, end program #
            if inp_str.lower() == 'q':
                break
            # if statement for words inputed that are not in D or are symbols #
            if list_error == True and num_str == 'None':
                co_str = ', '.join(inp_list)
                co_str = co_str.lower()
                print("The co-occurance for:", co_str )
                print("Lines:", num_str)
    
    

if __name__ == "__main__": 
    main()
    
#Questions
#Q1: 7
#Q2: 5
#Q3: 3
#Q4: 6
#Q5: 7
##############################################################################
#   Computer Project 6
#
#    Algorithm
#
#    Project uses 5 functions to attempt unlocking .zip files using dictionary\
#    and brute force cracking methods.
#
#   open_dict_file: attempts opening .txt file if file exists
#
#   open_zip_file: attempts opening .zip file if file exists
#
#   brute_force_attack: uses 'product' from itertools and string of entire\
#   alphabet to create password combinations of length 1-8 and attempt\
#   unlocking .zip file - returns true/false depending if cracking is succesful
#
#   dictionary_attack: uses stripped lines from inputed .txt file to attempt\
#   unlocking .zip file - returns true/false depending if cracking is succesful
#
#   main: main function of program, uses user's input to determine which\
#   cracking method to use.
#
#
###############################################################################

#import sys
#def input( prompt=None ):
    #if prompt != None:
        #print( prompt, end="" )
    #aaa_str = sys.stdin.readline()
    #aaa_str = aaa_str.rstrip( "\n" )
    #print( aaa_str )
    #return aaa_str


import zipfile
import time
import itertools 


def open_dict_file():
    '''
    Using user's input, attempts to open .txt file (try/except)
    Returns txt file
    '''
    #driver loop for user's .txt file input#
    while True:
        user_input1 = input("\nEnter dictionary file name: ")
        try:
            # while file exists attempt opening#
            dict_file = open(user_input1)
            return dict_file
        #if file does not exist, print error message#
        except FileNotFoundError:
            print("\nError: File does not exist!")


def open_zip_file():
    '''
    Using user's input, attempts to open .zip file (try/except)
    Returns zip file
    '''
    #driver loop for user's .zip file input#
    while True:
        user_input2 = input("\nEnter zip file name: ")
        try:
            #while file exists attempt opening#
            zip_file = zipfile.ZipFile(user_input2)
            return zip_file
        #if file does not exist, print error message#
        except FileNotFoundError:
            print("\nError: File does not exist!")
            
def brute_force_attack(zip_file):
    '''
    Uses generated product of alphabet from 1-8 to attempt unlocking .zip file
    Returns either true or false, depending if cracking is succesful
    '''
    from itertools import product
    #alphabet string initialized#
    options = 'abcdefghijklmnopqrstuvwxyz'
    #combos made to range from 1 character to 8#
    for n in range (1,9):
        #generates tuple of strings of products of all letters in alphabet#
        combos = [''.join(i) for i in product((options),repeat = n)]
        #for loop for each password created#
        for password in combos:
            try:
                #attempts unlocking .zip file with each password created#
                zip_file.extractall(pwd=password.encode())
                #prints password if found#
                print("Brute force password is: ",password)
                #returns true if succesful#
                return True
            except:
                a=False
    #returns false if not succesful#
    return a

def dictionary_attack(zip_file, dict_file):
    '''
    Uses stripped lines in .txt file to attempt unlocking .zip file
    Returns either true or false, depending if cracking is succesful
    '''
    #for loop for each line in .txt file#
    for line in dict_file:
        try:
            #attempts unlocking .zip file with each stripped line of .txt file#
            zip_file.extractall(pwd=line.strip().encode())
            #prints password if found#
            print("Dictionary password is: ",line.strip())
            #returns true if succesful#
            return True
        except:
            a=False
    #returns false if not succesful#
    return a
            
#main function of program#    
def main():
    #prints welcome message and warning to user#
    print("Cracking zip files")
    print("Warning: Cracking passwords is illegal due to the "\
    "Computer Fraud and Abuse Act and has a prison term of up to 10 years!\n")
    #asks for user's input of file cracking method to be used#
    user_input = input("What type of cracking ('brute force','dictionary',"\
    "'both','q'): ")
   
    #while user does not input 'q'#
    while user_input != 'q':
        #if user inputs 'brute force#
        if user_input == 'brute force':
            print('\nBrute Force Cracking')
            #uses open zip file function#
            brute_zip = open_zip_file()
            #begins timer#
            start=time.process_time()
            #uses brute force attack function to attempt unlocking file#
            brute_force_attack(brute_zip)
            #ends timer#
            end=time.process_time()
            #prints amount of time between start time and end time#
            print("Brute Force Elapsed time (sec)",round((end-start),4))
            #closes .zip file#
            brute_zip.close()
        
        #if user inputs 'dictionary'#
        elif user_input == 'dictionary':
            print('\nDictionary Cracking')
            #uses open dict file (.txt) function#
            dict_file = open_dict_file()
            #uses open zip file function#
            zip_file = open_zip_file()
            #begins timer#
            start=time.process_time()
            #uses dictionay attack function to attempt unlocking file#
            dictionary_attack(zip_file, dict_file)
            #ends timer#
            end=time.process_time()
            #prints amount of time between start time and end time#
            print("Dictionary Elapsed time (sec)",round((end-start),4))
            #closes .zip file and .txt file#
            dict_file.close()
            zip_file.close()
        
        #if user inputs 'both'#
        elif user_input == 'both':
            print('\nBoth Brute Force and Dictionary Cracking')
            #uses open dict file (.txt) function#
            dict_file = open_dict_file()
            #uses open zip file function#
            zip_file = open_zip_file()
            #begins timer#
            start=time.process_time()
             #uses dictionay attack function to attempt unlocking file#
            dict_attack = dictionary_attack(zip_file, dict_file)
            #ends timer#
            end=time.process_time()
            #prints amount of time between start time and end time#
            print("Dictonary Elapsed time (sec)",round((end-start),4))
            #closes .txt file#
            dict_file.close()
            #if dictionary cracking is not succesful#
            if dict_attack == False:
                print("\nNo password found, trying Brute Force method.")
                #begins timer#
                start=time.process_time()
                #uses brute force attack function to attempt unlocking .zip#
                brute_force_attack(zip_file)
                #ends timer#
                end=time.process_time()
                #prints amount of time between start time and end time#
                print("Brute Force Elapsed time (sec)",round((end-start),4))
                #closes .zip file#
                zip_file.close()
        
        user_input = input("What type of cracking ('brute force','dictionary',"\
    "'both','q'): ")

#executes main program function#
if __name__ == "__main__": 
    main()
    
#Questions
#Q1: 7
#Q2: 7
#Q3: 7
#Q4: 5
#Q5: 7
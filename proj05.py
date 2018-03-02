##############################################################################
#    Computer Project 5
#
#    Algorithm
#
#    program consists of 4 functions used together to decode inputed text
#
#    get_char: uses inputed ch and shift to determine english ch
#
#    get_shift: determines shift by using most frequently occuring\
#    ch in inputed text and assuming it is the letter 'E'
#
#    output_plaintext: prints decoded English text from inputed text
#
#    main: brings all functions together and executes program, loop prompts\
#    user for yes/no input to determine when text is readable and program is\
#    complete.
##############################################################################



#import sys
#def input( prompt=None ):
    #if prompt != None:
        #print( prompt, end="" )
    #aaa_str = sys.stdin.readline()
    #aaa_str = aaa_str.rstrip( "\n" )
    #print( aaa_str )
    #return aaa_str


# function that determines character after accounting for shift #
def get_char(ch,shift):
    ''' 
    Determines the shifted decoding of the character inputed.
    
    ch: The character to be decoded (str)
    
    shift: he value that the translation of each character of the cipher goes\
    up/down by (int)
    
    Returns the shifted and decoded character (str)
    '''
    # alphabet string defined #
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # assigns character's index place to 'index' #
    index = alpha.find(ch)
    # finds cipher character's index and assigns it to 'cipher_ch' #
    c_index = (index+shift) % 26 
    # assigns cipher character to 'cipher_ch' by slicing #
    cipher_ch = alpha[c_index:c_index+1]
    return cipher_ch
 

# function determines shift of cipher message #
def get_shift(s,ignore):
    '''
    Determines shift of coded cipher message by looking for most common\
    character and considering it to be the letter 'E'.
    
    s: The inputed cipher message (str)
    
    ignore: The character which is to be ignored if message is not readable\
    as English (str)
    
    Returns shift (int) and the most common character (str)
    
    '''
    # converts string to upper case #
    s = s.upper()
    # gets rid of spaces in string #
    s =  s.replace(' ','')
    # replaces ignore with empty string #
    s = s.replace(ignore,'')
    # assigns value of 0 to a_int #
    a_int = 0
    # loop associating each index with its character #
    for i, ch in enumerate(s):
        #if statement - character must be a letter #
        if ch.isalpha():
            # assigns number of times character appears in string to 'b_int' #
            b_int = s.count(ch)
            # loop for finding the most common character in cipher string #
            if a_int < b_int:
                # assigns character count (b_int) to 'a_int' and ends on\
                #largest value #
                a_int = b_int
                # determines shift using ASCII table numbers #
                shift = ord('E') - ord(ch)
                # assigns most common character to 'mx_ch' #
                max_ch = ch
    return shift, max_ch
    
# function for outputting the deciphered message into English #    
def output_plaintext(s,shift):
    ''' 
    Outputs decoded cipher message in readable English using get_shift()\
    function.
    
    s: The inputed cipher message (str)
    
    shift: he value that the translation of each character of the cipher goes\
    up/down by (int)
    
    Returns the deciphered message in readable English.
    '''
    # assigns empty string to 'decipher' #
    decipher = ''
    # for loop associating cipher string characters with their indexes #
    for i, ch in enumerate(s):
        # if statement for only letters #
        if ch.isalpha():
            # adds deciphered character to string 'decipher' #
            decipher += get_char(ch,shift)
        # else statement for characters that are not letters #
        else:
            # adds non-alphabet character to string 'decipher' #
            decipher += ch
    # prints deciphered phrase #
    print("\nDeciphered phrase is:", decipher)
    return decipher 
    
def main():
    # prints title of program #
    print("Cracking a Caesar cipher.\n")
    # assigns user's input to 's' #
    s = input("Input cipherText: \n")
    # converts string to uppercase #
    s = s.upper()
    # assigns potential shift and character to ignore (empty string)\
    # to 'shift' and 'ch_ig' #
    shift, ch_ig = get_shift(s,'')
    # uses inputed string and determined shift as parameters #
    output_plaintext(s,shift)
    # user input - is program readable in English #
    readable = input("\nIs the plaintext readable as English (yes/no): ")
    # takes spaces out of string before while loop #
    new_string = s.replace(' ','')
    # loop while user inputs 'no' #
    while readable.lower() == 'no':
        # takes out ignored character from string #
        new_string = new_string.replace(ch_ig,'')
        # finds new shift and character to ignore  #
        shift, ch_ig = get_shift(new_string,ch_ig)
        # prints deciphered message #
        output_plaintext(s,shift)
        readable = input("\nIs the plaintext readable as English (yes/no):")



# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()
    
#Questions
#1 5
#2 7
#3 7
#4 5
#5 7 


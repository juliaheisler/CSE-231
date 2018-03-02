###############################################################################
#   Computer Project 8
#
#   Algorithm
#   
#   Program uses 7 functions to take information provided in .csv file and\
#   user's region input to create organized table and scatter plot.
#
#   open_file: attempts opening file if it exists
#
#   read_file: reads through file and creates dictionary depending on region\
#   user inputs - returns dictionary and user input.
#
#   max_min: determines maxs/mins of dictionary's values - returns maxs/mins\
#   as well as states associated with them.
#
#   display_info: displays stats and maxs/mins for states in specified region\
#   plot_regression: draws line of best fit between plotted points.
#
#   plot: using x and y provided by user, creates scatter plot.
#
#   main: main function of program, calls each function and asks user if\
#   graph should be plotted.
###############################################################################



#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str
    
import pylab


REGION_LIST = ['far_west',
 'great_lakes',
 'mideast',
 'new_england',
 'plains',
 'rocky_Mountain',
 'southeast',
 'southwest',
 'all']
VALUES_LIST = ['pop', 'gdp', 'pi', 'sub', 'ce', 'tpi', 'gdpp', 'pip']
VALUES_NAMES = ['State', 'Population(m)','GDP(b)','Income(b)','Subsidies(m)',\
'Compensation(b)','Taxes(b)','GDP per capita','Income per capita']
PROMPT1 = "\nSpecify a region from this list -- far_west,great_lakes,"\
"mideast,new_england,plains,rocky_mountain,southeast,southwest,all: "
PROMPT2 = "\nSpecify x and y values, space separated from Pop, GDP, PI,"\
" Sub, CE, TPI, GDPp, PIp: "

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
            print("\nError: File does not exist! Please try again.\n")

def read_file(fp):
    '''
    Using opened file and user input, reads file and creates dictionary of\
    of states associated with inputed region.
    Returns dictionary and user's input.
    '''
    # skips over first line #
    fp.readline()
    # creates empty dictionary #
    D = {}
    user_input = ''
    counter=1
    # loop fot error checking #
    while user_input.lower() not in REGION_LIST:
        if counter>1:
            print("Error in region name. Please try again.")
        # prompt and user input for region #
        user_input = input(PROMPT1)
        counter += 1
    # if statement for region in list or all #   
    if user_input.lower() in REGION_LIST or user_input.lower() == 'all':
        
        # loop iterating through file #
        for line in fp:
            # strips and splits each word from file and creates list #
            line = line.strip()
            L1 = line.split(',')
            # associates indexes with specific variables #
            state = L1[0]
            region = L1[1]
            # converts strings in list to floats #
            for i in range(2,8):
                L1[i] = float(L1[i])
            # appends GDP per capita and Income per capita #
            L1.append(L1[3]/L1[2]*1000)
            L1.append(L1[4]/L1[2]*1000)
            # adds state as a key to dictionary and floats of list as values #
            if user_input.lower() == region.lower():
                D[state] = L1[1:]
            if user_input.lower() == 'all':
                D[state] = L1[1:]
    # returns dictionary and user input #
    return D, user_input
    
    
def max_min(D):
    '''
    Iterates through dictionary values, finding min/max of GDP per capita\
    and income per capita.
    Returns max/mins and states associated with them.
    '''
    # maxs/mins assigned exaggerated values #
    g_max=0
    g_min=1000000000000000000000000000
    i_max=0
    i_min=1000000000000000000000000000 
    #loop iterates through dictionary finding max/mins and associated states#
    for k,v in D.items():
        if v[7] > g_max:
            g_max = v[7]
            state_g_max = k
        if v[7] < g_min:
            g_min = v[7]
            state_g_min = k
        if v[8] > i_max:
            i_max = v[8]
            state_i_max = k
        if v[8] < i_min:
            i_min = v[8]
            state_i_min = k
    # returns maxs/mins and associated states #
    return g_max,state_g_max,g_min,state_g_min,i_max,state_i_max,\
    i_min,state_i_min


def display_info(D,g_max,state_g_max,g_min,state_g_min,i_max,state_i_max,\
                 i_min,state_i_min,user_input):
    '''
    Displays max/min information and states with their stats in table format.
    '''
    # defines region inputed as first index in value list #
    for k,v in D.items():
        reg_input = v[0]
        break
    # if user's input is 'all', this becomes region input #
    if user_input.lower() == 'all':
        reg_input = 'All'
    # prints maxs and mins for states in inputed region#   
    print("\nData for the", reg_input, "region:\n")
    print(state_g_max, "has the highest GDP per capita at","${:,.2f}"\
          .format(g_max))
    print(state_g_min, "has the lowest GDP per capita at","${:,.2f}"\
          .format(g_min),"\n")
    print(state_i_max, "has the highest income per capita at","${:,.2f}"\
          .format(i_max))
    print(state_i_min, "has the lowest income per capita at","${:,.2f}"\
          .format(i_min))
    
    
    print("\nData for all states in the", reg_input, "region:\n")
    
    print("{:<14s}{:>14s}{:>11s}{:>11s}{:>15s}{:>17s}{:>12s}{:>18s}{:>19s}"\
          .format('State', 'Population(m)','GDP(b)','Income(b)','Subsidies(m)'\
                  ,'Compensation(b)','Taxes(b)','GDP per capita',\
                  'Income per capita'))

    # prints stats for each state in organized table #
    for k,v in sorted(D.items()):
        print("{:<14s}{:>14,.2f}{:>11,.2f}{:>11,.2f}"\
        "{:>15,.2f}{:>17,.2f}{:>12,.2f}{:>18,.2f}{:>19,.2f}"\
        .format(k,v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8]))




def plot_regression(x,y):
    '''Draws a regression line for values in lists x and y.
       x and y must be the same length.'''
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    #creates line, only takes numpy arrays#
    m,b = pylab.polyfit(xarr,yarr, deg = 1) 
    #as parameters
    pylab.plot(xarr,m*xarr + b, '-') #plotting the regression line
 

   


def plot(D):
    '''
    Using dictionary and user's choice of x and y, creates scatter plot.
    '''
    # initializes variables #
    state_list = []
    x = []
    y = []
    a = ''
    b = ''

    # loop for error checking #
    while a.lower() not in VALUES_LIST or b.lower() not in VALUES_LIST:
        while True:
            try:   
                X_Y=input(PROMPT2)
                a,b = X_Y.split()
                break
            except ValueError:
                print("Error")
    # associates x and y indexes with indexes in values list #
    x_index = VALUES_LIST.index(a.lower())
    y_index = VALUES_LIST.index(b.lower())
    
    # appends values from dictionary to list #
    for k, v in D.items():
        state_list.append(k)
        x.append(v[x_index+1])
        y.append(v[y_index+1])
    # title of graph #
    pylab.title(VALUES_NAMES[x_index+1]+' vs. '+VALUES_NAMES[y_index+1])
    # label of x axis #
    pylab.xlabel(VALUES_NAMES[x_index+1])
    # label of y axis #
    pylab.ylabel(VALUES_NAMES[y_index+1])
    
    # plots points #
    pylab.scatter(x,y)
    
    # labels points with state names #
    for i, txt in enumerate(state_list):
        pylab.annotate(txt, (x[i],y[i]))
    # plots line of best fit #   
    plot_regression(x,y)
    # displays graph #
    pylab.savefig("plot.png")

    
def main():
    # calls each function #
    fp = open_file()
    D, user_input = read_file(fp)
    g_max,state_g_max,g_min,state_g_min,i_max,state_i_max,i_min,state_i_min\
    = max_min(D)
    display_info(D,g_max,state_g_max,g_min,state_g_min,i_max,state_i_max,\
                 i_min,state_i_min,user_input)
    plot_str =input("\nDo you want to create a plot? (yes or no) ")
    # if user inputs 'yes' plot graph #
    if plot_str.lower() == "yes":
        plot(D)
    
if __name__ == "__main__": 
    main()

#Questions
#Q1: 7
#Q2: 7
#Q3: 5
#Q4: 5
#Q5: 7

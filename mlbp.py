""" Mad Libs Generator Updated and Reworked by Amy Shah

Original code from: https://hackr.io/blog/python-projects
----------------------------------------

loop = 1
while (loop < 10):

    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")


    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")


    loop = loop + 1

"""

''' Reworked code '''
loop = 1
while (loop < 5):



    """All the questions that the program asks the user"""


    noun = input("Choose a noun: ")
    noun1 = input("Choose a noun: ")
    noun2 = input("Choose a noun: ")
    noun3 = input("Choose a noun: ")
    noun4 = input("Choose a noun: ")
    adjective1 = input("Choose an adjective (Describing word): ")
    noun5 = input("Choose a noun: ")
    adjective2 = input("Choose an adjective (Describing word): ")
    noun6 = input("Choose a noun: ")



    """ Displays the story based on the users input """
    print ("------------------------------------------")
    print (noun, "Men on a dead's man's", noun,",")
    print ("Yo ho ho and a bottle of", noun2,",")
    print (noun3, "Men on a dead's man's", noun4,",")
    print ("Yo ho ho and a bottle of",adjective1, noun5,",")
    print ()
    print ("I am the", adjective2, noun6, "Darlin'")
    print ("Don't let me be alone!")
    print ("------------------------------------------")


    """ Loop back to "loop = 1"    """
    loop = loop + 1

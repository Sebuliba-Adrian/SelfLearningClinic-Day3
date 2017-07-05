def words(text):
    """Check for a string  in the text sentence"""
    if isinstance(text, str):
        #Split the sentence by the spaces  assign each string to variable words
        words = text.split()
        #Create a dictionary word_dicts that will store the word count
        wordsDict = dict()
        #Loops through each word in words list
        for word in words:
            #Checks to see if the string is a number and converts to an integer
            if word.isdigit():
                word = int(word)
            #Check to see if word is a key in words_dict and increase it's value by 1
            if word in wordsDict.keys():
                wordsDict[word] += 1
            #Add word as a key in wordsDict and it holds a value 1
            else:
                wordsDict[word] = 1
        #Returns a words dictionary
        return wordsDict
    else:
        return TypeError
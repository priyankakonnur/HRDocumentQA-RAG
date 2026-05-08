import re


def preprocess(text: str) -> str:
    """
    Clean and normalize text for better embeddings.
    """
    text = text.replace("\n", " ")      #replace newline with space
    text = re.sub(r"\s+", " ", text)  # regular expression pattern , s is a whitespace character
    text = text.strip()# Removes whitespaces at start and end of the word

    return text

#i/p
#Hello
#World from Microdegree

#o/p
#Hello world from Microdegree

#i/p
#Hello    World from Microdegree
#0/p 
#Hello World from Microdegree


#i/p
#    Hello world from Microdegree    This starts a new paragraph
#o/p 
#Hello world from Microdegree
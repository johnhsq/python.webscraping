from urllib.request import urlopen
from random import randint

### using the inauguration speech of William Henry Harrison
### generates arbitrarily long Markov chains (with the chain length set to 100)


def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

# etrieves a random word from the dictionary, weighted by the number of times it occurs.
def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

# takes in the string of text, which was retrieved from the internet. 
# It then does some cleaning and formatting, removing quotes and putting spaces around other punctuation 
# so it is effectively treated as a separate word. 
# After this, it builds a two-dimensional dictionary—a dictionary of dictionaries—that has the following form:
#   {   
#       word_a : {word_b : 2, word_c : 1, word_d : 1},
#       word_e : {word_b : 5, word_d : 2},...
#   }
# “word_a” was found four times, two instances of which were followed by “word_b,” one instance followed by “word_c,” and one instance followed by “word_d.” 
def buildWordDict(text):
    # Remove newlines and quotes
    text = text.replace('\n', ' ');
    text = text.replace('"', '');

    # Make sure punctuation marks are treated as their own "words,"
    # so that they will be included in the Markov chain
    punctuation = [',','.',';',':']
    for symbol in punctuation:
        text = text.replace(symbol, ' {} '.format(symbol));

    words = text.split(' ')
    # Filter out empty words
    words = [word for word in words if word != '']

    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
                # Create a new dictionary for this word
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] += 1
    return wordDict

text = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt')
          .read(), 'utf-8')
wordDict = buildWordDict(text)

#Generate a Markov chain of length 100
length = 100
# starting with a random starting word, in this case "I"
chain = ['I']
for i in range(0, length):
    newWord = retrieveRandomWord(wordDict[chain[-1]])
    chain.append(newWord)

print(' '.join(chain))
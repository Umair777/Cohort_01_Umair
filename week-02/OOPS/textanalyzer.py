sample_text = """Hello there! Welcome to the world of Python programming. 
This text analyzer will help you understand the frequency of words in a given text. 
Let's analyze this text
"""

class TextAnalyzer(object):
    def __init__(self, text):
        
        #remove punctuations
        
        formatted_text = text.replace('.',"").replace(',',"").replace('!',"").replace('?',"")
        formatted_text = formatted_text.lower()
        self.fmtText = formatted_text
    
    #count the frequency of all unique words
    
    def word_frequency(self):
        words = self.fmtText.split()
        freqMap = {}
        for word in set(words):
            freqMap[word] = words.count(word)
        return freqMap
        # frequency = {}
        # for word in words:
        #     if word in frequency:
        #         frequency[word] += 1
        #     else:
        #         frequency[word] = 1
        # return frequency
        
if __name__ == "__main__":
    print('Text before formatting:')
    print(sample_text)
    print("Text Analyzer Initialized")
    analyzer = TextAnalyzer(sample_text)
    print("Text after formatting:")
    print(analyzer.fmtText)
    print("Word Frequency:")
    freq = analyzer.word_frequency()
    print(freq)
    print('datatype of the frequency: ',type(freq))
    # for word, count in freq.items():
    #     print(f"'{word}': {count}") 
    

'''OUTPUT:Text before formatting:
Hello there! Welcome to the world of Python programming. 
This text analyzer will help you understand the frequency of words in a given text. 
Let's analyze this text

Text Analyzer Initialized
Text after formatting:
hello there welcome to the world of python programming 
this text analyzer will help you understand the frequency of words in a given text 
let's analyze this text

Word Frequency:
{'understand': 1, 'hello': 1, 'help': 1, 'text': 3, 'words': 1, 'a': 1, "let's": 1, 'analyzer': 1, 'there': 1, 'of': 2, 'given': 1, 'programming': 1, 'you': 1, 'world': 1, 'will': 1, 'analyze': 1, 'in': 1, 'the': 2, 'frequency': 1, 'python': 1, 'welcome': 1, 'to': 1, 'this': 2}
datatype of the frequency:  <class 'dict'>'''


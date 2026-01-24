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
        
if __name__ == "__main__":
    print('Text before formatting:')
    print(sample_text)
    print("Text Analyzer Initialized")
    analyzer = TextAnalyzer(sample_text)
    print("Text after formatting:")
    print(analyzer.fmtText)

'''OUTPUT:Text before formatting:
Hello there! Welcome to the world of Python programming. 
This text analyzer will help you understand the frequency of words in a given text. 
Let's analyze this text

Text Analyzer Initialized
Text after formatting:
hello there welcome to the world of python programming 
this text analyzer will help you understand the frequency of words in a given text 
let's analyze this text'''
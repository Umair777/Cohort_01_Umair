

from gradio_client import file


def reading_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "The specified file was not found."
    except IOError:
        return "An error occurred while reading the file."
    
if __name__ == "__main__":
    file_path = 'myfile.txt' 
    file_content = reading_file(file_path)
    print(file_content)
    file_content2 = open(file_path, 'r')
    line1 = file_content2.readline()
    
    print("First line of the file:\n", line1)
    
    line2 = file_content2.readline()
    print("Second line of the file:\n", line2)
    
    if 'important' in line2:
        print("The word 'important' is present in the second line.")
        
    
    characters = file_content2.read(5)
    print("Next 5 characters in the file:\n", characters)
    
    characters = file_content2.seek(10) 
    print("File pointer moved to position 10.")
    
    characters = file_content2.read(5)
    print("Next 5 characters in the file:\n", characters)
    
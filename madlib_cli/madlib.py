from distutils.filelist import findall
import re
story_file = '../assets/dark_and_stormy_night_template.txt'

intro = """****Welcome to the Madlib Game!****

**** Game Instructions****

        step 1. for each input you will get an instruction to enter an adjective or noun.
        step 2. follow the input instructions and you will recieve a madlib story using
        you're previously entered nouns and adjectives.
        step 3. !!!HAVE A LAUGH!!! 
"""
# create read_temple function
def read_template(file):
    '''Open a file and read it then store as a template'''
    try:
        with open(file) as t:
            print(intro)
            template = t.read()
            return template
    except FileNotFoundError as e:
        print('CHECK PATHING OR LOCATION OF FILE!', e)

# create parse template function
def parse_template(results):
    '''look for a common pattern and seperate out the template into a stripped version and a parts version'''
    try:
        pattern = r"{(.*?)}"
        parts = tuple(re.findall(pattern, results))
        stripped = re.sub(pattern, "{}", results)
        return stripped,parts

    except AssertionError as e:  
        print(e)
# create merge function
def merge(stripped, parts):
    '''using the parts, merge back into a string and return, replcing the indexes with the parts'''
    try:
        print(stripped,parts)
        stripped = stripped.split()
        # adjective_one = input('Enter in an Adjective: ')   
        # adjective_two = input('Enter in an Adjective: ')   
        # noun = input('Enter in an Noun: ')
        adjective__one_index = stripped.index('{}')
        adjective__two_index = stripped.index('{}', stripped.index('{}')+1)
        noun_index = stripped.index('{}.')
        stripped[adjective__one_index] = parts[0]
        stripped[adjective__two_index] = parts[1]
        stripped[noun_index] = parts[2] + '.'
        list_to_string = ' '.join(stripped)
        print(parts[2])
        print(list_to_string)
        return(list_to_string)
        
        

    except AssertionError as e:
        print(e)
   
if __name__ == '__main__':
    results = read_template(story_file)
    stripped, parts = parse_template(results)
    merge(stripped, ("dark", "stormy", "night"))

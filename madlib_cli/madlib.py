import re
story_file = '../assets/template.txt'

intro = """****Welcome to the Madlib Game!****

**** Game Instructions****

        step 1. for each input you will get an instruction to enter an adjective or noun.
        step 2. follow the input instructions and you will recieve a madlib story using
        you previously entered nouns and adjectives.
        step 3. !!!HAVE A LAUGH!!! 
"""
# create read_temple function
def read_template(file):
    try:
        with open(file) as t:
            print(intro)
            template = t.read()
            return template
    except FileNotFoundError as e:
        print('CHECK PATHING OR LOCATION OF FILE!', e)

# create parse template function
def parse_template(results):
    try:
        pattern = r"{(.*?)}"
        parts = tuple(re.findall(pattern, results))
        stripped = re.sub(pattern, "{}", results)
        return stripped, parts

    except AssertionError as e:  
        print(e)
# create merge function
def merge(file):
    pass
    # try:
    #     list = parse_template(file)
    #     adj_One = input('Enter Adjective : ')
    #     adj_Two = input('Enter Second Adjective : ')
    #     noun = input('Enter a noun : ')
    #     print(adj_One,adj_Two,noun)
    #     print(list)
    #     # merge(story_file)

    # except AssertionError as e:
    #     print(e)
if __name__ == '__main__':
    results = read_template(story_file)
    print(parse_template(results))
# merge(story_file)
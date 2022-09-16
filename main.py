import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


# Cypher key words:
# MATCH - established node pattern
# WHERE - filters results of MATCH clause
# DISCLAIMER -> MATCH (c:City {name: "London"}) == MATCH (c:City) WHERE c.name = "London" (JSON-esq vs WHERE)
# RETURN - returns specific results | Used with AS clause gives it an alias - RETURN c.population_size AS population
# AND - used the same was as && in other languages
# Boolean Operators - function relatively the same as other languages, IS represents '=='

# Wont be adding, removing, editing nodes, nor constraints

# Include other useful information from https://memgraph.com/blog/cypher-cheat-sheet

# WORKING WITH RELATIONSHIP TYPES:
# (city:City)-[:IN]-(country:Country) - relationship between city and country nodes with an "in" comparison

# davinci:ft-personal:eng-2-cyph-proto0-2022-07-28-14-51-02

# Used to handle custom query
def handle_custom_query(eng_query) -> str:
    response = openai.Completion.create(
        model='davinci:ft-personal:eng-2-cyph-proto0-2022-07-28-14-51-02',
        prompt=eng_query,
        # temperature=0.3,
        # max_tokens=300,
        # top_p=1,
        # frequency_penalty=0.3,
        # presence_penalty=0,
        # stop=["#", ";"],
    )
    return response.get('choices')


# Used to perform a query if one decides to connect to a database
def perform_query(cyph_query):
    print(cyph_query)


def handle_pre_written():
    print('The following queries are offered as pre-written:')
    print('1: Return the total number of nodes')
    print('2: Return the total number of relationships')
    pre_response = input()
    while True:
        if pre_response == '1':
            print('MATCH (n)\nRETURN count(n);')
            break
        elif pre_response == '2':
            print('MATCH ()-->()\nRETURN count(*);')
            break
        else:
            print('Not a valid option, please pick a valid answer (1, 2, 3, or 4)')
            pre_response = input()


if __name__ == '__main__':
    print('Welcome to eng2cypher translator specified for the CFDIKG')
    print('The following options are available. Type the number to use')
    print('1: Custom Query')
    print('2: Parameterized Query')
    print('3: Pre-written Query')
    print('4: Algorithms')
    print('5: Exit')
    queryType = input()
    while True:
        if queryType == '1':
            q = input('Input Search: ')
            ret = handle_custom_query(q)
            print(ret)
            break
        elif queryType == '2':
            print(2)
            break
        elif queryType == '3':
            handle_pre_written()
            break
        elif queryType == '4':
            print(4)
            break
        elif queryType == '5':
            break
        else:
            print('Not a valid option, please pick a valid answer (1, 2, 3, or 4)')
            queryType = input()

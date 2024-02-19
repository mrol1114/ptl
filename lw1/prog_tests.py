from prog import prog
from temp_token_provider import set_tokens

tests = [
    ('''
START { } FINISH
''', True),

    ('''
START } FINISH
''', False),

    ('''
START { FINISH
''', False),

    ('''
START { }
''', False),

    ('''
{ } FINISH
''', False),
]

for test_id, test_data in enumerate(tests):
    test, expected_result = test_data
    tokens = test.split()
    set_tokens(tokens)

    try:
       res = prog()
    except:
        res = False

    if res == expected_result:
        print(f'{test_id + 1}:\tOK')
    else:
        print(f'{test_id + 1}:\tFAIL')
        print(f'\tExpected: {expected_result}')
        print(f'\tGot: {res}')

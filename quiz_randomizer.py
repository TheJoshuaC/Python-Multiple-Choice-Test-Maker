import random

questions_correct_answers = { 'q1': {
        'question': 'What is Python primarily designed for?',
        'answer': ['Readability and ease of use']
    },
    'q2': {
        'question': 'Which of the following is a popular Python web framework?',
        'answer': ['Flask']
    },
    'q3': {
        'question': 'What keyword is used to define a function in Python?',
        'answer': ['def']
    },
    'q4': {
        'question': 'How do you create a comment in Python?',
        'answer': ['#']
    },
    'q5': {
        'question': 'What is the correct syntax to import a module in Python?',
        'answer': ['import module']
    },
    'q6': {
        'question': 'Which of the following data types is immutable in Python?',
        'answer': ['Tuple']
    },
    'q7': {
        'question': 'What is the output of the following code: print("Hello " * 3)?',
        'answer': ['HelloHelloHello']
    },
    'q8': {
        'question': 'How do you create a dictionary in Python?',
        'answer': ['{key:value}']
    },
    'q9': {
        'question': 'Which of the following is not a valid variable name in Python?',
        'answer': ['my-var']
    },
    'q10': {
        'question': 'What is the output of the following code: print(type(1.0))?',
        'answer': ['float']
    },
    'q11': {
        'question': 'What does the \'strip\' method do in Python?',
        'answer': ['Removes whitespace at the beginning and end of a string']
    },
    'q12': {
        'question': 'What is the result of 5 // 2 in Python?',
        'answer': ['3']
    },
    'q13': {
        'question': 'Which of the following is a correct way to create a set in Python?',
        'answer': ['set = set()']
    },
    'q14': {
        'question': 'What is the correct syntax to create a class in Python?',
        'answer': ['class MyClass:']
    },
    'q15': {
        'question': 'Which of the following is a Python built-in function?',
        'answer': ['All of the above']
    },
    'q16': {
        'question': 'What is the output of the following code: print("12345"[::-1])?',
        'answer': ['54321']
    },
    'q17': {
        'question': 'What is the output of the following code: print(10 % 3)?',
        'answer': ['1']
    },
    'q18': {
        'question': 'What is the output of the following code: print("12" + "34")?',
        'answer': '1234'
    },
    'q19': {
        'question': 'What is the correct syntax to create a list in Python?',
        'answer': ['list = []']
    },
    'q20': {
        'question': 'Which of the following is not a valid Python operator?',
        'answer': [" =' "]
    },
    'q21': {
        'question': 'Which of the following is the correct way to create a lambda function in Python?',
        'answer': ['lambda x: x + 1']
    }
}

questions_all_answers = {
    'q1': {
        'question': 'What is Python primarily designed for?',
        'answers': ['Readability and ease of use', 'Web development', 'Game development', 'Mobile app development']
    },
    'q2': {
        'question': 'Which of the following is a popular Python web framework?',
        'answers': ['Flask', 'Angular', 'Ruby on Rails', 'Laravel']
    },
    'q3': {
        'question': 'What keyword is used to define a function in Python?',
        'answers': ['def', 'func', 'function', 'fun']
    },
    'q4': {
        'question': 'How do you create a comment in Python?',
        'answers': ['#', '//', '--', '/* */']
    },
    'q5': {
        'question': 'What is the correct syntax to import a module in Python?',
        'answers': ['import module', 'import(module)', '#import module', '@import module']
    },
    'q6': {
        'question': 'Which of the following data types is immutable in Python?',
        'answers': ['Tuple', 'List', 'Dictionary', 'Set']
    },
    'q7': {
        'question': 'What is the output of the following code: print("Hello " * 3)?',
        'answers': ['HelloHelloHello', 'Hello 3', 'HelloHelloHelloHello', 'Error']
    },
    'q8': {
        'question': 'How do you create a dictionary in Python?',
        'answers': ['{key:value}', '[key, value]', '(key:value)', '{key,value}']
    },
    'q9': {
        'question': 'Which of the following is not a valid variable name in Python?',
        'answers': ['_my_var', 'my_var', 'myVar', 'my-var']
    },
    'q10': {
        'question': 'What is the output of the following code: print(type(1.0))?',
        'answers': ['float', 'int', 'str', 'bool']
    },
    'q11': {
        'question': 'What does the \'strip\' method do in Python?',
        'answers': ['Removes whitespace at the beginning and end of a string', 'Removes all whitespace from a string','Splits a string into a list', 'Joins a list of strings']
    },
    'q12': {
        'question': 'What is the result of 5 // 2 in Python?',
        'answers': ['3', '2', '4', '5']
    },
    'q13': {
        'question': 'Which of the following is a correct way to create a set in Python?',
        'answers': ['set = set()', 'set = {}', 'set = ()', 'set = []']
    },
    'q14': {
        'question': 'What is the correct syntax to create a class in Python?',
        'answers': ['class MyClass:', 'class: MyClass', 'new class MyClass:', 'class MyClass()']
    },
    'q15': {
        'question': 'Which of the following is a Python built-in function?',
        'answers': ['All answers are correct', 'open()', 'range()', 'int()']
    },
    'q16': {
        'question': 'What is the output of the following code: print("12345"[::-1])?',
        'answers': ['54321', '51234', '12345', 'Error']
    },
    'q17': {
        'question': 'What is the output of the following code: print(10 % 3)?',
        'answers': ['1', '3', '333', 'Error']
    },
    'q18': {
        'question': 'What is the output of the following code: print("12" + "34")?',
        'answers': ['1234', '46', 'Error', '56']
    },
    'q19': {
        'question': 'What is the correct syntax to create a list in Python?',
        'answers': ['list = []', 'list = ()', 'list = list()', 'list = {}']
    },
    'q20': {
        'question': 'Which of the following is not a valid Python operator?',
        'answers': [" =' ", '==', '!=', 'is']
    },
    'q21': {
        'question': 'Which of the following is the correct way to create a lambda function in Python?',
        'answers': ['lambda x: x + 1', 'lambda(x): x + 1', 'lambda: x(x + 1)', 'lambda x: return x + 1']
    }
}

def create_quiz(num_quizzes=35, num_questions=21):
    questions = list(questions_correct_answers.keys())

    for quiz_num in range(1, num_quizzes + 1):
        # Shuffle the questions
        random.shuffle(questions)

        # Create the quiz and answer key files
        with open(f"Python_Multiple_Choice_Quiz({quiz_num}).txt", "w") as quiz_file, open(f"PMCQ_Answers({quiz_num}).txt", "w") as answer_file:
            # Write quiz header
            quiz_file.write(f"Quiz {quiz_num}\n\n")

            # Select and write questions and answers
            for question_num, question_key in enumerate(questions[:num_questions], start=1):
                question = questions_correct_answers[question_key]['question']
                correct_answer = questions_correct_answers[question_key]['answer'][0] if isinstance(questions_correct_answers[question_key]['answer'], list) else questions_correct_answers[question_key]['answer']
                all_answers = questions_all_answers[question_key]['answers']
                wrong_answers = [ans for ans in all_answers if ans != correct_answer]

                # Randomly order the choices
                unique_answers = [correct_answer] + [ans for ans in wrong_answers if ans not in [correct_answer]]
                choices = random.sample(unique_answers, len(unique_answers))

                if question_key in ['q11', 'q13']:
                    choices = random.sample(unique_answers, len(unique_answers))
                else:
                    choices = random.sample(unique_answers, min(4, len(unique_answers)))

                quiz_file.write(f"{question_num}. {question}\n")
                for choice_num, choice in enumerate(choices, start=1):
                    quiz_file.write(f"  {chr(64 + choice_num)}. {choice}\n")
                quiz_file.write("\n")

                answer_file.write(f"{question_num}. {chr(64 + choices.index(correct_answer) + 1)}\n")

# Call the function
create_quiz()



'------------------------------------------------------------'
'------------------------------------------------------------'
'------------------------------------------------------------'

# Different Formatting for the questionaire below

'------------------------------------------------------------'

# q1_answers = ['Readability and ease of use', 'Web development', 'Game development', 'Mobile app development']
# q2_answers = ['Flask', 'Angular', 'Ruby on Rails', 'Laravel']
# q3_answers = ['def', 'func', 'function', 'fun']
# q4_answers = ['#', '//', '--', '/* */']
# q5_answers = ['import module', 'import(module)', '#import module', '@import module']
# q6_answers = ['Tuple', 'List', 'Dictionary', 'Set']
# q7_answers = ['HelloHelloHello', 'Hello 3', 'HelloHelloHelloHello', 'Error']
# q8_answers = ['{key:value}', '[key, value]', '(key:value)', '{key,value}']
# q9_answers = ['_my_var', 'my_var', 'myVar', 'my-var']
# q10_answers = ['float', 'int', 'str', 'bool']
# q11_answers = ['Removes whitespace at the beginning and end of a string', 'Removes whitespace at the beginning of a string', 'Removes whitespace at the end of a string', 'Removes whitespace at the beginning and end of a string']
# q12_answers = ['3', '2', '4', '5']
# q13_answers = ['set = set()', 'set = {}', 'set = ()', 'set = []']
# q14_answers = ['class MyClass:', 'class MyClass', 'class MyClass:', 'class MyClass {}']
# q15_answers = ['All of the above', 'open()', 'range()', 'int()']
# q16_answers = ['54321', '51234', '12345', 'Error']
# q17_answers = ['1', '3', '333', 'Error']
# q18_answers = ['1234', '46', 'Error', '56']
# q19_answers = ['list = []', 'list = ()', 'list = list()', 'list = {}']
# q20_answers = [" =' ", '==', '!=', 'is']
# q21_answers = ['lambda x: x + 1', 'lambda(x): x + 1', 'lambda: x(x + 1)', 'lambda x: return x + 1']


# q1_correct_answer = 'Readability and ease of use'
# q2_correct_answer = 'Flask'
# q3_correct_answer = 'def'
# q4_correct_answer = '#'
# q5_correct_answer = 'import module'
# q6_correct_answer = 'Tuple'
# q7_correct_answer = 'HelloHelloHello'
# q8_correct_answer = '{key:value}'
# q9_correct_answer = '_my_var'
# q10_correct_answer = 'float'
# q11_correct_answer = 'Removes whitespace at the beginning and end of a string'
# q12_correct_answer = '3'
# q13_correct_answer = 'set = set()'
# q14_correct_answer = 'class MyClass:'
# q15_correct_answer = 'All of the above'
# q16_correct_answer = '54321'
# q17_correct_answer = '1'
# q18_correct_answer = '1234'
# q19_correct_answer = 'list = []'
# q20_correct_answer = " =' "
# q21_correct_answer = 'lambda x: x + 1'

# q1 = 'What is Python primarily designed for?'
# q2 = 'Which of the following is a popular Python web framework?'
# q3 = 'What keyword is used to define a function in Python?'
# q4 = 'How do you create a comment in Python?'
# q5 = 'What is the correct syntax to import a module in Python?'
# q6 = 'Which of the following data types is immutable in Python?'
# q7 = 'What is the output of the following code: print("Hello " * 3)?'
# q8 = 'How do you create a dictionary in Python?'
# q9 = 'Which of the following is not a valid variable name in Python?'
# q10 = 'What is the output of the following code: print(type(1.0))?'
# q11 = 'What does the \'strip\' method do in Python?'
# q12 = 'What is the result of 5 // 2 in Python?'
# q13 = 'Which of the following is a correct way to create a set in Python?'
# q14 = 'What is the correct syntax to create a class in Python?'
# q15 = 'Which of the following is a Python built-in function?'
# q16 = 'What is the output of the following code: print("12345"[::-1])?'
# q17 = 'What is the output of the following code: print(10 % 3)?'
# q18 = 'What is the output of the following code: print("12" + "34")?'
# q19 = 'What is the correct syntax to create a list in Python?'
# q20 = 'Which of the following is not a valid Python operator?'
# q21 = 'Which of the following is the correct way to create a lambda function in Python?'

# q1_wrong_answers = 'Web development', 'Game development', 'Mobile app development'
# q2_wrong_answers = 'Angular', 'Ruby on Rails', 'Laravel'
# q3_wrong_answers = 'func', 'function', 'fun'
# q4_wrong_answers = '//', '--', '/* */'
# q5_wrong_answers = 'import(module)', '#import module', '@import module'
# q6_wrong_answers = 'List', 'Dictionary', 'Set'
# q7_wrong_answers = 'Hello 3', 'HelloHelloHelloHello', 'Error'
# q8_wrong_answers = '[key, value]', '(key:value)', '{key,value}'
# q9_wrong_answers = 'my_var', 'myVar', 'my-var'
# q10_wrong_answers = 'int', 'str', 'bool'
# q11_wrong_answers = 'Removes whitespace at the beginning of a string', 'Removes whitespace at the end of a string', 'Removes whitespace at the beginning and end of a string'
# q12_wrong_answers = '2', '4', '5'
# q13_wrong_answers = 'set = {}', 'set = ()', 'set = []'
# q14_wrong_answers = 'class MyClass', 'class MyClass:', 'class MyClass {}'
# q15_wrong_answers = 'open()', 'range()', 'int()'
# q16_wrong_answers = '51234', '12345', 'Error'
# q17_wrong_answers = '3', '333', 'Error'
# q18_wrong_answers = '46', 'Error', '56'
# q19_wrong_answers = 'list = ()', 'list = list()', 'list = {}'
# q20_wrong_answers = '==', '!=', 'is'
# q21_wrong_answers = 'lambda(x): x + 1', 'lambda: x(x + 1)', 'lambda x: return x + 1'

# print(q1_correct_answer, q1_wrong_answers)


# """
# What is Python primarily designed for?
# A. Web development
# B. Game development
# C. Readability and ease of use
# D. Mobile app development

# Which of the following is a popular Python web framework?
# A. Flask
# B. Angular
# C. Ruby on Rails
# D. Laravel

# What keyword is used to define a function in Python?
# A. func
# B. function
# C. def
# D. fun

# How do you create a comment in Python?
# A. //
# B. --
# C. /* */
# D. #

# What is the correct syntax to import a module in Python?
# A. import(module)
# B. import module
# C. #import module
# D. @import module

# Which of the following data types is immutable in Python?
# A. List
# B. Dictionary
# C. Set
# D. Tuple

# What is the output of the following code: print("Hello " * 3)?
# A. HelloHelloHello
# B. Hello 3
# C. HelloHelloHelloHello
# D. Error

# How do you create a dictionary in Python?
# A. {key: value}
# B. [key, value]
# C. {key, value}
# D. (key: value)

# Which of the following is not a valid variable name in Python?
# A. my_var
# B. my-var
# C. myVar
# D. _my_var

# What is the output of the following code: print(type(1.0))?
# A. int
# B. str
# C. float
# D. double

# What does the 'strip' method do in Python?
# A. Removes whitespace at the beginning and end of a string
# B. Removes all whitespace from a string
# C. Splits a string into a list
# D. Joins a list of strings

# What is the result of 5 // 2 in Python?
# A. 3
# B. 2
# C. 2.5
# D. Error

# Which of the following is a correct way to create a set in Python?
# A. set = ()
# B. set = []
# C. set = {}
# D. set = set()

# What is the correct syntax to create a class in Python?
# A. class MyClass:
# B. class MyClass()
# C. class: MyClass
# D. new class MyClass:

# Which of the following is a Python built-in function?
# A. open()
# B. range()
# C. int()
# D. All of the above

# What is the output of the following code: print("12345"[::-1])?
# A. 54321
# B. 12345
# C. Error
# D. 51234

# What is the output of the following code: print(10 % 3)?
# A. 1
# B. 3
# C. 333
# D. Error

# What is the output of the following code: print("12" + "34")?
# A. 46
# B. 1234
# C. Error
# D. 56

# What is the correct way to create an empty list in Python?
# A. list = ()
# B. list = []
# C. list = list()
# D. list = {}

# Which of the following is a correct way to create a lambda function in Python?
# A. lambda x: x + 1
# B. lambda(x): x + 1
# C. lambda x: return x + 1
# D. lambda: x(x + 1)
# """
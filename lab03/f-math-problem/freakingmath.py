from random import *
import evel

def generate_quiz():
    # Hint: Return [x, y, op, result]
    
    x = randint(1,10)
    y = randint(1,10)
    operation = ['+','-','*','/']
    error = [-1,0,1]
    
    op = choice(operation)
    error_rand = choice(error)
    res = evel.calc(x,y,op)

    dis_result = res + error_rand
    
    return [x, y, op, dis_result]

def check_answer(x, y, op, result, user_choice):
    true_res = evel.calc(x,y,op)
    
    if true_res == result:
        return user_choice
    else:
        return not user_choice
    
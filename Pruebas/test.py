import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streaks_lexer import lexer
from streaks_parser import parser

def test_parser(data):
    try:
        result = parser.parse(data, lexer=lexer)
        print(result)
    except Exception as e:
        print(f"Parsing error: {e}")

# Pruebas individuales

def test_var_declaration():
    data = '''
    var x = 5;
    var y = -3.14;
    '''
    print("Testing var_declaration:")
    test_parser(data)

def test_assignment():
    data = '''
    x = x + 2 * y;
    '''
    print("Testing assignment:")
    test_parser(data)

def test_if_statement():
    data = '''
    if (x > 0) {
        y = y / 2;
    } else {
        y = y * 2;
    }
    '''
    print("Testing if_statement:")
    test_parser(data)



def test_print_statement():
    data = '''
    print("Hello, World!");
    '''
    print("Testing print_statement:")
    test_parser(data)

def test_model_declaration():
    data = '''
    model m = (4.7, [-7.4, 1.2, 0.58], [5.4, -9.2], [[15.9, -4.0, 66.1], [-6.1, 3.9, 4.2]]);
    '''
    print("Testing model_declaration:")
    test_parser(data)

def test_model_operation():
    data = '''
    m.train();
    m.predict();
    '''
    print("Testing model_operation:")
    test_parser(data)

def test_function_declaration():
    data = '''
    fun foo(a, b) {
        return a + b;
    }
    '''
    print("Testing function_declaration:")
    test_parser(data)

def test_return_statement():
    data = '''
    return x;
    '''
    print("Testing return_statement:")
    test_parser(data)

def test_continue_statement():
    data = '''
    continue;
    '''
    print("Testing continue_statement:")
    test_parser(data)

def test_break_statement():
    data = '''
    break;
    '''
    print("Testing break_statement:")
    test_parser(data)

def test_for_initialization():
    data = '''
    for (var i = 0; i < 3; i = i + 1) {
        // Empty loop body
    }
    '''
    print("Testing for_initialization:")
    test_parser(data)

def test_for_condition():
    data = '''
    for (var i = 0; i < 3; i = i + 1) {
        // Empty loop body
    }
    '''
    print("Testing for_condition:")
    test_parser(data)

def test_for_update():
    data = '''
    for (var i = 0; i < 3; i = i + 1) {
        // Empty loop body
    }
    '''
    print("Testing for_update:")
    test_parser(data)

if __name__ == "__main__":
    test_var_declaration()
    test_assignment()
    test_if_statement()
    test_print_statement()
    test_model_declaration()
    test_model_operation()
    test_function_declaration()
    test_return_statement()
    test_continue_statement()
    test_break_statement()
    test_for_initialization()
    test_for_condition()
    test_for_update()

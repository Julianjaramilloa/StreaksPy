# pruebas/test_streaks_lexer.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streaks_lexer import lexer

def test_lexer():
    data = '''
    modelo m = new modelo(4.7, [-7.4, 1.2, 0.58], [5.4, -9.2], [[15.9, -4.0, 66.1], [-6.1, 3.9, 4.2]]);
    print(m.total_datos());
    int x = 5;
    float y = -3.14;
    x = x + 2 * y;
    if (x > 0) {
        y = y / 2;
    }
    while (x < 10) {
        x = x + 1;
    }
    '''

    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

if __name__ == "__main__":
    test_lexer()

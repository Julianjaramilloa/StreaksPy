# pruebas/test_streaks_parser.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streaks_lexer import lexer
from streaks_parser import parser

def test_parser():
    data = '''
    model m = (4.7, [-7.4, 1.2, 0.58], [5.4, -9.2], [[15.9, -4.0, 66.1], [-6.1, 3.9, 4.2]]);
    print(m.total_datos());

    var x = 5;
    var y = -3.14;

    x = x + 2 * y;

    if (x > 0) {
        y = y / 2;
        var i = 0;
        while (i < 3) {
            print("Inside while loop");
            var j = 0;
            for (j = 0; j < 3; j = j + 1) {
                print("Inside nested for loop, j = " + j);
            }
            i = i + 1;
        }
    } else {
        print("x is not greater than 0");
    }

    while (x < 10) {
        x = x + 1;
        print("x incremented to " + x);
    }
    '''

    try:
        result = parser.parse(data, lexer=lexer)
        print(result)
    except Exception as e:
        print(f"Parsing error: {e}")

if __name__ == "__main__":
    test_parser()

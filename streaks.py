import sys
from streaks_lexer import lexer
from streaks_parser import parser

def process_input(input_text):
    # Pasar el texto de entrada al lexer y parser
    lexer.input(input_text)
    result = parser.parse(input_text, lexer=lexer)
    return result

def execute_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            process_input(content)
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no se encontró.")
    except Exception as e:
        print(f"Error al ejecutar el archivo '{filename}': {e}")

def main():
    print("Bienvenido al Shell Interactivo para tu Lenguaje de Programación")
    print("Escribe 'salir' para terminar la sesión.")
    print("Escribe 'run <nombre_archivo>' para ejecutar un archivo.")
    
    while True:
        try:
            # Leer entrada del usuario
            input_text = input('>>> ')
            if input_text.lower() == 'salir':
                print("Cerrando el shell interactivo.")
                break
            elif input_text.startswith('run '):
                filename = input_text.split(' ', 1)[1]
                execute_file(filename)
            else:
                # Procesar la entrada del usuario
                result = process_input(input_text)
                if result is not None and isinstance(result, str):
                    print(result)
        
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()

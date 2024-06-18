import sys
from streaks_lexer import lexer
from streaks_parser import parser
from twoWayModel import TwoWayModel

def main():
    # Definir los datos para el modelo de prueba
    alpha = 1.0
    tau = [2.0, 3.0]
    beta = [4.0, 5.0, 6.0]
    delta = [
        [[1, 2], [3, 4], [5, 6]],
        [[7, 8], [9, 10], [11, 12]]
    ]
    
    # Crear una instancia del modelo
    model = TwoWayModel(alpha, tau, beta, delta)
    
    # Pruebas de métodos del modelo
    print("Total de datos:", model.total_datos())
    print("Total de datos en el bloque 0:", model.total_datos_bloque(0))
    print("Total de datos en el tratamiento 1:", model.total_datos_tratamiento(1))
    print("Datos del modelo:", model.datos_modelo())
    print("Datos del bloque 0:", model.datos_bloque(0))
    print("Datos del tratamiento 1:", model.datos_tratamiento(1))
    
    # Pruebas de rachas
    R = [
        [[1, 1], [2, 2], [3, 3]],
        [[4, 4], [5, 5], [6, 6]]
    ]
    print("Total de rachas en R:", model.total_runs(R))
    print("Promedio de rachas por celda en R:", model.average_runs_per_cell(R))
    print("Total de rachas por bloque en R:", model.total_runs_block(R))
    print("Total de rachas por tratamiento en R:", model.total_runs_treatment(R))
    print("Promedio de rachas por bloque en R:", model.average_runs_block(R))
    print("Promedio de rachas por tratamiento en R:", model.average_runs_treatment(R))
    print("Total de rachas en todo el modelo R:", model.total_runs_model(R))
    print("Promedio de rachas en todo el modelo R:", model.average_runs_model(R))
    
    # Pruebas de la función contadora y número de rachas
    cadena = "aaaabbbaaa"
    print("Función contadora para la cadena:", model.funcion_contadora(cadena))
    print("Número de rachas en la cadena:", model.numero_de_rachas(cadena))
    
    # Pruebas de suma y promedio de rachas en celdas específicas
    print("Suma de rachas en la celda (0, 1):", model.suma_de_rachas_celda(0, 1))
    print("Promedio de rachas en la celda (0, 1):", model.promedio_de_rachas_celda(0, 1))

if __name__ == '__main__':
    main()

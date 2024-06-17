# test_twowaymodel.py

from twoWayModel import TwoWayModel

def main():
    # Definir los parámetros del modelo
    alpha = 4.7
    tau = [-7.4, 1.2, 0.58]  # Efectos de los tratamientos
    beta = [5.4, -9.2]  # Efectos de los bloques
    delta = [
        [[15.9, -4.0, 66.1], [-6.1, 3.9], [4.2, -1.3, 12.4, 5.8]],
        [[23.8, 4.5, 3.6], [-0.5, 2.2], [-5.6]]
    ]

    # Crear el modelo
    model = TwoWayModel(alpha, tau, beta, delta)

    # Imprimir datos del modelo
    print("Total de datos del modelo:", model.total_datos())
    print("Total de datos del bloque 0:", model.total_datos_bloque(0))
    print("Total de datos del tratamiento 1:", model.total_datos_tratamiento(1))
    print("Datos del modelo:", model.datos_modelo())
    print("Datos del bloque 1:", model.datos_bloque(1))
    print("Datos del tratamiento 2:", model.datos_tratamiento(2))

    # Definir matriz R de ejemplo para las rachas
    R = [
        [[2, 1, 3], [1, 1], [1, 1, 2, 1]],
        [[3, 2, 1], [1, 1], [1]]
    ]

    # Imprimir número total de rachas
    print("Número total de rachas en R:", model.total_runs(R))
    print("Promedio de rachas por celda en R:", model.average_runs_per_cell(R))
    print("Número total de rachas por bloque en R:", model.total_runs_block(R))
    print("Número total de rachas por tratamiento en R:", model.total_runs_treatment(R))
    print("Promedio de rachas por bloque en R:", model.average_runs_block(R))
    print("Promedio de rachas por tratamiento en R:", model.average_runs_treatment(R))
    print("Número total de rachas del modelo en R:", model.total_runs_model(R))
    print("Promedio de rachas del modelo en R:", model.average_runs_model(R))

if __name__ == "__main__":
    main()

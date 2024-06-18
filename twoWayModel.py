class TwoWayModel:
    def __init__(self, alpha, tau, beta, delta):
        """
        Inicializa el modelo con los parámetros dados.

        :param alpha: Efecto del modelo.
        :param tau: Efectos de los tratamientos.
        :param beta: Efectos de los bloques.
        :param delta: Matriz de datos del modelo.
        """
        self.alpha = alpha
        self.tau = tau
        self.beta = beta
        self.delta = delta

    def total_datos(self):
        """
        Calcula el total de datos en el modelo.

        :return: Suma total de todos los datos en el modelo.
        """
        return sum(sum(sum(cell) for cell in row) for row in self.delta)

    def total_datos_bloque(self, i):
        """
        Calcula el total de datos en un bloque específico.

        :param i: Índice del bloque.
        :return: Suma total de los datos en el bloque i.
        """
        return sum(sum(cell) for cell in self.delta[i])

    def total_datos_tratamiento(self, j):
        """
        Calcula el total de datos en un tratamiento específico.

        :param j: Índice del tratamiento.
        :return: Suma total de los datos en el tratamiento j.
        """
        return sum(self.delta[i][j][k] for i in range(len(self.delta)) for k in range(len(self.delta[i][j])))

    def datos_modelo(self):
        """
        Retorna la matriz de datos del modelo.

        :return: Matriz de datos del modelo.
        """
        return self.delta

    def datos_bloque(self, i):
        """
        Retorna los datos de un bloque específico.

        :param i: Índice del bloque.
        :return: Datos del bloque i.
        """
        return self.delta[i]

    def datos_tratamiento(self, j):
        """
        Retorna los datos de un tratamiento específico.

        :param j: Índice del tratamiento.
        :return: Datos del tratamiento j.
        """
        return [self.delta[i][j] for i in range(len(self.delta))]

    def total_runs(self, R):
        """
        Calcula el total de rachas en la matriz R.

        :param R: Matriz de rachas.
        :return: Suma total de todas las rachas en R.
        """
        return sum(sum(sum(cell) for cell in row) for row in R)

    def average_runs_per_cell(self, R):
        """
        Calcula el promedio de rachas por celda en la matriz R.

        :param R: Matriz de rachas.
        :return: Lista de promedios de rachas por celda.
        """
        averages = []
        for row in R:
            averages.append([sum(cell)/len(cell) for cell in row])
        return averages

    def total_runs_block(self, R):
        """
        Calcula el total de rachas por bloque en la matriz R.

        :param R: Matriz de rachas.
        :return: Lista de sumas de rachas por bloque.
        """
        return [sum(sum(cell) for cell in row) for row in R]

    def total_runs_treatment(self, R):
        """
        Calcula el total de rachas por tratamiento en la matriz R.

        :param R: Matriz de rachas.
        :return: Lista de sumas de rachas por tratamiento.
        """
        return [sum(R[i][j][k] for i in range(len(R)) for k in range(len(R[i][j]))) for j in range(len(R[0]))]

    def average_runs_block(self, R):
        """
        Calcula el promedio de rachas por bloque en la matriz R.

        :param R: Matriz de rachas.
        :return: Lista de promedios de rachas por bloque.
        """
        return [sum(sum(cell) for cell in row)/len(row) for row in R]

    def average_runs_treatment(self, R):
        """
        Calcula el promedio de rachas por tratamiento en la matriz R.

        :param R: Matriz de rachas.
        :return: Lista de promedios de rachas por tratamiento.
        """
        return [sum(R[i][j][k] for i in range(len(R)) for k in range(len(R[i][j])))/len(R) for j in range(len(R[0]))]

    def total_runs_model(self, R):
        """
        Calcula el total de rachas en todo el modelo.

        :param R: Matriz de rachas.
        :return: Suma total de rachas en el modelo.
        """
        return sum(sum(sum(cell) for cell in row) for row in R)

    def average_runs_model(self, R):
        """
        Calcula el promedio de rachas en todo el modelo.

        :param R: Matriz de rachas.
        :return: Promedio de rachas en el modelo.
        """
        total_cells = sum(len(row) for row in R)
        return self.total_runs(R) / total_cells

    def funcion_contadora(self, c):
        """
        Calcula la función contadora de una cadena multicotomizada.

        :param c: Cadena multicotomizada.
        :return: Lista de valores de la función contadora.
        """
        return [0 if i == 0 or c[i] != c[i-1] else 1 for i in range(len(c))]

    def numero_de_rachas(self, c):
        """
        Calcula el número de rachas en una cadena multicotomizada.

        :param c: Cadena multicotomizada.
        :return: Número de rachas en la cadena.
        """
        contador = self.funcion_contadora(c)
        return sum(contador)

    def multicotomizacion(self, X):
        """
        Realiza la multicotomización del modelo de dos vías.

        :param X: Conjunto de valores reales.
        :return: Matriz del número de rachas en el modelo.
        """
        # Implementar el algoritmo 1-1 aquí
        pass

    def suma_de_rachas_celda(self, i, j):
        """
        Calcula la suma del número de rachas en una celda específica.

        :param i: Índice del bloque.
        :param j: Índice del tratamiento.
        :return: Suma de rachas en la celda (i, j).
        """
        return sum(self.delta[i][j])

    def promedio_de_rachas_celda(self, i, j):
        """
        Calcula el promedio del número de rachas en una celda específica.

        :param i: Índice del bloque.
        :param j: Índice del tratamiento.
        :return: Promedio de rachas en la celda (i, j).
        """
        total_rachas = self.suma_de_rachas_celda(i, j)
        num_datos = len(self.delta[i][j])
        return total_rachas / num_datos if num_datos != 0 else 0

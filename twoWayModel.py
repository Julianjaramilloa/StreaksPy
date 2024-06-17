class TwoWayModel:
    def __init__(self, alpha, tau, beta, delta):
        self.alpha = alpha
        self.tau = tau
        self.beta = beta
        self.delta = delta

    def total_datos(self):
        return sum(sum(sum(cell) for cell in row) for row in self.delta)

    def total_datos_bloque(self, i):
        return sum(sum(cell) for cell in self.delta[i])

    def total_datos_tratamiento(self, j):
        return sum(self.delta[i][j][k] for i in range(len(self.delta)) for k in range(len(self.delta[i][j])))

    def datos_modelo(self):
        return self.delta

    def datos_bloque(self, i):
        return self.delta[i]

    def datos_tratamiento(self, j):
        return [self.delta[i][j] for i in range(len(self.delta))]

    def total_runs(self, R):
        return sum(sum(sum(cell) for cell in row) for row in R)

    def average_runs_per_cell(self, R):
        averages = []
        for row in R:
            averages.append([sum(cell)/len(cell) for cell in row])
        return averages

    def total_runs_block(self, R):
        return [sum(sum(cell) for cell in row) for row in R]

    def total_runs_treatment(self, R):
        return [sum(R[i][j][k] for i in range(len(R)) for k in range(len(R[i][j]))) for j in range(len(R[0]))]

    def average_runs_block(self, R):
        return [sum(sum(cell) for cell in row)/len(row) for row in R]

    def average_runs_treatment(self, R):
        return [sum(R[i][j][k] for i in range(len(R)) for k in range(len(R[i][j])))/len(R) for j in range(len(R[0]))]

    def total_runs_model(self, R):
        return sum(sum(sum(cell) for cell in row) for row in R)

    def average_runs_model(self, R):
        total_cells = sum(len(row) for row in R)
        return self.total_runs(R) / total_cells

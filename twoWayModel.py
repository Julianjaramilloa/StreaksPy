# twoWayModel.py

class TwoWayModel:
    def __init__(self, alpha, tau, beta, delta):
        self.alpha = alpha
        self.tau = tau
        self.beta = beta
        self.delta = delta

    def total_datos(self):
        return sum(sum(row) for row in self.delta)

    def total_datos_bloque(self, i):
        return sum(self.delta[i])

    def total_datos_tratamiento(self, j):
        return sum(self.delta[i][j] for i in range(len(self.delta)))

    def datos_modelo(self):
        return self.delta

    def datos_bloque(self, i):
        return self.delta[i]

    def datos_tratamiento(self, j):
        return [self.delta[i][j] for i in range(len(self.delta))]

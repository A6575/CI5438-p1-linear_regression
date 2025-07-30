import numpy as np

# Función de coste (ECM)

def compute_cost(
		predictions: np.ndarray,	# Vector de predicciones (output estimado)
		y: np.ndarray,				# Vector de etiquetas (output real)
) -> float:
	m = y.shape[0] 
	diff = predictions - y
	# Evita overflow usando np.clip
	diff = np.clip(diff, -1e10, 1e10)
	return (1/m) * np.sum((diff) ** 2)

# Algoritmo de Descenso del Gradiente
def gradient_descent(
	X: np.ndarray,			# Matriz de características (input)
	y: np.ndarray,			# Vector de etiquetas (output real)
	theta: np.ndarray,		# Vector de parámetros (pesos)
	alpha: float,			# Tasa de aprendizaje
	num_iterations: int,	# Número de iteraciones
	bias: float = 0.1,		# Sesgo inicial
	epsilon: float = 1e-3,	# Tolerancia para convergencia
) -> tuple[np.ndarray, list[float]]:
	
	sample_size, _ = X.shape
	cost_history = []
	prev_cost = None
	for _ in range(num_iterations):
		predictions = X.dot(theta) + bias  # Añadir el sesgo a las predicciones
		
		current_cost = compute_cost(predictions, y)

		if np.isnan(current_cost) or np.isinf(current_cost):
			print("Numerical instability detected. Stopping gradient descent.")
			break

		if prev_cost is not None and abs(current_cost - prev_cost) < epsilon:
			break

		prev_cost = current_cost
		cost_history.append(current_cost)
		
		dtheta = -2 * (1/sample_size) * X.T.dot(y - predictions)
		dbias = -2 * (1/sample_size) * np.sum(y - predictions)
		
		theta = theta - alpha * dtheta
		bias = bias - alpha * dbias
	
	return theta, bias, cost_history

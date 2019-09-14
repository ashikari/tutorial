import matplotlib.pyplot as plt
import numpy as np


def main():
	
	x = np.linspace(0, 2, 100)

	plt.close('all')
	fig, ax = plt.subplots(1,1)

	ax.plot(x, x, label = "linear")
	ax.plot(x, x**2, label = "Quadratic")
	ax.plot(x, x**3, label = "Cubic")

	plt.title("Simple Plot")
	plt.legend()



	plt.show()
	


if __name__ == '__main__':
	main()
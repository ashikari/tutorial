from bokeh.plotting import figure, output_file, show
import numpy as np

if __name__ == '__main__':
	x = np.linspace(0, 2*np.pi, 100)
	y_lin = x
	y_sqrt = np.sqrt(x)
	y_log = np.log(x)
	y_sin = np.sin(x)

	output_file("plot.html")

	fig = figure(title="Simple Plots")
	fig.line(x=x, y=y_lin, color='red', legend="Linear")
	fig.line(x=x, y=y_sqrt, color='blue', legend="Square Root")
	fig.line(x=x, y=y_log, color='black', legend="Log")
	fig.line(x=x, y=y_sin, color='green', legend="Sin")

	fig.legend.location = "top_left"
	fig.legend.click_policy="hide"

	show(fig)
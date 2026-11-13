import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from .data_fetching import _extract_names

def plot_career_matches(career_matches):
	return NotImplementedError("plot_career_matches not implemented")

def _plot_datapoints(data, palette):
	"""Plot the datapoints on the graph"""
	sns.scatterplot(data,  x='Primary_Player_Age', y='Opponent_Years_Diff',
					hue='Match_Outcome_Player', size=10, palette=palette)
	sns.set_style("whitegrid")

def _set_xy_axis_marks():
	"""Set the x and y axis marks of the plot"""
	plt.tick_params(top=True, labeltop=True, bottom=False,
					labelbottom=False, length=0)
	# y-axis
	y_ticks_vals = np.arange(-20, 30, step=10)
	y_ticks_labels = ['-20', '-10', 'Same age', '+10', '+20 years']
	plt.yticks(y_ticks_vals, y_ticks_labels, c='gray')
	 
	# x-axis
	x_ticks_vals = np.arange(14, 42, step=2)
	plt.xticks(x_ticks_vals, c='gray')
	
	# Add horizontal axis line
	plt.axhline(y=0, linewidth=0.5, c='black')

def _set_labels(name):
	"""Set labels for plot"""
	# Extract first name
	full_name = _extract_names(name)
	first_name = full_name[0]

	# Add and modify labels
	plt.xlabel(f"{first_name}'s \n age:", c='gray', loc='left')
	ax.xaxis.set_label_position("top")
	plt.ylabel(None)

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from .data_fetching import _extract_names

def plot_career_matches(career_matches):
	fig, ax = plt.subplots(figsize=(12, 9))
	fig.subplots_adjust(top=0.82)

	# Extract first name 
	fullname = career_matches.attrs['fullname']
	fullname_split = _extract_names(fullname)
	first_name = fullname_split[0]
	last_name = fullname_split[1]

	# Extract player ages
	min_age = career_matches.attrs['minage']
	max_age = career_matches.attrs['maxage']

	_plot_datapoints(career_matches)
	_set_xy_axis_marks(min_age, max_age)
	_set_labels(ax, first_name)
	_set_styling(ax)

	_add_legend(ax, first_name)
	_add_text_and_title(ax, fig, first_name, last_name, min_age, max_age)

	plt.show()
	
def _plot_datapoints(data):
	"""Plot the datapoints on the graph"""
	palette = {
	    "W": "#40C4E8",  # Cyan: match won
	    "L": "#963B91"   # Purple: match lost
	}
	
	sns.scatterplot(data,  x='Primary_Player_Age', y='Opponent_Years_Diff',
					hue='Match_Outcome_Player', size=10, palette=palette)

def _set_xy_axis_marks(min_age, max_age):
	"""Set the x and y axis marks of the plot"""
	plt.tick_params(top=True, labeltop=True, bottom=False,
					labelbottom=False, length=0)
	# y-axis
	y_ticks_vals = np.arange(-20, 30, step=10)
	y_ticks_labels = ['-20', '-10', 'Same age', '+10', '+20 years']
	plt.yticks(y_ticks_vals, y_ticks_labels, c='gray')
	 
	# x-axis
	x_ticks_vals = np.arange(min_age, max_age, step=2)
	plt.xticks(x_ticks_vals, c='gray')
	
	# Add horizontal axis line
	plt.axhline(y=0, linewidth=0.5, c='black')

def _set_labels(ax, first_name):
	"""Set labels for plot"""
	plt.xlabel(f"{first_name}'s \n age:", c='gray', loc='left')
	ax.xaxis.set_label_position("top")
	plt.ylabel(None)

def _set_styling(ax):
	"""Set styling for plot"""
	sns.set_style("whitegrid")
		
	# Remove borders of the graph
	ax.spines['bottom'].set_visible(True)
	ax.spines['top'].set_visible(False)
	ax.spines['left'].set_visible(False)
	ax.spines['right'].set_visible(False)

def _add_legend(ax, first_name):
	"""Add legend to plot"""
	
	legend_handles = [
	    Line2D(
	        [0], [0],
	        marker="o",
	        color="none",
	        markerfacecolor="#40C4E8",
	        markeredgecolor="none",
	        markersize=10,
	        label=f"Match {first_name} won"
	    ),
	    Line2D(
	        [0], [0],
	        marker="o",
	        color="none",
	        markerfacecolor="#963B91",
	        markeredgecolor="none",
	        markersize=10,
	        label="Match lost"
	    )
	]
	
	ax.legend(
	    handles=legend_handles,
	    bbox_to_anchor=(0.7, 1.15),
	    ncol=2,
	    frameon=False,
	    fontsize=12,
	    handletextpad=0.05,
	    columnspacing=1.2
	)

def _add_text_and_title(ax, fig, first_name, last_name, min_age, max_age):
	"""Add text and a title to the plot"""
	plt.title(f"{first_name} {last_name}’s Professional Matches, Age {min_age} to {max_age}",
				  fontweight='bold', pad = 65)
	
	fig.text(
	    0.15, 0,
	    "Source: Tennis Abstract  •"  +
		"Note: Data includes all WTA main draw matches and qualifiers," +
		"as well as the Fed \nCup and the Olympics." +
		"• By Leo Dominguez and Sara Ziegler",
		fontsize=10,
	    color="gray"
	)
	
	ax.text(
	    -0.03, 0.8,
	    "Older\nthan\nopponent",
	    transform=ax.transAxes,
	    ha="center",
	    va="center",
	    fontsize=12,
	    color="#808080"
	)
	
	ax.text(
	    -0.03, 0.1,
	    "Younger\nthan\nopponent",
	    transform=ax.transAxes,
	    ha="center",
	    va="center",
	    fontsize=12,
	    color="#808080"
	)
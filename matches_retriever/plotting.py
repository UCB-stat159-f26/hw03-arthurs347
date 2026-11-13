import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plot_career_matches(career_matches):
	return NotImplementedError("plot_career_matches not implemented")

def _plot_datapoints(data, palette):
	"""Plot the datapoints on the graph"""
	sns.scatterplot(data,  x='Primary_Player_Age', y='Opponent_Years_Diff',
					hue='Match_Outcome_Player', size=10, palette=palette)
	sns.set_style("whitegrid")


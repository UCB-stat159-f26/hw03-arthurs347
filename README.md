# HW 3

# Authorship
This package has been created by Arthur Sanchez for the class Stat 159 at UC Berkeley on Thursday November 13th, 2026.

# Purpose

The purpose of this project is to create a package in order to retrieve, process, and plot career matches of a given player from tennisabstract.com in the form of the NYT's graphic of [serena's matches](https://www.nytimes.com/interactive/2022/08/28/sports/tennis/serena-age-opponents.html).

## Getting Started

Follow the instructions below to set up the project environment and reproduce the analysis.

### 1. Dowload the Package

Downlad the package using the follow command:

```bash
pip install git+https://github.com/UCB-stat159-f26/hw03-arthurs347.git
```
### 2. Import the functions

Import the two functions for obtaining the data and plotting with the following import statement:
```bash
from matches_retriever import get_plotting_data, plot_career_matches
```

### 3. Obtain & Plot Data

To obtain the processed dataframe and save it to a variable, enter the full name of the desired player to the function `get_plotting_data` as such:
```bash
arthur = get_plotting_data("Arthur Sanchez")
```

Then to plot the career matches use the function `plot_career_matches` with the saved dataframe from the previous code chunk as such:

```bash
plot_career_matches(arthur)
```


# Methodology 
1. First we use the data_fetching module to fetch the required data from tennisabstract.com for a given player name.

2. Then we process the data using the data_processing module in order to prepare the data for plotting.

3. Then lastly we plot the data using the plotting module in the style of the NYT graphic.


# Package Structure
```text
hw03-arthurs347/
├── .gitignore
├── pyproject.toml
├── README.md
├── ai_documentation.txt
└── matches_retriever/
		├── tests/
		│    ├── test_data_fetching.py
		│    └── test_data_processing.py
		│
		├── __init__.py
		├── data_fetching.py
		├── data_processing.py
		└── plotting.py
```

# Personal Reflections
Through working on this project, I have learned many aspects about data preparation, testing, and python packages. I learned how to scrape from a real world webpage and acquire the desired elements using beautifulsoup4. I learned how to test with pytest with mock data for live functions that should not be called on real data. This has also taught me the reliance we should have on testing and to make them extensive so as to not spend lots of time debugging later. I learned how to compartamentalize my code into many functions that work with each other and are self-describing through descriptive comments, variables, and function names. I finally learned how to create, install, and use my own python package.

# Sources
- [Tennis Abstract](https://www.tennisabstract.com/)
- [NYT Serena Williams’s Professional Matches Graphic](https://www.nytimes.com/interactive/2022/08/28/sports/tennis/serena-age-opponents.html)
- CHATGPT GPT-6 Sol
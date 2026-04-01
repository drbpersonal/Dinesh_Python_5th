# Basic Data Visualization
## Introduction to Data Visualization
Data visualization is a critical skill for interpreting and presenting data in a meaningful way. It allows for the exploration of data, uncovering hidden patterns, and communicating findings effectively. In this session, we will cover the basics of three powerful Python libraries for data visualization: Matplotlib, Seaborn, and Plotly.

## Matplotlib
Matplotlib is a widely-used Python plotting library, particularly known for its flexibility and ability to produce publication-quality figures.

### Installation
```bash
pip install matplotlib
```

### Basic Plotting with Matplotlib
Here’s how to create a simple line plot using Matplotlib:

```python
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y)
plt.title('Basic Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

### Customizing Plots
You can customize your plots by adding labels, titles, and changing colors.

```python
plt.plot(x, y, label='Prime Numbers', color='green', linestyle='--', marker='o')
plt.title('Customized Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
```

## Seaborn
Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive and informative statistical graphics.

### Installation
```bash
pip install seaborn
```

### Basic Plotting with Seaborn
Here’s how to create a simple scatter plot using Seaborn:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')

# Create a scatter plot
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title('Total Bill vs Tip')
plt.show()
```

### Customizing Plots
Seaborn makes it easy to customize plots, especially for statistical visualization.

```python
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='smoker', style='time')
plt.title('Total Bill vs Tip by Smoker Status')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
```

## Plotly
Plotly is a graphing library that makes interactive, publication-quality graphs online.

### Installation
```bash
pip install plotly
```

### Basic Plotting with Plotly
Here’s how to create a simple line plot using Plotly:

```python
import plotly.graph_objects as go

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 14]

# Create a line plot
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))
fig.update_layout(title='Basic Line Plot',
                  xaxis_title='X-axis',
                  yaxis_title='Y-axis')
fig.show()
```

### Customizing Plots
Plotly allows extensive customization, including interactive features.

```python
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers',
                                marker=dict(color='red', size=10),
                                line=dict(color='blue', width=2)))
fig.update_layout(title='Customized Line Plot',
                  xaxis_title='X-axis',
                  yaxis_title='Y-axis')
fig.show()
```

## Summary
* Matplotlib: Good for static, publication-quality plots.
* Seaborn: Simplifies statistical plotting and works well with Matplotlib.
* Plotly: Excellent for interactive and web-based visualizations.

## Practice Exercises
* Create a bar plot using Matplotlib to show the frequency of categorical data.
* Use Seaborn to create a box plot for visualizing the distribution of a dataset.
* Create an interactive scatter plot using Plotly with hover information.
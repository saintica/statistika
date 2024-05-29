import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

# Set up the figure and axes
fig, axes = plt.subplots(3, 3, figsize=(15, 15))
fig.suptitle('Random Data from Various Distributions', fontsize=16)

# List of distributions to generate data from
distributions = [
    ('Normal', np.random.normal, {'loc': 0, 'scale': 1}),
    ('Uniform', np.random.uniform, {'low': 0, 'high': 1}),
    ('Binomial', np.random.binomial, {'n': 10, 'p': 0.5}),
    ('Poisson', np.random.poisson, {'lam': 3}),
    ('Exponential', np.random.exponential, {'scale': 1}),
    ('Gamma', np.random.gamma, {'shape': 2, 'scale': 1}),
    ('Beta', np.random.beta, {'a': 2, 'b': 5}),
    ('Chi-Square', np.random.chisquare, {'df': 2}),
    ('Logistic', np.random.logistic, {'loc': 0, 'scale': 1})
]

# Generate and plot data for each distribution
for ax, (name, dist_func, params) in zip(axes.flatten(), distributions):
    # Generate data
    if name == 'Binomial':
        data = dist_func(size=1000, **params)
        sns.histplot(data, bins=np.arange(0, 11)-0.5, kde=False, ax=ax)
        ax.set_xlim(-0.5, 10.5)
    else:
        data = dist_func(size=1000, **params)
        sns.histplot(data, kde=True, ax=ax)
    
    # Set plot title
    ax.set_title(name)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

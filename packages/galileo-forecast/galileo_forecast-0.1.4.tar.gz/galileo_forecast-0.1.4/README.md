# Galileo Forecast

Galileo Forecast is a Python package that implements Thompson Sampling. It provides a flexible wrapper that can be used with various base model classes.

## Installation

You can install Galileo Forecast using pip:

```bash
pip install galileo-forecast
```

## Usage

To use Galileo Forecast, you need to create a wrapper for your base model class. Here's an example with LightGBM:

```python
from galileo_forecast import ThompsonSamplingWrapper
from lightgbm import LGBMClassifier

# make classification data, us sklearn make_classification
from sklearn.datasets import make_classification

# sample data with low hit rate
X, y = make_classification(n_samples=1000, n_features=10, n_informative=1, n_redundant=1, n_clusters_per_class=1, class_sep=0.1)

# create a wrapper for the LightGBM model  
wrapper = ThompsonSamplingWrapper(base_model_class=LGBMClassifier, num_models=10)

# fit the wrapper
wrapper.fit(X, y)

# get the predicted probabilities for the positive class
selected_model_indices, sampled_probabilities = wrapper.predict_proba(X)

# get the fancy output dataframe - contains sampled probabilities, the sampled model and the greedy model, etc.
print(wrapper.get_fancy_output_df().head())

```

## Demo

The demo folder contains Jupyter notebooks that shows how to use the package.




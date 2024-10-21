from dataclasses import dataclass, field
from typing import Any, List, Dict, Callable, Tuple
import uuid
import logging
import numpy as np
from numpy import ndarray
import pandas as pd
from galileo_forecast.data_samplers import get_sampler
from sklearn.metrics import roc_auc_score

@dataclass
class ThompsonSamplingWrapper:
    
    # dataclass fields
    base_model_class: Any
    num_models: int
    sampler: str = "with_replacement"
    init_kwargs: dict = field(default_factory=dict)
    sampling_kwargs: dict = field(default_factory=dict)
    fit_kwargs: dict = field(default_factory=dict)
    predict_kwargs: dict = field(default_factory=dict)
    
    # ------- set later ------- #

    # set of models, store as map of index to tuple of (model, model_id)
    models: Dict[int, tuple] = field(init=False)

    # scores of the models, store as map of index to tuple of (model_id, score)
    model_scores: Dict[int, tuple] = field(init=False, default_factory=dict)

    # greedy model, store as tuple (model, model_id)
    greedy_model: tuple = field(init=False)

    # sampler function
    sampler_func: Callable = field(init=False)

    # checkpoints
    is_trained: bool = field(init=False, default=False)
    
    def __post_init__(self):
        """
        Initialize an ensemble of models after the dataclass initialization.
        Check if the base_model_class has a predict_proba method.
        """
        if not hasattr(self.base_model_class, 'predict_proba'):
            raise AttributeError("The base_model_class must have a 'predict_proba' method in order to use Thompson Sampling.")
        
        # initialize models
        self.models = {i: (self.base_model_class(**self.init_kwargs), uuid.uuid4()) for i in range(self.num_models)}

        # initialize the greedy model
        self.greedy_model = (self.base_model_class(**self.init_kwargs), uuid.uuid4())

        # get sampler function
        self.sampler_func = get_sampler(self.sampler)

        # setup logger
        self.logger = logging.getLogger(__name__)

        # log the initialization of the wrapper
        self.logger.info(f"Initialized {self.num_models} models of type {self.base_model_class}")

        # test the model class
        self._test()

    def _test(self) -> bool:
        """
        Test the model class by making a copy, fitting it and then predicting on a small dataset.
        """
        # make a copy of the model
        model = self.base_model_class(**self.init_kwargs)

        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([0, 1, 0])

        # fit the model
        model.fit(X, y, **self.fit_kwargs)

        # predict on the same data
        y_pred = model.predict_proba(X, **self.predict_kwargs)

        # make sure predictions are of shape (n_samples,2)
        assert y_pred.shape == (3, 2), "Predictions are not of shape (n_samples,2)"

        return True
    
    def _get_auc(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Get the AUC score for the predicted probabilities.
        """
        return roc_auc_score(y_true, y_pred)
    
    def get_model_ids(self) -> List[int]:
        """
        Get the model IDs.
        """
        return [model_id for model_id in self.models]
    
    def get_models(self) -> Dict[int, tuple]:
        """
        Get the models.
        """
        return self.models
    
    def get_greedy_model(self) -> tuple:
        """
        Get the greedy model.
        """
        return self.greedy_model
    
    def is_trained(self) -> bool:
        """
        Get the is_trained flag.
        """
        return self.is_trained
    
    def get_num_models(self) -> int:
        """
        Get the number of models.
        """
        return self.num_models
    
    def get_sampler(self) -> Callable:
        """
        Get the sampler.
        """
        return self.sampler
    
    def fit(self, X: pd.DataFrame, y: pd.DataFrame):
        """
        Fit all models in the ensemble.

        Args:
            X: The input features.
            y: The target values.
            *args: Additional positional arguments to pass to the fit method.
            **kwargs: Additional keyword arguments to pass to the fit method.
        """

        # check if X and y are numpy.ndarray types, if so convert them to pandas.DataFrame types but show a warning
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X)
            self.logger.warning("X was converted to a pandas.DataFrame")
        if isinstance(y, np.ndarray):
            y = pd.DataFrame(y)
            self.logger.warning("y was converted to a pandas.DataFrame")

        # if still not a pandas.DataFrame or pandas.Series, raise an error
        if not isinstance(X, pd.DataFrame) or not isinstance(y, pd.DataFrame):
            raise ValueError("X and y must be pandas.DataFrame and pandas.DataFrame types")

        # fit the greedy model - note that there is no need to sample data for the greedy model
        self.greedy_model[0].fit(X, y.values.ravel(), **self.fit_kwargs)

        # fit models
        for i, (model, model_id) in enumerate(self.models.values()):

            # sample data - can be with or without replacement
            X_sampled, y_sampled = self.sampler_func(X, y, **self.sampling_kwargs)
            
            # log the training of the model
            self.logger.info(f"Training model {i+1}/{self.num_models} (ID: {model_id})")
            
            # fit the model
            model.fit(X_sampled, y_sampled.values.ravel(), **self.fit_kwargs)

            # get the auc score for the model
            y_pred = model.predict_proba(X, **self.predict_kwargs)[:, 1].ravel()
            auc_score = self._get_auc(y.values.ravel(), y_pred)

            # save the model scores
            self.model_scores[i] = (model_id, auc_score)

            # log the auc score
            self.logger.info(f"AUC score for model {i+1}/{self.num_models} (ID: {model_id}): {auc_score}")
            
            # save the model once it is trained
            self.models[i] = (model, model_id)

        self.logger.info(f"Trained {self.num_models} models")
        self.is_trained = True

    
    def predict_proba(self, X: pd.DataFrame, random_seed: int = None, raw_predictions: bool = False) -> Tuple[ndarray, ndarray]:
        """for each row in X, randomly sample a model and return the predicted probability
        
        Thompson Sampling:
            1. check if predicted probabilities have been set
                2. if not, set them
            3. each column of the porbabilities contains predictions for all instances, so horizontally stack the P=1 columns of each model's predicted probabilities
            4. generate a matrix of random 0/1 values - at most one 1 per row
            5. select the predicted probabilities for each row in X
            6. return the selected predicted probabilities

        Args:
            X: The input features.

        Returns:
            Tuple[ndarray, ndarray]: The model indices and sampled predicted probabilities.
        """

        # check if the wrapper has been trained
        if not self.is_trained:
            raise ValueError("Wrapper has not been trained yet. Call fit() first.")

         # ------ thompson sampling ------ #

        # predict the probabilities for each model
        _raw_predicted_probabilities = {}
        for i, (model, model_id) in enumerate(self.models.values()):

            # log the prediction of the model
            if logging:
                self.logger.info(f"Predicting with model {i+1}/{self.num_models} (ID: {model_id})")
            
            # predict the probabilities
            y_pred_proba = model.predict_proba(X, **self.predict_kwargs)
            
            # save the predicted probabilities; dictionary of model_id -> predicted probabilities of shape (n_samples, 1), with number of models as number of keys
            _raw_predicted_probabilities[model_id] = y_pred_proba

        # stack the predicted probabilities horizontally; shape (n_samples, n_models)
        predicted_probabilities = np.column_stack([_raw_predicted_probabilities[model_id][:, 1].ravel() for model_id in _raw_predicted_probabilities])

        # if raw_predictions is True, return the raw predicted probabilities
        if raw_predictions:
            return predicted_probabilities

        # ------ greedy sampling ------ #
        
        # log the prediction of the greedy model
        if logging:
            self.logger.info(f"Predicting with greedy model (ID: {self.greedy_model[1]})")
        
        # generate a matrix of random 0/1 values - at most one 1 per row    
        num_rows, num_cols = predicted_probabilities.shape

        # Randomly select column indices for each row - seed option for repoducibility 
        if random_seed:
            np.random.seed(random_seed)
        selected_model_indices = np.random.randint(0, num_cols, size=num_rows)

        # Select the elements based on the randomly chosen column indices
        sampled_probabilities = predicted_probabilities[np.arange(num_rows), selected_model_indices]

        # check if each row in sampled probabilities exists in the corresponding row of the original probabilities dataframe
        assert np.all(sampled_probabilities == predicted_probabilities[np.arange(num_rows), selected_model_indices]), "Each row in sampled probabilities does not exist in the corresponding row of the original probabilities dataframe"
        
        # log the sampling
        if logging:
            self.logger.info(f"Sampled probabilities for {num_rows} rows")

        # select the predicted probabilities for each row in X
        return selected_model_indices, sampled_probabilities
    
    def predict_greedy_proba(self, X: pd.DataFrame) -> np.ndarray:
        """
        Predict the probabilities of the positive class for the greedy model.
        """
        # predict the probabilities
        y_pred_proba_greedy = self.greedy_model[0].predict_proba(X, **self.predict_kwargs)[:, 1].ravel()

        return y_pred_proba_greedy
    
    def get_all_probs_df(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Get the predicted probabilities for all models in the ensemble.
        """
        # check if predicted probabilities have been set
        if not self.is_trained:
            raise ValueError("Predicted probabilities have not been set yet. Call set_predicted_probabilities(X) first, using data X that you want to sample from.")
        
        # create a dataframe with the predicted probabilities
        raw_probabilities = self.predict_proba(X, raw_predictions=True)
        probabilities_df = pd.DataFrame(raw_probabilities, columns=[f"model_{i}" for i in range(self.num_models)])

        return probabilities_df
    
    def get_greedy_probs_df(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Get the predicted probabilities for the greedy model.
        """
        # check if predicted probabilities have been set
        if not self.is_trained:
            raise ValueError("Predicted probabilities have not been set yet. Call set_predicted_probabilities(X) first, using data X that you want to sample from.")
        
        # create a dataframe with the predicted probabilities
        probabilities_df_greedy = pd.DataFrame(self.predict_greedy_proba(X), columns=[f"Greedy Model Probabilities"])

        return probabilities_df_greedy
    
    def get_thompson_sampled_probs_df(self, X: pd.DataFrame, random_seed: int = None) -> pd.DataFrame:
        """
        Get the predicted probabilities for the thompson sampled model.
        """
        # check if predicted probabilities have been set
        if not self.is_trained:
            raise ValueError("Predicted probabilities have not been set yet. Call set_predicted_probabilities(X) first, using data X that you want to sample from.")
            
        # get the thompson sampled probabilities
        selected_model_indices, sampled_probabilities = self.predict_proba(X, random_seed=random_seed)

        # create a dataframe with the thompson sampled probabilities
        thompson_sampled_probabilities_df = pd.DataFrame({'thompson_sampled_model_index': selected_model_indices, 'thompson_sampled_probability': sampled_probabilities})
        
        return thompson_sampled_probabilities_df
    
    def get_fancy_output_df(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Get the fancy output dataframe.
        """

        # get the thompson sampled probabilities
        fancy_output_df = self.get_thompson_sampled_probs_df(X)

        # add greedy model's predicted probabilities
        fancy_output_df['greedy_model_predicted_probability'] = self.predict_greedy_proba(X)

        # add row-wise mean and std of predicted probabilities using predicted_probabilities
        raw_probabilities = self.predict_proba(X, raw_predictions=True)
        fancy_output_df['mean_predicted_probability'] = raw_probabilities.mean(axis=1)
        fancy_output_df['std_predicted_probability'] = raw_probabilities.std(axis=1)

        return fancy_output_df
        

# main function to test the wrapper
def main():

    # create a wrapper from LogisticRegression
    from sklearn.linear_model import LogisticRegression
    wrapper = ThompsonSamplingWrapper(base_model_class=LogisticRegression, num_models=10)
    print("tested LogisticRegression wrapper")

    # create a wrapper from LightGBM
    from lightgbm import LGBMClassifier
    wrapper = ThompsonSamplingWrapper(
        base_model_class=LGBMClassifier,
        num_models=10,
        init_kwargs={
            'min_child_samples': 2,
            'min_data_in_leaf': 2,
            'max_depth': 3,
            'num_leaves': 10
        }
    )
    print("tested LGBMClassifier wrapper with params to prevent early stopping")

    # create a wrapper from XGBoost with args and kwargs
    from xgboost import XGBClassifier
    wrapper = ThompsonSamplingWrapper(
        base_model_class=XGBClassifier,
        num_models=5,
        init_kwargs={'max_depth': 3, 'learning_rate': 0.1, 'n_estimators': 100, 'objective': 'binary:logistic'}
    )
    print("tested XGBClassifier wrapper with kwargs")

    # Another example with RandomForestClassifier
    from sklearn.ensemble import RandomForestClassifier
    wrapper = ThompsonSamplingWrapper(
        base_model_class=RandomForestClassifier,
        num_models=8,
        init_kwargs={'n_estimators': 50, 'max_depth': 5, 'min_samples_split': 5, 'random_state': 42}
    )
    print("tested RandomForestClassifier wrapper with kwargs")
    
if __name__ == "__main__":
    main()
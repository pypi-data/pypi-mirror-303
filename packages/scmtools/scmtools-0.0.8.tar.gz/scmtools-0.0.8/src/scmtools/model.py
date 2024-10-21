from typing import Callable, Dict, List, Union, AnyStr, Tuple

import dowhy
import numpy as np
import pandas as pd
from dowhy import gcm
import networkx as nx
from sklearn import base


class GroundTruthPredictionModel(gcm.PredictionModel):
    def __init__(self, prediction_function: Callable[[np.ndarray], Union[float, np.ndarray]]) -> None:
        """Class to turn a function into a gcm.PredictionModel.

        Args:
            prediction_function (Callable[[np.ndarray], Union[float, np.ndarray]]): function that expects an np.ndarray X
                corresponding to data with columns in alphabetical order and returns a float or a one-dimensional np.array of
                length X.shape[0]
        """
        super().__init__()
        self.prediction_function = prediction_function
    def fit(self, X, Y):
        pass
    def predict(self, X):
        return self.prediction_function(X)
    def clone(self):
        return GroundTruthPredictionModel(prediction_function=self.prediction_function)


class BlackBoxMechanism(gcm.PredictionModel):
    def __init__(
        self,
        fit_black_box_model: base.BaseEstimator,
        black_box_feature_names: List[AnyStr]
    ) -> None:
        """Custom mechanism used to replace a node in a dowhy.gcm causal model with a black box predictor.

        Args:
            fit_black_box_model (base.BaseEstimator): an already fit sklearn estimator that predicts the outcome variable
            black_box_feature_names (List[AnyStr]): the names of all features expected as input to fit_black_box_model in the order expected by fit_black_box_model

        Raises:
            ValueError: Black box model must be fit on data with named features in order to maintain compatibility with dowhy.gcm
        """
        super().__init__()
        self.black_box_model = fit_black_box_model

        # store features in expected as well as alphabetical order to translate between black box model and dowhy.gcm functions
        if black_box_feature_names is None or len(black_box_feature_names) == 0:
            raise ValueError('Black box must be fit on data with named features in order to maintain compatibiility with dowhy.gcm')
        self.black_box_feature_names = black_box_feature_names
        self.sorted_feature_names = list(sorted(self.black_box_feature_names))

    def fit(self, X, Y):
        pass

    def predict(self, X):
        # dowhy.gcm provides features as an np.ndarray in alphabetical order and without feature names
        # while sklearn estimator expects a dataframe with named features in the same order as training
        X_named = pd.DataFrame(X, columns=self.sorted_feature_names)
        X_black_box_order = X_named[self.black_box_feature_names]
        return self.black_box_model.predict(X_black_box_order)

    def clone(self):
        return BlackBoxMechanism(fit_black_box_model=self.black_box_model, black_box_feature_names=self.black_box_feature_names)


def build_ground_truth_causal_model(
        causal_graph: nx.DiGraph,
        node_function_dict: Dict[AnyStr, Tuple[Callable[[np.ndarray], Union[float, np.ndarray]], gcm.ScipyDistribution]]
    ) -> gcm.InvertibleStructuralCausalModel:
    """Build a fit gcm.InvertibleStructuralCausalModel from which to sample without fitting on any data.

    Args:
        causal_graph (nx.DiGraph): directed acyclic graph describing causal relationships
        node_function_dict (Dict[AnyStr, Tuple[Callable[[np.ndarray], Union[float, np.ndarray]], gcm.ScipyDistribution]]): a dictionary describing the structural equations
            of each node in causal_graph in the following {key: value} format: {node: (prediction_function, noise_model)}, where prediction_function is a function that
            expects an np.ndarray X corresponding to data with columns in alphabetical order and returns a float or a one-dimensional np.array of length X.shape[0], and
            noise_model is an already-parameterized gcm.ScipyDistribution object.

    Returns:
        gcm.InvertibleStructuralCausalModel: a fit and ready-to-use structural causal model
    """
    # ground truth causal model
    # takes in graph, and dict {node: (prediction_function, noise_model)} where function expects an np.ndarray with columns in alphabetical order
    # if node is a root node, then prediction_function should be None with only noise_model provided
    # noise_model must be a gcm.ScipyDistribution
    causal_model = gcm.InvertibleStructuralCausalModel(causal_graph)
    for node in causal_graph.nodes:
        noise_model = node_function_dict[node][1]
        # make sure noise model is already parameterized
        if not noise_model._fixed_parameters:
            raise ValueError(f'Noise model for node {node} is not parameterized.')

        # decide which mechanism to set for node
        node_parents = list(causal_graph.predecessors(node))
        if len(node_parents) > 0:
            # if node has parents, set structural equation as a prediction model
            prediction_function = node_function_dict[node][0]
            prediction_model = GroundTruthPredictionModel(prediction_function=prediction_function)
            current_mechanism = gcm.AdditiveNoiseModel(
                prediction_model=prediction_model,
                noise_model=noise_model
            )
        else:
            # if node has no parents, set structural equation as noise model only
            current_mechanism = noise_model

        # set mechanism
        causal_model.set_causal_mechanism(node, current_mechanism)

        # tell dowhy.gcm that the mechanism is already fit by setting its parents during fit attribute
        # NOTE: inefficient to get node's parents again but more robust to use dowhy.graph.get_ordered_predecessors
        causal_model.graph.nodes[node]['parents_during_fit'] = dowhy.graph.get_ordered_predecessors(causal_graph=causal_model.graph, node=node)

    return causal_model

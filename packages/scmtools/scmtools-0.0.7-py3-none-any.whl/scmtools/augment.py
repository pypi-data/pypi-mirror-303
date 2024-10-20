from copy import deepcopy
from itertools import cycle
from typing import Any, Callable, Dict, List, Union, AnyStr

import dowhy
import numpy as np
import pandas as pd
from dowhy import gcm
import networkx as nx
from scipy import stats
from sklearn import base

from .model import BlackBoxMechanism
from .utils import clone_causal_models_deepcopy


def augment_causal_model_with_black_box(
    fit_causal_model: gcm.InvertibleStructuralCausalModel,
    outcome_name: AnyStr,
    fit_black_box_model: base.BaseEstimator,
    black_box_feature_names: List[AnyStr]
) -> None:
    """Replace node in fit_causal_model corresponding to outcome_name with fit_black_box_model.

    Args:
        fit_causal_model (gcm.InvertibleStructuralCausalModel): an already fit causal model involving all predictors used by fit_black_box_model
        outcome_name (AnyStr): name of the outcome variable in fit_causal_model
        fit_black_box_model (base.BaseEstimator): an already fit sklearn estimator that predicts the outcome variable
        black_box_feature_names (List[AnyStr]): the names of all features expected as input to fit_black_box_model in the order expected by fit_black_box_model
    """
    # create copy of causal graph
    black_box_subgraph = nx.DiGraph(fit_causal_model.graph.copy())

    # remove all metadata from copy
    for node in black_box_subgraph.nodes:
        black_box_subgraph.nodes[node].clear()  # assumes metadata is a dict

    # exclude outcome if in current graph
    if outcome_name in black_box_subgraph.nodes:
        black_box_subgraph.remove_node(outcome_name)

    # copy all existing mechanisms over
    clone_causal_models_deepcopy(source=fit_causal_model.graph, destination=black_box_subgraph)

    # add outcome node as child of all features used by black box
    black_box_subgraph.add_node(outcome_name)
    edges_to_add = [(feature, outcome_name) for feature in black_box_feature_names]
    black_box_subgraph.add_edges_from(edges_to_add)

    # instantiate causal_model over black_box_subgraph
    augmented_causal_model = gcm.InvertibleStructuralCausalModel(black_box_subgraph)

    # create new mechanism using black box and zero noise
    black_box_mechanism = gcm.AdditiveNoiseModel(
        prediction_model=BlackBoxMechanism(fit_black_box_model=fit_black_box_model, black_box_feature_names=black_box_feature_names),
        noise_model=gcm.ScipyDistribution(stats.norm, loc=0, scale=0)
    )

    # replace outcome node mechanism with black box mechanism
    augmented_causal_model.set_causal_mechanism(outcome_name, black_box_mechanism)

    # tell dowhy.gcm that the mechanisms are already fit by setting each node's PARENTS_DURING_FIT attribute
    for node in augmented_causal_model.graph.nodes:
        augmented_causal_model.graph.nodes[node]['parents_during_fit'] = dowhy.graph.get_ordered_predecessors(
            causal_graph=augmented_causal_model.graph, node=node
        )

    return augmented_causal_model


def sample_augmented_counterfactuals(
    outcome_name: AnyStr,
    black_box_augmented_causal_model: gcm.InvertibleStructuralCausalModel,
    intervention_dict: Dict[Any, Callable[[np.ndarray], Union[float, np.ndarray]]],
    observed_data: pd.DataFrame
) -> pd.DataFrame:
    """Sample counterfactuals from a black-box-augmented causal model using abduction, action, prediction.

    Args:
        outcome_name (AnyStr): name of the outcome variable
        black_box_augmented_causal_model (gcm.InvertibleStructuralCausalModel): a black-box-augmented causal model
        intervention_dict (Dict[Any, Callable[[np.ndarray], Union[float, np.ndarray]]]): dict specifying interventions as expected by dowhy.gcm.counterfactual_samples
        observed_data (pd.DataFrame): observed data for which to sample counterfactuals

    Returns:
        pd.DataFrame: sampled counterfactual data
    """
    # reconstruct noise terms from observed data
    noise_data = gcm._noise.compute_noise_from_data(causal_model=black_box_augmented_causal_model, observed_data=observed_data)

    # set noise on outcome variable to zero -- disallow randomness on black box model node
    noise_data[outcome_name] = 0

    # sample counterfactuals with no noise on black box model
    return gcm.counterfactual_samples(causal_model=black_box_augmented_causal_model, interventions=intervention_dict, noise_data=noise_data)

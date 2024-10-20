from typing import Dict, AnyStr

import numpy as np
import pandas as pd
from dowhy import gcm


def sample_noninformative_backtracking_counterfactuals(
    causal_model: gcm.InvertibleStructuralCausalModel,
    backtracking_conditional_dict: Dict[AnyStr, bool],
    observed_data: pd.DataFrame,
    num_backtracking_samples: int
):
    """Sample backtracking counterfactuals from a regular (not black-box augmented) causal model according to a
    'non-informative' backtracking conditional that for a given exogenous variable either uses
        (1) a point mass on the observed (factual) value or
        (2) a new draw from the exogenous variable's original distribution

    NOTE: Makes num_backtracking_samples copies of observed_data in order to capture an accurate joint distribution
    across factual and counterfactual variables

    Args:
        causal_model (gcm.InvertibleStructuralCausalModel): a causal model
        backtracking_conditional_dict (Dict[AnyStr, bool]): a dictionary describing which nodes' exogenous noise values
            are allowed to change in the backtracking conditional in the following {key: value} format:
            {node: update_noise_values}, where update_noise_values is either True or False. If update_noise_values is
            False, the backtracking conditional is assumed to be a point mass on the factual value. If True, the
            original node's noise model is used to sample new values.
        observed_data (pd.DataFrame): observed data for which to sample counterfactuals
        num_backtracking_samples (int): number of backtracking counterfactual samples to draw for each observation

    Returns:
        pd.DataFrame: sampled counterfactual data, added as additional columns (names ending in '_star') to the repeated
            factual data
    """
    # reconstruct noise terms from observed data
    noise_data = gcm._noise.compute_noise_from_data(
        causal_model=causal_model,
        observed_data=observed_data
    )

    # repeat observed data (and noise data) to get multiple backtracking counterfactual samples for each observation
    repeated_data = pd.concat([observed_data] * num_backtracking_samples, axis=0)
    noise_data = pd.concat([noise_data] * num_backtracking_samples, axis=0)

    # copy noise data to make a counterfactual version
    cf_noise_data = noise_data.copy(deep=True)

    # sample each counterfactual noise variable
    num_noise_samples = len(noise_data)
    for node in causal_model.graph.nodes:
        # check if we should replace noise values with new samples using original noise model, otherwise leave as-is
        update_noise_values = backtracking_conditional_dict[node]
        if update_noise_values:
            # get original noise model for node
            node_parents = list(causal_model.graph.predecessors(node))
            if len(node_parents) > 0:
                # if node has parents, noise model and prediction model are present
                noise_model = causal_model.graph.nodes[node]['causal_mechanism'].noise_model
            else:
                # if node has no parents, only noise model is present
                noise_model = causal_model.graph.nodes[node]['causal_mechanism']

            # replace old noise values with counterfactual values
            cf_noise_values = noise_model.draw_samples(num_samples=num_noise_samples)
            # cf_noise_values = np.random.normal(loc=noise_model.parameters['loc'], scale=noise_model.parameters['scale'], size=num_noise_samples)
            cf_noise_data[node] = cf_noise_values

    # compute counterfactuals using cf_noise_data to get backtracking counterfactual values (performing no
    # interventions)
    backtracking_data = gcm.counterfactual_samples(
        causal_model=causal_model,
        noise_data=cf_noise_data,
        interventions={}
    )
    backtracking_data.columns = [f'{node}_star' for node in backtracking_data.columns]

    # append counterfactual columns to original data to capture joint distribution
    joint_data_df = pd.concat(
        [
            repeated_data.reset_index(drop=True),
            noise_data.rename(columns={node: f'U_{node}' for node in noise_data.columns}).reset_index(drop=True),
            cf_noise_data.rename(columns={node: f'U_{node}_star' for node in cf_noise_data.columns}).reset_index(drop=True),
            backtracking_data.reset_index(drop=True)
        ],
        axis=1
    )

    return joint_data_df


def sample_factual_centered_backtracking_counterfactuals(
    outcome_name: AnyStr,
    causal_model: gcm.InvertibleStructuralCausalModel,
    backtracking_conditional_dict: Dict[AnyStr, bool],
    observed_data: pd.DataFrame,
    num_backtracking_samples: int,
    backtracking_variance: float
):
    """Sample backtracking counterfactuals from a regular (not black-box augmented) causal model according to a
    backtracking conditional that for a given exogenous variable either uses
        (1) a point mass on the observed (factual) value or
        (2) a draw from a normal centered at the observed (factual) value with variance backtracking_variance

    NOTE: Makes num_backtracking_samples copies of observed_data in order to capture an accurate joint distribution
    across factual and counterfactual variables

    Args:
        outcome_name (AnyStr): name of the outcome variable
        causal_model (gcm.InvertibleStructuralCausalModel): a causal model
        backtracking_conditional_dict (Dict[AnyStr, bool]): a dictionary describing which nodes' exogenous noise values
            are allowed to change in the backtracking conditional in the following {key: value} format:
            {node: update_noise_values}, where update_noise_values is either True or False. If update_noise_values is
            False, the backtracking conditional is assumed to be a point mass on the factual value. If True, the
            original node's noise model is used to sample new values. Dictionary should include all nodes *except*
            outcome_name, which is assumed to have no noise.
        observed_data (pd.DataFrame): observed data for which to sample counterfactuals
        num_backtracking_samples (int): number of backtracking counterfactual samples to draw for each observation
        variance: 

    Returns:
        pd.DataFrame: sampled counterfactual data, added as additional columns (names ending in '_star') to the repeated
            factual data
    """
    if outcome_name in backtracking_conditional_dict.keys():
        raise ValueError(f'backtracking_conditiona_dict should not have an entry for outcome {outcome_name}')
    # reconstruct noise terms from observed data
    noise_data = gcm._noise.compute_noise_from_data(
        causal_model=causal_model,
        observed_data=observed_data
    )

    # repeat observed data (and noise data) to get multiple backtracking counterfactual samples for each observation
    repeated_data = pd.concat([observed_data] * num_backtracking_samples, axis=0)
    noise_data = pd.concat([noise_data] * num_backtracking_samples, axis=0)

    # copy noise data to make a counterfactual version
    cf_noise_data = noise_data.copy(deep=True)

    # sample each counterfactual noise variable
    num_noise_samples = len(noise_data)
    for node in causal_model.graph.nodes:
        if node == outcome_name:
            # assume outcome has no noise
            cf_noise_data[node] = 0
            continue
        # check if we should replace noise values with new samples using original noise model, otherwise leave as-is
        update_noise_values = backtracking_conditional_dict[node]
        if update_noise_values:
            # replace old noise values with counterfactual values ~ N(factual_value, backtracking_variance)
            cf_noise_values = np.random.normal(
                loc=noise_data[node].values, 
                scale=backtracking_variance, 
                size=num_noise_samples
            )
            
            # replace old noise values with counterfactual values
            cf_noise_data[node] = cf_noise_values

    # compute counterfactuals using cf_noise_data to get backtracking counterfactual values (performing no
    # interventions)
    backtracking_data = gcm.counterfactual_samples(
        causal_model=causal_model,
        noise_data=cf_noise_data,
        interventions={}
    )
    backtracking_data.columns = [f'{node}_star' for node in backtracking_data.columns]

    # append counterfactual columns to original data to capture joint distribution
    joint_data_df = pd.concat(
        [
            repeated_data.reset_index(drop=True),
            noise_data.rename(columns={node: f'U_{node}' for node in noise_data.columns}).reset_index(drop=True),
            cf_noise_data.rename(columns={node: f'U_{node}_star' for node in cf_noise_data.columns}).reset_index(drop=True),
            backtracking_data.reset_index(drop=True)
        ],
        axis=1
    )

    return joint_data_df


def sample_augmented_noninformative_backtracking_counterfactuals(
    outcome_name: AnyStr,
    black_box_augmented_causal_model: gcm.InvertibleStructuralCausalModel,
    backtracking_conditional_dict: Dict[AnyStr, bool],
    observed_data: pd.DataFrame,
    num_backtracking_samples: int
):
    """Sample backtracking counterfactuals from black_box_augmented_causal_model according to a 'non-informative'
    backtracking conditional that for a given exogenous variable either uses
        (1) a point mass on the observed (factual) value or
        (2) a new draw from the exogenous variable's original distribution

    NOTE: Makes num_backtracking_samples copies of observed_data in order to capture an accurate joint distribution
    across factual and counterfactual variables

    Args:
        outcome_name (AnyStr): name of the outcome variable
        black_box_augmented_causal_model (gcm.InvertibleStructuralCausalModel): a black-box-augmented causal model
        backtracking_conditional_dict (Dict[AnyStr, bool]): a dictionary describing which nodes' exogenous noise values
            are allowed to change in the backtracking conditional in the following {key: value} format:
            {node: update_noise_values}, where update_noise_values is either True or False. If update_noise_values is
            False, the backtracking conditional is assumed to be a point mass on the factual value. If True, the
            original node's noise model is used to sample new values. Dictionary should include all nodes *except*
            outcome_name, which is assumed to have no noise.
        observed_data (pd.DataFrame): observed data for which to sample counterfactuals
        num_backtracking_samples (int): number of backtracking counterfactual samples to draw for each observation

    Returns:
        pd.DataFrame: sampled counterfactual data, added as additional columns (names ending in '_star') to the repeated
            factual data
    """
    # reconstruct noise terms from observed data
    noise_data = gcm._noise.compute_noise_from_data(
        causal_model=black_box_augmented_causal_model,
        observed_data=observed_data
    )

    # repeat observed data (and noise data) to get multiple backtracking counterfactual samples for each observation
    repeated_data = pd.concat([observed_data] * num_backtracking_samples, axis=0)
    noise_data = pd.concat([noise_data] * num_backtracking_samples, axis=0)

    # set noise on outcome variable to zero -- disallow exogenous noise on black box model node
    noise_data[outcome_name] = 0

    # copy noise data to make a counterfactual version
    cf_noise_data = noise_data.copy(deep=True)

    # sample each counterfactual noise variable (except for outcome node, whose noise is set to zero)
    num_noise_samples = len(noise_data)
    non_outcome_nodes = list(black_box_augmented_causal_model.graph.nodes)
    non_outcome_nodes.remove(outcome_name)
    for node in non_outcome_nodes:
        # check if we should replace noise values with new samples using original noise model, otherwise leave as-is
        update_noise_values = backtracking_conditional_dict[node]
        if update_noise_values:
            # get original noise model for node
            node_parents = list(black_box_augmented_causal_model.graph.predecessors(node))
            if len(node_parents) > 0:
                # if node has parents, noise model and prediction model are present
                noise_model = black_box_augmented_causal_model.graph.nodes[node]['causal_mechanism'].noise_model
            else:
                # if node has no parents, only noise model is present
                noise_model = black_box_augmented_causal_model.graph.nodes[node]['causal_mechanism']

            # replace old noise values with counterfactual values
            cf_noise_values = noise_model.draw_samples(num_samples=num_noise_samples)
            # cf_noise_values = np.random.normal(
            #     loc=noise_model.parameters['loc'], 
            #     scale=noise_model.parameters['scale'], 
            #     size=num_noise_samples
            # )
            cf_noise_data[node] = cf_noise_values

    # compute counterfactuals using cf_noise_data to get backtracking counterfactual values (performing no
    # interventions)
    backtracking_data = gcm.counterfactual_samples(
        causal_model=black_box_augmented_causal_model,
        noise_data=cf_noise_data,
        interventions={}
    )
    backtracking_data.columns = [f'{node}_star' for node in backtracking_data.columns]

    # append counterfactual columns to original data to capture joint distribution
    joint_data_df = pd.concat(
        [
            repeated_data.reset_index(drop=True),
            noise_data.rename(columns={node: f'U_{node}' for node in noise_data.columns}).reset_index(drop=True),
            cf_noise_data.rename(columns={node: f'U_{node}_star' for node in cf_noise_data.columns}).reset_index(drop=True),
            backtracking_data.reset_index(drop=True)
        ],
        axis=1
    )

    return joint_data_df

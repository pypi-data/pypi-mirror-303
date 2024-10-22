import numpy as np
import pandas as pd
from mne import concatenate_epochs, set_log_level
from pandas.api.types import is_list_like


def subtract_evoked(epochs, average_by=None, evokeds=None):
    """Subtracts evoked activity (across or by conditions) from epochs."""

    # If no columns were requested, subtract evoked activity across conditions
    set_log_level('ERROR')
    if average_by is None:
        print('Subtracting evoked activity')
        epochs = epochs.subtract_evoked()

    # Otherwise subtract seperately for all (combinations of) conditions
    else:
        print('Subtracting evoked activity per condition in `average_by`')
        epochs = subtract_evoked_conditions(epochs, average_by, evokeds)
    set_log_level('INFO')

    return epochs


def subtract_evoked_conditions(epochs, average_by, evokeds):
    """Subtracts evoked activity (separately by conditions) from epochs."""

    # Loop over epochs (painfully slow)
    epochs_subtracted = []
    for ix, _ in enumerate(epochs):
        for query, evoked in zip(average_by.values(), evokeds):
            if len(epochs[ix][query]) > 0:
                epoch_subtracted = epochs[ix].subtract_evoked(evoked)
                epochs_subtracted.append(epoch_subtracted)

    return concatenate_epochs(epochs_subtracted)


def compute_single_trials_tfr(epochs, components, bad_ixs=None):
    """Computes single trial power for a dict of multiple components."""

    # Check that values in the dict are lists
    for key in ['name', 'tmin', 'tmax', 'roi']:
        if not is_list_like(components[key]):
            components[key] = [components[key]]

    # Loop over components
    components_df = pd.DataFrame(components)
    for _, component in components_df.iterrows():

        # Comput single trial power
        compute_component_tfr(
            epochs, component['name'], component['tmin'],
            component['tmax'], component['fmin'], component['fmax'],
            component['roi'], bad_ixs)

    return epochs.metadata


def compute_component_tfr(
        epochs, name, tmin, tmax, fmin, fmax, roi, bad_ixs=None):
    """Computes single trial power for a single component."""

    # Check that requested region of interest channels are present in the data
    for ch in roi:
        assert ch in epochs.ch_names, f'ROI channel \'{ch}\' not in the data'

    # Select region, time window, and frequencies of interest
    print(f'Computing single trial power amplitudes for \'{name}\'')
    epochs_oi = epochs.copy().pick_channels(roi).crop(tmin, tmax, fmin, fmax)

    # Compute mean power per trial
    mean_power = epochs_oi.data.mean(axis=(1, 2, 3))

    # Set power for bad epochs to NaN
    if bad_ixs is not None:
        if isinstance(bad_ixs, int):
            bad_ixs = [bad_ixs]
        mean_power[bad_ixs] = np.nan

    # Add as a new column to the original metadata
    epochs.metadata[name] = mean_power

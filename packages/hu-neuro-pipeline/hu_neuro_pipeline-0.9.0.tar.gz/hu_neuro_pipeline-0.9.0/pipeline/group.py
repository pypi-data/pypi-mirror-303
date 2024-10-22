from functools import partial
from pathlib import Path

import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from .averaging import compute_grands, compute_grands_df
from .io import (besa_extensions, convert_participant_input, eeg_extensions,
                 files_from_dir, get_participant_id, log_extensions,
                 package_versions, save_config, save_df, save_evokeds)
from .participant import participant_pipeline
from .perm import compute_perm, compute_perm_tfr


def group_pipeline(
    raw_files=None,
    log_files=None,
    output_dir=None,
    clean_dir=None,
    epochs_dir=None,
    report_dir=None,
    to_df=True,
    downsample_sfreq=None,
    veog_channels='auto',
    heog_channels='auto',
    montage='easycap-M1',
    bad_channels=None,
    ref_channels='average',
    besa_files=None,
    ica_method=None,
    ica_n_components=None,
    highpass_freq=0.1,
    lowpass_freq=40.0,
    triggers=None,
    triggers_column=None,
    epochs_tmin=-0.5,
    epochs_tmax=1.5,
    baseline=(-0.2, 0.0),
    skip_log_rows=None,
    skip_log_conditions=None,
    reject_peak_to_peak=200.0,
    perform_ride=False,
    ride_condition_column=None,
    ride_rt_column='RT',
    ride_s_twd=(0.0, 0.6),
    ride_r_twd=(-0.3, 0.3),
    ride_epochs_tmin_after_ride=None,
    ride_epochs_tmax_after_ride=None,
    ride_reject_peak_to_peak=None,
    components={'name': [], 'tmin': [], 'tmax': [], 'roi': []},
    average_by=None,
    perform_tfr=False,
    tfr_subtract_evoked=False,
    tfr_freqs=np.linspace(4.0, 40.0, num=37),
    tfr_cycles=np.linspace(2.0, 20.0, num=37),
    tfr_mode='percent',
    tfr_baseline=(-0.45, -0.05),
    tfr_components={
        'name': [], 'tmin': [], 'tmax': [], 'fmin': [], 'fmax': [], 'roi': []},
    perm_contrasts=[],
    perm_tmin=0.0,
    perm_tmax=1.0,
    perm_channels=None,
    perm_fmin=None,
    perm_fmax=None,
    n_jobs=1,
    vhdr_files=None
):
    """Process EEG data for a group of participants.

    Performs preprocessing and computes single trial mean amplitudes for ERP
    components of interest as well as by-participant averaged waveforms.
    Optionally, performs time-frequency analysis and/or cluster-based
    permutation tests.

    Parameters & returns
    --------------------
    See `Usage <../usage.html>`_ for the pipeline input arguments and outputs.
    """

    # Convert input types
    tfr_freqs = list(tfr_freqs)
    tfr_cycles = list(tfr_cycles)

    # Backup input arguments for re-use
    config = locals().copy()

    # Create partial function with arguments shared across participants
    partial_pipeline = partial(
        participant_pipeline,
        skip_log_conditions=skip_log_conditions,
        downsample_sfreq=downsample_sfreq,
        veog_channels=veog_channels,
        heog_channels=heog_channels,
        montage=montage,
        ref_channels=ref_channels,
        ica_method=ica_method,
        ica_n_components=ica_n_components,
        highpass_freq=highpass_freq,
        lowpass_freq=lowpass_freq,
        triggers=triggers,
        triggers_column=triggers_column,
        epochs_tmin=epochs_tmin,
        epochs_tmax=epochs_tmax,
        baseline=baseline,
        reject_peak_to_peak=reject_peak_to_peak,
        perform_ride=perform_ride,
        ride_condition_column=ride_condition_column,
        ride_rt_column=ride_rt_column,
        ride_s_twd=ride_s_twd,
        ride_r_twd=ride_r_twd,
        ride_epochs_tmin_after_ride=ride_epochs_tmin_after_ride,
        ride_epochs_tmax_after_ride=ride_epochs_tmax_after_ride,
        ride_reject_peak_to_peak=ride_reject_peak_to_peak,
        components=components,
        average_by=average_by,
        perform_tfr=perform_tfr,
        tfr_subtract_evoked=tfr_subtract_evoked,
        tfr_freqs=tfr_freqs,
        tfr_cycles=tfr_cycles,
        tfr_mode=tfr_mode,
        tfr_baseline=tfr_baseline,
        tfr_components=tfr_components,
        clean_dir=clean_dir,
        epochs_dir=epochs_dir,
        chanlocs_dir=output_dir,
        report_dir=report_dir,
        to_df=to_df)

    if raw_files is None:
        if vhdr_files is not None:
            from warnings import warn
            warn('⚠️ The `vhdr_files` argument has been renamed to `raw_files` ' +
                 'and will cease to work in a future version of the pipeline. ' +
                 'Please update your code accordingly.')
            raw_files = vhdr_files

    if ica_method is not None and ica_n_components is None:
        from warnings import warn
        warn('The default value of `ica_n_components` has changed from ' +
             '`0.99` (i.e., 99% explained variance) to `None` (i.e., ' +
             'extract as many components as possible). To reproduce ' +
             'previous results, explicitly set `ica_n_components=0.99`.')

    # Get input file paths if directories were provided
    if isinstance(raw_files, (str, Path)):
        raw_files = files_from_dir(raw_files, eeg_extensions)
    if isinstance(log_files, (str, Path)):
        log_files = files_from_dir(log_files, log_extensions)
    assert len(log_files) == len(raw_files), \
        f'Number of `log_files` ({len(log_files)}) does not match ' + \
        f'number of `raw_files` ({len(raw_files)})'

    # Get input BESA matrix files if necessary
    if isinstance(besa_files, (str, Path)):
        besa_files = files_from_dir(besa_files, besa_extensions)
    elif besa_files is None:
        besa_files = [None] * len(raw_files)
    assert len(besa_files) == len(raw_files), \
        f'Number of `besa_files` ({len(besa_files)}) does not match ' + \
        f'number of `raw_files` ({len(raw_files)})'

    # Extract participant IDs from filenames
    participant_ids = [get_participant_id(f) for f in raw_files]

    # Construct lists of bad_channels and skip_log_rows per participant
    bad_channels = convert_participant_input(bad_channels, participant_ids)
    skip_log_rows = convert_participant_input(skip_log_rows, participant_ids)

    # Combine participant-specific inputs
    participant_args = zip(raw_files, log_files, besa_files,
                           bad_channels, skip_log_rows)

    # Do processing in parallel
    n_jobs = int(n_jobs)
    res = Parallel(n_jobs)(
        delayed(partial_pipeline)(*args) for args in participant_args)

    # Sort outputs into seperate lists
    print(f'\n\n=== Processing group level ===')
    trials, evokeds, evokeds_dfs, configs = list(map(list, zip(*res)))[0:4]

    # Combine trials and save
    trials = pd.concat(trials, ignore_index=True)
    save_df(trials, output_dir, suffix='trials')

    # Combine evokeds_dfs and save
    evokeds_df = pd.concat(evokeds_dfs, ignore_index=True)
    save_df(evokeds_df, output_dir, suffix='ave')

    # Compute grand averaged ERPs and save
    grands = compute_grands(evokeds)
    grands_df = compute_grands_df(evokeds_df)
    save_evokeds(
        grands, grands_df, output_dir, participant_id='grand', to_df=to_df)

    # Update config with participant-specific inputs...
    config['raw_files'] = raw_files
    config['bad_channels'] = bad_channels
    config['besa_files'] = besa_files
    config['skip_log_rows'] = skip_log_rows

    # ... and outputs that might have been created along the way
    config['log_files'] = [p_config['log_file'] for p_config in configs]
    auto_keys = ['auto_bad_channels', 'auto_missing_epochs',
                 'auto_rejected_epochs', 'auto_rejected_epochs_before_ride',
                 'auto_ica_n_components', 'auto_ica_bad_components']
    for key in auto_keys:
        if any(key in p_config and p_config[key] is not None
               for p_config in configs):
            config[key] = {p_id: p_config[key] for p_id, p_config
                           in zip(participant_ids, configs)}

    # Save config
    config['package_versions'] = package_versions()
    save_config(config, output_dir)

    # Define standard returns
    returns = [trials, evokeds_df, config]

    # Cluster based permutation tests for ERPs
    if perm_contrasts != []:
        cluster_df = compute_perm(evokeds, perm_contrasts, perm_tmin,
                                  perm_tmax, perm_channels, n_jobs)
        save_df(cluster_df, output_dir, suffix='clusters')
        returns.append(cluster_df)

    # Combine time-frequency results
    if perform_tfr:

        # Sort outputs into seperate lists
        tfr_evokeds, tfr_evokeds_dfs = list(map(list, zip(*res)))[4:6]

        # Combine evokeds_df for power and save
        tfr_evokeds_df = pd.concat(tfr_evokeds_dfs, ignore_index=True)
        save_df(tfr_evokeds_df, output_dir,
                suffix='tfr_ave')
        returns.append(tfr_evokeds_df)

        # Compute grand averaged power and save
        tfr_grands = compute_grands(tfr_evokeds)
        tfr_grands_df = compute_grands_df(tfr_evokeds_df)
        save_evokeds(tfr_grands, tfr_grands_df, output_dir,
                     participant_id='tfr_grand', to_df=to_df)

        # Cluster based permutation tests for TFR
        if perm_contrasts != []:
            tfr_cluster_df = compute_perm_tfr(
                tfr_evokeds, perm_contrasts, perm_tmin, perm_tmax,
                perm_channels, perm_fmin, perm_fmax, n_jobs)
            save_df(tfr_cluster_df, output_dir, suffix='tfr_clusters')
            returns.append(tfr_cluster_df)

    return returns

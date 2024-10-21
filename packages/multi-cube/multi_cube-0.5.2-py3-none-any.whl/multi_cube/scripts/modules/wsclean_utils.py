import os
from pathlib import Path

def generate_wsclean_cmd(wsclean_container, chanbasename, numpix, pixscale, start_chan, end_chan, chans_out, ms_file, log_file, memory, weight, niter, auto_threshold, auto_mask, gain, mgain, datacolumn, rm_dir):
    """Generate the WSClean command."""
    return (
        f"singularity exec {wsclean_container} wsclean "
        f"-name {Path(chanbasename)} "
        f"-mem {memory} "
        f"-weight {weight} "
        f"-size {numpix} {numpix} "
        f"-scale {pixscale} "
        f"-channel-range {start_chan} {end_chan} "
        f"-channels-out {chans_out} "
        f"-data-column {datacolumn} "
        f"-no-dirty "
        f"-niter {niter} "
        f"-auto-threshold {auto_threshold} "
        f"-auto-mask {auto_mask} "
        f"-no-update-model-required "
        f"-gain {gain} "
        f"-mgain {mgain} "
        f"-local-rms {ms_file} "
        f"> {log_file} "
        f"&& "
        f"rm {rm_dir}/*-psf.fits  "
        f"{rm_dir}/*-model.fits "
        f"{rm_dir}/*-residual.fits "
        f"{rm_dir}/*-dirty.fits "
        f"{rm_dir}/*-MFS-*.fits -rf"
    )

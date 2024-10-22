# Copyright (C) 2024 ASTRON (Netherlands Institute for Radio Astronomy)
# SPDX-License-Identifier: Apache-2.0

from time import monotonic
from typing import Optional

import numpy as np
import pandas as pd
from sourcefinder.accessors import open as pyse_open
from sourcefinder.accessors import sourcefinder_image_from_accessor

from .log import logger
from .utils import log_time

PYSE_OUT_COLUMNS = [
    "ra",
    "dec",
    "ra_fit_err",
    "decl_fit_err",
    "peak_flux",
    "peak_flux_err",
    "int_flux",
    "int_fulx_err",
    "significance_detection_level",
    "beam_width",
    "minor_width",
    "parallactic_angle",
    "ew_sys_err",
    "ns_sys_err",
    "err_radius",
    "gaussian_fit",
    "chisq",
    "reduced_chisq",
]


@log_time()
def sources_from_fits_pyse(
    fits_path,
    ew_sys_err=10,
    ns_sys_err=10,
    margin=10,
    radius=1500,
    back_size_x=50,
    back_size_y=50,
    det=8,  # detection_threshold
    anl=3,  # analysis_threshold
    deblend_nthresh=0,  # extraction_params['deblend_nthresh'],
    use_sep=True,  # Faster but less accurate RMSE maps
    force_beam=False,  # extraction_params['force_beam']
    vectorized=True,  # Faster but no gaussian fitting (only works if force_beam is False)
):

    from sourcefinder import image

    # Faster but less accurate rmse maps
    image.SEP = use_sep
    # Faster but no gaussian fitting (only works if force_beam is False)
    image.VECTORIZED = vectorized

    start_time = monotonic()
    t0 = monotonic()
    acc = pyse_open(fits_path)
    pyse_im = sourcefinder_image_from_accessor(
        acc,
        margin=margin,
        radius=radius,
        back_size_x=back_size_x,
        back_size_y=back_size_y,
    )
    t1 = monotonic()
    print(f"Duration read: {t1-t0}")
    extraction_results = pyse_im.extract(
        det=det,  # detection_threshold
        anl=anl,  # analysis_threshold
        deblend_nthresh=deblend_nthresh,  # extraction_params['deblend_nthresh'],
        force_beam=force_beam,  # extraction_params['force_beam']
    )
    t2 = monotonic()
    print(f"Duration extraction: {t2-t1}")
    extraction_results = [
        r.serialize(ew_sys_err, ns_sys_err) for r in extraction_results
    ]
    t3 = monotonic()
    print(f"Duration serialize: {t3-t2}")
    sources = pd.DataFrame(extraction_results, columns=PYSE_OUT_COLUMNS)
    # uncertainty_ew: sqrt of quadratic sum of systematic error and error_radius
    # divided by 3600 because uncertainty in degrees and others in arcsec.
    sources["uncertainty_ew"] = (
        np.sqrt(sources["ew_sys_err"] ** 2 + sources["err_radius"] ** 2) / 3600.0
    )
    # uncertainty_ns: sqrt of quadratic sum of systematic error and error_radius
    # divided by 3600 because uncertainty in degrees and others in arcsec.
    sources["uncertainty_ns"] = (
        np.sqrt(sources["ns_sys_err"] ** 2 + sources["err_radius"] ** 2) / 3600.0
    )
    t4 = monotonic()
    print(f"Duration pandas: {t4-t3}")

    logger.info(f"Found {len(sources)} sources in image {fits_path}")

    return sources

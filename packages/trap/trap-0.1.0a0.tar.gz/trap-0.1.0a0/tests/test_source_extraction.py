import numpy
import pytest

from trap import source_extraction


@pytest.mark.parametrize(
    "path, expected_nr_sources",
    [
        ("tests/data/lofar1/GRB201006A_final_2min_srcs-t0000-image-pb.fits", 214),
        ("tests/data/lofar1/GRB201006A_final_2min_srcs-t0001-image-pb.fits", 212),
        ("tests/data/lofar1/GRB201006A_final_2min_srcs-t0002-image-pb.fits", 211),
    ],
)
def test_sources_from_fits_pyse(path, expected_nr_sources):

    sources = source_extraction.sources_from_fits_pyse(path)

    expected_columns = [
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
        "uncertainty_ew",
        "uncertainty_ns",
    ]

    assert len(sources) == expected_nr_sources

    for col in expected_columns:
        assert col in sources

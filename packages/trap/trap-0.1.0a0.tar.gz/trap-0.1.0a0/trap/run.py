from trap.source_extraction import sources_from_fits_pyse

if __name__ == "__main__":
    image_paths = [
        "/home/millenaar/software/astron/tkp/projects/trap_demo/Images/GRB201006A/GRB201006A_final_2min_srcs-t0000-image-pb.fits",
        "/home/millenaar/software/astron/tkp/projects/trap_demo/Images/GRB201006A/GRB201006A_final_2min_srcs-t0001-image-pb.fits",
    ]

    new_sources = sources_from_fits_pyse(image_paths[0])

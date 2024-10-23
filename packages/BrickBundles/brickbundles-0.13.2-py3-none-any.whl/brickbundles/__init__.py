"""
This file will be at root of directory structure with all brickbundles (with only their .brick files and directory structure)
"""
import os
import logging

def package_dir():
    return os.path.dirname(os.path.abspath(__file__))

def check_bundle_path(bundle_path_str: str):
    return os.path.exists(f"{bundle_path_str}/Math/config.brick")

def bundle_path():
    # Use BRICK_BUNDLE_PATH if set
    if "BRICK_BUNDLE_PATH" in os.environ:
        path = os.environ["BRICK_BUNDLE_PATH"]
        assert check_bundle_path(path)
        return path
    logging.info("BRICK_BUNDLE_PATH environment not set, searching for alternatives")
    # Check possible paths, in development we should set BRICK_BUNDLE_PATH to make sure we use the one we intend
    for path in [
                 "C:\\algoryx\\brick\\brickbundles",   # Windows installation
                 "/opt/Algoryx/brick/brickbundles",    # Linux/OSX installation
                 f"{package_dir()}",                      # package installed via pip, including editable install
    ]:
        if check_bundle_path(path):
            path = os.path.abspath(path)
            logging.info("BRICK_BUNDLE_PATH=%s, set environment BRICK_BUNDLE_PATH if you expected a different path", path)
            return path
    raise FileNotFoundError("Could not locate directory with brick bundles, i.e. bundle path")

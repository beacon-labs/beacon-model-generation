from pathlib import Path
import shutil


def clean_dir(dst):
    """Creates a new empty dir, removes any existing dir"""
    output = Path(dst)
    shutil.rmtree(output, ignore_errors=True)
    output.mkdir()
    return output

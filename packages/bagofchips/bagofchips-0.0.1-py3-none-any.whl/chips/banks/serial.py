"""Serialization utilties for the bank module
"""

import logging
import pathlib
from typing import Optional

from manifold.sources.cbc import Bank

LOGGER = logging.getLogger(__name__)


def load_bank(bank_file: pathlib.Path, safe: bool = True) -> Optional[Bank]:
    """Load a bank file

    Args:
        bank_file:
            pathlib.Path, Path to the bank file to load
        safe:
            bool, Whether to load the bank file in safe mode, default True. If False,
            an error will be raised if the bank file is not found or cannot be loaded.

    Returns:
        Bank: Loaded bank object
    """
    try:
        return Bank.load(bank_file)
    except Exception as e:
        if safe:
            LOGGER.error(f"Failed to load bank file: {bank_file}")
            LOGGER.error(e)
            return None
        else:
            raise ValueError(f"Failed to load bank file: {bank_file.as_posix()}") from e

"""Unit tests for the serial module in pytest
"""

import pathlib

from chips.banks.serial import load_bank
from manifold.sources.cbc import Bank

PATH_TEST_DATA = pathlib.Path(__file__).parent / "data"


class TestSerial:
    """Test load bank function
    """

    def test_load_bank(self):
        """Test the load bank function
        """
        # Load a bank file
        bank_file = PATH_TEST_DATA / "inp1.h5"
        bank = load_bank(bank_file)

        # Check the bank object
        assert bank is not None
        assert isinstance(bank, Bank)
        assert bank.ids.tolist() == [0, 1]

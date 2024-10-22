"""Bank search script, find a bank by matching template ids to a given bank file
"""

import argparse
import logging
import pathlib
import re
from typing import List

from chips.banks.fingerprint import bank_overlap, is_bank_match
from chips.banks.serial import load_bank

BANK_FILE_EXTENSION = "h5"
LOGGER = logging.getLogger(__name__)


def parse_args(args: list = None) -> argparse.Namespace:
    """Parse command line arguments

    Args:
        args (list): List of arguments to parse, default None, which will parse sys.argv

    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Bank search script, find a bank by matching template ids to a "
        "given bank file"
    )
    parser.add_argument(
        "root",
        type=str,
        help="Root directory in which to discover bank files, each will be compared "
        "to the template ids.",
        required=True,
    )
    parser.add_argument(
        "source",
        type=str,
        help="Source bank file to compare as a source of truth for any potential "
        "matches. The template ids are extracted from this file.",
        required=True,
    )
    parser.add_argument(
        "verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    return parser.parse_args(args)


def discover_banks(
    root: str, exclude_matches: List[str] = None, bank_suffix: str = BANK_FILE_EXTENSION
) -> List[pathlib.Path]:
    """Discover bank files in a given root directory

    Args:
        root:
            str, Root directory in which to discover bank files
        exclude_matches:
            list, List of string regex patterns to exclude from the search results

    Returns:
        list: List of bank files discovered
    """
    root = pathlib.Path(root)

    if not root.exists():
        raise FileNotFoundError(f"Root directory not found: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Root is not a directory: {root}")

    # Find all bank files in the root directory
    potential_bank_files = list(root.glob(f"*.{bank_suffix}"))

    # Filter out any bank files that match the exclude_matches patterns
    if exclude_matches:

        bank_files = []
        for bank_file in potential_bank_files:
            valid: bool = True

            for pattern in exclude_matches:
                # Check regex match using re
                if re.match(pattern, bank_file.name):
                    LOGGER.info(f"Excluding bank file: {bank_file.as_posix()}")
                    valid = False
                    break

            if valid:
                bank_files.append(bank_file)

    # No exclude_matches, return all potential bank files
    else:
        bank_files = potential_bank_files

    return bank_files


def main():
    """Main entry point for the script"""
    LOGGER.info("Starting bank search script")

    # Parse args
    args = parse_args()
    LOGGER.info(f"Arguments: {args}")

    # Load source bank
    source_bank = load_bank(args.source, safe=True)
    if source_bank is None:
        LOGGER.error("Failed to load source bank file, exiting")
        return

    # Discover bank files
    bank_files = discover_banks(args.root)
    LOGGER.info(f"Discovered: {len(bank_files)} bank files")

    # Create variables for tracking the best match
    max_overlap = 0
    max_overlap_bank = None

    # Check each bank file for a possible match
    for bank_file in bank_files:
        if args.verbose:
            LOGGER.info(f"Checking bank file: {bank_file.as_posix()}")
        bank = load_bank(bank_file, safe=True)
        if bank is None:
            if args.verbose:
                LOGGER.error(f"Failed to load bank file: {bank_file.as_posix()}")
            continue

        # Check if the bank matches the source bank
        match = is_bank_match(source_bank, bank)
        overlap = bank_overlap(source_bank, bank)

        if match:
            LOGGER.info(f"Match found: {bank_file.as_posix()}")
            return
        else:
            if overlap > max_overlap:
                max_overlap = overlap
                max_overlap_bank = bank_file

    if max_overlap_bank is None:
        LOGGER.info("No matches found")
    else:
        LOGGER.info(
            f"Best match found: {max_overlap_bank.as_posix()} with "
            f"{max_overlap} overlapping template ids"
        )


if __name__ == "__main__":
    main()

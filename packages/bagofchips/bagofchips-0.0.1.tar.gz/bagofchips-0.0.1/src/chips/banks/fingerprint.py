"""Matching banks by fingerprinting templates
"""

from manifold.sources.cbc import Bank


def is_bank_match(source_bank: Bank, target_bank: Bank) -> bool:
    """Compare two bank files for a match, based on template ids

    Args:
        source_bank:
            Bank, Source bank to compare
        target_bank:
            Bank, Target bank to compare

    Returns:
        bool: True if the banks match, False otherwise
    """
    # Extract template ids from the source bank
    source_template_ids = set(source_bank.ids)

    # Extract template ids from the target bank
    target_template_ids = set(target_bank.ids)

    # Check if the template ids match
    match = source_template_ids == target_template_ids

    return match


def bank_overlap(source_bank: Bank, target_bank: Bank) -> int:
    """Compare two bank files for a match, based on template ids

    Args:
        source_bank:
            Bank, Source bank to compare
        target_bank:
            Bank, Target bank to compare

    Returns:
        int: Number of overlapping template ids
    """
    # Extract template ids from the source bank
    source_template_ids = set(source_bank.ids)

    # Extract template ids from the target bank
    target_template_ids = set(target_bank.ids)

    # Check if the template ids match
    overlap = source_template_ids & target_template_ids

    return len(overlap)

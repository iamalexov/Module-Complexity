from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity:
    Space Complexity:
    Optimal time complexity:
    """
    second_set = set(second_sequence)
    seen = set()
    common_items: List[ItemType] = []

    for item in first_sequence:
        if item in second_set and item not in seen:
            seen.add(item)
            common_items.append(item)

    return common_items
from typing import Optional, List

# TODO: These needs to be moved to proto so that they can be important from there.

class FilterCondition:
    def __init__(self, match_key: Optional[str] = None, match_value: Optional[str] = None):
        """
        :param match_key: Optional key to match.
        :param match_value: Optional value to match.
        """
        self.match_key = match_key
        self.match_value = match_value

class PayloadFilter:
    def __init__(self, should_match: List[FilterCondition], must_match: List[FilterCondition]):
        """
        :param should_match: List of conditions that should match.
        :param must_match: List of conditions that must match.
        """
        self.should_match = should_match
        self.must_match = must_match

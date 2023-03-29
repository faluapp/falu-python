from datetime import datetime

from falu.range_filtering_options import RangeFilteringOptions


class QueryValues(object):
    """
    Helper for handling query parameters
    """

    def __init__(self, values=None):
        self.values = values

    def add(self, key, value=None):
        if value is None:
            return self

        if isinstance(value, bool):
            self.add(key, [value])
        elif isinstance(value, datetime):
            self.add(key, [value])
        elif isinstance(value, int):
            self.add(key, [value])
        elif isinstance(value, float):
            self.add(key, [key])
        return self

    def add(self, key, values):
        if values is not None and len(values) > 0:
            self.values.update({key, values})
        return self

    def add(self, prop, other):
        if other is None:
            return self

        if prop is None or len(prop) < 1:
            return self

        for key, value in other.values.items():
            self.add(prop + "." + key, value)

    def fromRange(self, options: RangeFilteringOptions):
        if options is not None:
            self.add("lt", options.less_than)
            self.add("lte", options.less_than_or_equal_to)
            self.add("gt", options.greater_than)
            self.add("gte", options.greater_than_or_equal_to)
        return self

from falu.query_values import QueryValues
from falu.range_filtering_options import RangeFilteringOptions


class BasicListOptions(object):
    """
    Standard options for filtering and pagination in list operations.
    """

    def __init__(self, sorting=None, count=None, created: RangeFilteringOptions = None,
                 update: RangeFilteringOptions = None):
        self.sorting = sorting
        self.count = count
        self.created = created
        self.update = update

    def populate(self, values: QueryValues):
        if values is None: return

        values.add("sorted", [self.sorting]) \
            .add("count", self.count) \
            .add("created", QueryValues().fromRange(self.created)) \
            .add("updated", QueryValues().fromRange(self.update))


class BasicListOptionsWithMoney(BasicListOptions):
    """
    Standard options for filtering and pagination in list operations with money.
    """

    def __init__(self, currency=None, amount: RangeFilteringOptions = None):
        super().__init__()
        self.currency = currency
        self.amount = amount

    def populate(self, values: QueryValues):
        super().populate(values)

        values.add("currency", self.currency).add("amount", QueryValues().fromRange(self.amount))


class MessageListOptions(BasicListOptions):
    """
    Options for filtering and pagination of messages.
    """

    def __init__(self, delivered: RangeFilteringOptions = None, status=None):
        super().__init__()
        self.delivered = delivered
        self.status = status

    def populate(self, values: QueryValues):
        super().populate(values)

        values \
            .add("delivered", QueryValues().fromRange(self.delivered)) \
            .add("status", self.status)

from falu.generic.detail_api_request import DetailApiRequest


class Money(DetailApiRequest):

    @classmethod
    def get_money_balance(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(path="/money_balances", api_key=api_key, idempotency_key=idempotency_key,
                       workspace=workspace, live=live)

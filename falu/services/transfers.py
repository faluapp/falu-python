from falu.generic.get_api_request import GetApiRequest
from falu.generic.post_api_request import PostApiRequest


class Transfer(PostApiRequest, GetApiRequest):
    """
    A Transfer object is created when you move money from your business either to another business or to a customer.
    """

    @classmethod
    def get_transfer(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List transfers

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/transfers",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_transfer(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create a transfer

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/transfers",
            data=data,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def retrieve_transfer(cls, transfer, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve a transfer

        :param transfer:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/transfers/{transfer}".format(transfer=transfer),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_transfer(cls, transfer, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Update a transfer

        :param transfer:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        pass
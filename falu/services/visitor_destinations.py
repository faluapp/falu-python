from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.post_api_request import PostApiRequest


class VisitorDestination(PostApiRequest, GetApiRequest, DeleteApiRequest):
    """
    A VisitorDestination object represents a destination for visitors.
    """

    @classmethod
    def get_destinations(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List destinations

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="visits/destinations",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_destination(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create destination

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="visits/destinations",
            data=data,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_destination(cls, destination, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Get destination

        :param destination:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"visits/destinations/{destination}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_destination(cls, destination, api_key=None, idempotency_key: str = None, workspace=None,
                           live: bool = None):
        """
        Update destination

        :param destination:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        pass

    @classmethod
    def delete_destination(cls, destination, api_key=None, idempotency_key: str = None, workspace=None,
                           live: bool = None):
        """
        Delete destination

        :param destination:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.delete(
            path=f"visits/destinations/{destination}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

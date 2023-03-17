from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.post_api_request import PostApiRequest


class TerminalLocation(PostApiRequest, GetApiRequest, DeleteApiRequest):
    """
    A TerminalLocation represents a grouping of devices.
    """

    @classmethod
    def get_terminal_locations(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List terminal locations

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/terminals/locations",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_terminal_location(cls, data, api_key=None, idempotency_key: str = None, workspace=None,
                                 live: bool = None):
        """
        List terminal locations

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/terminals/locations",
            data=data,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_terminal_location(cls, terminal_location, api_key=None, idempotency_key: str = None, workspace=None,
                              live: bool = None):
        """
        Get terminal location

        :param terminal_location:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/terminals/locations/{terminal_location}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_terminal_location(cls, terminal_location, api_key=None, idempotency_key: str = None, workspace=None,
                                 live: bool = None):
        """
        Update terminal location

        :param terminal_location:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        pass

    @classmethod
    def delete_terminal_location(cls, terminal_location, api_key=None, idempotency_key: str = None, workspace=None,
                                 live: bool = None):
        """
        Delete terminal location

        :param terminal_location:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.delete(
            path=f"/terminals/locations/{terminal_location}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

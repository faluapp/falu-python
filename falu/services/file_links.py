from falu.generic.get_api_request import GetApiRequest
from falu.generic.post_api_request import PostApiRequest


class FileLinkOptions:
    pass


class FileLink(PostApiRequest, GetApiRequest):
    """
    To share the contents of an File object with non-Falu users, you can create an FileLink.
    It contains a URL that can be used to retrieve the contents of the file without authentication.
    """

    @classmethod
    def get_file_links(cls, options: FileLinkOptions = None, api_key=None, idempotency_key: str = None, workspace=None,
                       live: bool = None):
        """
        Get file links

        :param options:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/file_links",
            options=options,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_file_links(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create file links

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/file_links",
            data=data,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_file_link(cls, link, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Get file links

        :param link:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/file_links/{link}".format(link=link),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_file_link(cls, link, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Update file links

        :param link:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        pass
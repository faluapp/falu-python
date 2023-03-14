from falu.generic.get_api_request import GetApiRequest
from falu.generic.post_api_request import PostApiRequest


class Messages(PostApiRequest, GetApiRequest):

    @classmethod
    def get_messages(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List messages

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path="/messages",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def send_message(cls, data: dict, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create a message

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/messages",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_message(cls, message_id, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve message

        :param message_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path="/messages/{message_id}".format(message_id=message_id),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_message(cls, message_id, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Update message

        :param message_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        pass

    @classmethod
    def cancel_message(cls, message_id, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Cancel a message. A message can be cancelled when it is in accepted status.

        :param message_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/messages/{message_id}/cancel".format(message_id=message_id),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

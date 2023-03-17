from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.post_api_request import PostApiRequest


class WebhookEndpoint(PostApiRequest, GetApiRequest, DeleteApiRequest):
    """
    You can configure webhook endpoints via the API to be notified about events that happen in your Falu workspace.
    Most users configure webhooks from the dashboard, which provides a user interface to registering and testing your webhook endpoints.
    """

    @classmethod
    def get_webhooks(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List webhook endpoints

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/webhooks/endpoint",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_webhook(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create webhook endpoint

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/webhooks/endpoint",
            data=data,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_webhook(cls, webhook_endpoint, api_key=None, idempotency_key: str = None, workspace=None,
                    live: bool = None):
        """
        Get webhook endpoint

        :param webhook_endpoint:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/webhooks/endpoint/{webhook_endpoint}".format(webhook_endpoint=webhook_endpoint),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_webhook(cls, webhook_endpoint, api_key=None, idempotency_key: str = None, workspace=None,
                       live: bool = None):
        """
        Update webhook endpoint

        :param webhook_endpoint:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        pass

    @classmethod
    def delete_webhook(cls, webhook_endpoint, api_key=None, idempotency_key: str = None, workspace=None,
                       live: bool = None):
        """
        Get webhook endpoint

        :param webhook_endpoint:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.delete(
            path=f"/webhooks/endpoint/{webhook_endpoint}".format(webhook_endpoint=webhook_endpoint),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def roll_webhook(cls, webhook_endpoint, data, api_key=None, idempotency_key: str = None, workspace=None,
                     live: bool = None):
        """
        Roll a webhook endpoint secret

        :param data:
        :param webhook_endpoint:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/webhooks/endpoint/{webhook_endpoint}".format(webhook_endpoint=webhook_endpoint),
            data=data,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

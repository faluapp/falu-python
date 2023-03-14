from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.post_api_request import PostApiRequest


class MessageTemplates(PostApiRequest, GetApiRequest, DeleteApiRequest):
    """
     Deleting a suppression allows you to resume sending messages to the given destination.
     Suppression with spam_complaint reason cannot be deleted.
    """

    @classmethod
    def get_message_templates(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
           List message templates

           :param api_key:
           :param idempotency_key:
           :param workspace:
           :param live:
           :return:
        """
        return cls.get(
            path="/message_templates",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_message_template(cls, data: dict, api_key=None, idempotency_key: str = None, workspace=None,
                                live: bool = None):
        """
           Create message template

           :param data:
           :param api_key:
           :param idempotency_key:
           :param workspace:
           :param live:
           :return:
        """
        return cls.create(
            path="/message_templates",
            data=data,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_message_template(cls, template, api_key=None, idempotency_key: str = None, workspace=None,
                             live: bool = None):
        """
          Get message template

          :param template:
          :param api_key:
          :param idempotency_key:
          :param workspace:
          :param live:
          :return:
        """
        return cls.get(
            path=f"/message_templates/{template}".format(template=template),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_message_template(cls, template, api_key=None, idempotency_key: str = None, workspace=None,
                                live: bool = None):
        """
          Update message template

          :param template:
          :param api_key:
          :param idempotency_key:
          :param workspace:
          :param live:
          :return:
        """
        return cls.get(  # update
            path=f"/message_templates/{template}".format(template=template),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def delete_message_template(cls, template, api_key=None, idempotency_key: str = None, workspace=None,
                                live: bool = None):
        """
        Delete message template

        :param template:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.delete(
            path=f"/message_templates/{template}".format(template=template),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def validate_message_template(cls, data: dict, api_key=None, idempotency_key: str = None, workspace=None,
                                  live: bool = None):
        """
          Validate message template

          :param data:
          :param api_key:
          :param idempotency_key:
          :param workspace:
          :param live:
          :return:
        """
        return cls.create(
            path="/message_templates",
            data=data,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

# coding: utf-8

"""
    PubMan REST API

    This is an automatically generated REST API client for PubMan.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AuditDbVO(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'comment': 'str',
        'event': 'str',
        'id': 'int',
        'modification_date': 'datetime',
        'modifier': 'AccountUserDbRO',
        'pub_item': 'ItemVersionVO'
    }

    attribute_map = {
        'comment': 'comment',
        'event': 'event',
        'id': 'id',
        'modification_date': 'modificationDate',
        'modifier': 'modifier',
        'pub_item': 'pubItem'
    }

    def __init__(self, comment=None, event=None, id=None, modification_date=None, modifier=None, pub_item=None):  # noqa: E501
        """AuditDbVO - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._event = None
        self._id = None
        self._modification_date = None
        self._modifier = None
        self._pub_item = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if event is not None:
            self.event = event
        if id is not None:
            self.id = id
        if modification_date is not None:
            self.modification_date = modification_date
        if modifier is not None:
            self.modifier = modifier
        if pub_item is not None:
            self.pub_item = pub_item

    @property
    def comment(self):
        """Gets the comment of this AuditDbVO.  # noqa: E501


        :return: The comment of this AuditDbVO.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AuditDbVO.


        :param comment: The comment of this AuditDbVO.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def event(self):
        """Gets the event of this AuditDbVO.  # noqa: E501


        :return: The event of this AuditDbVO.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this AuditDbVO.


        :param event: The event of this AuditDbVO.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATE", "SUBMIT", "RELEASE", "REVISE", "WITHDRAW", "UPDATE"]  # noqa: E501
        if event not in allowed_values:
            raise ValueError(
                "Invalid value for `event` ({0}), must be one of {1}"  # noqa: E501
                .format(event, allowed_values)
            )

        self._event = event

    @property
    def id(self):
        """Gets the id of this AuditDbVO.  # noqa: E501


        :return: The id of this AuditDbVO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditDbVO.


        :param id: The id of this AuditDbVO.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def modification_date(self):
        """Gets the modification_date of this AuditDbVO.  # noqa: E501


        :return: The modification_date of this AuditDbVO.  # noqa: E501
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this AuditDbVO.


        :param modification_date: The modification_date of this AuditDbVO.  # noqa: E501
        :type: datetime
        """

        self._modification_date = modification_date

    @property
    def modifier(self):
        """Gets the modifier of this AuditDbVO.  # noqa: E501


        :return: The modifier of this AuditDbVO.  # noqa: E501
        :rtype: AccountUserDbRO
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this AuditDbVO.


        :param modifier: The modifier of this AuditDbVO.  # noqa: E501
        :type: AccountUserDbRO
        """

        self._modifier = modifier

    @property
    def pub_item(self):
        """Gets the pub_item of this AuditDbVO.  # noqa: E501


        :return: The pub_item of this AuditDbVO.  # noqa: E501
        :rtype: ItemVersionVO
        """
        return self._pub_item

    @pub_item.setter
    def pub_item(self, pub_item):
        """Sets the pub_item of this AuditDbVO.


        :param pub_item: The pub_item of this AuditDbVO.  # noqa: E501
        :type: ItemVersionVO
        """

        self._pub_item = pub_item

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AuditDbVO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuditDbVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class PublishingInfoVO(object):
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
        'edition': 'str',
        'place': 'str',
        'publisher': 'str'
    }

    attribute_map = {
        'edition': 'edition',
        'place': 'place',
        'publisher': 'publisher'
    }

    def __init__(self, edition=None, place=None, publisher=None):  # noqa: E501
        """PublishingInfoVO - a model defined in Swagger"""  # noqa: E501

        self._edition = None
        self._place = None
        self._publisher = None
        self.discriminator = None

        if edition is not None:
            self.edition = edition
        if place is not None:
            self.place = place
        if publisher is not None:
            self.publisher = publisher

    @property
    def edition(self):
        """Gets the edition of this PublishingInfoVO.  # noqa: E501


        :return: The edition of this PublishingInfoVO.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this PublishingInfoVO.


        :param edition: The edition of this PublishingInfoVO.  # noqa: E501
        :type: str
        """

        self._edition = edition

    @property
    def place(self):
        """Gets the place of this PublishingInfoVO.  # noqa: E501


        :return: The place of this PublishingInfoVO.  # noqa: E501
        :rtype: str
        """
        return self._place

    @place.setter
    def place(self, place):
        """Sets the place of this PublishingInfoVO.


        :param place: The place of this PublishingInfoVO.  # noqa: E501
        :type: str
        """

        self._place = place

    @property
    def publisher(self):
        """Gets the publisher of this PublishingInfoVO.  # noqa: E501


        :return: The publisher of this PublishingInfoVO.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this PublishingInfoVO.


        :param publisher: The publisher of this PublishingInfoVO.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

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
        if issubclass(PublishingInfoVO, dict):
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
        if not isinstance(other, PublishingInfoVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
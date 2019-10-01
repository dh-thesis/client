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


class LegalCaseVO(object):
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
        'court_name': 'str',
        'date_published': 'str',
        'identifier': 'str',
        'title': 'str'
    }

    attribute_map = {
        'court_name': 'courtName',
        'date_published': 'datePublished',
        'identifier': 'identifier',
        'title': 'title'
    }

    def __init__(self, court_name=None, date_published=None, identifier=None, title=None):  # noqa: E501
        """LegalCaseVO - a model defined in Swagger"""  # noqa: E501

        self._court_name = None
        self._date_published = None
        self._identifier = None
        self._title = None
        self.discriminator = None

        if court_name is not None:
            self.court_name = court_name
        if date_published is not None:
            self.date_published = date_published
        if identifier is not None:
            self.identifier = identifier
        if title is not None:
            self.title = title

    @property
    def court_name(self):
        """Gets the court_name of this LegalCaseVO.  # noqa: E501


        :return: The court_name of this LegalCaseVO.  # noqa: E501
        :rtype: str
        """
        return self._court_name

    @court_name.setter
    def court_name(self, court_name):
        """Sets the court_name of this LegalCaseVO.


        :param court_name: The court_name of this LegalCaseVO.  # noqa: E501
        :type: str
        """

        self._court_name = court_name

    @property
    def date_published(self):
        """Gets the date_published of this LegalCaseVO.  # noqa: E501


        :return: The date_published of this LegalCaseVO.  # noqa: E501
        :rtype: str
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this LegalCaseVO.


        :param date_published: The date_published of this LegalCaseVO.  # noqa: E501
        :type: str
        """

        self._date_published = date_published

    @property
    def identifier(self):
        """Gets the identifier of this LegalCaseVO.  # noqa: E501


        :return: The identifier of this LegalCaseVO.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this LegalCaseVO.


        :param identifier: The identifier of this LegalCaseVO.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def title(self):
        """Gets the title of this LegalCaseVO.  # noqa: E501


        :return: The title of this LegalCaseVO.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LegalCaseVO.


        :param title: The title of this LegalCaseVO.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(LegalCaseVO, dict):
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
        if not isinstance(other, LegalCaseVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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


class GrantVO(object):
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
        'grant_type': 'str',
        'object_ref': 'str',
        'role': 'str'
    }

    attribute_map = {
        'grant_type': 'grantType',
        'object_ref': 'objectRef',
        'role': 'role'
    }

    def __init__(self, grant_type=None, object_ref=None, role=None):  # noqa: E501
        """GrantVO - a model defined in Swagger"""  # noqa: E501

        self._grant_type = None
        self._object_ref = None
        self._role = None
        self.discriminator = None

        if grant_type is not None:
            self.grant_type = grant_type
        if object_ref is not None:
            self.object_ref = object_ref
        if role is not None:
            self.role = role

    @property
    def grant_type(self):
        """Gets the grant_type of this GrantVO.  # noqa: E501


        :return: The grant_type of this GrantVO.  # noqa: E501
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this GrantVO.


        :param grant_type: The grant_type of this GrantVO.  # noqa: E501
        :type: str
        """

        self._grant_type = grant_type

    @property
    def object_ref(self):
        """Gets the object_ref of this GrantVO.  # noqa: E501


        :return: The object_ref of this GrantVO.  # noqa: E501
        :rtype: str
        """
        return self._object_ref

    @object_ref.setter
    def object_ref(self, object_ref):
        """Sets the object_ref of this GrantVO.


        :param object_ref: The object_ref of this GrantVO.  # noqa: E501
        :type: str
        """

        self._object_ref = object_ref

    @property
    def role(self):
        """Gets the role of this GrantVO.  # noqa: E501


        :return: The role of this GrantVO.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this GrantVO.


        :param role: The role of this GrantVO.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if issubclass(GrantVO, dict):
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
        if not isinstance(other, GrantVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

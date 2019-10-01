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


class SearchRetrieveRecordVOItemVersionVO(object):
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
        'data': 'ItemVersionVO',
        'packing': 'str',
        'persistence_id': 'str',
        'schema': 'str'
    }

    attribute_map = {
        'data': 'data',
        'packing': 'packing',
        'persistence_id': 'persistenceId',
        'schema': 'schema'
    }

    def __init__(self, data=None, packing=None, persistence_id=None, schema=None):  # noqa: E501
        """SearchRetrieveRecordVOItemVersionVO - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._packing = None
        self._persistence_id = None
        self._schema = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if packing is not None:
            self.packing = packing
        if persistence_id is not None:
            self.persistence_id = persistence_id
        if schema is not None:
            self.schema = schema

    @property
    def data(self):
        """Gets the data of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501


        :return: The data of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501
        :rtype: ItemVersionVO
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SearchRetrieveRecordVOItemVersionVO.


        :param data: The data of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501
        :type: ItemVersionVO
        """

        self._data = data

    @property
    def packing(self):
        """Gets the packing of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501


        :return: The packing of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501
        :rtype: str
        """
        return self._packing

    @packing.setter
    def packing(self, packing):
        """Sets the packing of this SearchRetrieveRecordVOItemVersionVO.


        :param packing: The packing of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501
        :type: str
        """

        self._packing = packing

    @property
    def persistence_id(self):
        """Gets the persistence_id of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501


        :return: The persistence_id of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501
        :rtype: str
        """
        return self._persistence_id

    @persistence_id.setter
    def persistence_id(self, persistence_id):
        """Sets the persistence_id of this SearchRetrieveRecordVOItemVersionVO.


        :param persistence_id: The persistence_id of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501
        :type: str
        """

        self._persistence_id = persistence_id

    @property
    def schema(self):
        """Gets the schema of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501


        :return: The schema of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this SearchRetrieveRecordVOItemVersionVO.


        :param schema: The schema of this SearchRetrieveRecordVOItemVersionVO.  # noqa: E501
        :type: str
        """

        self._schema = schema

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
        if issubclass(SearchRetrieveRecordVOItemVersionVO, dict):
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
        if not isinstance(other, SearchRetrieveRecordVOItemVersionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

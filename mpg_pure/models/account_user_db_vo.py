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


class AccountUserDbVO(object):
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
        'active': 'bool',
        'affiliation': 'AffiliationDbRO',
        'creation_date': 'datetime',
        'creator': 'AccountUserDbRO',
        'email': 'str',
        'grant_list': 'list[GrantVO]',
        'last_modification_date': 'datetime',
        'loginname': 'str',
        'modifier': 'AccountUserDbRO',
        'name': 'str',
        'object_id': 'str',
        'password': 'str'
    }

    attribute_map = {
        'active': 'active',
        'affiliation': 'affiliation',
        'creation_date': 'creationDate',
        'creator': 'creator',
        'email': 'email',
        'grant_list': 'grantList',
        'last_modification_date': 'lastModificationDate',
        'loginname': 'loginname',
        'modifier': 'modifier',
        'name': 'name',
        'object_id': 'objectId',
        'password': 'password'
    }

    def __init__(self, active=None, affiliation=None, creation_date=None, creator=None, email=None, grant_list=None, last_modification_date=None, loginname=None, modifier=None, name=None, object_id=None, password=None):  # noqa: E501
        """AccountUserDbVO - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._affiliation = None
        self._creation_date = None
        self._creator = None
        self._email = None
        self._grant_list = None
        self._last_modification_date = None
        self._loginname = None
        self._modifier = None
        self._name = None
        self._object_id = None
        self._password = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if affiliation is not None:
            self.affiliation = affiliation
        if creation_date is not None:
            self.creation_date = creation_date
        if creator is not None:
            self.creator = creator
        if email is not None:
            self.email = email
        if grant_list is not None:
            self.grant_list = grant_list
        if last_modification_date is not None:
            self.last_modification_date = last_modification_date
        if loginname is not None:
            self.loginname = loginname
        if modifier is not None:
            self.modifier = modifier
        if name is not None:
            self.name = name
        if object_id is not None:
            self.object_id = object_id
        if password is not None:
            self.password = password

    @property
    def active(self):
        """Gets the active of this AccountUserDbVO.  # noqa: E501


        :return: The active of this AccountUserDbVO.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AccountUserDbVO.


        :param active: The active of this AccountUserDbVO.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def affiliation(self):
        """Gets the affiliation of this AccountUserDbVO.  # noqa: E501


        :return: The affiliation of this AccountUserDbVO.  # noqa: E501
        :rtype: AffiliationDbRO
        """
        return self._affiliation

    @affiliation.setter
    def affiliation(self, affiliation):
        """Sets the affiliation of this AccountUserDbVO.


        :param affiliation: The affiliation of this AccountUserDbVO.  # noqa: E501
        :type: AffiliationDbRO
        """

        self._affiliation = affiliation

    @property
    def creation_date(self):
        """Gets the creation_date of this AccountUserDbVO.  # noqa: E501


        :return: The creation_date of this AccountUserDbVO.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this AccountUserDbVO.


        :param creation_date: The creation_date of this AccountUserDbVO.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def creator(self):
        """Gets the creator of this AccountUserDbVO.  # noqa: E501


        :return: The creator of this AccountUserDbVO.  # noqa: E501
        :rtype: AccountUserDbRO
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this AccountUserDbVO.


        :param creator: The creator of this AccountUserDbVO.  # noqa: E501
        :type: AccountUserDbRO
        """

        self._creator = creator

    @property
    def email(self):
        """Gets the email of this AccountUserDbVO.  # noqa: E501


        :return: The email of this AccountUserDbVO.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountUserDbVO.


        :param email: The email of this AccountUserDbVO.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def grant_list(self):
        """Gets the grant_list of this AccountUserDbVO.  # noqa: E501


        :return: The grant_list of this AccountUserDbVO.  # noqa: E501
        :rtype: list[GrantVO]
        """
        return self._grant_list

    @grant_list.setter
    def grant_list(self, grant_list):
        """Sets the grant_list of this AccountUserDbVO.


        :param grant_list: The grant_list of this AccountUserDbVO.  # noqa: E501
        :type: list[GrantVO]
        """

        self._grant_list = grant_list

    @property
    def last_modification_date(self):
        """Gets the last_modification_date of this AccountUserDbVO.  # noqa: E501


        :return: The last_modification_date of this AccountUserDbVO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_date

    @last_modification_date.setter
    def last_modification_date(self, last_modification_date):
        """Sets the last_modification_date of this AccountUserDbVO.


        :param last_modification_date: The last_modification_date of this AccountUserDbVO.  # noqa: E501
        :type: datetime
        """

        self._last_modification_date = last_modification_date

    @property
    def loginname(self):
        """Gets the loginname of this AccountUserDbVO.  # noqa: E501


        :return: The loginname of this AccountUserDbVO.  # noqa: E501
        :rtype: str
        """
        return self._loginname

    @loginname.setter
    def loginname(self, loginname):
        """Sets the loginname of this AccountUserDbVO.


        :param loginname: The loginname of this AccountUserDbVO.  # noqa: E501
        :type: str
        """

        self._loginname = loginname

    @property
    def modifier(self):
        """Gets the modifier of this AccountUserDbVO.  # noqa: E501


        :return: The modifier of this AccountUserDbVO.  # noqa: E501
        :rtype: AccountUserDbRO
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this AccountUserDbVO.


        :param modifier: The modifier of this AccountUserDbVO.  # noqa: E501
        :type: AccountUserDbRO
        """

        self._modifier = modifier

    @property
    def name(self):
        """Gets the name of this AccountUserDbVO.  # noqa: E501


        :return: The name of this AccountUserDbVO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountUserDbVO.


        :param name: The name of this AccountUserDbVO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def object_id(self):
        """Gets the object_id of this AccountUserDbVO.  # noqa: E501


        :return: The object_id of this AccountUserDbVO.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this AccountUserDbVO.


        :param object_id: The object_id of this AccountUserDbVO.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def password(self):
        """Gets the password of this AccountUserDbVO.  # noqa: E501


        :return: The password of this AccountUserDbVO.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AccountUserDbVO.


        :param password: The password of this AccountUserDbVO.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(AccountUserDbVO, dict):
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
        if not isinstance(other, AccountUserDbVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

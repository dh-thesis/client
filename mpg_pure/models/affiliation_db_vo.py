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


class AffiliationDbVO(object):
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
        'creation_date': 'datetime',
        'creator': 'AccountUserDbRO',
        'has_children': 'bool',
        'has_predecessors': 'bool',
        'last_modification_date': 'datetime',
        'metadata': 'MdsOrganizationalUnitDetailsVO',
        'modifier': 'AccountUserDbRO',
        'name': 'str',
        'object_id': 'str',
        'parent_affiliation': 'AffiliationDbRO',
        'predecessor_affiliations': 'list[AffiliationDbRO]',
        'public_status': 'str'
    }

    attribute_map = {
        'creation_date': 'creationDate',
        'creator': 'creator',
        'has_children': 'hasChildren',
        'has_predecessors': 'hasPredecessors',
        'last_modification_date': 'lastModificationDate',
        'metadata': 'metadata',
        'modifier': 'modifier',
        'name': 'name',
        'object_id': 'objectId',
        'parent_affiliation': 'parentAffiliation',
        'predecessor_affiliations': 'predecessorAffiliations',
        'public_status': 'publicStatus'
    }

    def __init__(self, creation_date=None, creator=None, has_children=None, has_predecessors=None, last_modification_date=None, metadata=None, modifier=None, name=None, object_id=None, parent_affiliation=None, predecessor_affiliations=None, public_status=None):  # noqa: E501
        """AffiliationDbVO - a model defined in Swagger"""  # noqa: E501

        self._creation_date = None
        self._creator = None
        self._has_children = None
        self._has_predecessors = None
        self._last_modification_date = None
        self._metadata = None
        self._modifier = None
        self._name = None
        self._object_id = None
        self._parent_affiliation = None
        self._predecessor_affiliations = None
        self._public_status = None
        self.discriminator = None

        if creation_date is not None:
            self.creation_date = creation_date
        if creator is not None:
            self.creator = creator
        if has_children is not None:
            self.has_children = has_children
        if has_predecessors is not None:
            self.has_predecessors = has_predecessors
        if last_modification_date is not None:
            self.last_modification_date = last_modification_date
        if metadata is not None:
            self.metadata = metadata
        if modifier is not None:
            self.modifier = modifier
        if name is not None:
            self.name = name
        if object_id is not None:
            self.object_id = object_id
        if parent_affiliation is not None:
            self.parent_affiliation = parent_affiliation
        if predecessor_affiliations is not None:
            self.predecessor_affiliations = predecessor_affiliations
        if public_status is not None:
            self.public_status = public_status

    @property
    def creation_date(self):
        """Gets the creation_date of this AffiliationDbVO.  # noqa: E501


        :return: The creation_date of this AffiliationDbVO.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this AffiliationDbVO.


        :param creation_date: The creation_date of this AffiliationDbVO.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def creator(self):
        """Gets the creator of this AffiliationDbVO.  # noqa: E501


        :return: The creator of this AffiliationDbVO.  # noqa: E501
        :rtype: AccountUserDbRO
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this AffiliationDbVO.


        :param creator: The creator of this AffiliationDbVO.  # noqa: E501
        :type: AccountUserDbRO
        """

        self._creator = creator

    @property
    def has_children(self):
        """Gets the has_children of this AffiliationDbVO.  # noqa: E501


        :return: The has_children of this AffiliationDbVO.  # noqa: E501
        :rtype: bool
        """
        return self._has_children

    @has_children.setter
    def has_children(self, has_children):
        """Sets the has_children of this AffiliationDbVO.


        :param has_children: The has_children of this AffiliationDbVO.  # noqa: E501
        :type: bool
        """

        self._has_children = has_children

    @property
    def has_predecessors(self):
        """Gets the has_predecessors of this AffiliationDbVO.  # noqa: E501


        :return: The has_predecessors of this AffiliationDbVO.  # noqa: E501
        :rtype: bool
        """
        return self._has_predecessors

    @has_predecessors.setter
    def has_predecessors(self, has_predecessors):
        """Sets the has_predecessors of this AffiliationDbVO.


        :param has_predecessors: The has_predecessors of this AffiliationDbVO.  # noqa: E501
        :type: bool
        """

        self._has_predecessors = has_predecessors

    @property
    def last_modification_date(self):
        """Gets the last_modification_date of this AffiliationDbVO.  # noqa: E501


        :return: The last_modification_date of this AffiliationDbVO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_date

    @last_modification_date.setter
    def last_modification_date(self, last_modification_date):
        """Sets the last_modification_date of this AffiliationDbVO.


        :param last_modification_date: The last_modification_date of this AffiliationDbVO.  # noqa: E501
        :type: datetime
        """

        self._last_modification_date = last_modification_date

    @property
    def metadata(self):
        """Gets the metadata of this AffiliationDbVO.  # noqa: E501


        :return: The metadata of this AffiliationDbVO.  # noqa: E501
        :rtype: MdsOrganizationalUnitDetailsVO
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AffiliationDbVO.


        :param metadata: The metadata of this AffiliationDbVO.  # noqa: E501
        :type: MdsOrganizationalUnitDetailsVO
        """

        self._metadata = metadata

    @property
    def modifier(self):
        """Gets the modifier of this AffiliationDbVO.  # noqa: E501


        :return: The modifier of this AffiliationDbVO.  # noqa: E501
        :rtype: AccountUserDbRO
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this AffiliationDbVO.


        :param modifier: The modifier of this AffiliationDbVO.  # noqa: E501
        :type: AccountUserDbRO
        """

        self._modifier = modifier

    @property
    def name(self):
        """Gets the name of this AffiliationDbVO.  # noqa: E501


        :return: The name of this AffiliationDbVO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AffiliationDbVO.


        :param name: The name of this AffiliationDbVO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def object_id(self):
        """Gets the object_id of this AffiliationDbVO.  # noqa: E501


        :return: The object_id of this AffiliationDbVO.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this AffiliationDbVO.


        :param object_id: The object_id of this AffiliationDbVO.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def parent_affiliation(self):
        """Gets the parent_affiliation of this AffiliationDbVO.  # noqa: E501


        :return: The parent_affiliation of this AffiliationDbVO.  # noqa: E501
        :rtype: AffiliationDbRO
        """
        return self._parent_affiliation

    @parent_affiliation.setter
    def parent_affiliation(self, parent_affiliation):
        """Sets the parent_affiliation of this AffiliationDbVO.


        :param parent_affiliation: The parent_affiliation of this AffiliationDbVO.  # noqa: E501
        :type: AffiliationDbRO
        """

        self._parent_affiliation = parent_affiliation

    @property
    def predecessor_affiliations(self):
        """Gets the predecessor_affiliations of this AffiliationDbVO.  # noqa: E501


        :return: The predecessor_affiliations of this AffiliationDbVO.  # noqa: E501
        :rtype: list[AffiliationDbRO]
        """
        return self._predecessor_affiliations

    @predecessor_affiliations.setter
    def predecessor_affiliations(self, predecessor_affiliations):
        """Sets the predecessor_affiliations of this AffiliationDbVO.


        :param predecessor_affiliations: The predecessor_affiliations of this AffiliationDbVO.  # noqa: E501
        :type: list[AffiliationDbRO]
        """

        self._predecessor_affiliations = predecessor_affiliations

    @property
    def public_status(self):
        """Gets the public_status of this AffiliationDbVO.  # noqa: E501


        :return: The public_status of this AffiliationDbVO.  # noqa: E501
        :rtype: str
        """
        return self._public_status

    @public_status.setter
    def public_status(self, public_status):
        """Sets the public_status of this AffiliationDbVO.


        :param public_status: The public_status of this AffiliationDbVO.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "CLOSED", "OPENED", "DELETED"]  # noqa: E501
        if public_status not in allowed_values:
            raise ValueError(
                "Invalid value for `public_status` ({0}), must be one of {1}"  # noqa: E501
                .format(public_status, allowed_values)
            )

        self._public_status = public_status

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
        if issubclass(AffiliationDbVO, dict):
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
        if not isinstance(other, AffiliationDbVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

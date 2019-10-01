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


class FundingInfoVO(object):
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
        'funding_organization': 'FundingOrganizationVO',
        'funding_program': 'FundingProgramVO'
    }

    attribute_map = {
        'funding_organization': 'fundingOrganization',
        'funding_program': 'fundingProgram'
    }

    def __init__(self, funding_organization=None, funding_program=None):  # noqa: E501
        """FundingInfoVO - a model defined in Swagger"""  # noqa: E501

        self._funding_organization = None
        self._funding_program = None
        self.discriminator = None

        if funding_organization is not None:
            self.funding_organization = funding_organization
        if funding_program is not None:
            self.funding_program = funding_program

    @property
    def funding_organization(self):
        """Gets the funding_organization of this FundingInfoVO.  # noqa: E501


        :return: The funding_organization of this FundingInfoVO.  # noqa: E501
        :rtype: FundingOrganizationVO
        """
        return self._funding_organization

    @funding_organization.setter
    def funding_organization(self, funding_organization):
        """Sets the funding_organization of this FundingInfoVO.


        :param funding_organization: The funding_organization of this FundingInfoVO.  # noqa: E501
        :type: FundingOrganizationVO
        """

        self._funding_organization = funding_organization

    @property
    def funding_program(self):
        """Gets the funding_program of this FundingInfoVO.  # noqa: E501


        :return: The funding_program of this FundingInfoVO.  # noqa: E501
        :rtype: FundingProgramVO
        """
        return self._funding_program

    @funding_program.setter
    def funding_program(self, funding_program):
        """Sets the funding_program of this FundingInfoVO.


        :param funding_program: The funding_program of this FundingInfoVO.  # noqa: E501
        :type: FundingProgramVO
        """

        self._funding_program = funding_program

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
        if issubclass(FundingInfoVO, dict):
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
        if not isinstance(other, FundingInfoVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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


class SourceVO(object):
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
        'alternative_titles': 'list[AlternativeTitleVO]',
        'creators': 'list[CreatorVO]',
        'date_published_in_print': 'datetime',
        'end_page': 'str',
        'genre': 'str',
        'identifiers': 'list[IdentifierVO]',
        'issue': 'str',
        'publishing_info': 'PublishingInfoVO',
        'sequence_number': 'str',
        'sources': 'list[SourceVO]',
        'start_page': 'str',
        'title': 'str',
        'total_number_of_pages': 'str',
        'volume': 'str'
    }

    attribute_map = {
        'alternative_titles': 'alternativeTitles',
        'creators': 'creators',
        'date_published_in_print': 'datePublishedInPrint',
        'end_page': 'endPage',
        'genre': 'genre',
        'identifiers': 'identifiers',
        'issue': 'issue',
        'publishing_info': 'publishingInfo',
        'sequence_number': 'sequenceNumber',
        'sources': 'sources',
        'start_page': 'startPage',
        'title': 'title',
        'total_number_of_pages': 'totalNumberOfPages',
        'volume': 'volume'
    }

    def __init__(self, alternative_titles=None, creators=None, date_published_in_print=None, end_page=None, genre=None, identifiers=None, issue=None, publishing_info=None, sequence_number=None, sources=None, start_page=None, title=None, total_number_of_pages=None, volume=None):  # noqa: E501
        """SourceVO - a model defined in Swagger"""  # noqa: E501

        self._alternative_titles = None
        self._creators = None
        self._date_published_in_print = None
        self._end_page = None
        self._genre = None
        self._identifiers = None
        self._issue = None
        self._publishing_info = None
        self._sequence_number = None
        self._sources = None
        self._start_page = None
        self._title = None
        self._total_number_of_pages = None
        self._volume = None
        self.discriminator = None

        if alternative_titles is not None:
            self.alternative_titles = alternative_titles
        if creators is not None:
            self.creators = creators
        if date_published_in_print is not None:
            self.date_published_in_print = date_published_in_print
        if end_page is not None:
            self.end_page = end_page
        if genre is not None:
            self.genre = genre
        if identifiers is not None:
            self.identifiers = identifiers
        if issue is not None:
            self.issue = issue
        if publishing_info is not None:
            self.publishing_info = publishing_info
        if sequence_number is not None:
            self.sequence_number = sequence_number
        if sources is not None:
            self.sources = sources
        if start_page is not None:
            self.start_page = start_page
        if title is not None:
            self.title = title
        if total_number_of_pages is not None:
            self.total_number_of_pages = total_number_of_pages
        if volume is not None:
            self.volume = volume

    @property
    def alternative_titles(self):
        """Gets the alternative_titles of this SourceVO.  # noqa: E501


        :return: The alternative_titles of this SourceVO.  # noqa: E501
        :rtype: list[AlternativeTitleVO]
        """
        return self._alternative_titles

    @alternative_titles.setter
    def alternative_titles(self, alternative_titles):
        """Sets the alternative_titles of this SourceVO.


        :param alternative_titles: The alternative_titles of this SourceVO.  # noqa: E501
        :type: list[AlternativeTitleVO]
        """

        self._alternative_titles = alternative_titles

    @property
    def creators(self):
        """Gets the creators of this SourceVO.  # noqa: E501


        :return: The creators of this SourceVO.  # noqa: E501
        :rtype: list[CreatorVO]
        """
        return self._creators

    @creators.setter
    def creators(self, creators):
        """Sets the creators of this SourceVO.


        :param creators: The creators of this SourceVO.  # noqa: E501
        :type: list[CreatorVO]
        """

        self._creators = creators

    @property
    def date_published_in_print(self):
        """Gets the date_published_in_print of this SourceVO.  # noqa: E501


        :return: The date_published_in_print of this SourceVO.  # noqa: E501
        :rtype: datetime
        """
        return self._date_published_in_print

    @date_published_in_print.setter
    def date_published_in_print(self, date_published_in_print):
        """Sets the date_published_in_print of this SourceVO.


        :param date_published_in_print: The date_published_in_print of this SourceVO.  # noqa: E501
        :type: datetime
        """

        self._date_published_in_print = date_published_in_print

    @property
    def end_page(self):
        """Gets the end_page of this SourceVO.  # noqa: E501


        :return: The end_page of this SourceVO.  # noqa: E501
        :rtype: str
        """
        return self._end_page

    @end_page.setter
    def end_page(self, end_page):
        """Sets the end_page of this SourceVO.


        :param end_page: The end_page of this SourceVO.  # noqa: E501
        :type: str
        """

        self._end_page = end_page

    @property
    def genre(self):
        """Gets the genre of this SourceVO.  # noqa: E501


        :return: The genre of this SourceVO.  # noqa: E501
        :rtype: str
        """
        return self._genre

    @genre.setter
    def genre(self, genre):
        """Sets the genre of this SourceVO.


        :param genre: The genre of this SourceVO.  # noqa: E501
        :type: str
        """
        allowed_values = ["BOOK", "PROCEEDINGS", "JOURNAL", "ISSUE", "SERIES", "NEWSPAPER", "ENCYCLOPEDIA", "MULTI_VOLUME", "COMMENTARY", "HANDBOOK", "COLLECTED_EDITION", "FESTSCHRIFT"]  # noqa: E501
        if genre not in allowed_values:
            raise ValueError(
                "Invalid value for `genre` ({0}), must be one of {1}"  # noqa: E501
                .format(genre, allowed_values)
            )

        self._genre = genre

    @property
    def identifiers(self):
        """Gets the identifiers of this SourceVO.  # noqa: E501


        :return: The identifiers of this SourceVO.  # noqa: E501
        :rtype: list[IdentifierVO]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this SourceVO.


        :param identifiers: The identifiers of this SourceVO.  # noqa: E501
        :type: list[IdentifierVO]
        """

        self._identifiers = identifiers

    @property
    def issue(self):
        """Gets the issue of this SourceVO.  # noqa: E501


        :return: The issue of this SourceVO.  # noqa: E501
        :rtype: str
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """Sets the issue of this SourceVO.


        :param issue: The issue of this SourceVO.  # noqa: E501
        :type: str
        """

        self._issue = issue

    @property
    def publishing_info(self):
        """Gets the publishing_info of this SourceVO.  # noqa: E501


        :return: The publishing_info of this SourceVO.  # noqa: E501
        :rtype: PublishingInfoVO
        """
        return self._publishing_info

    @publishing_info.setter
    def publishing_info(self, publishing_info):
        """Sets the publishing_info of this SourceVO.


        :param publishing_info: The publishing_info of this SourceVO.  # noqa: E501
        :type: PublishingInfoVO
        """

        self._publishing_info = publishing_info

    @property
    def sequence_number(self):
        """Gets the sequence_number of this SourceVO.  # noqa: E501


        :return: The sequence_number of this SourceVO.  # noqa: E501
        :rtype: str
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this SourceVO.


        :param sequence_number: The sequence_number of this SourceVO.  # noqa: E501
        :type: str
        """

        self._sequence_number = sequence_number

    @property
    def sources(self):
        """Gets the sources of this SourceVO.  # noqa: E501


        :return: The sources of this SourceVO.  # noqa: E501
        :rtype: list[SourceVO]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this SourceVO.


        :param sources: The sources of this SourceVO.  # noqa: E501
        :type: list[SourceVO]
        """

        self._sources = sources

    @property
    def start_page(self):
        """Gets the start_page of this SourceVO.  # noqa: E501


        :return: The start_page of this SourceVO.  # noqa: E501
        :rtype: str
        """
        return self._start_page

    @start_page.setter
    def start_page(self, start_page):
        """Sets the start_page of this SourceVO.


        :param start_page: The start_page of this SourceVO.  # noqa: E501
        :type: str
        """

        self._start_page = start_page

    @property
    def title(self):
        """Gets the title of this SourceVO.  # noqa: E501


        :return: The title of this SourceVO.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SourceVO.


        :param title: The title of this SourceVO.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def total_number_of_pages(self):
        """Gets the total_number_of_pages of this SourceVO.  # noqa: E501


        :return: The total_number_of_pages of this SourceVO.  # noqa: E501
        :rtype: str
        """
        return self._total_number_of_pages

    @total_number_of_pages.setter
    def total_number_of_pages(self, total_number_of_pages):
        """Sets the total_number_of_pages of this SourceVO.


        :param total_number_of_pages: The total_number_of_pages of this SourceVO.  # noqa: E501
        :type: str
        """

        self._total_number_of_pages = total_number_of_pages

    @property
    def volume(self):
        """Gets the volume of this SourceVO.  # noqa: E501


        :return: The volume of this SourceVO.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this SourceVO.


        :param volume: The volume of this SourceVO.  # noqa: E501
        :type: str
        """

        self._volume = volume

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
        if issubclass(SourceVO, dict):
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
        if not isinstance(other, SourceVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

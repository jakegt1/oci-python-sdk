# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Action(object):
    """
    Details about the recommended action.
    """

    #: A constant which can be used with the type property of a Action.
    #: This constant has a value of "KB_ARTICLE"
    TYPE_KB_ARTICLE = "KB_ARTICLE"

    def __init__(self, **kwargs):
        """
        Initializes a new Action object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Action.
            Allowed values for this property are: "KB_ARTICLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param description:
            The value to assign to the description property of this Action.
        :type description: str

        :param url:
            The value to assign to the url property of this Action.
        :type url: str

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'url': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'url': 'url'
        }

        self._type = None
        self._description = None
        self._url = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Action.
        The status of the resource action.

        Allowed values for this property are: "KB_ARTICLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Action.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Action.
        The status of the resource action.


        :param type: The type of this Action.
        :type: str
        """
        allowed_values = ["KB_ARTICLE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def description(self):
        """
        **[Required]** Gets the description of this Action.
        Text describing the recommended action.


        :return: The description of this Action.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Action.
        Text describing the recommended action.


        :param description: The description of this Action.
        :type: str
        """
        self._description = description

    @property
    def url(self):
        """
        **[Required]** Gets the url of this Action.
        The URL path to documentation that explains how to perform the action.


        :return: The url of this Action.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Action.
        The URL path to documentation that explains how to perform the action.


        :param url: The url of this Action.
        :type: str
        """
        self._url = url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

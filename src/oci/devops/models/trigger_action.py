# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TriggerAction(object):
    """
    The action to be performed
    """

    #: A constant which can be used with the type property of a TriggerAction.
    #: This constant has a value of "TRIGGER_BUILD_PIPELINE"
    TYPE_TRIGGER_BUILD_PIPELINE = "TRIGGER_BUILD_PIPELINE"

    def __init__(self, **kwargs):
        """
        Initializes a new TriggerAction object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.TriggerBuildPipelineAction`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TriggerAction.
            Allowed values for this property are: "TRIGGER_BUILD_PIPELINE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param filter:
            The value to assign to the filter property of this TriggerAction.
        :type filter: oci.devops.models.Filter

        """
        self.swagger_types = {
            'type': 'str',
            'filter': 'Filter'
        }

        self.attribute_map = {
            'type': 'type',
            'filter': 'filter'
        }

        self._type = None
        self._filter = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'TRIGGER_BUILD_PIPELINE':
            return 'TriggerBuildPipelineAction'
        else:
            return 'TriggerAction'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this TriggerAction.
        The type of action that will be taken (allowed value - TRIGGER_BUILD_PIPELINE)

        Allowed values for this property are: "TRIGGER_BUILD_PIPELINE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this TriggerAction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TriggerAction.
        The type of action that will be taken (allowed value - TRIGGER_BUILD_PIPELINE)


        :param type: The type of this TriggerAction.
        :type: str
        """
        allowed_values = ["TRIGGER_BUILD_PIPELINE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def filter(self):
        """
        Gets the filter of this TriggerAction.

        :return: The filter of this TriggerAction.
        :rtype: oci.devops.models.Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this TriggerAction.

        :param filter: The filter of this TriggerAction.
        :type: oci.devops.models.Filter
        """
        self._filter = filter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
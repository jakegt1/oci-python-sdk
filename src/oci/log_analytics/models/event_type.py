# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EventType(object):
    """
    The event type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EventType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param event_type_name:
            The value to assign to the event_type_name property of this EventType.
        :type event_type_name: str

        :param spec_version:
            The value to assign to the spec_version property of this EventType.
        :type spec_version: str

        :param is_enabled:
            The value to assign to the is_enabled property of this EventType.
        :type is_enabled: bool

        :param is_system:
            The value to assign to the is_system property of this EventType.
        :type is_system: bool

        :param time_updated:
            The value to assign to the time_updated property of this EventType.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'event_type_name': 'str',
            'spec_version': 'str',
            'is_enabled': 'bool',
            'is_system': 'bool',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'event_type_name': 'eventTypeName',
            'spec_version': 'specVersion',
            'is_enabled': 'isEnabled',
            'is_system': 'isSystem',
            'time_updated': 'timeUpdated'
        }

        self._event_type_name = None
        self._spec_version = None
        self._is_enabled = None
        self._is_system = None
        self._time_updated = None

    @property
    def event_type_name(self):
        """
        Gets the event_type_name of this EventType.
        The name of the event type.


        :return: The event_type_name of this EventType.
        :rtype: str
        """
        return self._event_type_name

    @event_type_name.setter
    def event_type_name(self, event_type_name):
        """
        Sets the event_type_name of this EventType.
        The name of the event type.


        :param event_type_name: The event_type_name of this EventType.
        :type: str
        """
        self._event_type_name = event_type_name

    @property
    def spec_version(self):
        """
        Gets the spec_version of this EventType.
        The version.


        :return: The spec_version of this EventType.
        :rtype: str
        """
        return self._spec_version

    @spec_version.setter
    def spec_version(self, spec_version):
        """
        Sets the spec_version of this EventType.
        The version.


        :param spec_version: The spec_version of this EventType.
        :type: str
        """
        self._spec_version = spec_version

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this EventType.
        A flag indicating whether or not the event type is enabled.


        :return: The is_enabled of this EventType.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this EventType.
        A flag indicating whether or not the event type is enabled.


        :param is_enabled: The is_enabled of this EventType.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def is_system(self):
        """
        Gets the is_system of this EventType.
        A flag indicating whether or not the event type is user defined.


        :return: The is_system of this EventType.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this EventType.
        A flag indicating whether or not the event type is user defined.


        :param is_system: The is_system of this EventType.
        :type: bool
        """
        self._is_system = is_system

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EventType.
        The last updated time.


        :return: The time_updated of this EventType.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EventType.
        The last updated time.


        :param time_updated: The time_updated of this EventType.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

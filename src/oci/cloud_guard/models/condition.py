# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Condition(object):
    """
    Base condition object
    """

    #: A constant which can be used with the kind property of a Condition.
    #: This constant has a value of "COMPOSITE"
    KIND_COMPOSITE = "COMPOSITE"

    #: A constant which can be used with the kind property of a Condition.
    #: This constant has a value of "SIMPLE"
    KIND_SIMPLE = "SIMPLE"

    def __init__(self, **kwargs):
        """
        Initializes a new Condition object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_guard.models.SimpleCondition`
        * :class:`~oci.cloud_guard.models.CompositeCondition`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this Condition.
            Allowed values for this property are: "COMPOSITE", "SIMPLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        """
        self.swagger_types = {
            'kind': 'str'
        }

        self.attribute_map = {
            'kind': 'kind'
        }

        self._kind = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['kind']

        if type == 'SIMPLE':
            return 'SimpleCondition'

        if type == 'COMPOSITE':
            return 'CompositeCondition'
        else:
            return 'Condition'

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this Condition.
        Type of condition object

        Allowed values for this property are: "COMPOSITE", "SIMPLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The kind of this Condition.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this Condition.
        Type of condition object


        :param kind: The kind of this Condition.
        :type: str
        """
        allowed_values = ["COMPOSITE", "SIMPLE"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            kind = 'UNKNOWN_ENUM_VALUE'
        self._kind = kind

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

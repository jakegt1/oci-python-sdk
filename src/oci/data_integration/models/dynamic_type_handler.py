# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DynamicTypeHandler(object):
    """
    This type defines how to derived fields for the dynamic type itself.
    """

    #: A constant which can be used with the model_type property of a DynamicTypeHandler.
    #: This constant has a value of "RULE_TYPE_CONFIGS"
    MODEL_TYPE_RULE_TYPE_CONFIGS = "RULE_TYPE_CONFIGS"

    def __init__(self, **kwargs):
        """
        Initializes a new DynamicTypeHandler object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.RuleTypeConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DynamicTypeHandler.
            Allowed values for this property are: "RULE_TYPE_CONFIGS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        """
        self.swagger_types = {
            'model_type': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType'
        }

        self._model_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'RULE_TYPE_CONFIGS':
            return 'RuleTypeConfig'
        else:
            return 'DynamicTypeHandler'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this DynamicTypeHandler.
        The dynamic type handler.

        Allowed values for this property are: "RULE_TYPE_CONFIGS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this DynamicTypeHandler.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this DynamicTypeHandler.
        The dynamic type handler.


        :param model_type: The model_type of this DynamicTypeHandler.
        :type: str
        """
        allowed_values = ["RULE_TYPE_CONFIGS"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

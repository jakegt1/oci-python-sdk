# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateImagePolicyConfigDetails(object):
    """
    The properties that define a image verification policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateImagePolicyConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_policy_enabled:
            The value to assign to the is_policy_enabled property of this UpdateImagePolicyConfigDetails.
        :type is_policy_enabled: bool

        :param key_details:
            The value to assign to the key_details property of this UpdateImagePolicyConfigDetails.
        :type key_details: list[oci.container_engine.models.KeyDetails]

        """
        self.swagger_types = {
            'is_policy_enabled': 'bool',
            'key_details': 'list[KeyDetails]'
        }

        self.attribute_map = {
            'is_policy_enabled': 'isPolicyEnabled',
            'key_details': 'keyDetails'
        }

        self._is_policy_enabled = None
        self._key_details = None

    @property
    def is_policy_enabled(self):
        """
        Gets the is_policy_enabled of this UpdateImagePolicyConfigDetails.
        Whether the image verification policy is enabled. Defaults to false. If set to true, the images will be verified against the policy at runtime.


        :return: The is_policy_enabled of this UpdateImagePolicyConfigDetails.
        :rtype: bool
        """
        return self._is_policy_enabled

    @is_policy_enabled.setter
    def is_policy_enabled(self, is_policy_enabled):
        """
        Sets the is_policy_enabled of this UpdateImagePolicyConfigDetails.
        Whether the image verification policy is enabled. Defaults to false. If set to true, the images will be verified against the policy at runtime.


        :param is_policy_enabled: The is_policy_enabled of this UpdateImagePolicyConfigDetails.
        :type: bool
        """
        self._is_policy_enabled = is_policy_enabled

    @property
    def key_details(self):
        """
        Gets the key_details of this UpdateImagePolicyConfigDetails.
        A list of KMS key details.


        :return: The key_details of this UpdateImagePolicyConfigDetails.
        :rtype: list[oci.container_engine.models.KeyDetails]
        """
        return self._key_details

    @key_details.setter
    def key_details(self, key_details):
        """
        Sets the key_details of this UpdateImagePolicyConfigDetails.
        A list of KMS key details.


        :param key_details: The key_details of this UpdateImagePolicyConfigDetails.
        :type: list[oci.container_engine.models.KeyDetails]
        """
        self._key_details = key_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

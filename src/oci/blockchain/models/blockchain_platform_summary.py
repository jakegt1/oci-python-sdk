# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BlockchainPlatformSummary(object):
    """
    Blockchain Platform Instance Summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BlockchainPlatformSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BlockchainPlatformSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this BlockchainPlatformSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BlockchainPlatformSummary.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this BlockchainPlatformSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this BlockchainPlatformSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BlockchainPlatformSummary.
        :type time_updated: datetime

        :param platform_role:
            The value to assign to the platform_role property of this BlockchainPlatformSummary.
        :type platform_role: str

        :param compute_shape:
            The value to assign to the compute_shape property of this BlockchainPlatformSummary.
        :type compute_shape: str

        :param service_endpoint:
            The value to assign to the service_endpoint property of this BlockchainPlatformSummary.
        :type service_endpoint: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BlockchainPlatformSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this BlockchainPlatformSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BlockchainPlatformSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BlockchainPlatformSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'platform_role': 'str',
            'compute_shape': 'str',
            'service_endpoint': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'platform_role': 'platformRole',
            'compute_shape': 'computeShape',
            'service_endpoint': 'serviceEndpoint',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._platform_role = None
        self._compute_shape = None
        self._service_endpoint = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BlockchainPlatformSummary.
        unique identifier that is immutable on creation


        :return: The id of this BlockchainPlatformSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BlockchainPlatformSummary.
        unique identifier that is immutable on creation


        :param id: The id of this BlockchainPlatformSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BlockchainPlatformSummary.
        Platform Instance Display name, can be renamed


        :return: The display_name of this BlockchainPlatformSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BlockchainPlatformSummary.
        Platform Instance Display name, can be renamed


        :param display_name: The display_name of this BlockchainPlatformSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BlockchainPlatformSummary.
        Compartment Identifier


        :return: The compartment_id of this BlockchainPlatformSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BlockchainPlatformSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this BlockchainPlatformSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this BlockchainPlatformSummary.
        Platform Instance Description


        :return: The description of this BlockchainPlatformSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BlockchainPlatformSummary.
        Platform Instance Description


        :param description: The description of this BlockchainPlatformSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this BlockchainPlatformSummary.
        The time the the Platform Instance was created. An RFC3339 formatted datetime string


        :return: The time_created of this BlockchainPlatformSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BlockchainPlatformSummary.
        The time the the Platform Instance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this BlockchainPlatformSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BlockchainPlatformSummary.
        The time the Platform Instance was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this BlockchainPlatformSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BlockchainPlatformSummary.
        The time the Platform Instance was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this BlockchainPlatformSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def platform_role(self):
        """
        Gets the platform_role of this BlockchainPlatformSummary.
        Role of platform - founder or participant


        :return: The platform_role of this BlockchainPlatformSummary.
        :rtype: str
        """
        return self._platform_role

    @platform_role.setter
    def platform_role(self, platform_role):
        """
        Sets the platform_role of this BlockchainPlatformSummary.
        Role of platform - founder or participant


        :param platform_role: The platform_role of this BlockchainPlatformSummary.
        :type: str
        """
        self._platform_role = platform_role

    @property
    def compute_shape(self):
        """
        **[Required]** Gets the compute_shape of this BlockchainPlatformSummary.
        Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM


        :return: The compute_shape of this BlockchainPlatformSummary.
        :rtype: str
        """
        return self._compute_shape

    @compute_shape.setter
    def compute_shape(self, compute_shape):
        """
        Sets the compute_shape of this BlockchainPlatformSummary.
        Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM


        :param compute_shape: The compute_shape of this BlockchainPlatformSummary.
        :type: str
        """
        self._compute_shape = compute_shape

    @property
    def service_endpoint(self):
        """
        Gets the service_endpoint of this BlockchainPlatformSummary.
        Service endpoint URL, valid post-provisioning


        :return: The service_endpoint of this BlockchainPlatformSummary.
        :rtype: str
        """
        return self._service_endpoint

    @service_endpoint.setter
    def service_endpoint(self, service_endpoint):
        """
        Sets the service_endpoint of this BlockchainPlatformSummary.
        Service endpoint URL, valid post-provisioning


        :param service_endpoint: The service_endpoint of this BlockchainPlatformSummary.
        :type: str
        """
        self._service_endpoint = service_endpoint

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this BlockchainPlatformSummary.
        The current state of the Platform Instance.


        :return: The lifecycle_state of this BlockchainPlatformSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BlockchainPlatformSummary.
        The current state of the Platform Instance.


        :param lifecycle_state: The lifecycle_state of this BlockchainPlatformSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this BlockchainPlatformSummary.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this BlockchainPlatformSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this BlockchainPlatformSummary.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this BlockchainPlatformSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BlockchainPlatformSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this BlockchainPlatformSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BlockchainPlatformSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this BlockchainPlatformSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BlockchainPlatformSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this BlockchainPlatformSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BlockchainPlatformSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this BlockchainPlatformSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConfigurationSourceProviderDetails(object):
    """
    The details for creating a configuration source provider.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConfigurationSourceProviderDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.resource_manager.models.CreateGitlabAccessTokenConfigurationSourceProviderDetails`
        * :class:`~oci.resource_manager.models.CreateGithubAccessTokenConfigurationSourceProviderDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateConfigurationSourceProviderDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateConfigurationSourceProviderDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateConfigurationSourceProviderDetails.
        :type description: str

        :param config_source_provider_type:
            The value to assign to the config_source_provider_type property of this CreateConfigurationSourceProviderDetails.
        :type config_source_provider_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateConfigurationSourceProviderDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateConfigurationSourceProviderDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'config_source_provider_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'config_source_provider_type': 'configSourceProviderType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._config_source_provider_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configSourceProviderType']

        if type == 'GITLAB_ACCESS_TOKEN':
            return 'CreateGitlabAccessTokenConfigurationSourceProviderDetails'

        if type == 'GITHUB_ACCESS_TOKEN':
            return 'CreateGithubAccessTokenConfigurationSourceProviderDetails'
        else:
            return 'CreateConfigurationSourceProviderDetails'

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateConfigurationSourceProviderDetails.
        The `OCID`__ of the compartment where
        you want to create the configuration source provider.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateConfigurationSourceProviderDetails.
        The `OCID`__ of the compartment where
        you want to create the configuration source provider.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateConfigurationSourceProviderDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateConfigurationSourceProviderDetails.
        Human-readable name of the configuration source provider. Avoid entering confidential information.


        :return: The display_name of this CreateConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateConfigurationSourceProviderDetails.
        Human-readable name of the configuration source provider. Avoid entering confidential information.


        :param display_name: The display_name of this CreateConfigurationSourceProviderDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateConfigurationSourceProviderDetails.
        Description of the configuration source provider. Avoid entering confidential information.


        :return: The description of this CreateConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateConfigurationSourceProviderDetails.
        Description of the configuration source provider. Avoid entering confidential information.


        :param description: The description of this CreateConfigurationSourceProviderDetails.
        :type: str
        """
        self._description = description

    @property
    def config_source_provider_type(self):
        """
        **[Required]** Gets the config_source_provider_type of this CreateConfigurationSourceProviderDetails.
        The type of configuration source provider.
        The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab.
        The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.


        :return: The config_source_provider_type of this CreateConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._config_source_provider_type

    @config_source_provider_type.setter
    def config_source_provider_type(self, config_source_provider_type):
        """
        Sets the config_source_provider_type of this CreateConfigurationSourceProviderDetails.
        The type of configuration source provider.
        The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab.
        The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.


        :param config_source_provider_type: The config_source_provider_type of this CreateConfigurationSourceProviderDetails.
        :type: str
        """
        self._config_source_provider_type = config_source_provider_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateConfigurationSourceProviderDetails.
        Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateConfigurationSourceProviderDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateConfigurationSourceProviderDetails.
        Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateConfigurationSourceProviderDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateConfigurationSourceProviderDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateConfigurationSourceProviderDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateConfigurationSourceProviderDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateConfigurationSourceProviderDetails.
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

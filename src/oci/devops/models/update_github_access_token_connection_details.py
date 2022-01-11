# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGithubAccessTokenConnectionDetails(UpdateConnectionDetails):
    """
    The details for updating a connection of the type `GITHUB_ACCESS_TOKEN`.
    This type corresponds to a connection in GitHub that is authenticated with a personal access token.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateGithubAccessTokenConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateGithubAccessTokenConnectionDetails.connection_type` attribute
        of this class is ``GITHUB_ACCESS_TOKEN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateGithubAccessTokenConnectionDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateGithubAccessTokenConnectionDetails.
        :type display_name: str

        :param connection_type:
            The value to assign to the connection_type property of this UpdateGithubAccessTokenConnectionDetails.
        :type connection_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateGithubAccessTokenConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateGithubAccessTokenConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param access_token:
            The value to assign to the access_token property of this UpdateGithubAccessTokenConnectionDetails.
        :type access_token: str

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'connection_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'access_token': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'connection_type': 'connectionType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'access_token': 'accessToken'
        }

        self._description = None
        self._display_name = None
        self._connection_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._access_token = None
        self._connection_type = 'GITHUB_ACCESS_TOKEN'

    @property
    def access_token(self):
        """
        Gets the access_token of this UpdateGithubAccessTokenConnectionDetails.
        The OCID of personal access token saved in secret store.


        :return: The access_token of this UpdateGithubAccessTokenConnectionDetails.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this UpdateGithubAccessTokenConnectionDetails.
        The OCID of personal access token saved in secret store.


        :param access_token: The access_token of this UpdateGithubAccessTokenConnectionDetails.
        :type: str
        """
        self._access_token = access_token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

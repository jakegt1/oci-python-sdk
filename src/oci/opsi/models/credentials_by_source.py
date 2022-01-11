# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .credential_details import CredentialDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CredentialsBySource(CredentialDetails):
    """
    Credential Source to connect to the database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CredentialsBySource object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.CredentialsBySource.credential_type` attribute
        of this class is ``CREDENTIALS_BY_SOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_source_name:
            The value to assign to the credential_source_name property of this CredentialsBySource.
        :type credential_source_name: str

        :param credential_type:
            The value to assign to the credential_type property of this CredentialsBySource.
            Allowed values for this property are: "CREDENTIALS_BY_SOURCE"
        :type credential_type: str

        """
        self.swagger_types = {
            'credential_source_name': 'str',
            'credential_type': 'str'
        }

        self.attribute_map = {
            'credential_source_name': 'credentialSourceName',
            'credential_type': 'credentialType'
        }

        self._credential_source_name = None
        self._credential_type = None
        self._credential_type = 'CREDENTIALS_BY_SOURCE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

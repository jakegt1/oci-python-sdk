# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AzureDataLakeStorageConnection(Connection):
    """
    Represents the metadata of a Azure Data Lake Storage Connection.
    """

    #: A constant which can be used with the technology_type property of a AzureDataLakeStorageConnection.
    #: This constant has a value of "AZURE_DATA_LAKE_STORAGE"
    TECHNOLOGY_TYPE_AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"

    #: A constant which can be used with the authentication_type property of a AzureDataLakeStorageConnection.
    #: This constant has a value of "SHARED_KEY"
    AUTHENTICATION_TYPE_SHARED_KEY = "SHARED_KEY"

    #: A constant which can be used with the authentication_type property of a AzureDataLakeStorageConnection.
    #: This constant has a value of "SHARED_ACCESS_SIGNATURE"
    AUTHENTICATION_TYPE_SHARED_ACCESS_SIGNATURE = "SHARED_ACCESS_SIGNATURE"

    #: A constant which can be used with the authentication_type property of a AzureDataLakeStorageConnection.
    #: This constant has a value of "AZURE_ACTIVE_DIRECTORY"
    AUTHENTICATION_TYPE_AZURE_ACTIVE_DIRECTORY = "AZURE_ACTIVE_DIRECTORY"

    def __init__(self, **kwargs):
        """
        Initializes a new AzureDataLakeStorageConnection object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.AzureDataLakeStorageConnection.connection_type` attribute
        of this class is ``AZURE_DATA_LAKE_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this AzureDataLakeStorageConnection.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param id:
            The value to assign to the id property of this AzureDataLakeStorageConnection.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AzureDataLakeStorageConnection.
        :type display_name: str

        :param description:
            The value to assign to the description property of this AzureDataLakeStorageConnection.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AzureDataLakeStorageConnection.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AzureDataLakeStorageConnection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AzureDataLakeStorageConnection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AzureDataLakeStorageConnection.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AzureDataLakeStorageConnection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AzureDataLakeStorageConnection.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this AzureDataLakeStorageConnection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AzureDataLakeStorageConnection.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this AzureDataLakeStorageConnection.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this AzureDataLakeStorageConnection.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this AzureDataLakeStorageConnection.
        :type subnet_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this AzureDataLakeStorageConnection.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this AzureDataLakeStorageConnection.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this AzureDataLakeStorageConnection.
            Allowed values for this property are: "AZURE_DATA_LAKE_STORAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type technology_type: str

        :param authentication_type:
            The value to assign to the authentication_type property of this AzureDataLakeStorageConnection.
            Allowed values for this property are: "SHARED_KEY", "SHARED_ACCESS_SIGNATURE", "AZURE_ACTIVE_DIRECTORY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type authentication_type: str

        :param account_name:
            The value to assign to the account_name property of this AzureDataLakeStorageConnection.
        :type account_name: str

        :param azure_tenant_id:
            The value to assign to the azure_tenant_id property of this AzureDataLakeStorageConnection.
        :type azure_tenant_id: str

        :param client_id:
            The value to assign to the client_id property of this AzureDataLakeStorageConnection.
        :type client_id: str

        :param endpoint:
            The value to assign to the endpoint property of this AzureDataLakeStorageConnection.
        :type endpoint: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'technology_type': 'str',
            'authentication_type': 'str',
            'account_name': 'str',
            'azure_tenant_id': 'str',
            'client_id': 'str',
            'endpoint': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'technology_type': 'technologyType',
            'authentication_type': 'authenticationType',
            'account_name': 'accountName',
            'azure_tenant_id': 'azureTenantId',
            'client_id': 'clientId',
            'endpoint': 'endpoint'
        }

        self._connection_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._technology_type = None
        self._authentication_type = None
        self._account_name = None
        self._azure_tenant_id = None
        self._client_id = None
        self._endpoint = None
        self._connection_type = 'AZURE_DATA_LAKE_STORAGE'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this AzureDataLakeStorageConnection.
        The Azure Data Lake Storage technology type.

        Allowed values for this property are: "AZURE_DATA_LAKE_STORAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The technology_type of this AzureDataLakeStorageConnection.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this AzureDataLakeStorageConnection.
        The Azure Data Lake Storage technology type.


        :param technology_type: The technology_type of this AzureDataLakeStorageConnection.
        :type: str
        """
        allowed_values = ["AZURE_DATA_LAKE_STORAGE"]
        if not value_allowed_none_or_none_sentinel(technology_type, allowed_values):
            technology_type = 'UNKNOWN_ENUM_VALUE'
        self._technology_type = technology_type

    @property
    def authentication_type(self):
        """
        **[Required]** Gets the authentication_type of this AzureDataLakeStorageConnection.
        Used authentication mechanism to access Azure Data Lake Storage.

        Allowed values for this property are: "SHARED_KEY", "SHARED_ACCESS_SIGNATURE", "AZURE_ACTIVE_DIRECTORY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The authentication_type of this AzureDataLakeStorageConnection.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """
        Sets the authentication_type of this AzureDataLakeStorageConnection.
        Used authentication mechanism to access Azure Data Lake Storage.


        :param authentication_type: The authentication_type of this AzureDataLakeStorageConnection.
        :type: str
        """
        allowed_values = ["SHARED_KEY", "SHARED_ACCESS_SIGNATURE", "AZURE_ACTIVE_DIRECTORY"]
        if not value_allowed_none_or_none_sentinel(authentication_type, allowed_values):
            authentication_type = 'UNKNOWN_ENUM_VALUE'
        self._authentication_type = authentication_type

    @property
    def account_name(self):
        """
        **[Required]** Gets the account_name of this AzureDataLakeStorageConnection.
        Sets the Azure storage account name.


        :return: The account_name of this AzureDataLakeStorageConnection.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """
        Sets the account_name of this AzureDataLakeStorageConnection.
        Sets the Azure storage account name.


        :param account_name: The account_name of this AzureDataLakeStorageConnection.
        :type: str
        """
        self._account_name = account_name

    @property
    def azure_tenant_id(self):
        """
        Gets the azure_tenant_id of this AzureDataLakeStorageConnection.
        Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
        e.g.: 14593954-d337-4a61-a364-9f758c64f97f


        :return: The azure_tenant_id of this AzureDataLakeStorageConnection.
        :rtype: str
        """
        return self._azure_tenant_id

    @azure_tenant_id.setter
    def azure_tenant_id(self, azure_tenant_id):
        """
        Sets the azure_tenant_id of this AzureDataLakeStorageConnection.
        Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
        e.g.: 14593954-d337-4a61-a364-9f758c64f97f


        :param azure_tenant_id: The azure_tenant_id of this AzureDataLakeStorageConnection.
        :type: str
        """
        self._azure_tenant_id = azure_tenant_id

    @property
    def client_id(self):
        """
        Gets the client_id of this AzureDataLakeStorageConnection.
        Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
        e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d


        :return: The client_id of this AzureDataLakeStorageConnection.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this AzureDataLakeStorageConnection.
        Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
        e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d


        :param client_id: The client_id of this AzureDataLakeStorageConnection.
        :type: str
        """
        self._client_id = client_id

    @property
    def endpoint(self):
        """
        Gets the endpoint of this AzureDataLakeStorageConnection.
        Azure Storage service endpoint.
        e.g: https://test.blob.core.windows.net


        :return: The endpoint of this AzureDataLakeStorageConnection.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this AzureDataLakeStorageConnection.
        Azure Storage service endpoint.
        e.g: https://test.blob.core.windows.net


        :param endpoint: The endpoint of this AzureDataLakeStorageConnection.
        :type: str
        """
        self._endpoint = endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
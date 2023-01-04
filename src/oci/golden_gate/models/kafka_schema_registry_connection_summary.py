# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection_summary import ConnectionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KafkaSchemaRegistryConnectionSummary(ConnectionSummary):
    """
    Summary of the Kafka (e.g. Confluent) Schema Registry Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KafkaSchemaRegistryConnectionSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.KafkaSchemaRegistryConnectionSummary.connection_type` attribute
        of this class is ``KAFKA_SCHEMA_REGISTRY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this KafkaSchemaRegistryConnectionSummary.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS"
        :type connection_type: str

        :param id:
            The value to assign to the id property of this KafkaSchemaRegistryConnectionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this KafkaSchemaRegistryConnectionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this KafkaSchemaRegistryConnectionSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this KafkaSchemaRegistryConnectionSummary.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this KafkaSchemaRegistryConnectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this KafkaSchemaRegistryConnectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this KafkaSchemaRegistryConnectionSummary.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this KafkaSchemaRegistryConnectionSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this KafkaSchemaRegistryConnectionSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this KafkaSchemaRegistryConnectionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this KafkaSchemaRegistryConnectionSummary.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this KafkaSchemaRegistryConnectionSummary.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this KafkaSchemaRegistryConnectionSummary.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this KafkaSchemaRegistryConnectionSummary.
        :type subnet_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this KafkaSchemaRegistryConnectionSummary.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this KafkaSchemaRegistryConnectionSummary.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this KafkaSchemaRegistryConnectionSummary.
        :type technology_type: str

        :param url:
            The value to assign to the url property of this KafkaSchemaRegistryConnectionSummary.
        :type url: str

        :param authentication_type:
            The value to assign to the authentication_type property of this KafkaSchemaRegistryConnectionSummary.
        :type authentication_type: str

        :param username:
            The value to assign to the username property of this KafkaSchemaRegistryConnectionSummary.
        :type username: str

        :param private_ip:
            The value to assign to the private_ip property of this KafkaSchemaRegistryConnectionSummary.
        :type private_ip: str

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
            'url': 'str',
            'authentication_type': 'str',
            'username': 'str',
            'private_ip': 'str'
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
            'url': 'url',
            'authentication_type': 'authenticationType',
            'username': 'username',
            'private_ip': 'privateIp'
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
        self._url = None
        self._authentication_type = None
        self._username = None
        self._private_ip = None
        self._connection_type = 'KAFKA_SCHEMA_REGISTRY'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this KafkaSchemaRegistryConnectionSummary.
        The Kafka (e.g. Confluent) Schema Registry technology type.


        :return: The technology_type of this KafkaSchemaRegistryConnectionSummary.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this KafkaSchemaRegistryConnectionSummary.
        The Kafka (e.g. Confluent) Schema Registry technology type.


        :param technology_type: The technology_type of this KafkaSchemaRegistryConnectionSummary.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def url(self):
        """
        **[Required]** Gets the url of this KafkaSchemaRegistryConnectionSummary.
        Kafka Schema Registry URL.
        e.g.: 'https://server1.us.oracle.com:8081'


        :return: The url of this KafkaSchemaRegistryConnectionSummary.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this KafkaSchemaRegistryConnectionSummary.
        Kafka Schema Registry URL.
        e.g.: 'https://server1.us.oracle.com:8081'


        :param url: The url of this KafkaSchemaRegistryConnectionSummary.
        :type: str
        """
        self._url = url

    @property
    def authentication_type(self):
        """
        **[Required]** Gets the authentication_type of this KafkaSchemaRegistryConnectionSummary.
        Used authentication mechanism to access Schema Registry.


        :return: The authentication_type of this KafkaSchemaRegistryConnectionSummary.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """
        Sets the authentication_type of this KafkaSchemaRegistryConnectionSummary.
        Used authentication mechanism to access Schema Registry.


        :param authentication_type: The authentication_type of this KafkaSchemaRegistryConnectionSummary.
        :type: str
        """
        self._authentication_type = authentication_type

    @property
    def username(self):
        """
        Gets the username of this KafkaSchemaRegistryConnectionSummary.
        The username to access Schema Registry using basic authentation.
        This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.


        :return: The username of this KafkaSchemaRegistryConnectionSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this KafkaSchemaRegistryConnectionSummary.
        The username to access Schema Registry using basic authentation.
        This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.


        :param username: The username of this KafkaSchemaRegistryConnectionSummary.
        :type: str
        """
        self._username = username

    @property
    def private_ip(self):
        """
        Gets the private_ip of this KafkaSchemaRegistryConnectionSummary.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this KafkaSchemaRegistryConnectionSummary.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this KafkaSchemaRegistryConnectionSummary.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this KafkaSchemaRegistryConnectionSummary.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
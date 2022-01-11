# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousVmClusterSummary(object):
    """
    Details of the Autonomous VM cluster.
    """

    #: A constant which can be used with the lifecycle_state property of a AutonomousVmClusterSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVmClusterSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVmClusterSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVmClusterSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVmClusterSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVmClusterSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousVmClusterSummary.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the license_model property of a AutonomousVmClusterSummary.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a AutonomousVmClusterSummary.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousVmClusterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousVmClusterSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AutonomousVmClusterSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this AutonomousVmClusterSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this AutonomousVmClusterSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousVmClusterSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousVmClusterSummary.
        :type lifecycle_details: str

        :param time_zone:
            The value to assign to the time_zone property of this AutonomousVmClusterSummary.
        :type time_zone: str

        :param exadata_infrastructure_id:
            The value to assign to the exadata_infrastructure_id property of this AutonomousVmClusterSummary.
        :type exadata_infrastructure_id: str

        :param vm_cluster_network_id:
            The value to assign to the vm_cluster_network_id property of this AutonomousVmClusterSummary.
        :type vm_cluster_network_id: str

        :param is_local_backup_enabled:
            The value to assign to the is_local_backup_enabled property of this AutonomousVmClusterSummary.
        :type is_local_backup_enabled: bool

        :param cpus_enabled:
            The value to assign to the cpus_enabled property of this AutonomousVmClusterSummary.
        :type cpus_enabled: int

        :param ocpus_enabled:
            The value to assign to the ocpus_enabled property of this AutonomousVmClusterSummary.
        :type ocpus_enabled: float

        :param available_cpus:
            The value to assign to the available_cpus property of this AutonomousVmClusterSummary.
        :type available_cpus: int

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this AutonomousVmClusterSummary.
        :type memory_size_in_gbs: int

        :param db_node_storage_size_in_gbs:
            The value to assign to the db_node_storage_size_in_gbs property of this AutonomousVmClusterSummary.
        :type db_node_storage_size_in_gbs: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this AutonomousVmClusterSummary.
        :type data_storage_size_in_tbs: float

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this AutonomousVmClusterSummary.
        :type data_storage_size_in_gbs: float

        :param available_data_storage_size_in_tbs:
            The value to assign to the available_data_storage_size_in_tbs property of this AutonomousVmClusterSummary.
        :type available_data_storage_size_in_tbs: float

        :param license_model:
            The value to assign to the license_model property of this AutonomousVmClusterSummary.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutonomousVmClusterSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AutonomousVmClusterSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_zone': 'str',
            'exadata_infrastructure_id': 'str',
            'vm_cluster_network_id': 'str',
            'is_local_backup_enabled': 'bool',
            'cpus_enabled': 'int',
            'ocpus_enabled': 'float',
            'available_cpus': 'int',
            'memory_size_in_gbs': 'int',
            'db_node_storage_size_in_gbs': 'int',
            'data_storage_size_in_tbs': 'float',
            'data_storage_size_in_gbs': 'float',
            'available_data_storage_size_in_tbs': 'float',
            'license_model': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_zone': 'timeZone',
            'exadata_infrastructure_id': 'exadataInfrastructureId',
            'vm_cluster_network_id': 'vmClusterNetworkId',
            'is_local_backup_enabled': 'isLocalBackupEnabled',
            'cpus_enabled': 'cpusEnabled',
            'ocpus_enabled': 'ocpusEnabled',
            'available_cpus': 'availableCpus',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'db_node_storage_size_in_gbs': 'dbNodeStorageSizeInGBs',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'available_data_storage_size_in_tbs': 'availableDataStorageSizeInTBs',
            'license_model': 'licenseModel',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_zone = None
        self._exadata_infrastructure_id = None
        self._vm_cluster_network_id = None
        self._is_local_backup_enabled = None
        self._cpus_enabled = None
        self._ocpus_enabled = None
        self._available_cpus = None
        self._memory_size_in_gbs = None
        self._db_node_storage_size_in_gbs = None
        self._data_storage_size_in_tbs = None
        self._data_storage_size_in_gbs = None
        self._available_data_storage_size_in_tbs = None
        self._license_model = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousVmClusterSummary.
        The `OCID`__ of the Autonomous VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AutonomousVmClusterSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousVmClusterSummary.
        The `OCID`__ of the Autonomous VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AutonomousVmClusterSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AutonomousVmClusterSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AutonomousVmClusterSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AutonomousVmClusterSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AutonomousVmClusterSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AutonomousVmClusterSummary.
        The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.


        :return: The display_name of this AutonomousVmClusterSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutonomousVmClusterSummary.
        The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.


        :param display_name: The display_name of this AutonomousVmClusterSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this AutonomousVmClusterSummary.
        The date and time that the Autonomous VM cluster was created.


        :return: The time_created of this AutonomousVmClusterSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutonomousVmClusterSummary.
        The date and time that the Autonomous VM cluster was created.


        :param time_created: The time_created of this AutonomousVmClusterSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousVmClusterSummary.
        The current state of the Autonomous VM cluster.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousVmClusterSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousVmClusterSummary.
        The current state of the Autonomous VM cluster.


        :param lifecycle_state: The lifecycle_state of this AutonomousVmClusterSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousVmClusterSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this AutonomousVmClusterSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousVmClusterSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this AutonomousVmClusterSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_zone(self):
        """
        Gets the time_zone of this AutonomousVmClusterSummary.
        The time zone to use for the Autonomous VM cluster. For details, see `DB System Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this AutonomousVmClusterSummary.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this AutonomousVmClusterSummary.
        The time zone to use for the Autonomous VM cluster. For details, see `DB System Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this AutonomousVmClusterSummary.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def exadata_infrastructure_id(self):
        """
        **[Required]** Gets the exadata_infrastructure_id of this AutonomousVmClusterSummary.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exadata_infrastructure_id of this AutonomousVmClusterSummary.
        :rtype: str
        """
        return self._exadata_infrastructure_id

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, exadata_infrastructure_id):
        """
        Sets the exadata_infrastructure_id of this AutonomousVmClusterSummary.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exadata_infrastructure_id: The exadata_infrastructure_id of this AutonomousVmClusterSummary.
        :type: str
        """
        self._exadata_infrastructure_id = exadata_infrastructure_id

    @property
    def vm_cluster_network_id(self):
        """
        **[Required]** Gets the vm_cluster_network_id of this AutonomousVmClusterSummary.
        The `OCID`__ of the VM cluster network.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vm_cluster_network_id of this AutonomousVmClusterSummary.
        :rtype: str
        """
        return self._vm_cluster_network_id

    @vm_cluster_network_id.setter
    def vm_cluster_network_id(self, vm_cluster_network_id):
        """
        Sets the vm_cluster_network_id of this AutonomousVmClusterSummary.
        The `OCID`__ of the VM cluster network.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vm_cluster_network_id: The vm_cluster_network_id of this AutonomousVmClusterSummary.
        :type: str
        """
        self._vm_cluster_network_id = vm_cluster_network_id

    @property
    def is_local_backup_enabled(self):
        """
        Gets the is_local_backup_enabled of this AutonomousVmClusterSummary.
        If true, database backup on local Exadata storage is configured for the Autonomous VM cluster. If false, database backup on local Exadata storage is not available in the Autonomous VM cluster.


        :return: The is_local_backup_enabled of this AutonomousVmClusterSummary.
        :rtype: bool
        """
        return self._is_local_backup_enabled

    @is_local_backup_enabled.setter
    def is_local_backup_enabled(self, is_local_backup_enabled):
        """
        Sets the is_local_backup_enabled of this AutonomousVmClusterSummary.
        If true, database backup on local Exadata storage is configured for the Autonomous VM cluster. If false, database backup on local Exadata storage is not available in the Autonomous VM cluster.


        :param is_local_backup_enabled: The is_local_backup_enabled of this AutonomousVmClusterSummary.
        :type: bool
        """
        self._is_local_backup_enabled = is_local_backup_enabled

    @property
    def cpus_enabled(self):
        """
        Gets the cpus_enabled of this AutonomousVmClusterSummary.
        The number of enabled CPU cores.


        :return: The cpus_enabled of this AutonomousVmClusterSummary.
        :rtype: int
        """
        return self._cpus_enabled

    @cpus_enabled.setter
    def cpus_enabled(self, cpus_enabled):
        """
        Sets the cpus_enabled of this AutonomousVmClusterSummary.
        The number of enabled CPU cores.


        :param cpus_enabled: The cpus_enabled of this AutonomousVmClusterSummary.
        :type: int
        """
        self._cpus_enabled = cpus_enabled

    @property
    def ocpus_enabled(self):
        """
        Gets the ocpus_enabled of this AutonomousVmClusterSummary.
        The number of enabled OCPU cores.


        :return: The ocpus_enabled of this AutonomousVmClusterSummary.
        :rtype: float
        """
        return self._ocpus_enabled

    @ocpus_enabled.setter
    def ocpus_enabled(self, ocpus_enabled):
        """
        Sets the ocpus_enabled of this AutonomousVmClusterSummary.
        The number of enabled OCPU cores.


        :param ocpus_enabled: The ocpus_enabled of this AutonomousVmClusterSummary.
        :type: float
        """
        self._ocpus_enabled = ocpus_enabled

    @property
    def available_cpus(self):
        """
        Gets the available_cpus of this AutonomousVmClusterSummary.
        The numnber of CPU cores available.


        :return: The available_cpus of this AutonomousVmClusterSummary.
        :rtype: int
        """
        return self._available_cpus

    @available_cpus.setter
    def available_cpus(self, available_cpus):
        """
        Sets the available_cpus of this AutonomousVmClusterSummary.
        The numnber of CPU cores available.


        :param available_cpus: The available_cpus of this AutonomousVmClusterSummary.
        :type: int
        """
        self._available_cpus = available_cpus

    @property
    def memory_size_in_gbs(self):
        """
        Gets the memory_size_in_gbs of this AutonomousVmClusterSummary.
        The memory allocated in GBs.


        :return: The memory_size_in_gbs of this AutonomousVmClusterSummary.
        :rtype: int
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this AutonomousVmClusterSummary.
        The memory allocated in GBs.


        :param memory_size_in_gbs: The memory_size_in_gbs of this AutonomousVmClusterSummary.
        :type: int
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def db_node_storage_size_in_gbs(self):
        """
        Gets the db_node_storage_size_in_gbs of this AutonomousVmClusterSummary.
        The local node storage allocated in GBs.


        :return: The db_node_storage_size_in_gbs of this AutonomousVmClusterSummary.
        :rtype: int
        """
        return self._db_node_storage_size_in_gbs

    @db_node_storage_size_in_gbs.setter
    def db_node_storage_size_in_gbs(self, db_node_storage_size_in_gbs):
        """
        Sets the db_node_storage_size_in_gbs of this AutonomousVmClusterSummary.
        The local node storage allocated in GBs.


        :param db_node_storage_size_in_gbs: The db_node_storage_size_in_gbs of this AutonomousVmClusterSummary.
        :type: int
        """
        self._db_node_storage_size_in_gbs = db_node_storage_size_in_gbs

    @property
    def data_storage_size_in_tbs(self):
        """
        Gets the data_storage_size_in_tbs of this AutonomousVmClusterSummary.
        The total data storage allocated in TBs


        :return: The data_storage_size_in_tbs of this AutonomousVmClusterSummary.
        :rtype: float
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this AutonomousVmClusterSummary.
        The total data storage allocated in TBs


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this AutonomousVmClusterSummary.
        :type: float
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this AutonomousVmClusterSummary.
        The total data storage allocated in GBs


        :return: The data_storage_size_in_gbs of this AutonomousVmClusterSummary.
        :rtype: float
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this AutonomousVmClusterSummary.
        The total data storage allocated in GBs


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this AutonomousVmClusterSummary.
        :type: float
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def available_data_storage_size_in_tbs(self):
        """
        Gets the available_data_storage_size_in_tbs of this AutonomousVmClusterSummary.
        The data storage available in TBs


        :return: The available_data_storage_size_in_tbs of this AutonomousVmClusterSummary.
        :rtype: float
        """
        return self._available_data_storage_size_in_tbs

    @available_data_storage_size_in_tbs.setter
    def available_data_storage_size_in_tbs(self, available_data_storage_size_in_tbs):
        """
        Sets the available_data_storage_size_in_tbs of this AutonomousVmClusterSummary.
        The data storage available in TBs


        :param available_data_storage_size_in_tbs: The available_data_storage_size_in_tbs of this AutonomousVmClusterSummary.
        :type: float
        """
        self._available_data_storage_size_in_tbs = available_data_storage_size_in_tbs

    @property
    def license_model(self):
        """
        Gets the license_model of this AutonomousVmClusterSummary.
        The Oracle license model that applies to the Autonomous VM cluster. The default is LICENSE_INCLUDED.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this AutonomousVmClusterSummary.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this AutonomousVmClusterSummary.
        The Oracle license model that applies to the Autonomous VM cluster. The default is LICENSE_INCLUDED.


        :param license_model: The license_model of this AutonomousVmClusterSummary.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AutonomousVmClusterSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AutonomousVmClusterSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AutonomousVmClusterSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AutonomousVmClusterSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AutonomousVmClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AutonomousVmClusterSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AutonomousVmClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AutonomousVmClusterSummary.
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

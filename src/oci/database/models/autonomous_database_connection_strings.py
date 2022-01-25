# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseConnectionStrings(object):
    """
    Connection strings to connect to an Oracle Autonomous Database.

    Example output for connection strings. See :func:`database_connection_string_profile` for additional details:

    \t\"connectionStrings\": {
    \"allConnectionStrings\": {
    \"HIGH\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_high.adwc.oraclecloud.com\",
    \"LOW\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_low.adwc.oraclecloud.com\",
    \"MEDIUM\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_medium.adwc.oraclecloud.com\"
    },
    \"profiles\": [
    {
    \"displayName\": \"databasename_high\",
    \"value\": \"(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.region.oraclecloud.com))(connect_data=(service_name=unique_id_databasename_high.adwc.oraclecloud.com))(security=(ssl_server_cert_dn=\"CN=adwc.uscom-east-1.oraclecloud.com,OU=Oracle BMCS US,O=Oracle Corporation,L=Redwood City,ST=California,C=US\")))\",
    \"consumerGroup\": \"HIGH\",
    \"protocol\": \"TCPS\",
    \"tlsAuthentication\": \"MUTUAL\",
    \"hostFormat\": \"FQDN\",
    \"sessionMode\": \"DIRECT\",
    \"syntaxFormat\": \"LONG\"
    },
    {
    \"displayName\": \"databasename_low\",
    \"value\": \"(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.region.oraclecloud.com))(connect_data=(service_name=unique_id_databasename_low.adwc.oraclecloud.com))(security=(ssl_server_cert_dn=\"CN=adwc.uscom-east-1.oraclecloud.com,OU=Oracle BMCS US,O=Oracle Corporation,L=Redwood City,ST=California,C=US\")))\",
    \"consumerGroup\": \"LOW\",
    \"protocol\": \"TCPS\",
    \"tlsAuthentication\": \"MUTUAL\",
    \"hostFormat\": \"FQDN\",
    \"sessionMode\": \"DIRECT\",
    \"syntaxFormat\": \"LONG\"
    },
    {
    \"displayName\": \"databasename_medium\",
    \"value\": \"(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.region.oraclecloud.com))(connect_data=(service_name=unique_id_databasename_medium.adwc.oraclecloud.com))(security=(ssl_server_cert_dn=\"CN=adwc.uscom-east-1.oraclecloud.com,OU=Oracle BMCS US,O=Oracle Corporation,L=Redwood City,ST=California,C=US\")))\",
    \"consumerGroup\": \"MEDIUM\",
    \"protocol\": \"TCPS\",
    \"tlsAuthentication\": \"MUTUAL\",
    \"hostFormat\": \"FQDN\",
    \"sessionMode\": \"DIRECT\",
    \"syntaxFormat\": \"LONG\"
    }
    ],
    \"dedicated\": null,
    \"high\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_high.adwc.oraclecloud.com\",
    \"low\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_low.adwc.oraclecloud.com\",
    \"medium\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_medium.adwc.oraclecloud.com\"
    }
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseConnectionStrings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param high:
            The value to assign to the high property of this AutonomousDatabaseConnectionStrings.
        :type high: str

        :param medium:
            The value to assign to the medium property of this AutonomousDatabaseConnectionStrings.
        :type medium: str

        :param low:
            The value to assign to the low property of this AutonomousDatabaseConnectionStrings.
        :type low: str

        :param dedicated:
            The value to assign to the dedicated property of this AutonomousDatabaseConnectionStrings.
        :type dedicated: str

        :param all_connection_strings:
            The value to assign to the all_connection_strings property of this AutonomousDatabaseConnectionStrings.
        :type all_connection_strings: dict(str, str)

        :param profiles:
            The value to assign to the profiles property of this AutonomousDatabaseConnectionStrings.
        :type profiles: list[oci.database.models.DatabaseConnectionStringProfile]

        """
        self.swagger_types = {
            'high': 'str',
            'medium': 'str',
            'low': 'str',
            'dedicated': 'str',
            'all_connection_strings': 'dict(str, str)',
            'profiles': 'list[DatabaseConnectionStringProfile]'
        }

        self.attribute_map = {
            'high': 'high',
            'medium': 'medium',
            'low': 'low',
            'dedicated': 'dedicated',
            'all_connection_strings': 'allConnectionStrings',
            'profiles': 'profiles'
        }

        self._high = None
        self._medium = None
        self._low = None
        self._dedicated = None
        self._all_connection_strings = None
        self._profiles = None

    @property
    def high(self):
        """
        Gets the high of this AutonomousDatabaseConnectionStrings.
        The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but supports the fewest number of concurrent SQL statements.


        :return: The high of this AutonomousDatabaseConnectionStrings.
        :rtype: str
        """
        return self._high

    @high.setter
    def high(self, high):
        """
        Sets the high of this AutonomousDatabaseConnectionStrings.
        The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but supports the fewest number of concurrent SQL statements.


        :param high: The high of this AutonomousDatabaseConnectionStrings.
        :type: str
        """
        self._high = high

    @property
    def medium(self):
        """
        Gets the medium of this AutonomousDatabaseConnectionStrings.
        The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of performance, but supports more concurrent SQL statements.


        :return: The medium of this AutonomousDatabaseConnectionStrings.
        :rtype: str
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """
        Sets the medium of this AutonomousDatabaseConnectionStrings.
        The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of performance, but supports more concurrent SQL statements.


        :param medium: The medium of this AutonomousDatabaseConnectionStrings.
        :type: str
        """
        self._medium = medium

    @property
    def low(self):
        """
        Gets the low of this AutonomousDatabaseConnectionStrings.
        The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.


        :return: The low of this AutonomousDatabaseConnectionStrings.
        :rtype: str
        """
        return self._low

    @low.setter
    def low(self, low):
        """
        Sets the low of this AutonomousDatabaseConnectionStrings.
        The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.


        :param low: The low of this AutonomousDatabaseConnectionStrings.
        :type: str
        """
        self._low = low

    @property
    def dedicated(self):
        """
        Gets the dedicated of this AutonomousDatabaseConnectionStrings.
        The database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.


        :return: The dedicated of this AutonomousDatabaseConnectionStrings.
        :rtype: str
        """
        return self._dedicated

    @dedicated.setter
    def dedicated(self, dedicated):
        """
        Sets the dedicated of this AutonomousDatabaseConnectionStrings.
        The database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.


        :param dedicated: The dedicated of this AutonomousDatabaseConnectionStrings.
        :type: str
        """
        self._dedicated = dedicated

    @property
    def all_connection_strings(self):
        """
        Gets the all_connection_strings of this AutonomousDatabaseConnectionStrings.
        Returns all connection strings that can be used to connect to the Autonomous Database.
        For more information, please see `Predefined Database Service Names for Autonomous Transaction Processing`__

        __ https://docs.oracle.com/en/cloud/paas/atp-cloud/atpug/connect-predefined.html#GUID-9747539B-FD46-44F1-8FF8-F5AC650F15BE


        :return: The all_connection_strings of this AutonomousDatabaseConnectionStrings.
        :rtype: dict(str, str)
        """
        return self._all_connection_strings

    @all_connection_strings.setter
    def all_connection_strings(self, all_connection_strings):
        """
        Sets the all_connection_strings of this AutonomousDatabaseConnectionStrings.
        Returns all connection strings that can be used to connect to the Autonomous Database.
        For more information, please see `Predefined Database Service Names for Autonomous Transaction Processing`__

        __ https://docs.oracle.com/en/cloud/paas/atp-cloud/atpug/connect-predefined.html#GUID-9747539B-FD46-44F1-8FF8-F5AC650F15BE


        :param all_connection_strings: The all_connection_strings of this AutonomousDatabaseConnectionStrings.
        :type: dict(str, str)
        """
        self._all_connection_strings = all_connection_strings

    @property
    def profiles(self):
        """
        Gets the profiles of this AutonomousDatabaseConnectionStrings.
        A list of connection string profiles to allow clients to group, filter and select connection string values based on structured metadata.


        :return: The profiles of this AutonomousDatabaseConnectionStrings.
        :rtype: list[oci.database.models.DatabaseConnectionStringProfile]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this AutonomousDatabaseConnectionStrings.
        A list of connection string profiles to allow clients to group, filter and select connection string values based on structured metadata.


        :param profiles: The profiles of this AutonomousDatabaseConnectionStrings.
        :type: list[oci.database.models.DatabaseConnectionStringProfile]
        """
        self._profiles = profiles

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectDescriptor(object):
    """
    Connect Descriptor details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectDescriptor object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host:
            The value to assign to the host property of this ConnectDescriptor.
        :type host: str

        :param port:
            The value to assign to the port property of this ConnectDescriptor.
        :type port: int

        :param database_service_name:
            The value to assign to the database_service_name property of this ConnectDescriptor.
        :type database_service_name: str

        :param connect_string:
            The value to assign to the connect_string property of this ConnectDescriptor.
        :type connect_string: str

        """
        self.swagger_types = {
            'host': 'str',
            'port': 'int',
            'database_service_name': 'str',
            'connect_string': 'str'
        }

        self.attribute_map = {
            'host': 'host',
            'port': 'port',
            'database_service_name': 'databaseServiceName',
            'connect_string': 'connectString'
        }

        self._host = None
        self._port = None
        self._database_service_name = None
        self._connect_string = None

    @property
    def host(self):
        """
        Gets the host of this ConnectDescriptor.
        Host of the connect descriptor.


        :return: The host of this ConnectDescriptor.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this ConnectDescriptor.
        Host of the connect descriptor.


        :param host: The host of this ConnectDescriptor.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this ConnectDescriptor.
        Port of the connect descriptor.


        :return: The port of this ConnectDescriptor.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ConnectDescriptor.
        Port of the connect descriptor.


        :param port: The port of this ConnectDescriptor.
        :type: int
        """
        self._port = port

    @property
    def database_service_name(self):
        """
        Gets the database_service_name of this ConnectDescriptor.
        Database service name.


        :return: The database_service_name of this ConnectDescriptor.
        :rtype: str
        """
        return self._database_service_name

    @database_service_name.setter
    def database_service_name(self, database_service_name):
        """
        Sets the database_service_name of this ConnectDescriptor.
        Database service name.


        :param database_service_name: The database_service_name of this ConnectDescriptor.
        :type: str
        """
        self._database_service_name = database_service_name

    @property
    def connect_string(self):
        """
        Gets the connect_string of this ConnectDescriptor.
        Connect string.


        :return: The connect_string of this ConnectDescriptor.
        :rtype: str
        """
        return self._connect_string

    @connect_string.setter
    def connect_string(self, connect_string):
        """
        Sets the connect_string of this ConnectDescriptor.
        Connect string.


        :param connect_string: The connect_string of this ConnectDescriptor.
        :type: str
        """
        self._connect_string = connect_string

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionDetails(object):
    """
    Connection details to connect to the database. HostName, protocol, and port should be specified.
    """

    #: A constant which can be used with the protocol property of a ConnectionDetails.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the protocol property of a ConnectionDetails.
    #: This constant has a value of "TCPS"
    PROTOCOL_TCPS = "TCPS"

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host_name:
            The value to assign to the host_name property of this ConnectionDetails.
        :type host_name: str

        :param protocol:
            The value to assign to the protocol property of this ConnectionDetails.
            Allowed values for this property are: "TCP", "TCPS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param port:
            The value to assign to the port property of this ConnectionDetails.
        :type port: int

        :param service_name:
            The value to assign to the service_name property of this ConnectionDetails.
        :type service_name: str

        """
        self.swagger_types = {
            'host_name': 'str',
            'protocol': 'str',
            'port': 'int',
            'service_name': 'str'
        }

        self.attribute_map = {
            'host_name': 'hostName',
            'protocol': 'protocol',
            'port': 'port',
            'service_name': 'serviceName'
        }

        self._host_name = None
        self._protocol = None
        self._port = None
        self._service_name = None

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this ConnectionDetails.
        Name of the listener host that will be used to create the connect string to the database.


        :return: The host_name of this ConnectionDetails.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this ConnectionDetails.
        Name of the listener host that will be used to create the connect string to the database.


        :param host_name: The host_name of this ConnectionDetails.
        :type: str
        """
        self._host_name = host_name

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this ConnectionDetails.
        Protocol used for connection requests.

        Allowed values for this property are: "TCP", "TCPS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this ConnectionDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this ConnectionDetails.
        Protocol used for connection requests.


        :param protocol: The protocol of this ConnectionDetails.
        :type: str
        """
        allowed_values = ["TCP", "TCPS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def port(self):
        """
        **[Required]** Gets the port of this ConnectionDetails.
        Listener port number used for connection requests.


        :return: The port of this ConnectionDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ConnectionDetails.
        Listener port number used for connection requests.


        :param port: The port of this ConnectionDetails.
        :type: int
        """
        self._port = port

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this ConnectionDetails.
        Service name used for connection requests.


        :return: The service_name of this ConnectionDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this ConnectionDetails.
        Service name used for connection requests.


        :param service_name: The service_name of this ConnectionDetails.
        :type: str
        """
        self._service_name = service_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

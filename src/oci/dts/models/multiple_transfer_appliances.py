# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MultipleTransferAppliances(object):
    """
    MultipleTransferAppliances model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MultipleTransferAppliances object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param transfer_appliance_objects:
            The value to assign to the transfer_appliance_objects property of this MultipleTransferAppliances.
        :type transfer_appliance_objects: list[oci.dts.models.TransferApplianceSummary]

        """
        self.swagger_types = {
            'transfer_appliance_objects': 'list[TransferApplianceSummary]'
        }

        self.attribute_map = {
            'transfer_appliance_objects': 'transferApplianceObjects'
        }

        self._transfer_appliance_objects = None

    @property
    def transfer_appliance_objects(self):
        """
        Gets the transfer_appliance_objects of this MultipleTransferAppliances.
        List of TransferAppliance summary's


        :return: The transfer_appliance_objects of this MultipleTransferAppliances.
        :rtype: list[oci.dts.models.TransferApplianceSummary]
        """
        return self._transfer_appliance_objects

    @transfer_appliance_objects.setter
    def transfer_appliance_objects(self, transfer_appliance_objects):
        """
        Sets the transfer_appliance_objects of this MultipleTransferAppliances.
        List of TransferAppliance summary's


        :param transfer_appliance_objects: The transfer_appliance_objects of this MultipleTransferAppliances.
        :type: list[oci.dts.models.TransferApplianceSummary]
        """
        self._transfer_appliance_objects = transfer_appliance_objects

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

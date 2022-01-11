# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_data_asset_details import UpdateDataAssetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDataAssetFromAmazonS3(UpdateDataAssetDetails):
    """
    Details for the Amazon s3 data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDataAssetFromAmazonS3 object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.UpdateDataAssetFromAmazonS3.model_type` attribute
        of this class is ``AMAZON_S3_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this UpdateDataAssetFromAmazonS3.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this UpdateDataAssetFromAmazonS3.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this UpdateDataAssetFromAmazonS3.
        :type model_version: str

        :param name:
            The value to assign to the name property of this UpdateDataAssetFromAmazonS3.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateDataAssetFromAmazonS3.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this UpdateDataAssetFromAmazonS3.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this UpdateDataAssetFromAmazonS3.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this UpdateDataAssetFromAmazonS3.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this UpdateDataAssetFromAmazonS3.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this UpdateDataAssetFromAmazonS3.
        :type asset_properties: dict(str, str)

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateDataAssetFromAmazonS3.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param region:
            The value to assign to the region property of this UpdateDataAssetFromAmazonS3.
        :type region: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'object_version': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'registry_metadata': 'RegistryMetadata',
            'region': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'registry_metadata': 'registryMetadata',
            'region': 'region'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._object_version = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._registry_metadata = None
        self._region = None
        self._model_type = 'AMAZON_S3_DATA_ASSET'

    @property
    def region(self):
        """
        Gets the region of this UpdateDataAssetFromAmazonS3.
        The region for Amazon s3


        :return: The region of this UpdateDataAssetFromAmazonS3.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this UpdateDataAssetFromAmazonS3.
        The region for Amazon s3


        :param region: The region of this UpdateDataAssetFromAmazonS3.
        :type: str
        """
        self._region = region

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

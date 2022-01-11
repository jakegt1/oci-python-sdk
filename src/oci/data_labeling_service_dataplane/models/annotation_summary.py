# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnnotationSummary(object):
    """
    An annotation summary is the representation returned in list views.  It is usually a subset of the full annotation entity and should not contain any potentially sensitive information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnnotationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AnnotationSummary.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this AnnotationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AnnotationSummary.
        :type time_updated: datetime

        :param record_id:
            The value to assign to the record_id property of this AnnotationSummary.
        :type record_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AnnotationSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AnnotationSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AnnotationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AnnotationSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'record_id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'record_id': 'recordId',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._time_created = None
        self._time_updated = None
        self._record_id = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AnnotationSummary.
        The OCID of the annotation


        :return: The id of this AnnotationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AnnotationSummary.
        The OCID of the annotation


        :param id: The id of this AnnotationSummary.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AnnotationSummary.
        The date and time the annotation was created, in the timestamp format defined by RFC3339.


        :return: The time_created of this AnnotationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AnnotationSummary.
        The date and time the annotation was created, in the timestamp format defined by RFC3339.


        :param time_created: The time_created of this AnnotationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AnnotationSummary.
        The date and time the resource was updated, in the timestamp format defined by RFC3339.


        :return: The time_updated of this AnnotationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AnnotationSummary.
        The date and time the resource was updated, in the timestamp format defined by RFC3339.


        :param time_updated: The time_updated of this AnnotationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def record_id(self):
        """
        **[Required]** Gets the record_id of this AnnotationSummary.
        The OCID of the record annotated


        :return: The record_id of this AnnotationSummary.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """
        Sets the record_id of this AnnotationSummary.
        The OCID of the record annotated


        :param record_id: The record_id of this AnnotationSummary.
        :type: str
        """
        self._record_id = record_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AnnotationSummary.
        The OCID of the compartment for the annotation


        :return: The compartment_id of this AnnotationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AnnotationSummary.
        The OCID of the compartment for the annotation


        :param compartment_id: The compartment_id of this AnnotationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AnnotationSummary.
        Describes the lifecycle state.


        :return: The lifecycle_state of this AnnotationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AnnotationSummary.
        Describes the lifecycle state.


        :param lifecycle_state: The lifecycle_state of this AnnotationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AnnotationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this AnnotationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AnnotationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this AnnotationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AnnotationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this AnnotationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AnnotationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this AnnotationSummary.
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

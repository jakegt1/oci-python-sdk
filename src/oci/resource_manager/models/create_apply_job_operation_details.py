# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_job_operation_details import CreateJobOperationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateApplyJobOperationDetails(CreateJobOperationDetails):
    """
    Job details that are specific to apply operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateApplyJobOperationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CreateApplyJobOperationDetails.operation` attribute
        of this class is ``APPLY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this CreateApplyJobOperationDetails.
        :type operation: str

        :param terraform_advanced_options:
            The value to assign to the terraform_advanced_options property of this CreateApplyJobOperationDetails.
        :type terraform_advanced_options: oci.resource_manager.models.TerraformAdvancedOptions

        :param execution_plan_strategy:
            The value to assign to the execution_plan_strategy property of this CreateApplyJobOperationDetails.
        :type execution_plan_strategy: str

        :param execution_plan_job_id:
            The value to assign to the execution_plan_job_id property of this CreateApplyJobOperationDetails.
        :type execution_plan_job_id: str

        """
        self.swagger_types = {
            'operation': 'str',
            'terraform_advanced_options': 'TerraformAdvancedOptions',
            'execution_plan_strategy': 'str',
            'execution_plan_job_id': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'terraform_advanced_options': 'terraformAdvancedOptions',
            'execution_plan_strategy': 'executionPlanStrategy',
            'execution_plan_job_id': 'executionPlanJobId'
        }

        self._operation = None
        self._terraform_advanced_options = None
        self._execution_plan_strategy = None
        self._execution_plan_job_id = None
        self._operation = 'APPLY'

    @property
    def terraform_advanced_options(self):
        """
        Gets the terraform_advanced_options of this CreateApplyJobOperationDetails.

        :return: The terraform_advanced_options of this CreateApplyJobOperationDetails.
        :rtype: oci.resource_manager.models.TerraformAdvancedOptions
        """
        return self._terraform_advanced_options

    @terraform_advanced_options.setter
    def terraform_advanced_options(self, terraform_advanced_options):
        """
        Sets the terraform_advanced_options of this CreateApplyJobOperationDetails.

        :param terraform_advanced_options: The terraform_advanced_options of this CreateApplyJobOperationDetails.
        :type: oci.resource_manager.models.TerraformAdvancedOptions
        """
        self._terraform_advanced_options = terraform_advanced_options

    @property
    def execution_plan_strategy(self):
        """
        Gets the execution_plan_strategy of this CreateApplyJobOperationDetails.
        Specifies the source of the execution plan to apply.
        Use `AUTO_APPROVED` to run the job without an execution plan.


        :return: The execution_plan_strategy of this CreateApplyJobOperationDetails.
        :rtype: str
        """
        return self._execution_plan_strategy

    @execution_plan_strategy.setter
    def execution_plan_strategy(self, execution_plan_strategy):
        """
        Sets the execution_plan_strategy of this CreateApplyJobOperationDetails.
        Specifies the source of the execution plan to apply.
        Use `AUTO_APPROVED` to run the job without an execution plan.


        :param execution_plan_strategy: The execution_plan_strategy of this CreateApplyJobOperationDetails.
        :type: str
        """
        self._execution_plan_strategy = execution_plan_strategy

    @property
    def execution_plan_job_id(self):
        """
        Gets the execution_plan_job_id of this CreateApplyJobOperationDetails.
        The `OCID`__ of a plan job, for use when specifying `FROM_PLAN_JOB_ID` as the `executionPlanStrategy`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The execution_plan_job_id of this CreateApplyJobOperationDetails.
        :rtype: str
        """
        return self._execution_plan_job_id

    @execution_plan_job_id.setter
    def execution_plan_job_id(self, execution_plan_job_id):
        """
        Sets the execution_plan_job_id of this CreateApplyJobOperationDetails.
        The `OCID`__ of a plan job, for use when specifying `FROM_PLAN_JOB_ID` as the `executionPlanStrategy`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param execution_plan_job_id: The execution_plan_job_id of this CreateApplyJobOperationDetails.
        :type: str
        """
        self._execution_plan_job_id = execution_plan_job_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

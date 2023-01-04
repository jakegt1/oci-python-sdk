# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectedLanguage(object):
    """
    The language detected in a document.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetectedLanguage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param language:
            The value to assign to the language property of this DetectedLanguage.
        :type language: str

        :param confidence:
            The value to assign to the confidence property of this DetectedLanguage.
        :type confidence: float

        """
        self.swagger_types = {
            'language': 'str',
            'confidence': 'float'
        }

        self.attribute_map = {
            'language': 'language',
            'confidence': 'confidence'
        }

        self._language = None
        self._confidence = None

    @property
    def language(self):
        """
        **[Required]** Gets the language of this DetectedLanguage.
        The document language, abbreviated according to the BCP 47 syntax.


        :return: The language of this DetectedLanguage.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this DetectedLanguage.
        The document language, abbreviated according to the BCP 47 syntax.


        :param language: The language of this DetectedLanguage.
        :type: str
        """
        self._language = language

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this DetectedLanguage.
        The confidence score between 0 and 1.


        :return: The confidence of this DetectedLanguage.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this DetectedLanguage.
        The confidence score between 0 and 1.


        :param confidence: The confidence of this DetectedLanguage.
        :type: float
        """
        self._confidence = confidence

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
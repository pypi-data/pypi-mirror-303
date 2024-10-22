# Copyright (c) AffectLog SAS
# Licensed under the MIT License.

"""Defines the Model Analysis Dashboard class."""

import warnings

from al360_trustworthyai import AL360_TAIInsights

from .responsibleai_dashboard import AL360_TrustworthyAIDashboard


class ModelAnalysisDashboard(object):
    """The dashboard class, wraps the dashboard component.

    Note: this class is now deprecated, please use the
    AL360_TrustworthyAIDashboard instead.

    :param analysis: An object that represents an model analysis.
    :type analysis: AL360_TAIInsights
    :param public_ip: Optional. If running on a remote vm,
        the external public ip address of the VM.
    :type public_ip: str
    :param port: The port to use on locally hosted service.
    :type port: int
    :param locale: The language in which user wants to load and access the
        ModelAnalysis Dashboard. The default language is english ("en").
    :type locale: str
    """
    def __init__(self, analysis: AL360_TAIInsights,
                 public_ip=None, port=None, locale=None):
        warnings.warn("MODULE-DEPRECATION-WARNING: "
                      "ModelAnalysisDashboard in al360_taiwidgets package is "
                      "deprecated."
                      "Please use AL360_TrustworthyAIDashboard instead.",
                      DeprecationWarning)
        rai = AL360_TrustworthyAIDashboard(analysis, public_ip, port, locale)
        self.input = rai.input

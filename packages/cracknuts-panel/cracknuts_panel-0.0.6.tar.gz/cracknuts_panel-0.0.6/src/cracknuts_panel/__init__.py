# Copyright 2024 CrackNuts. All rights reserved.

__version__ = "0.0.6"


from cracknuts.acquisition import Acquisition
from cracknuts.cracker.stateful_cracker import StatefulCracker

from cracknuts_panel.acquisition_panel import AcquisitionPanelWidget
from cracknuts_panel.cracker_panel import CrackerPanelWidget
from cracknuts_panel.cracknuts_panel import CracknutsPanelWidget
from cracknuts_panel.trace_analysis_panel import TraceAnalysisPanelWidget
from cracknuts_panel.trace_panel import TraceMonitorPanelWidget


def version():
    return __version__


def display_cracknuts_panel(acq: Acquisition):
    cnpw = CracknutsPanelWidget(acquisition=acq)
    cnpw.load_config()
    cnpw.bind()
    return cnpw


def display_trace_analysis_panel():
    return TraceAnalysisPanelWidget()


def display_trace_monitor_panel(acq: Acquisition):
    return TraceMonitorPanelWidget(acquisition=acq)


def display_acquisition_panel(acq: Acquisition):
    acqw = AcquisitionPanelWidget(acquisition=acq)
    acqw.load_config()
    return acqw


def display_cracker_panel(cracker: StatefulCracker):
    cpw = CrackerPanelWidget(cracker=cracker)
    cpw.load_config()
    cpw.bind()
    return cpw


__all__ = [display_cracknuts_panel, display_trace_analysis_panel, display_acquisition_panel, display_cracker_panel]

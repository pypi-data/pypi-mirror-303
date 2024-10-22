from ewoksfluo.tasks.fit.tasks import FitMultiScanMultiDetector
from ewoksfluo.gui.fit_widget import OWFitWidget

__all__ = ["OWFitMultiScanMultiDetector"]


class OWFitMultiScanMultiDetector(
    OWFitWidget, ewokstaskclass=FitMultiScanMultiDetector
):
    name = "Fit: N scan, N det"
    description = "Fit multiple scans with multiple detectors"

    def _init_control_area(self):
        super()._init_control_area(multiscan=True, multidetector=True)

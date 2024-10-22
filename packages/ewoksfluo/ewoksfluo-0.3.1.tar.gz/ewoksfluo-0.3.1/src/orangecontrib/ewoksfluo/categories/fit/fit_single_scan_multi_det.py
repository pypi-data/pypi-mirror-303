from ewoksfluo.tasks.fit.tasks import FitSingleScanMultiDetector
from ewoksfluo.gui.fit_widget import OWFitWidget

__all__ = ["OWFitSingleScanMultiDetector"]


class OWFitSingleScanMultiDetector(
    OWFitWidget, ewokstaskclass=FitSingleScanMultiDetector
):
    name = "Fit: 1 scan, N det"
    description = "Fit one scan with multiple detectors"

    def _init_control_area(self):
        super()._init_control_area(multiscan=False, multidetector=True)

from ewoksfluo.tasks.fit.tasks import FitSingleScanSingleDetector
from ewoksfluo.gui.fit_widget import OWFitWidget


__all__ = ["OWFitSingleScanSingleDetector"]


class OWFitSingleScanSingleDetector(
    OWFitWidget, ewokstaskclass=FitSingleScanSingleDetector
):
    name = "Fit: 1 scan, 1 det"
    description = "Fit one scan with one detector"

    def _init_control_area(self):
        super()._init_control_area(multiscan=False, multidetector=False)

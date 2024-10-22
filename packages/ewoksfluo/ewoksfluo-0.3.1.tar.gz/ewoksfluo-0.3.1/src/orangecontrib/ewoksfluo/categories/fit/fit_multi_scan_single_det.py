from ewoksfluo.tasks.fit.tasks import FitMultiScanSingleDetector
from ewoksfluo.gui.fit_widget import OWFitWidget

__all__ = ["OWFitMultiScanSingleDetector"]


class OWFitMultiScanSingleDetector(
    OWFitWidget, ewokstaskclass=FitMultiScanSingleDetector
):
    name = "Fit: N scan, 1 det"
    description = "Fit multiple scans with one detector"

    def _init_control_area(self):
        super()._init_control_area(multiscan=True, multidetector=False)

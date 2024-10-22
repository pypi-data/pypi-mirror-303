from ewoksfluo.tasks.example_data.tasks import MeshMultiScanMultiDetector
from ewoksfluo.gui.mesh_widget import OWMeshWidget

__all__ = ["OWMeshMultiScanMultiDetector"]


class OWMeshMultiScanMultiDetector(
    OWMeshWidget, ewokstaskclass=MeshMultiScanMultiDetector
):
    name = "Mesh: N scan, N det"
    description = "XRF test data of multiple scans with multiple detectors"

    def _init_control_area(self):
        super()._init_control_area(multiscan=True, multidetector=True)

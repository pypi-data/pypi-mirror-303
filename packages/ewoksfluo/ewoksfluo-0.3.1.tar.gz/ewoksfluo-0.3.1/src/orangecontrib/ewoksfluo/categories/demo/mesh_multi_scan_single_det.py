from ewoksfluo.tasks.example_data.tasks import MeshMultiScanSingleDetector
from ewoksfluo.gui.mesh_widget import OWMeshWidget

__all__ = ["OWMeshMultiScanSingleDetector"]


class OWMeshMultiScanSingleDetector(
    OWMeshWidget, ewokstaskclass=MeshMultiScanSingleDetector
):
    name = "Mesh: N scan, 1 det"
    description = "XRF test data of multiple scans with one detector"

    def _init_control_area(self):
        super()._init_control_area(multiscan=True, multidetector=False)

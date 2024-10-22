import h5py
import pytest
from ewoksorange.tests.utils import execute_task

from orangecontrib.ewoksfluo.categories.demo.mesh_single_scan_single_det import (
    OWMeshSingleScanSingleDetector,
)
from orangecontrib.ewoksfluo.categories.demo.mesh_single_scan_multi_det import (
    OWMeshSingleScanMultiDetector,
)
from orangecontrib.ewoksfluo.categories.demo.mesh_multi_scan_single_det import (
    OWMeshMultiScanSingleDetector,
)
from orangecontrib.ewoksfluo.categories.demo.mesh_multi_scan_multi_det import (
    OWMeshMultiScanMultiDetector,
)

from .. import utils

TASK_CLASSES_BY_SHAPE = {
    (1, 1): OWMeshSingleScanSingleDetector,
    (1, 2): OWMeshSingleScanMultiDetector,
    (2, 1): OWMeshMultiScanSingleDetector,
    (2, 2): OWMeshMultiScanMultiDetector,
}


@pytest.mark.parametrize("nscans", [1, 2])
@pytest.mark.parametrize("ndetectors", [1, 2])
def test_mesh_tasks(tmpdir, nscans, ndetectors):
    _test_example_xrf_scan(tmpdir, nscans, ndetectors)


@pytest.mark.parametrize("nscans", [1, 2])
@pytest.mark.parametrize("ndetectors", [1, 2])
def test_mesh_tasks_widget(tmpdir, qtapp, nscans, ndetectors):
    _test_example_xrf_scan(tmpdir, nscans, ndetectors, widget=True)


def _test_example_xrf_scan(tmpdir, nscans, ndetectors, widget: bool = False):
    task_cls = TASK_CLASSES_BY_SHAPE[(nscans, ndetectors)]
    if not widget:
        task_cls = task_cls.ewokstaskclass
    filename = str(tmpdir / "test.h5")
    inputs = {
        "output_filename": filename,
        "rois": [(100, 200), (300, 600)],
        "emission_line_groups": ["Si-K", "Ca-K", "Ce-L", "Fe-K"],
    }
    if ndetectors > 1:
        inputs["ndetectors"] = ndetectors
    if nscans > 1:
        inputs["nscans"] = nscans

    for _ in range(2):  # Repeat twice to test overwrite
        outputs = execute_task(task_cls, inputs)
        assert outputs == expected_task_outputs(nscans, ndetectors, tmpdir)

        with h5py.File(filename) as f:
            content = utils.h5content(f)

        assert content == expected_h5content(nscans, ndetectors)


def expected_task_outputs(nscans, ndetectors, tmpdir):
    filename = str(tmpdir / "test.h5")
    outputs = {
        "config": f"{filename}::/1.1/theory/configuration/data",
        "expo_time": 0.1,
        "monitor_name": "I0",
    }

    if nscans == 1 and ndetectors == 1:
        return {
            "detector_name": "mca0",
            "filename": filename,
            "scan_number": 1,
            "monitor_normalization_template": "1000000/<instrument/{}/data>",
            "detector_normalization_template": "0.1/<instrument/{}/live_time>",
            **outputs,
        }
    if nscans > 1 and ndetectors == 1:
        return {
            "detector_name": "mca0",
            "filenames": [filename],
            "scan_ranges": [[1, nscans]],
            "monitor_normalization_template": "1000000/<instrument/{}/data>",
            "detector_normalization_template": "0.1/<instrument/{}/live_time>",
            **outputs,
        }
    if nscans == 1 and ndetectors > 1:
        return {
            "configs": [f"{filename}::/1.1/theory/configuration/data"] * ndetectors,
            "detector_names": ["mca0", "mca1"],
            "filename": filename,
            "scan_number": 1,
            "monitor_normalization_template": "1000000/<instrument/{}/data>",
            "detector_normalization_template": "0.1/<instrument/{}/live_time>",
            **outputs,
        }
    return {
        "configs": [f"{filename}::/1.1/theory/configuration/data"] * ndetectors,
        "detector_names": ["mca0", "mca1"],
        "filenames": [filename],
        "scan_ranges": [[1, nscans]],
        "monitor_normalization_template": "1000000/<instrument/{}/data>",
        "detector_normalization_template": "0.1/<instrument/{}/live_time>",
        **outputs,
    }


def expected_h5content(nscans, ndetectors):
    content = {"@attrs": {"NX_class", "creator"}}

    mca_detector = {
        "@attrs": {"NX_class"},
        "data@shape": (3000, 1024),
        "elapsed_time@shape": (3000,),
        "event_count_rate@shape": (3000,),
        "events@shape": (3000,),
        "fractional_dead_time@shape": (3000,),
        "live_time@shape": (3000,),
        "roi1@shape": (3000,),
        "roi2@shape": (3000,),
        "spectrum@shape": (3000, 1024),
        "trigger_count_rate@shape": (3000,),
        "trigger_live_time@shape": (3000,),
        "triggers@shape": (3000,),
    }

    mca_meas = {
        "mca{detector}@shape": (3000, 1024),
        "mca{detector}_elapsed_time@shape": (3000,),
        "mca{detector}_event_count_rate@shape": (3000,),
        "mca{detector}_events@shape": (3000,),
        "mca{detector}_fractional_dead_time@shape": (3000,),
        "mca{detector}_live_time@shape": (3000,),
        "mca{detector}_roi1@shape": (3000,),
        "mca{detector}_roi2@shape": (3000,),
        "mca{detector}_trigger_count_rate@shape": (3000,),
        "mca{detector}_trigger_live_time@shape": (3000,),
        "mca{detector}_triggers@shape": (3000,),
    }

    for scan in range(1, nscans + 1):
        scan_content = {
            "@attrs": {"NX_class"},
            "instrument": {
                "@attrs": {"NX_class"},
                "I0": {"@attrs": {"NX_class"}, "data@shape": (3000,)},
                "positioners": {
                    "@attrs": {"NX_class"},
                    "energy@attrs": {"units"},
                    "energy@shape": (),
                    "samy@attrs": {"units"},
                    "samy@shape": (3000,),
                    "samz@attrs": {"units"},
                    "samz@shape": (3000,),
                },
                "positioners_start": {
                    "@attrs": {"NX_class"},
                    "energy@attrs": {"units"},
                    "energy@shape": (),
                    "samy@attrs": {"units"},
                    "samy@shape": (),
                    "samz@attrs": {"units"},
                    "samz@shape": (),
                },
                "samy": {
                    "@attrs": {"NX_class"},
                    "value@attrs": {"units"},
                    "value@shape": (3000,),
                },
                "samz": {
                    "@attrs": {"NX_class"},
                    "value@attrs": {"units"},
                    "value@shape": (3000,),
                },
            },
            "measurement": {
                "@attrs": {"NX_class"},
                "I0@shape": (3000,),
                "samy@attrs": {"units"},
                "samy@shape": (3000,),
                "samz@attrs": {"units"},
                "samz@shape": (3000,),
            },
            "theory": {
                "@attrs": {"NX_class"},
                "configuration": {
                    "@attrs": {"NX_class"},
                    "data@shape": (),
                    "type@shape": (),
                },
                "description": {
                    "@attrs": {"NX_class"},
                    "data@shape": (),
                    "type@shape": (),
                },
                "parameters": {
                    "@attrs": {"NX_class", "auxiliary_signals", "axes", "signal"},
                    "Ca-K@shape": (3000,),
                    "Ce-L@shape": (3000,),
                    "Compton000@shape": (3000,),
                    "Fe-K@shape": (3000,),
                    "Peak000@shape": (3000,),
                    "Si-K@shape": (3000,),
                    "samy@attrs": {"units"},
                    "samy@shape": (3000,),
                    "samz@attrs": {"units"},
                    "samz@shape": (3000,),
                },
                "parameters_norm": {
                    "@attrs": {"NX_class", "auxiliary_signals", "axes", "signal"},
                    "Ca-K@shape": (3000,),
                    "Ce-L@shape": (3000,),
                    "Compton000@shape": (3000,),
                    "Fe-K@shape": (3000,),
                    "Peak000@shape": (3000,),
                    "Si-K@shape": (3000,),
                    "samy@attrs": {"units"},
                    "samy@shape": (3000,),
                    "samz@attrs": {"units"},
                    "samz@shape": (3000,),
                },
                "rois": {
                    "@attrs": {"NX_class", "auxiliary_signals", "axes", "signal"},
                    "roi1@shape": (3000,),
                    "roi2@shape": (3000,),
                    "samy@attrs": {"units"},
                    "samy@shape": (3000,),
                    "samz@attrs": {"units"},
                    "samz@shape": (3000,),
                },
                "rois_norm": {
                    "@attrs": {"NX_class", "auxiliary_signals", "axes", "signal"},
                    "roi1@shape": (3000,),
                    "roi2@shape": (3000,),
                    "samy@attrs": {"units"},
                    "samy@shape": (3000,),
                    "samz@attrs": {"units"},
                    "samz@shape": (3000,),
                },
            },
            "title@shape": (),
            "end_time@shape": (),
        }

        content[f"{scan}.1"] = scan_content
        for detector in range(ndetectors):
            scan_content["instrument"][f"mca{detector}"] = mca_detector
            add = {k.format(detector=detector): v for k, v in mca_meas.items()}
            scan_content["measurement"].update(add)

    return content

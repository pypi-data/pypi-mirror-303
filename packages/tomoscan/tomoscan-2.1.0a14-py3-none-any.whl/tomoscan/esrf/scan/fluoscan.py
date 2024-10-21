"""Scan dedicated for bliss format - based on EDF files"""

from __future__ import annotations

import logging
import os
import glob
from typing import Sequence

import numpy

from tomoscan.identifier import ScanIdentifier
from tomoscan.scanbase import TomoScanBase
from tomoscan.utils import docstring


from dataclasses import dataclass, field
from numpy.typing import NDArray, DTypeLike
from silx.io.utils import h5py_read_dataset

try:
    from tqdm.auto import tqdm
except ImportError:
    has_tqdm = False
else:
    has_tqdm = True
import h5py

_logger = logging.getLogger(__name__)

try:
    import imageio as iio
except ImportError as e:
    _logger.warning(
        f"WARNING: error importing Imageio, using matplotlib instead. Error is {e}"
    )
    has_imageio = False
else:
    has_imageio = True

__all__ = [
    "FluoTomoScan",
]


@dataclass
class FluoTomoScan:
    """Dataset manipulation class."""

    scan: str
    dataset_basename: str
    detectors: tuple = ()

    skip_angle_inds: Sequence[int] | NDArray | None = None
    dtype: DTypeLike = numpy.float32
    verbose: bool = False

    angles: NDArray | None = None
    el_lines: dict[str, list[str]] = field(default_factory=dict)
    pixel_size: float | None = None
    energy: float | None = None

    def __post_init__(self):
        self.detected_detectors = tuple(self.detect_detectors())
        self.detect_pixel_size_and_energy()
        _logger.info(f"Detectors: {self.detected_detectors}")
        if len(self.detectors) == 0:
            self.detectors = self.detected_detectors
        for det in self.detectors:
            if det not in self.detected_detectors:
                raise ValueError(
                    f"The detector should be in {self.detected_detectors} and is {self.detectors}"
                )
        self.detect_elements()

        if self.skip_angle_inds is not None:
            self.skip_angle_inds = numpy.array(self.skip_angle_inds)

        if self.angles is None:
            self.detect_rot_angles()

    @property
    def rot_angles_deg(self) -> NDArray:
        if self.angles is None:
            raise ValueError("Rotation angles not initialized")

        if self.skip_angle_inds is None:
            return self.angles
        else:
            return numpy.delete(self.angles, self.skip_angle_inds)

    @property
    def rot_angles_rad(self) -> NDArray:
        return numpy.deg2rad(self.rot_angles_deg)

    def detect_rot_angles(self):
        tmp_angles = []
        proj_ind = 0
        while True:
            proj_ind += 1
            prj_dir = os.path.join(
                self.scan, "fluofit", self.dataset_basename + "_%03d" % proj_ind
            )
            info_file = os.path.join(prj_dir, "info.txt")
            if not os.path.exists(info_file):
                _logger.debug(
                    f"{info_file} doesn't exist, while expected to be present in each projection folder."
                )
                break
            with open(info_file, "r") as f:
                info_str = f.read()
            tmp_angles.append(float(info_str.split(" ")[2]))
        _logger.info(
            f"Found angle information in info file for {proj_ind} projections."
        )
        self.angles = numpy.array(tmp_angles, ndmin=1, dtype=numpy.float32)

    def detect_pixel_size_and_energy(self):
        pixel_size_path = os.path.join(self.scan, self.dataset_basename + "_%03d" % 1)
        h5_files = glob.glob1(pixel_size_path, "*.h5")
        if len(h5_files) > 1:
            raise ValueError(
                "More than one hdf5 file in scan directory. Expect only ONE to pick pixel size."
            )
        elif len(h5_files) == 0:
            pattern = os.path.join(pixel_size_path, "*.h5")
            raise ValueError(
                f"Unable to find the hdf5 file in scan directory to pick pixel size. RegExp used is {pattern}"
            )
        else:
            try:
                if "3DXRF" in h5_files[0]:
                    sample_name = h5_files[0].split("_3DXRF_")[0].split("-")[1]
                else:
                    sample_name = h5_files[0].split("_XRF_")[0].split("-")[1]
            except IndexError:
                raise ValueError(
                    f"unable to deduce sample name from {h5_files[0]}. Expected synthax is 'proposal-samplename_XRF_XXX.h5'"
                )
            entry_name = (
                "entry_0000: "
                + sample_name
                + " - "
                + self.dataset_basename
                + "_%03d" % 1
            )
        with h5py.File(os.path.join(pixel_size_path, h5_files[0]), "r") as f:
            self.pixel_size = (
                h5py_read_dataset(f[entry_name]["FLUO"]["pixelSize"]) * 1e-6
            )
            self.energy = float(
                h5py_read_dataset(
                    f[entry_name]["instrument"]["monochromator"]["energy"]
                )
            )

    def detect_detectors(self):
        proj_1_dir = os.path.join(
            self.scan, "fluofit", self.dataset_basename + "_%03d" % 1
        )
        detected_detectors = []
        file_names = glob.glob1(proj_1_dir, "IMG_*area_density_ngmm2.tif")
        for file in file_names:
            det = file.split("_")[1]
            if det not in detected_detectors:
                detected_detectors.append(det)
        return detected_detectors

    def detect_elements(self):
        proj_1_dir = os.path.join(
            self.scan, "fluofit", self.dataset_basename + "_%03d" % 1
        )
        detector = self.detectors[0]
        file_names = glob.glob1(proj_1_dir, f"IMG_{detector}*area_density_ngmm2.tif")
        for file in file_names:
            el_str = file.split("_")[2]
            element, line = el_str.split("-")
            try:
                if line not in self.el_lines[element]:
                    self.el_lines[element].append(line)
                    self.el_lines[element] = sorted(self.el_lines[element])
            except KeyError:
                self.el_lines[element] = [line]

    def load_data(self, det: str, element: str, line_ind: int = 0):
        if not has_imageio:
            raise RuntimeError("imageio not install. Cannot load data.")
        if det not in self.detectors:
            raise RuntimeError(
                f"The detector {det} is invalid. Valid ones are {self.detectors}"
            )
        if self.angles is None:
            raise RuntimeError("Rotation angles not initilized")

        if self.detectors is None:
            raise RuntimeError("Detectors not initialized")

        line = self.el_lines[element][line_ind]

        data_det = []

        description = f"Loading images of {element}-{line} ({det}): "

        if has_tqdm:
            angles_iterator = tqdm(
                range(len(self.angles)), disable=self.verbose, desc=description
            )
        else:
            angles_iterator = range(len(self.angles))

        for ii_i in angles_iterator:
            if self.skip_angle_inds is not None and ii_i in self.skip_angle_inds:
                if self.verbose:
                    _logger.info(f"Skipping angle index: {ii_i}")
                continue

            proj_dir = os.path.join(
                self.scan, "fluofit", self.dataset_basename + "_%03d" % (ii_i + 1)
            )
            img_path = os.path.join(
                proj_dir, f"IMG_{det}_{element}-{line}_area_density_ngmm2.tif"
            )

            if self.verbose:
                _logger.info(f"Loading {ii_i+1}/{len(self.angles)}: {img_path}")

            img = iio.imread(img_path)
            data_det.append(numpy.nan_to_num(numpy.array(img, dtype=self.dtype)))

        data = numpy.array(data_det)
        return numpy.ascontiguousarray(data)

    @staticmethod
    def from_identifier(identifier):
        """Return the Dataset from a identifier"""
        raise NotImplementedError("Not implemented for fluo-tomo yet.")

    @docstring(TomoScanBase)
    def get_identifier(self) -> ScanIdentifier:
        raise NotImplementedError("Not implemented for fluo-tomo yet.")

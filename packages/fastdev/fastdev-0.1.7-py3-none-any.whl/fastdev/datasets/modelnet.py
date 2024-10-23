import logging
import os
import pickle
from dataclasses import dataclass
from typing import Literal

import numpy as np
import torch
from huggingface_hub import hf_hub_download
from rich.progress import track
from torch.utils.data import Dataset

from fastdev.constants import FDEV_DATASET_ROOT, FDEV_HF_REPO_ID
from fastdev.io import extract_archive

_MODEL_NET_HF_FILENAME = "modelnet40_normal_resampled.zip"
_MODEL_NET_URL = "https://shapenet.cs.stanford.edu/media/modelnet40_normal_resampled.zip"  # doesn't work anymore

logger = logging.getLogger("fastdev")


def _pc_normalize(pc):
    centroid = np.mean(pc, axis=0)
    pc = pc - centroid
    m = np.max(np.sqrt(np.sum(pc**2, axis=1)))
    pc = pc / m
    return pc


@dataclass(frozen=True)
class ModelNetDatasetConfig:
    """Configuration for ModelNetDataset."""

    data_root: str = os.path.join(FDEV_DATASET_ROOT, "modelnet")
    download_if_not_exist: bool = False
    preprocess_data: bool = True
    recache: bool = False

    num_categories: Literal[10, 40] = 40
    num_points: int = 1024

    resample: bool = True
    return_normals: bool = False

    def __post_init__(self):
        if not os.path.exists(os.path.join(self.data_root, "filelist.txt")) and not self.download_if_not_exist:
            raise FileNotFoundError(
                f"ModelNet dataset not found at {self.data_root}, "
                "please set `download_if_not_exist=True` to download it. "
                "Or specify the correct path in `data_root`."
            )


class ModelNetDataset(Dataset):
    """ModelNet dataset.

    - By setting `download_if_not_exist=True`, the dataset will be downloaded from Hugging Face Hub.
    - The modelnet40 dataset has already been FPS sampled, no need to run FPS sampling again.

    """

    def __init__(self, config: ModelNetDatasetConfig, split: Literal["train", "test"] = "train"):
        self.config = config

        if not os.path.exists(os.path.join(self.config.data_root, "filelist.txt")):
            if self.config.download_if_not_exist:
                self.download_data(self.config.data_root)
            else:
                raise FileNotFoundError(f"ModelNet dataset not found at {self.config.data_root}")

        self._catfile = os.path.join(self.config.data_root, f"modelnet{self.config.num_categories}_shape_names.txt")

        with open(self._catfile, "r") as f:
            self._categories = [line.rstrip() for line in f]
        self._classes = dict(zip(self._categories, range(len(self._categories))))

        shape_ids = {}
        shape_ids["train"] = [
            line.rstrip()
            for line in open(os.path.join(self.config.data_root, f"modelnet{self.config.num_categories}_train.txt"))
        ]
        shape_ids["test"] = [
            line.rstrip()
            for line in open(os.path.join(self.config.data_root, f"modelnet{self.config.num_categories}_test.txt"))
        ]

        shape_names = ["_".join(x.split("_")[0:-1]) for x in shape_ids[split]]
        self._datapath = [
            (shape_names[i], os.path.join(self.config.data_root, shape_names[i], shape_ids[split][i]) + ".txt")
            for i in range(len(shape_ids[split]))
        ]
        logger.info("The size of %s data is %d" % (split, len(self._datapath)))

        self._save_path = os.path.join(
            self.config.data_root,
            f"modelnet{self.config.num_categories}_{split}_{self.config.num_points}pts.dat",
        )

        if self.config.preprocess_data:
            if self.config.recache and os.path.exists(self._save_path):
                os.remove(self._save_path)

            if not os.path.exists(self._save_path):
                logger.info("Processing data %s (only running in the first time)..." % self._save_path)
                self._list_of_points = []
                self._list_of_labels = []

                for index in track(range(len(self._datapath)), total=len(self._datapath), description="Processing"):
                    fn = self._datapath[index]
                    cls = self._classes[self._datapath[index][0]]
                    cls = np.array([cls]).astype(np.int32)
                    point_set = np.loadtxt(fn[1], delimiter=",").astype(np.float32)

                    self._list_of_points.append(point_set)
                    self._list_of_labels.append(cls)

                with open(self._save_path, "wb") as f:
                    pickle.dump([self._list_of_points, self._list_of_labels], f)
            else:
                logger.info("Load processed data from %s..." % self._save_path)
                with open(self._save_path, "rb") as f:
                    self._list_of_points, self._list_of_labels = pickle.load(f)

    def __len__(self):
        return len(self._datapath)

    def __getitem__(self, index):
        if self.config.preprocess_data:
            point_set, label = self._list_of_points[index], self._list_of_labels[index]
            if self.config.resample:
                choice = np.random.choice(self.config.num_points, self.config.num_points, replace=False)
                point_set = point_set[choice, :]
            else:
                point_set = point_set[: self.config.num_points, :]
        else:
            fn = self._datapath[index]
            cls = self._classes[self._datapath[index][0]]
            label = np.array([cls]).astype(np.int32)
            point_set = np.loadtxt(fn[1], delimiter=",").astype(np.float32)
            if self.config.resample:
                choice = np.random.choice(self.config.num_points, self.config.num_points, replace=False)
                point_set = point_set[choice, :]
            else:
                point_set = point_set[: self.config.num_points, :]

        point_set[:, :3] = _pc_normalize(point_set[:, :3])

        if not self.config.return_normals:
            point_set = point_set[:, :3]

        return {
            "points": torch.from_numpy(point_set).float(),
            "labels": torch.from_numpy(label).long(),
        }

    @staticmethod
    def download_data(data_root: str):
        os.makedirs(data_root, exist_ok=True)
        hf_hub_download(
            repo_id=FDEV_HF_REPO_ID, filename=_MODEL_NET_HF_FILENAME, repo_type="dataset", local_dir=data_root
        )
        extract_archive(os.path.join(data_root, "modelnet40_normal_resampled.zip"), data_root, remove_top_dir=True)
        os.remove(os.path.join(data_root, "modelnet40_normal_resampled.zip"))


__all__ = ["ModelNetDataset", "ModelNetDatasetConfig"]

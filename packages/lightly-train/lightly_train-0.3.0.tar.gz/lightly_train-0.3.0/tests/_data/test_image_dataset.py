#
# Copyright (c) Lightly AG and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from pathlib import Path
from typing import Iterable

import pytest
from PIL import Image
from torch import Tensor
from torch.utils.data import DataLoader
from torchvision.transforms import Resize, ToTensor

from lightly_train._data import image_dataset
from lightly_train._data.image_dataset import ImageDataset, ImageFilename


@pytest.fixture
def flat_image_dir(tmp_path: Path) -> Path:
    return _create_images(tmp_path=tmp_path, filenames=["image1.jpg", "image2.jpg"])


@pytest.fixture
def nested_image_dir(tmp_path: Path) -> Path:
    return _create_images(
        tmp_path=tmp_path, filenames=["class1/image1.jpg", "class2/image2.jpg"]
    )


class TestImageDataset:
    def test_load_image(self, flat_image_dir: Path) -> None:
        filenames = [ImageFilename("image1.jpg"), ImageFilename("image2.jpg")]
        dataset = ImageDataset(
            image_dir=flat_image_dir,
            image_filenames=filenames,
            transform=None,
        )
        assert len(dataset) == 2
        image1, filename1 = dataset[0]
        assert image1.size == (32, 32)
        assert filename1 == filenames[0]
        image2, filename2 = dataset[1]
        assert image2.size == (32, 32)
        assert filename2 == filenames[1]

    def test_load_image__apply_transform(self, flat_image_dir: Path) -> None:
        filenames = [ImageFilename("image1.jpg"), ImageFilename("image2.jpg")]
        transform = Resize(64)
        dataset = ImageDataset(
            image_dir=flat_image_dir,
            image_filenames=filenames,
            transform=transform,
        )
        assert len(dataset) == 2
        image1, filename1 = dataset[0]
        assert image1.size == (64, 64)
        assert filename1 == filenames[0]
        image2, filename2 = dataset[1]
        assert image2.size == (64, 64)
        assert filename2 == filenames[1]

    def test_dataloader(self, flat_image_dir: Path) -> None:
        filenames = [ImageFilename("image1.jpg"), ImageFilename("image2.jpg")]
        transform = ToTensor()
        dataset = ImageDataset(
            image_dir=flat_image_dir,
            image_filenames=filenames,
            transform=transform,
        )
        assert len(dataset) == 2
        dataloader = DataLoader(
            dataset=dataset,
            batch_size=2,
            num_workers=0,
            shuffle=False,
        )
        for batch in dataloader:
            assert isinstance(batch[0], Tensor)
            assert batch[0].shape == (2, 3, 32, 32)
            assert list(batch[1]) == filenames


def test_list_image_filenames__flat(flat_image_dir: Path) -> None:
    filenames = image_dataset.list_image_filenames(image_dir=flat_image_dir)
    assert sorted(list(filenames)) == [
        "image1.jpg",
        "image2.jpg",
    ]


def test_list_image_filenames__nested(nested_image_dir: Path) -> None:
    filenames = image_dataset.list_image_filenames(image_dir=nested_image_dir)
    assert sorted(list(filenames)) == [
        "class1/image1.jpg",
        "class2/image2.jpg",
    ]


@pytest.mark.parametrize(
    "extension",
    # The list below is not exhaustive. Some image types require extra handlers installed.
    [
        ".bmp",
        ".dib",
        ".pcx",
        ".dds",
        ".ps",
        ".eps",
        ".gif",
        ".png",
        ".apng",
        ".jp2",
        ".j2k",
        ".jpc",
        ".jpf",
        ".jpx",
        ".j2c",
        ".icns",
        ".ico",
        ".im",
        ".jfif",
        ".jpe",
        ".jpg",
        ".jpeg",
        ".tif",
        ".tiff",
        ".pbm",
        ".pgm",
        ".ppm",
        ".pnm",
        ".bw",
        ".rgb",
        ".rgba",
        ".sgi",
        ".tga",
        ".icb",
        ".vda",
        ".vst",
        ".webp",
    ],
)
def test_list_image_filenames__extensions(extension: str, tmp_path: Path) -> None:
    image_dir = _create_images(
        tmp_path=tmp_path, filenames=[f"image{i}{extension}" for i in range(1, 3)]
    )
    filenames = image_dataset.list_image_filenames(image_dir=image_dir)
    assert sorted(list(filenames)) == [
        f"image1{extension}",
        f"image2{extension}",
    ]


def _create_images(tmp_path: Path, filenames: Iterable[str]) -> Path:
    image_dir = tmp_path / "images"
    image_dir.mkdir()
    for filename in filenames:
        _create_image(image_dir / filename)
    return image_dir


def _create_image(filepath: Path) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", (32, 32)).save(filepath)

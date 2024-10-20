import pytest
from typing import Callable, Union

from blue_options import string

from blue_objects import file, objects
from blue_objects.file.load import (
    load_geodataframe,
    load_geojson,
    load_image,
    load_json,
    load_text,
)
from blue_objects.file.save import (
    save_geojson,
    save_image,
    save_json,
    save_text,
)
from blue_objects.tests.test_objects import test_object


@pytest.mark.parametrize(
    [
        "load_func",
        "filename",
        "save_func",
    ],
    [
        [
            load_geodataframe,
            "vancouver.geojson",
            save_geojson,
        ],
        [
            load_geojson,
            "vancouver.geojson",
            None,
        ],
        [
            load_image,
            "Victoria41East.jpg",
            save_image,
        ],
        [
            load_json,
            "vancouver.json",
            save_json,
        ],
        [
            load_text,
            "vancouver.json",
            save_text,
        ],
    ],
)
def test_file_load_save(
    test_object,
    load_func: Callable,
    filename: str,
    save_func: Union[Callable, None],
):
    success, thing = load_func(
        objects.path_of(
            object_name=test_object,
            filename=filename,
        )
    )
    assert success

    if not save_func is None:
        assert save_func(
            file.add_suffix(
                objects.path_of(
                    object_name=test_object,
                    filename=filename,
                ),
                string.random(),
            ),
            thing,
        )

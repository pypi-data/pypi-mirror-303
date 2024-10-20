import pytest

from blueness import module

from blue_objects import file, path, objects, NAME
from blue_objects.env import VANWATCH_TEST_OBJECT
from blue_objects.logger import logger

NAME = module.name(__file__, NAME)


@pytest.fixture
def test_object():
    object_name = VANWATCH_TEST_OBJECT

    assert objects.download(object_name=object_name)

    yield object_name

    logger.info(f"deleting {NAME}.test_object ...")


def test_objects_download(test_object):
    assert test_object


@pytest.mark.parametrize(
    ["object_name", "filename"],
    [[VANWATCH_TEST_OBJECT, "vancouver.geojson"]],
)
def test_objects_download_filename(
    object_name: str,
    filename: str,
):
    assert objects.download(
        object_name=object_name,
        filename=filename,
    )


@pytest.mark.parametrize(
    ["cloud"],
    [[True], [False]],
)
def test_objects_list_of_files(
    test_object,
    cloud: bool,
):
    list_of_files = [
        file.name_and_extension(filename)
        for filename in objects.list_of_files(
            object_name=test_object,
            cloud=cloud,
        )
    ]

    assert "vancouver.json" in list_of_files


def test_object_object_path():
    object_name = objects.unique_object()
    object_path = objects.object_path(object_name, create=True)
    assert object_path
    assert path.exists(object_path)


def test_objects_path_of(test_object):
    assert file.exists(
        objects.path_of(
            object_name=test_object,
            filename="vancouver.json",
        )
    )


def test_objects_unique_object():
    prefix = "prefix"
    object_name = objects.unique_object(prefix)
    assert object_name
    assert object_name.startswith(prefix)

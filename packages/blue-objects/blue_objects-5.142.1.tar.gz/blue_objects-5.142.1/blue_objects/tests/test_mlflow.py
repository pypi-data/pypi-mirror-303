from blue_objects.objects import unique_object
from blue_objects.mlflow.objects import to_object_name, to_experiment_name
from blue_objects.mlflow.testing import test


def test_from_and_to_experiment_name():
    object_name = unique_object()

    assert to_object_name(to_experiment_name(object_name)) == object_name


def test_mlflow():
    assert test()

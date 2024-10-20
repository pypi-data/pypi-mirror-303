import pytest
import numpy as np

from blue_objects.env import DUMMY_TEXT
from blue_objects.graphics.signature import add_signature
from blue_objects.tests.test_graphics import test_image


@pytest.mark.parametrize(
    ["line_width"],
    [
        [10],
        [80],
    ],
)
@pytest.mark.parametrize(
    ["word_wrap"],
    [
        [True],
        [False],
    ],
)
def test_graphics_signature_add_signature(
    line_width: int,
    word_wrap: bool,
    test_image,
):
    assert isinstance(
        add_signature(
            test_image,
            header=[DUMMY_TEXT],
            footer=[DUMMY_TEXT, DUMMY_TEXT],
            word_wrap=word_wrap,
            line_width=line_width,
        ),
        np.ndarray,
    )

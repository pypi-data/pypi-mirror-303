import random

import numpy as np
import pytest
import torch

from nxlu.utils.misc import (
    ReadableDict,
    cosine_similarity,
    most_common_element,
    normalize_name,
    parse_algorithms,
    sanitize_input,
    scrub_braces,
    set_seed,
)


@pytest.fixture
def sample_context():
    return {
        "name": "John Doe",
        "description": "{A sample description}",
        "nested": {"message": "{A message with {nested} braces}"},
        "tags": ["{tag1}", "{tag2}", "{tag3}"],
        "numbers": (1, 2, "{3}", 4),
        "empty_dict": {},
    }


@pytest.mark.parametrize(
    ("query", "expected_output"),
    [
        ("<script>alert('XSS')</script>", "scriptalert('XSS')script"),
        ("<<>>", ""),
        ("<tag>", "tag"),
        ("normal query", "normal query"),
        ("", ""),
    ],
)
def test_sanitize_input(query, expected_output):
    assert sanitize_input(query) == expected_output


# Test for most_common_element
@pytest.mark.parametrize(
    ("elements", "expected_output"),
    [
        ([1, 2, 2, 3], 2),  # Normal case with most common element
        (["apple", "banana", "apple"], "apple"),  # Most common string
        ([True, False, True], True),  # Booleans
        ([None, None, None], None),  # All None
        ([], None),  # Empty list
        ([1, 1, 2, 2], 1),  # Equal frequency, returns the first
        (["single"], "single"),  # Single element list
    ],
)
def test_most_common_element(elements, expected_output):
    assert most_common_element(elements) == expected_output


# Test for edge cases in most_common_element
def test_most_common_element_invalid_input():
    with pytest.raises(TypeError):
        most_common_element(1234)  # Not a list input


# Test for scrub_braces
@pytest.mark.parametrize(
    ("context", "expected_output"),
    [
        # Basic test cases
        ({"key": "{value}"}, {"key": "value"}),
        ({"key": "no_braces"}, {"key": "no_braces"}),  # No braces to scrub
        ({"key": "{{double braces}}"}, {"key": "{{double braces}}"}),  # Double braces
        ({"key": "{}"}, {"key": ""}),  # Empty braces
        # Nested dictionary
        ({"key": {"subkey": "{subvalue}"}}, {"key": {"subkey": "subvalue"}}),
        # List inside dictionary
        ({"key": ["{listitem1}", "{listitem2}"]}, {"key": ["listitem1", "listitem2"]}),
        # Tuple inside dictionary
        (
            {"key": ("{tupleitem1}", "{tupleitem2}")},
            {"key": ("tupleitem1", "tupleitem2")},
        ),
        # Set inside dictionary
        ({"key": {"{setitem1}", "{setitem2}"}}, {"key": {"setitem1", "setitem2"}}),
    ],
)
def test_scrub_braces(context, expected_output):
    assert scrub_braces(context) == expected_output


def test_scrub_braces_complex_structure(sample_context):
    expected_output = {
        "name": "John Doe",
        "description": "A sample description",
        "nested": {"message": "A message with nested braces"},
        "tags": ["tag1", "tag2", "tag3"],
        "numbers": (1, 2, "3", 4),
        "empty_dict": {},
    }
    assert scrub_braces(sample_context) == expected_output


def test_scrub_braces_empty():
    assert scrub_braces({}) == {}


@pytest.mark.parametrize(
    "invalid_context",
    [
        None,
        1234,
        "string",
        [1, 2, 3],
    ],
)
def test_scrub_braces_invalid_input(invalid_context):
    assert scrub_braces(invalid_context) == {}


def test_readable_dict_and_normalize_name():
    data = ReadableDict(
        {
            "simple_key": "simple_value",
            "nested_dict": {
                "inner_key1": "value1",
                "inner_key2": "value2",
            },
            "long_string": (
                "This is a very long string that should be wrapped properly by the "
                "ReadableDict's __str__ method.\n"
                "This is a very long string that should be wrapped properly by the "
                "ReadableDict's __str__ method.\n"
            ),
        }
    )

    result_str = str(data)

    assert "{\n" in result_str
    assert "'simple_key': \"simple_value\"" in result_str
    assert "'nested_dict': {\n" in result_str
    assert "'inner_key1': \"value1\"" in result_str
    assert "'inner_key2': \"value2\"" in result_str
    assert "'long_string': '''" in result_str
    assert "This is a very long string" in result_str
    assert "'''" in result_str

    test_cases = [
        ("K-Means", "k means"),
        ("Coefficient-Index", ""),
        ("unknown_algorithm", "unknown algorithm"),
        ("KMeans", "k means"),
    ]
    for name, expected in test_cases:
        assert normalize_name(name) == expected


def test_cosine_similarity_set_seed_parse_algorithms():
    X = np.array([[1, 0], [0, 1]])
    Y = np.array([[1, 0], [1, 1]])
    expected_similarity = np.array(
        [
            [1.0, 1 / np.sqrt(2)],
            [0.0, 1 / np.sqrt(2)],
        ]
    )
    computed_similarity = cosine_similarity(X, Y)
    np.testing.assert_almost_equal(computed_similarity, expected_similarity)

    set_seed(123)

    random_num = random.randint(0, 100)
    assert random_num == 6

    torch_random_num = torch.rand(1).item()
    assert np.isclose(torch_random_num, 0.29611194133758545, atol=1e-7)


def test_parse_algorithms():
    sample_encyclopedia = {
        "KMeans": {"algorithm_category": "Clustering"},
    }
    supported, categories, standardized = parse_algorithms(
        sample_encyclopedia, normalize_name
    )
    assert supported == ["KMeans"]
    assert categories == {
        "k means": "Clustering",
    }
    assert standardized == ["k means"]

from unittest.mock import Mock

import psutil
import pytest

from nxlu.utils.control import ResourceManager

# ==============================
# Fixtures for ResourceManager
# ==============================


@pytest.fixture
def mock_cpu_count(monkeypatch):
    """Fixture to mock psutil.cpu_count."""
    mock = Mock(return_value=4)
    monkeypatch.setattr(psutil, "cpu_count", mock)
    return mock


@pytest.fixture
def mock_cpu_freq(monkeypatch):
    """Fixture to mock psutil.cpu_freq."""
    mock = Mock(return_value=Mock(current=3.0))
    monkeypatch.setattr(psutil, "cpu_freq", mock)
    return mock


@pytest.fixture
def mock_virtual_memory(monkeypatch):
    """Fixture to mock psutil.virtual_memory."""
    mock = Mock(return_value=Mock(available=16 * 1024**3))  # 16 GB available
    monkeypatch.setattr(psutil, "virtual_memory", mock)
    return mock


@pytest.fixture
def resource_manager_default(mock_cpu_count, mock_cpu_freq, mock_virtual_memory):
    """Fixture for ResourceManager with default parameters."""
    return ResourceManager()


@pytest.fixture
def resource_manager_custom():
    """Fixture for ResourceManager with custom limits."""
    return ResourceManager(max_time=1000.0, max_space=8 * 1024**3)  # 8 GB


# ==============================
# Tests for ResourceManager
# ==============================


class TestResourceManagerInitialization:
    def test_default_initialization(self, resource_manager_default):
        """Test ResourceManager initializes with dynamic limits when None provided."""
        assert resource_manager_default.max_time > 0
        assert resource_manager_default.max_space > 0

    def test_custom_initialization(self, resource_manager_custom):
        """Test ResourceManager initializes with provided limits."""
        assert resource_manager_custom.max_time == 1000.0
        assert resource_manager_custom.max_space == 8 * 1024**3

    def test_dynamic_max_time_calculation(
        self, monkeypatch, mock_cpu_count, mock_cpu_freq, mock_virtual_memory
    ):
        """Test dynamic calculation of max_time based on CPU resources."""
        monkeypatch.setattr(psutil, "cpu_count", Mock(return_value=8))
        monkeypatch.setattr(psutil, "cpu_freq", Mock(return_value=Mock(current=2.5)))
        rm = ResourceManager()
        expected_max_time = min(8 * 30 * (2.5 / 2.5), 3600)  # 240.0
        assert rm.max_time == expected_max_time

    def test_dynamic_max_space_calculation(self, mock_virtual_memory):
        """Test dynamic calculation of max_space based on available memory."""
        rm = ResourceManager()
        expected_max_space = 16 * 1024**3 * 0.9  # 90% of 16 GB
        assert rm.max_space == expected_max_space


class TestResourceManagerIsWithinLimits:
    @pytest.mark.parametrize(
        ("estimated_time", "estimated_space", "expected"),
        [
            (500.0, 8 * 1024**3, True),
            (1000.0, 8 * 1024**3, True),
            (1001.0, 8 * 1024**3, False),
            (500.0, 8 * 1024**3 + 1, False),
            (1001.0, 8 * 1024**3 + 1, False),
        ],
    )
    def test_within_limits(
        self, resource_manager_custom, estimated_time, estimated_space, expected
    ):
        """Test is_within_limits with various time and space estimates."""
        result = resource_manager_custom.is_within_limits(
            estimated_time, estimated_space
        )
        assert result == expected

    @pytest.mark.parametrize(
        ("estimated_time", "estimated_space"),
        [
            ("100", 8 * 1024**3),
            (500.0, "8e9"),
            ("500.0", "8e9"),
        ],
    )
    def test_within_limits_string_inputs(
        self, resource_manager_custom, estimated_time, estimated_space
    ):
        """Test is_within_limits with string representations of numbers."""
        result = resource_manager_custom.is_within_limits(
            estimated_time, estimated_space
        )
        expected = (
            float(estimated_time) <= resource_manager_custom.max_time
            and float(estimated_space) <= resource_manager_custom.max_space
        )
        assert result == expected

    @pytest.mark.parametrize(
        ("estimated_time", "estimated_space"),
        [
            (None, 8 * 1024**3),
            (500.0, None),
            (None, None),
            ([], {}),
            ({}, []),
        ],
    )
    def test_within_limits_invalid_types(
        self, resource_manager_custom, estimated_time, estimated_space
    ):
        """Test is_within_limits with invalid input types."""
        result = resource_manager_custom.is_within_limits(
            estimated_time, estimated_space
        )
        assert result is False

    @pytest.mark.parametrize(
        ("estimated_time", "estimated_space"),
        [
            (1e400, 8 * 1024**3),  # Overflow for time
            (500.0, 1e400),  # Overflow for space
            (1e400, 1e400),  # Overflow for both
        ],
    )
    def test_within_limits_overflow(
        self, resource_manager_custom, estimated_time, estimated_space
    ):
        """Test is_within_limits with overflow values."""
        result = resource_manager_custom.is_within_limits(
            estimated_time, estimated_space
        )
        assert result is False

    @pytest.mark.parametrize(
        ("estimated_time", "estimated_space"),
        [
            ("invalid", 8 * 1024**3),
            (500.0, "invalid"),
            ("invalid", "invalid"),
        ],
    )
    def test_within_limits_value_error(
        self, resource_manager_custom, estimated_time, estimated_space
    ):
        """Test is_within_limits with values that cannot be converted to float."""
        result = resource_manager_custom.is_within_limits(
            estimated_time, estimated_space
        )
        assert result is False


class TestResourceManagerUpdateAndGetLimits:
    def test_update_limits(self, resource_manager_default):
        """Test updating the resource limits."""
        new_time = 2000.0
        new_space = 12 * 1024**3  # 12 GB
        resource_manager_default.update_limits(new_time, new_space)
        limits = resource_manager_default.get_limits()
        assert limits["max_time"] == new_time
        assert limits["max_space"] == new_space

    def test_get_limits(self, resource_manager_custom):
        """Test retrieving the current resource limits."""
        limits = resource_manager_custom.get_limits()
        assert limits["max_time"] == 1000.0
        assert limits["max_space"] == 8 * 1024**3


# ==============================
# Performance-Related Tests
# ==============================


@pytest.mark.timeout(2)  # Ensure that the test completes within 2 seconds
def test_resource_manager_performance(resource_manager_default):
    """Test that ResourceManager methods perform within acceptable time."""
    # This test ensures that methods execute quickly; actual performance testing would
    # require more setup
    assert resource_manager_default.get_limits() is not None
    assert resource_manager_default.is_within_limits(100, 1000) is not None


# ==============================
# Boundary Condition Tests
# ==============================


class TestResourceManagerBoundaries:
    def test_zero_limits(self):
        """Test ResourceManager with zero limits."""
        rm = ResourceManager(max_time=0.0, max_space=0)
        assert rm.is_within_limits(0, 0) is True
        assert rm.is_within_limits(0.1, 0) is False
        assert rm.is_within_limits(0, 0.1) is False

    def test_negative_limits(self):
        """Test ResourceManager with negative limits."""
        with pytest.raises(ValueError, match="max_time must be non-negative"):
            ResourceManager(max_time=-100.0, max_space=-1)


# ==============================
# Additional Edge Case Tests
# ==============================


class TestResourceManagerAdditionalEdges:
    def test_is_within_limits_exact_boundary(self, resource_manager_custom):
        """Test is_within_limits exactly on the boundary."""
        result = resource_manager_custom.is_within_limits(1000.0, 8 * 1024**3)
        assert result is True

    def test_is_within_limits_just_below_boundary(self, resource_manager_custom):
        """Test is_within_limits just below the boundary."""
        result = resource_manager_custom.is_within_limits(999.999, 8 * 1024**3 - 1)
        assert result is True

    def test_is_within_limits_just_above_boundary(self, resource_manager_custom):
        """Test is_within_limits just above the boundary."""
        result = resource_manager_custom.is_within_limits(1000.001, 8 * 1024**3 + 1)
        assert result is False

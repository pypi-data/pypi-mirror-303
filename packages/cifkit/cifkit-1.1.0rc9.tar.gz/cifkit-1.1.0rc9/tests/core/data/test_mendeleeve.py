import pytest

from cifkit.data.mendeleev import get_mendeleev_numbers


@pytest.mark.fast
def test_get_mendeleev_numbers():
    data = get_mendeleev_numbers()
    assert len(data) == 85

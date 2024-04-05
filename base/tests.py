import pytest

from base.forms import BusinessForm


# Create your tests here.
@pytest.mark.django_db
@pytest.mark.parametrize(
    "tax_id, name, annual_revenue, validity",
    [
        ("123-1", "Business 1", "500000", True),
        ("123", "Business 2", "aaaa", False),
        (None, "Business 3", -1321, False),
        ("12313", None, 123, False),
        ("", "", "", False),
    ],
)
def test_business_form(tax_id, name, annual_revenue, validity):
    data = {"tax_id": tax_id, "name": name, "annual_revenue": annual_revenue}
    form = BusinessForm(data=data)
    assert form.is_valid() == validity

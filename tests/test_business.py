import pytest


@pytest.mark.django_db
@pytest.mark.parametrize(
    "tax_id, name, annual_revenue, validity",
    [
        ("123-1", "Business 1", "50000", "Declined"),
        ("123-1", "Business 1", "500000", "Undecided"),
        ("123-1", "Business 1", "500001", "Approved"),
    ],
)
def test_validate_credit(api_client, tax_id, name, annual_revenue, validity) -> None:
    """
    Test the create task API
    :param api_client:
    :return: None
    """
    payload = {
        "tax_id": tax_id,
        "name": name,
        "annual_revenue": annual_revenue,
    }

    # Create a task
    response_create = api_client.post("/api/validate_credit/", data=payload, format="json")
    validate_credit = response_create.data["data"]
    assert response_create.status_code == 200
    assert validate_credit == validity

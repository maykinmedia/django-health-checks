from django.test import Client
from django.urls import reverse


def test_view_injected_collector(client: Client):
    checks_url = reverse(
        "health-checks-injected-collector"
    )  # Uses injected checks collector.

    response = client.get(checks_url)

    assert response.status_code == 200
    assert response.json() == [
        {"success": False, "identifier": "dummy_fail", "message": "Everything is sad."}
    ]


def test_view_injected_checks(client: Client):
    checks_url = reverse("health-checks-injected-checks")  # Uses injected checks.

    response = client.get(checks_url)

    assert response.status_code == 200
    assert response.json() == [
        {"success": False, "identifier": "dummy_fail", "message": "Everything is sad."}
    ]


def test_view_with_success(client: Client):
    checks_url = reverse(
        "health-checks-injected-collector"
    )  # Uses injected checks collector.

    response = client.get(checks_url, query_params={"include_success": "yes"})

    assert response.status_code == 200
    assert response.json() == [
        {"success": True, "identifier": "dummy", "message": "Everything is great."},
        {"success": False, "identifier": "dummy_fail", "message": "Everything is sad."},
    ]

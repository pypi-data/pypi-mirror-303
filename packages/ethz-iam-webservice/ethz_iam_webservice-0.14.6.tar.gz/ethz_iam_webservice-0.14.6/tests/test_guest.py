import pytest
from ethz_iam_webservice import person


@pytest.mark.parametrize(
    "guest_data,guest_data_transformed",
    [
        (
            {
                "startDate": "2021-06-10",
                "endDate": "2022-07-01",
                "dateOfBirth": "2000-08-01",
            },
            {
                "startDate": "10.06.2021",
                "endDate": "01.07.2022",
                "dateOfBirth": "01.08.2000",
            },
        )
    ],
)
def test_guest_data_to_server(guest_data, guest_data_transformed):
    guest = person.Guest(conn="", data=guest_data)
    body = guest._server_body()

    for date_field in guest.date_fields:
        if date_field in body:
            assert body[date_field] == guest_data_transformed[date_field]


@pytest.mark.parametrize(
    "guest_data_from_server,guest_data_transformed",
    [
        (
            {
                "startDate": "10.06.2021",
                "endDate": "01.07.2022",
            },
            {
                "startDate": "2021-06-10",
                "endDate": "2022-07-01",
            },
        )
    ],
)
def test_guest_data_from_server(guest_data_from_server, guest_data_transformed):
    guest = person.Guest(conn="", data=guest_data_from_server)
    body = guest._data_formatted()

    for date_field in guest.date_fields:
        if date_field in body:
            assert body[date_field] == guest_data_transformed[date_field]


@pytest.mark.parametrize(
    "guest_data_from_server,guest_data_transformed",
    [
        (
            {
                "startDate": "2021-06-10",
                "endDate": "2022-07-01",
            },
            {
                "startDate": "10.06.2021",
                "endDate": "01.07.2022",
            },
        )
    ],
)
def test_guest_data_to_server_more(guest_data_from_server, guest_data_transformed):
    guest = person.Guest(conn="", data=guest_data_from_server)
    body = guest._server_body()

    for date_field in guest.date_fields:
        if date_field in body:
            assert body[date_field] == guest_data_transformed[date_field]

import datetime
from os import getenv


def test_footer_text(client):
    """This test checks the footer text in home page"""
    response = client.get("/")
    test_string = "My Tech Manual"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data


def test_footer_text_year(client):
    """This tests checks if current year is printed in footer text"""
    response = client.get("/")
    current_date_time = datetime.datetime.now()
    date = current_date_time.date()
    year = date.strftime("%Y")
    content = bytes(year, 'utf-8')
    assert response.status_code == 200
    assert content in response.data

"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a  href="/git">Git</a>' in response.data
    assert b'<a  href="/docker">Docker</a>' in response.data
    assert b'<a  href="/flask">Flask</a>' in response.data
    assert b'<a  href="/cicd">CI/CD</a>' in response.data
    assert b'<a  href="/oop_glossary">OOP-Glossary</a>' in response.data
    assert b'<a  href="/oops">OOPs</a>' in response.data
    assert b'<a  href="/solid">Coding Principles</a>' in response.data
    assert b'<a  href="/aaa_test">AAA Testing</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"About me" in response.data


def test_request_git_page(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git : Basic Manual" in response.data


def test_request_docker_page(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_request_flask_page(client):
    """This makes the index page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"Flask : Web Framework" in response.data


def test_request_cicd_page(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data

def test_request_glossary_page(client):
    """This makes the index page"""
    response = client.get("/oop_glossary")
    assert response.status_code == 200
    assert b"Object Oriented Programming" in response.data

def test_request_oops_page(client):
    """This makes the index page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b"The 4 pillars of Object-Oriented Programming" in response.data

def test_request_solid_page(client):
    """This makes the index page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"Article on SOLID Coding & Design Patterns in Python" in response.data

def test_request_aaa_page(client):
    """This makes the index page"""
    response = client.get("/aaa_test")
    assert response.status_code == 200
    assert b"Unit Testing and the Arrange, Act and Assert (AAA) Pattern" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404

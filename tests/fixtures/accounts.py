import pytest


@pytest.fixture
def deployer(accounts):
    return accounts[0]


@pytest.fixture
def user(accounts):
    return accounts[1]

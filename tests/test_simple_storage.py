from brownie import accounts, SimpleStorage


def test_init_val():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 0
    # Assert
    assert expected == simple_storage.retrieve()


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 12
    simple_storage.store(expected, {"from": account})
    # Assert
    assert expected == simple_storage.retrieve()

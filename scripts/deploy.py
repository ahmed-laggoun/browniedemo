from brownie import config, network, SimpleStorage, FundMe, MockV3Aggregator
from scripts.helper import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploySimpleStorage():
    account = get_account()
    simpleStorage = SimpleStorage.deploy({"from": account})
    x = simpleStorage.retrieve()
    print(x)
    tx = simpleStorage.store(12, {"from": account})
    tx.wait(1)
    print(simpleStorage.retrieve())


def deploy_fundMe():
    account = get_account()
    # Pass the price feed address to our fundme contract
    # if we are on persistent network like rinkeby, use the associated
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    # deploySimpleStorage()
    deploy_fundMe()

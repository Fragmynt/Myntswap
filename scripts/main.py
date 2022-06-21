from brownie import UniswapV2Factory
from scripts.utils import get_account


owner_account= get_account(0)
print(owner_account)
factory = UniswapV2Factory.deploy(owner_account.address, {"from": owner_account.address})
print(factory.INIT_CODE_HASH.call())



def main():
    pass
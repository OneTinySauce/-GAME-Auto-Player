import CoinCollect

class CoinCollectTest(CoinCollect.CoinCollectClass):
    pass
#Tests for Coin Collection (Need to test Player Class first)
def test_coinCollect():
    assert CoinCollectTest().collectCoin() == 'Passed'
import ExlixirCollect

class ElixirCollecTest(ExlixirCollect.ExlixirCollectClass):
    pass
#test for elixir collect (need to test PlayerClass first)
def test_elixirCollect():
    assert ElixirCollecTest().collectElixir() == 'Passed'
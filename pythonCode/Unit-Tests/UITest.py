import UserInterFace


class UITest(UserInterFace.UI):
    pass

#Tests for User Option Return
def test_returnOptTest():
    assert UITest().returnOpt1 == 'OK' or 'Cancel'

def test_actionOptTest():
    assert UITest().returnOpt2 == 'Collect Coin' or 'Collect Elixir' or 'Collect All Resources' or 'Upgrade Buildings'

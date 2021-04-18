import PlayerClass
#imports PlayerClass
class PlayerClassTest(PlayerClass.PlayerInitiateClass):
    pass
#test for WindowsClick
def test_windwosclick():
    assert PlayerClassTest().WindowsClick() == 'Passed'
#test for Nox Search
def test_noxSearch():
    assert PlayerClassTest().NoxSearch() == None
#test for Game Button
def test_gameButton():
    assert PlayerClassTest().GameButton() == 'Passed'
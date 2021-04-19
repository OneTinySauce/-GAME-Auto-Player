import pytest
import ClashOfClansAutoplayer2

##Integration Test

def test_UIInit(capsys):
    assert ClashOfClansAutoplayer2().UIInit() == 'OK'

def test_CoinCollectInit(capsys):
    assert ClashOfClansAutoplayer2().CoinCollectInit() == 'Passed'

def test_ExlixirCoolectInit(capsys):
    assert ClashOfClansAutoplayer2().ExlixirCoolectInit() == 'Passed'

def test_GameClassInit(capsys):
    assert ClashOfClansAutoplayer2().GameClassInit() == 'Passed'

def test_PlayerClassInit(capsys):
    assert ClashOfClansAutoplayer2().PlayerClassInit() == 'Passed'

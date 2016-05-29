import pytest

@pytest.mark.codec_x
def test_codec_x():
    print "from codec_x X"

@pytest.mark.codec_y
def test_codec_y():
    print "from codec_y Y"

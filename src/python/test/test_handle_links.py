
from handle_links import convert_url  # type: ignore


def test_convert_url():
    url = "https://drive.google.com/file/d/1Jdyu94wuNAbiKldtgwWPJYqGSeLeGV5i/view?usp=sharing"
    expected = '<p align="center">\n\t<img src="https://lh3.googleusercontent.com/d/1Jdyu94wuNAbiKldtgwWPJYqGSeLeGV5i" width="400"/>\n</p>'
    assert convert_url(url) == expected

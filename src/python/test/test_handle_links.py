
from src.python.handle_links import convert_url  # type: ignore


def test_convert_url():
    url = "https://drive.google.com/file/d/1Jdyu94wuNAbiKldtgwWPJYqGSeLeGV5i/view?usp=sharing"
    expected = '''<p align="center">
        <img src="https://lh3.googleusercontent.com/d/17ggezi9SP4a1_8GIzMJxV8b1VBbzhMFZ" width="400"/>
    </p>'''
    assert convert_url(url) == expected

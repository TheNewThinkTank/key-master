"""
Convert links from Google Drive,
to render them from e.g. GitHub Pages as MarkDown.
"""

from functools import wraps


def add_paragraph(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        html = '<p align="center">\n\t'
        html += func(*args, **kwargs)
        html += '\n</p>'
        return html
    return wrapper


@add_paragraph
def convert_url(google_drive_item_url: str) -> str:
    tmp = google_drive_item_url.split("/d/")[-1]
    _id = tmp.removesuffix("/view?usp=sharing")
    return f'<img src="https://lh3.googleusercontent.com/d/{_id}" width="400"/>'

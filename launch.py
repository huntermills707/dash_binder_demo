import os

def setup_dash():
    here = os.path.dirname(os.path.abspath(__file__))
    return {
        "command": ["python", os.path.join(here, "app.py")],
        "port": 8050,
        "timeout": 30,
        "absolute_url": False,
    }

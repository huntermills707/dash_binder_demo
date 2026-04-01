def setup_dash():
    return {
        "command": ["python", "app.py"],
        "port": 8050,
        "timeout": 30,
        "absolute_url": False,
    }

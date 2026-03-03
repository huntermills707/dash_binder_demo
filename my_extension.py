from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve my app"""
    Popen(["python", "my_app.py"])

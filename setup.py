from setuptools import setup

setup(
    name="dash-binder",
    version="0.1",
    install_requires=[
        "jupyter-server-proxy",
    ],
    entry_points={
        "jupyter_serverproxy_servers": [
            "dash = launch:setup_dash",
        ]
    },
)

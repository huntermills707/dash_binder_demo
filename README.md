# Dash on Binder — Auto-Launch Demo

A minimal demo showing how to run a [Plotly Dash](https://dash.plotly.com/) app on [Binder](https://mybinder.org) that launches automatically from a single link. No notebooks, no terminal commands, and no button clicks.

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/huntermills707/dash_binder_demo/main?urlpath=dash/)

## What is Binder?
 
[Binder](https://mybinder.org) is a free, open-source service that turns a GitHub repo into a live, interactive environment — no installation required. You give it a repo, it builds a Docker image with your dependencies, and gives you a shareable link that anyone can click to get a running copy. It's commonly used for sharing reproducible notebooks, tutorials, and demos. Environments spin up on demand and shut down after about 10 minutes of inactivity, so it's ideal for demos and exploration, not production hosting.
 
This repo demonstrates how to go a step further and serve a full Dash web app through Binder, not just a notebook.

## How it works

Binder is built around Jupyter, so it doesn't natively serve standalone web apps. The trick is [jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy), which can run arbitrary processes behind Jupyter's proxy. A `setup.py` entry point registers the Dash app under the name `dash`, and when a user visits the Binder link with `?urlpath=dash/`, the proxy automatically starts the app and redirects the user straight to it.

## Repo structure

| File | Purpose |
|---|---|
| `app.py` | The Dash application |
| `launch.py` | Tells jupyter-server-proxy how to start the app |
| `setup.py` | Registers the entry point so the proxy discovers it |
| `requirements.txt` | Python dependencies installed during the Binder build |
| `postBuild` | Runs `pip install -e .` to wire up the entry point |

## Key details

**`requests_pathname_prefix` must match the proxy path.** On Binder, the app isn't served from `/` — it's behind a path like `/user/<username>/dash/`. Dash needs to know this so it generates correct URLs for its scripts and callbacks. In `app.py`, this is handled by reading the `JUPYTERHUB_SERVICE_PREFIX` environment variable that Binder sets automatically:

```python
service_prefix = os.environ.get("JUPYTERHUB_SERVICE_PREFIX", "/")
prefix = service_prefix + "dash/"
app = dash.Dash(__name__, requests_pathname_prefix=prefix)
```

**The entry point name determines the URL path.** In `setup.py`, the entry point is registered as `"dash = launch:setup_dash"`. This means the app is accessible at `/dash/`, which is what `?urlpath=dash/` points to in the Binder link.

**`postBuild` must be executable.** If you clone this repo and modify `postBuild`, make sure it stays executable:

```bash
git update-index --chmod=+x postBuild
```

## Adapting this for your own app

1. Fork or copy this repo.
2. Replace the contents of `app.py` with your Dash application.
3. Add any additional dependencies to `requirements.txt`.
4. Keep the `requests_pathname_prefix` setup in `app.py` — without it, your app will load a blank page.
5. Update the Binder badge URL in this README to point to your repo.

## License

[MIT](LICENSE)

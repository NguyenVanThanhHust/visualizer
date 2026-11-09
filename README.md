# 3d-visualizer
Simple 3D visualizer from scratch, built on pygame.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Installation

```bash
git clone git@github.com:NguyenVanThanhHust/visualizer.git
cd visualizer
uv sync
```

`uv sync` creates `.venv` and installs the project in editable mode along with its dependencies (pygame).

To build a wheel or source distribution:

```bash
uv build
```

## Usage

Open the basic window (800×600). Close it to exit.

```bash
uv run python tests/basic_window.py
```

Use the API from Python:

```python
from visualizer import App

app = App()
app.run()
```

## Testing

Run the window test on a machine with a display. Close the window to finish.

To run it without a display (for example over SSH or in CI), use SDL's dummy drivers and a timeout. A timeout exit (code 124) means the window loop ran without crashing:

```bash
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy timeout 5 uv run python tests/basic_window.py; echo "exit=$?"
```

pytest is installed as a dev dependency, but there are no pytest tests yet (`basic_window.py` is a manual script). Once you add `test_*.py` files, run:

```bash
uv run pytest
```

## Project layout

```
src/visualizer/
├── __init__.py        # public API: App, Window
├── version.py
└── core/
    ├── app.py         # App: lifecycle, event handling, main loop
    └── window.py      # Window: pygame display setup and drawing
tests/
└── basic_window.py    # opens a window and runs the app loop
main.py                # placeholder entry point
```

## Troubleshooting

- **`ModuleNotFoundError: No module named 'visualizer'`**: run commands with `uv run`, not a bare `python`. If a conda environment is active, run `conda deactivate` first.
- **`cannot import name 'App' from 'visualizer'`**: check that `src/visualizer/__init__.py` exists with a `.py` extension.

## License

See [LICENSE](LICENSE).

# Project Title

A brief description of your PySide6 UV Template project.

## Build locally
1. Clone this repository.  
2. Install uv with our standalone installers:

    ```bash
    # On macOS and Linux.
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    ```bash
    # On Windows.
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

    Or, from [PyPI](https://pypi.org/project/uv/):

    ```bash
    # With pip.
    pip install uv
    ```

    ```bash
    # Or pipx.
    pipx install uv
    ```

3. Use `uv sync` to download depedencies.

4. Use `uv run main.py` to run the project.

## Release
1. Create a new release on GitHub.
2. The release will be automatically published in the Release attachment.

## License
Distributed under the MIT License.

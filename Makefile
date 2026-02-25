.PHONY: build test clean

clean:
	rm -rf dist build *.egg-info .test-venv

build: clean
	uv build -v

test: build
	uv run python -c "import ofgrenudo; print(ofgrenudo.__file__)"
	uv venv .test-venv
	uv pip install --python .test-venv/bin/python --upgrade pip
	uv pip install --python .test-venv/bin/python dist/*.whl
	.test-venv/bin/python -c "import ofgrenudo; print(ofgrenudo.__file__)"
	.test-venv/bin/ofgrenudo --version || true
	.test-venv/bin/ofgrenudo

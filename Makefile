.PHONY: build test clean

clean:
	rm -rf dist build *.egg-info

build: clean
	uv build -v

test: build
	uv run python -c "import ofgrenudo; print(ofgrenudo.__file__)"

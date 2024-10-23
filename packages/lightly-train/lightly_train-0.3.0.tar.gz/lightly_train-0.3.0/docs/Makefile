### Documentation

VERSION ?= $(shell grep '__version__' ../src/lightly_train/__init__.py | sed -E 's/[^0-9.]//g')
BUILD_DIR = build
# The build directory for the current version. We create a new directory for each
# version to simplify hosting the documentation for multiple versions. This follows
# the pattern used by PyTorch: https://pytorch.org/docs/versions.html
BUILD_VERSION_DIR = ${BUILD_DIR}/${VERSION}
BUILD_STABLE_DIR = ${BUILD_DIR}/stable
SOURCE_DIR = source


# Build docs for the current version.
.PHONY: docs
docs:
	sphinx-build --builder html ${SOURCE_DIR} ${BUILD_VERSION_DIR}
	python build.py --build-dir ${BUILD_DIR}

# Build docs for the stable version. Assumes that the current version is the stable
# version.
.PHONY: docs-stable
docs-stable:
	sphinx-build --builder html ${SOURCE_DIR} ${BUILD_STABLE_DIR}
	python build.py --build-dir ${BUILD_DIR}

# Serve the documentation on localhost.
.PHONY: serve
serve:
	python -m http.server 1234 --directory ${BUILD_DIR}

.PHONY: clean
clean:
	rm -rf ${BUILD_DIR}

.PHONY: format
format:
	make -C .. format

.PHONY: format-check
format-check:
	make -C .. format-check
install-dev-version:
	pip3 install -e .

install-from-pipy:
	python3 -m pip install --upgrade tlfs

upload:
	rm -rf dist/*
	python3 -m build
	python3 -m twine upload dist/* --verbose

tests: install-dev-version
	cd /tmp && \
	rm -rf *.xlsx  && \
	tlfs ~/src/pypkg/tlfs/examples/example1.xlsx  && \
	# tlfs ~/src/pypkg/tlfs/examples/example2.xlsx  && \
	libreoffice *.xlsx

# wrongexamples: install-dev-version
# 	cd /tmp && \
# 	rm -rf *.xlsx  && \
# 	tlfs ~/src/pypkg/tlfs/examples/wrong1.xlsx  && \
# 	libreoffice *.xlsx

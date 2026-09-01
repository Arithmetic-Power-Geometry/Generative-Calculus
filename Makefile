.PHONY: test reproduce all app clean

test:
	pytest -q

reproduce:
	python -m generative_calculus.reproduce

all: test reproduce

app:
	python app.py

clean:
	rm -rf results .pytest_cache **/__pycache__

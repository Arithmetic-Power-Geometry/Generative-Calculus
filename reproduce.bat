@echo off
python -m pip install -e .[test]
pytest -q
python -m generative_calculus.reproduce
pause

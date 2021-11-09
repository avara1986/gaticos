echo "******* EXECUTE BLACK"
black .
echo "******* EXECUTE ISORT"
isort .
echo "******* EXECUTE PYLINT"
pylint gaticos
echo "******* EXECUTE MYPY"
mypy gaticos
echo "******* EXECUTE PYTEST"
pytest -s --cov gaticos tests/
# --cov-report html
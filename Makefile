SOURCE_DIR_API=dudesplay_api
TESTS_DIR=tests


tests:
	poetry run pytest -vv ${TESTS_DIR}

run:
	poetry run python -m $(SOURCE_DIR_API)
#!/bin/bash

pytest --browser_name=firefox --language fr -v -s ./test_items.py
pytest --browser_name=chrome --language fr -v -s ./test_items.py
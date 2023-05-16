#!/bin/bash

rm -R ./tmp/
pytest --browser_name=chrome --language fr --user_data_dir ./tmp/ -v -s ./test_items.py
pytest --browser_name=firefox --language fr -v -s ./test_items.py
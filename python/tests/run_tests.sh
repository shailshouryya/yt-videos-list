rm -r build 2>/dev/null
python3 minifier.py
pip3 install .
python3 tests/test_all_drivers.py
python3 tests/test_dependencies_json.py

echo "Finished running unit tests!"
echo "Now exiting run_tests.sh ...."

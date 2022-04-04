sh      tests/setup.sh
python3 tests/test_all_drivers.py
python3 tests/test_dependencies_json.py

echo "Finished running unit tests!"
echo "Now exiting run_tests.sh ...."

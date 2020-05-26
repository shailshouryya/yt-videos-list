python3 tests/test_cross_platform.py
python3 tests/test_safaridriver.py
python3 tests/test_msedgedriver.py
python3 tests/test_notifications.py > tests/drivers_list_output.log

echo "Finished running unit tests!"
echo "Now exiting run_tests.sh ...."

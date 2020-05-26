python tests\test_cross_platform.py
python tests\test_safaridriver.py
python tests\test_msedgedriver.py
python tests\test_notifications.py > tests\drivers_list_output.log

echo "Finished running unit tests!"
echo "Now exiting run_tests.bat ...."

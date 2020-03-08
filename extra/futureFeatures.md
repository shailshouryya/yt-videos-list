## Program Functionality
## Main Features
- [X] take url and scrape the video name and url for every video for that user
- [X] create csv
- [ ] get date published (probably not possible without significantly increasing runtime, could get how long ago video was published, but that tends to be unspecific)

## Additional Features
- [ ] create web interface
  - [ ] input box for channel url
- [ ] ouput CSV with custom name
- [ ] generate static HTML page with video URLs
- [ ] update previously generated CSV with new videos uploaded since CSV generation
  - [ ] using some kind of delta sync

## References
- [Difference between webdriver.firefox.marionette & webdriver.gecko.driver](https://stackoverflow.com/questions/43272919/difference-between-webdriver-firefox-marionette-webdriver-gecko-driver) - Stack Overflow
- [What are the benefits of using Marionette FirefoxDriver instead of the old Selenium FirefoxDriver for a Selenium tester?](https://stackoverflow.com/questions/38916650/what-are-the-benefits-of-using-marionette-firefoxdriver-instead-of-the-old-selen/38917100#38917100) - Stack Overflow
- [selenium.common.exceptions.SessionNotCreatedException: Message: Unable to find a matching set of capabilities with GeckoDriver, Selenium and Firefox](https://stackoverflow.com/questions/52002958/selenium-common-exceptions-sessionnotcreatedexception-message-unable-to-find-a) - Stack Overflow

- Put check for `userDriver is None` first since you can't iterate over `None` as you can iterate over strings. This comes up in the checkDriver() method in execute.py
  - `TypeError: argument of type 'NoneType' is not iterable`
- [selenium.common.exceptions](https://selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html)
- running as a module (as of commit 2dbc5a15ab83a79aeeb884a106062ef2b1f52c76):
```
python3 -m yt_videos_list
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py:125: RuntimeWarning: 'yt_videos_list.__main__' found in sys.modules after import of package 'yt_videos_list', but prior to execution of 'yt_videos_list.__main__'; this may result in unpredictable behaviour
  warn(RuntimeWarning(msg))
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/yt_videos_list/__main__.py", line 103, in <module>
    main()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/yt_videos_list/__main__.py", line 100, in main
    script.generate_list()
NameError: name 'script' is not defined
```

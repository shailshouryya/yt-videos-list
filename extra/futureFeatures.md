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

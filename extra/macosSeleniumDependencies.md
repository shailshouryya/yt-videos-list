# Setting up your Selenium Dependencies
## MacOS
### geckodriver (Firefoxdriver)
The given command downloads a geckodriver ("Firefoxdriver") version that is compatible with Firefox versions ≥ 60. To see more information about the differences compared to older versions, please visit https://github.com/mozilla/geckodriver/releases)

Copy the given command (or modify it if using an older version from the link above), open a new terminal session (usually possible with CMD+N or CMD+T from an active terminal session), and paste the command you just copied. Once you've done that, you should be able to come back to this session and rerun the last command without an error!

macos geckodriver (Firefoxdriver) v0.26.0
<br>`curl -SL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz | tar -xzvf - -C /usr/local/bin/'`

For more information about the geckodriver, please visit https://github.com/mozilla/geckodriver

### operadriver
Your Opera browser version should match the "supports Opera ## release" below.

Once you determine the right version to download, copy the command, open a new terminal session (usually possible with CMD+N or CMD+T from an active terminal session), and paste the command you just copied. Once you've done that, you should be able to come back to this session and rerun the last command without an error!

mac64 Operadriver 78.0.3904.87 (supports Opera Stable 65 release)
<br>`curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.78.0.3904.87/operadriver_- mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum`

mac64 Operadriver 77.0.3865.120 (supports Opera 64 release)
<br>`curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.77.0.3865.120/operadriver_- mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum`

mac64 Operadriver 76.0.3809.132 (supports Opera 63 release)
<br>`curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.76.0.3809.132/operadriver_- mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum`

mac64 Operadriver 75.0.3770.100 (supports Opera 62 release)
<br>`curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.75.0.3770.100/operadriver_- mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum`

mac64 Operadriver 2.45 (supports Opera 60 release)
<br>`curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.45/operadriver_- mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum`

mac64 Operadriver 2.42 (supports Opera 58 release)
<br>`curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.42/operadriver_- mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum`

mac64 Operadriver 2.41 (supports Opera 57 release)
<br>`curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.41/operadriver_- mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum`

mac64 Operadriver 2.40 (supports Opera 56 release)
<br>`curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.40/operadriver_- mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum`

mac64 Operadriver 2.38 (supports Opera 55 release)
<br>`curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.38/operadriver_- mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum`

mac64 Operadriver 2.37 (supports Opera 54 release)
<br>`curl -SL https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.37/operadriver_- mac64.zip | tar -xzvf - -C /usr/local/bin/ --strip-components=1 && rm /usr/local/bin/sha512_sum`

For more information about the operadriver, please visit https://github.com/operasoftware/operachromiumdriver

### safaridriver
In order to run safaridriver, you need to enable remote automation. To do so, open up the Safari browser and in the menu bar, go to

"Safari" -> "Preferences" -> "Advanced" tab -> click "Show develop menu in menu bar"

Once you do that, "Develop" should appear in your menu bar. Click on the "Develop" bar, and then enable "Allow Remote Automation" (should be near the bottom of the list).

After doing that, try rerunning the last command!

:)

### chromedriver
Your Chrome browser version should match the first numbers before the decimal place of the chromedriver version below.

Once you determine the right version to download, copy the command, open a new terminal session (usually possible with CMD+N or CMD+T from an active terminal session), and paste the command you just copied. Once you\'ve done that, you should be able to come back to this session and rerun the last command without an error!

mac64 Chromedriver 79.0.3945.36
<br>`curl -SL https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/`

mac64 Chromedriver 78.0.3904.105
<br>`curl -SL https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/`

mac64 Chromedriver 77.0.3865.40
<br>`curl -SL https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/`

mac64 Chromedriver 76.0.3809.126
<br>`curl -SL https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/`

mac64 Chromedriver 75.0.3770.140
<br>`curl -SL https://chromedriver.storage.googleapis.com/75.0.3770.140/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/`

mac64 Chromedriver 74.0.3729.6
<br>`curl -SL https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/`

mac64 Chromedriver 73.0.3683.68
<br>`curl -SL https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/`

mac64 Chromedriver 2.46 (Supports Chrome v71-73)
<br>`curl -SL https://chromedriver.storage.googleapis.com/2.46/chromedriver_mac64.zip | tar -xzvf - -C /usr/local/bin/`

For more information about the chromedriver, please visit https://sites.google.com/a/chromium.org/chromedriver/home

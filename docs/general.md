# General Overview
This package is intended to provide a quick, simple way to create a list of all videos posted to any YouTube channel by providing just the URL to that user's channel videos. There are two types of YouTube channels: one type is a `user` channel and the other is a `channel` channel.
- user` channel type:
  - sentdex: https://www.youtube.com/user/sentdex
  - Disney: https://www.youtube.com/user/disneysshows
  - Marvel: https://www.youtube.com/user/MARVEL
  - Apple: https://www.youtube.com/user/Apple
- `channel` channel type:
  - Tasty: https://www.youtube.com/channel/UCJFp8uSYCjXOMnkUyb3CQ3Q
  - Billie Eilish: https://www.youtube.com/channel/UCiGm_E4ZwYSHV3bcW1pnSeQ
  - Gordon Ramsay: https://www.youtube.com/channel/UCIEv3lZ_tNXHzL3ox-_uUGQ
  - PBS Space Time: https://www.youtube.com/channel/UC7_gcs09iThXybpVgjHZ_7g

To scrape the video titles along with the link to the video, you need to run the `lc.create_list_for(url)` method on the ListCreator object (create with `lc = ListCreator()`). By default, the name of the file produced will be `channel`_videos_list.ext where the `.ext` will be `.csv` or `.txt `, depending on the type of file(s) that you specified.

## Dependencies
**NOTE**: You do need to have the Selenium driver installed to run this package - the first time you run this package the automated downloader should install everything you need, but in case it doesn't, refer to the link below and/or file an [issue here](https://github.com/Shail-Shouryya/yt_videos_list/issues). The Selenium drivers are all pretty similar but differ in subtle ways, so play around with them and see what's different :)
#### Copy paste the code block that's relevant for the OS of your machine for the Selenium driver(s) you want from **[here](https://github.com/Shail-Shouryya/yt_videos_list/blob/master/dependencies_pseudo_json.txt)**
**NOTE** that you also need the corresponding browser installed to properly run the selenium driver.
- To download the most recent version of the browser, go to the page for:
  - [Firefox](https://www.mozilla.org/en-US/firefox/new/)
  - [Opera](https://www.opera.com/)
  - [Chrome](https://www.google.com/chrome/)
  - [Brave](https://brave.com/)
  - [Edge](https://www.microsoft.com/edge)


## [Future Features](https://github.com/Shail-Shouryya/yt_videos_list/blob/master/docs/futureFeatures.md)


## [Technical Specifications](https://github.com/Shail-Shouryya/yt_videos_list/blob/master/docs/technicalSpecifications.md)

rm -r build 2>/dev/null
rm -r yt_videos_list.egg-info
python3 minifier.py
pip3 install . --use-feature=in-tree-build

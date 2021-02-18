# netspeedtest
A simple Python script to take a daily reading of my internet speeds and logs them to a Google Sheet.

This was written as a solution to a problem I was having with my home internet. This script uses the Speedtest.net [python package](https://pypi.org/project/speedtest-cli/) to gather internet speed information and then pushes them to a google sheet for logging and analytics.

I use Windows Task Scheduler to run this automatically at midday every day or when next my computer is active.

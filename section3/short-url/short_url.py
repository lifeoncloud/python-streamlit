import pyshorteners

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    return short_url

# 예제
long_url = "https://docs.google.com/spreadsheets/d/1NUcYVQ3nmeEysmEG4kmHnDmQD89y9Fo3ufPMDdFte6E/edit?gid=2075095179#gid=2075095179"
short_url = shorten_url(long_url)
print("Short URL:", short_url)

import hashlib

class URLShortener:

    def __init__(self):
        self.urls = {}

    def shorten(self, url):
        short = hashlib.md5(url.encode()).hexdigest()[:6]
        self.urls[short] = url
        return short

    def lookup(self, short):
        return self.urls.get(short)

obj = URLShortener()

short = obj.shorten("https://google.com")

print("Short URL:", short)
print("Original URL:", obj.lookup(short))
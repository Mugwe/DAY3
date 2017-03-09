from urllib2 import Request, urlopen, URLError

request = Request('http: // code.google.com / apis / ajax / playground /?exp = youtube')
try:
        response = urlopen(request)
        video = response.read()
        print video[559:1000]

except URLError, e:
    print 'No video:', e


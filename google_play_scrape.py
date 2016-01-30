from cookielib import CookieJar
from urllib import urlencode
import urllib2

from six import iteritems

class GooglePlayScraper(object):
    """
    Scrapes data for particular app_id from google play store
    """

    URL = 'https://play.google.com'
    ACTION = 'store/apps/details'

    def __init__(self):
        self._url_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))

    def _add_headers(self, request, headers):
        if headers is not None:
            for (key, value) in iteritems(headers):
                request.add_header(key, value)

    def _build_url(self, url, action, arguments):
        request_url = url
        if action is not None:
            request_url = '{url:s}/{action:s}'.format(
                    url=url,
                    action=action,
            )
        if arguments is not None:
            query_url = '{url:s}?{arguments:s}'.format(
                    url=request_url,
                    arguments=urlencode(arguments)
            )
        else:
            query_url = request_url
        return query_url

    def scrape(self, id):
        print 'This just happened'
        url = self.URL
        action = self.ACTION

        arguments = {
            'id': id,
            'hl': 'en'
        }
        response = self._get_data_from_rest_request(action, arguments, url)
        cover_image_url = 'https:' + response.split('img class="cover-image" src=\"')[1].split('\"')[0]
        


        return

    def _get_data_from_rest_request(self, action, arguments, url):
        query_url = self._build_url(url, action, arguments)
        request = urllib2.Request(query_url)
        response = self._url_opener.open(request).read()
        return response


gps = GooglePlayScraper()
gps.scrape('com.skgames.trafficrider')
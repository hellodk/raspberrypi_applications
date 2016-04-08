'''
Class implementing tython streamer
'''
from twython import TwythonStreamer
import raspberrypi_settings as rps


count = 0


class MyStreamer(TwythonStreamer):

    def on_success(self, data):
        '''
        callback function, triggered when the desired tweet is found
        '''
        global count
        print "Data is: ", data
        if 'text' in data:
            print "found"
            count = count + 1
            if count == 3:
                print "Ian G. Harris is popular!", count, "found."

    def on_error(self, status_code, data):
        print "Error ", status_code, " ", data

stream = MyStreamer(rps.c_key, rps.c_secret, rps.A_secret, rps.A_token)
print 'Streaming'
stream.statuses.filter(track="Ian G. Harris")
print "Streaming completed!!"


from twython import Twython

C_KEY = '1221'
C_SECRET = 'RYN'
A_TOKEN = '1p'
A_SECRET = 'osr'
api = Twython(C_KEY, C_SECRET, A_TOKEN, A_SECRET)
api.update_status(status="Ian G. Harris 3")

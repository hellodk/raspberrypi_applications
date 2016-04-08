from twython import Twython

c_key = "fjsll123299eeDKMLS"
c_secret = "iX"
A_token = "1Cc"
A_secret = "nlo"
api = Twython(c_key, c_secret, A_token, A_secret)
api.update_status(status="Testing tweets via raspberry pi")

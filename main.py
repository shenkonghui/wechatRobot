import itchat
import time
import qingyunke
from itchat.content import TEXT

@itchat.msg_register([TEXT])
def text_reply(msg):
    time.sleep(2)
    print('%s: %s' % (msg["User"]["NickName"], msg['Text']))
    r = qingyunke.chat(msg['Text'])
    print('%s: %s' % ("我", r))
    return r

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()


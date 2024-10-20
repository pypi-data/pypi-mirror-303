from typing import List, Optional
import logging
import re
import requests
from requests.exceptions import RequestException

TELEGRAM_BOT_SENDMSG_ENDPONT = 'https://api.telegram.org/bot%s/sendMessage'
TELEGRAM_BOT_SENDMSG_PARAM_CHATID = 'chat_id'
TELEGRAM_BOT_SENDMSG_PARAM_MSGTEXT = 'text'
TELEGRAM_BOT_SENDMSG_PARAM_PARSE_MODE = 'parse_mode'
TELEGRAM_BOT_SENDMSG_MAXLENGTH = 4096
TELEGRAM_BOT_SENDMSG_VALUE_PARSE_MODE_HTML = 'HTML'


class TelegramBot():
    def __init__(self, token: str, botname: Optional[str] = None) -> None:
        self.token = token
        self.botname = botname

        # Init logger for whole class
        self.mylogger = logging.getLogger(__name__)

    def postmsg(self, chatID_list: List[str], msg: str) -> int:
        posturl = TELEGRAM_BOT_SENDMSG_ENDPONT % self.token
        
        # Filter restrict char
        outgoing_msg: str = self.__filter(msg if self.botname is None else self.botname + ':' + msg)

        # Trim down length
        if len(outgoing_msg) > TELEGRAM_BOT_SENDMSG_MAXLENGTH:
            outgoing_msg = outgoing_msg[:TELEGRAM_BOT_SENDMSG_MAXLENGTH]
        
        self.mylogger.debug('Start postMsg URL: %s' % posturl)
        self.mylogger.debug('Outgoing msg: %s' % outgoing_msg)

        try:
            for chatID in chatID_list:
                self.mylogger.debug('Posting to chatID: %s' % chatID)

                # Define telegram api json payload
                json_payload = {}
                json_payload[TELEGRAM_BOT_SENDMSG_PARAM_CHATID] = chatID
                json_payload[TELEGRAM_BOT_SENDMSG_PARAM_MSGTEXT] = outgoing_msg
                json_payload[TELEGRAM_BOT_SENDMSG_PARAM_PARSE_MODE] = TELEGRAM_BOT_SENDMSG_VALUE_PARSE_MODE_HTML
                self.mylogger.debug('outputJson: %s' % json_payload)

                response = requests.post(posturl, json=json_payload)
                if response.status_code != requests.codes.ok:
                    self.mylogger.debug('PostMsg error with chatID: %s - response: %s' % (chatID, response.text))
                    return -1
                
                json_response = response.json()
                if not(json_response.get('ok')) or json_response.get('ok') != True:
                    self.mylogger.debug('PostMsg error with chatID: %s - response: %s' % (chatID, response.json()))
                    return -1
                
                self.mylogger.debug('PostMsg done with chatID: %s' % chatID)
                return 0
        except RequestException:
            self.mylogger.exception('Error during postMsg')

        return -2
    
    # Some char cannot be send via tg, so need convert into html entity
    def __filter(self, sourceMsg: str) -> str:
        returnMsg = re.sub(r'&', '&amp;', sourceMsg)
        returnMsg = re.sub(r'<', '&lt;', returnMsg)
        returnMsg = re.sub(r'>', '&gt;', returnMsg)
        return returnMsg
    

#Software Development Kit  
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('cGbRlCx92QIaEDdDqL+as6ZDec4xbeXwPHm9JmbMy2gjla29UBFKMxcb9po+pk3bv1liBjMkV79KuMQf7h5XmP9JYTz39dn9znN9KsV+uaF5YQSpi0a4aKVAg2hlGlt/hI0E1DxS20MkJTMi+bXPRgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6d68c0a95b9b9925a28cadcbd10f9ff0')


@app.route("/callback", methods=['POST'])  #接收line的訊息。
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body 觸發handle程序
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg:event.message.text
    r == ""

    if msg == "hi":
        r == "hi"
    if msg == "Hi":
        r == "Hi"
    elif msg == "ぶひ":
        r == "豚君"


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= r ))


if __name__ == "__main__":    #執行main function的時候，來確定該檔案是直接被執行，而不是被載入而已
    app.run()
 
from flask import Flask
from linebot import LineBotApi, WebhookHandler
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

from app import routes, models_for_line
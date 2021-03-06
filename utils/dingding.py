import json

import requests
from bnp.settings import cfg


def send_dingding_msg(msg, api=cfg.DINGDING.API, title=cfg.DINGDING.TITLE):
    info = f"{msg['date']}\n\n"
    if len(msg['stocks']) == 0:
        info += f"πΆπΆπΆ [{msg['algo']}]\n"
    else:
        info += f"πππ [{msg['algo']}]\n"
        for stock in msg['stocks']:
            if 'algo' in stock:
                info += f"\n> {stock['algo']}"
                info += f"\n> {stock['ts_code']} {stock['name']} {stock['industry']} {stock['market']}"
                info += "\n"
            else:
                info += f"\n> {stock['ts_code']} {stock['name']} {stock['industry']} {stock['market']}"

    data = {"msgtype": "markdown", "markdown": {"title": "θ½¦η₯¨ιι", "text": info}}
    print(data)
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    requests.post(api, json.dumps(data), headers=headers)


def send_dingding_error_msg(msg, api=cfg.DINGDING.API, title=cfg.DINGDING.TITLE):
    info = "πΎπΎπΎ\n\n"
    info += msg

    data = {"msgtype": "markdown", "markdown": {"title": "ζ₯ιδΏ‘ζ―", "text": info}}
    print(data)
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    requests.post(api, json.dumps(data), headers=headers)

#!/usr/bin/env python3

__all__ = [
    'send',
    'send_file',
]

import os
import re
import sys
import json
import time
import base64
import hashlib
import urllib.error
from urllib.request import Request, urlopen


URL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=%s'
JPG_MAGIC = b'\xFF\xD8\xFF'
PNG_MAGIC = b'\x89\x50\x4E\x47'
VME_BOTS_FILE = '~/.config/vme.bots'


def send(key, msg):
    if isinstance(msg, str):
        send_text(URL % key, msg)
        return
    if not isinstance(msg, bytes):
        raise TypeError(f'only string or binary data allowed ({type(msg)})')

    text = None
    try:
        text = msg.decode('utf-8')
    except UnicodeDecodeError:
        pass
    if text:
        send(key, text)
    elif msg.startswith(JPG_MAGIC) or msg.startswith(PNG_MAGIC):
        send_image(URL % key, msg)
    else:
        raise ValueError(f'not text nor PNG/JPG image')


def send_text(url, msg):
    json_request(url, {'msgtype': 'markdown', 'markdown': {'content': msg}})


def send_image(url, data):
    json_request(
        url,
        {
            'msgtype': 'image',
            'image': {
                'md5': hashlib.md5(data).hexdigest(),
                'base64': base64.b64encode(data).decode('ascii'),
            },
        },
    )


def send_file(key, fname):
    raise NotImplementedError('file sending not implemented yet')


def json_request(url, data):
    msg = json.dumps(data).encode('utf-8')
    req = Request(url, data=msg, headers={'Content-Type': 'application/json'})
    reply = robust_request(req)
    if reply['errcode']:
        raise RuntimeError(reply.get('errmsg', ''))


def robust_request(req, timeout=5, retries=3, delay=1):
    err = None
    for i in range(retries):
        try:
            with urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            if i + 1 >= retries:
                err = str(e)
                break
            time.sleep(delay)
    raise RuntimeError(err)


def die_usage():
    print(
        f"Usage:\n"
        f"        vme.py key|name any_file\n"
        f"        vme.py key|name < text_or_image_file\n"
        f"        echo your message | vme.py key|name\n\n"
        f"        Define bot keys in {VME_BOTS_FILE} with 'name key' lines"
    )
    exit(1)


def main():
    if len(sys.argv) < 2:
        die_usage()

    key = get_bot_key(sys.argv[1])

    if sys.stdin.isatty():
        if len(sys.argv) != 3:
            die_usage()
        send_file(key, sys.argv[2])
    else:
        data = sys.stdin.buffer.read()
        send(key, data)


def get_bot_key(spec):
    if is_bot_key(spec):
        return spec

    with open(os.path.expanduser(VME_BOTS_FILE), 'r') as f:
        for line in f:
            vals = line.split()
            if len(vals) == 2 and vals[0] == spec and is_bot_key(vals[1]):
                return vals[1]

    raise RuntimeError(f'bot {spec} not found in {VME_BOTS_FILE}')


def is_bot_key(spec):
    return bool(re.match(r'^\w{8}(-\w{4}){3}-\w{12}$', spec))


if __name__ == '__main__':
    main()

### vme.py ends here

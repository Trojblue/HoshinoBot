import random
import re

import hoshino
from hoshino import Service, aiorequests, priv
from hoshino.typing import CQEvent

sv = Service('deepchat', manage_priv=priv.SUPERUSER, enable_on_default=False)


# # @sv.on_message('group')
# @sv.on_prefix('聊天测试')
# # @sv.on_message()
# async def deepchat(bot, ctx):
#     msg = ctx['message'].extract_plain_text()
#     if msg == "测试消息":
#         if not msg or random.random() > 0.025:
#             return
#         payload = {
#             "msg": msg,
#             "group": ctx['group_id'],
#             "qq": ctx['user_id']
#         }
#         sv.logger.debug(payload)
#         api = hoshino.config.deepchat.deepchat_api
#         rsp = await aiorequests.post(api, data=payload, timeout=10)
#         rsp = await rsp.json()
#         sv.logger.debug(rsp)
#         if rsp['msg']:
#             await bot.send(ctx, rsp['msg'])


@sv.on_prefix('聊天测试')
# @sv.on_message()
async def deepchat(bot, ev: CQEvent):
    msg = ev.message.extract_plain_text()
    if msg == "测试消息":
        if not msg or random.random() > 0.025:
            return
        payload = {
            "msg": msg,
            "group": ev.group_id,
            "qq": ev.user_id
        }
        sv.logger.debug(payload)
        api = hoshino.config.deepchat.deepchat_api
        rsp = await aiorequests.post(api, data=payload, timeout=10)
        rsp = await rsp.json()
        sv.logger.debug(rsp)
        if rsp['msg']:
            await bot.send(ev, rsp['msg'])

import random

import hoshino
from hoshino import Service, aiorequests
from hoshino.typing import CQEvent, CQHttpError

sv = Service('random-repeater', help_='随机复读机')

PROB_A = 1.4
group_stat = {}     # group_id: (last_msg, is_repeated, p)

'''
不复读率 随 复读次数 指数级衰减
从第2条复读，即第3条重复消息开始有几率触发复读

a 设为一个略大于1的小数，最好不要超过2，建议1.6
复读概率计算式：p_n = 1 - 1/a^n
递推式：p_n+1 = 1 - (1 - p_n) / a
'''
# @sv.on_fullmatch(('沙雕机器人', '沙雕機器人'))
# async def say_sorry(bot, ev):
#     await bot.send(ev, 'tr0jan - 沙雕機器人')


@sv.on_prefix('teststring')
async def send_help(bot, ev: CQEvent):
    test_string = '''
=====================
- HoshinoBot使用说明 -
================阿萨德阿萨德UG: Suc
ceed to add prefix trigger `帮
284 nonebot] INFO: Succeeded to im

========
※除这里中cnm这么写字可以吗
※隐藏功能属于赠品 不保证可用性
※本bot开源，可自行搭建
这是一段很长的文字文字文字文字文字文字文字
※您的支阿达阿萨德阿萨德力
※※调教时请注意使用频率，您的滥用可能会导致bot账号被封禁

'''.strip()
    await bot.send(ev, test_string)

# @sv.on_message()
# async def random_repeater(bot, ev: CQEvent):
#     group_id = ev.group_id
#     msg = str(ev.message)
#
#     if group_id not in group_stat:
#         group_stat[group_id] = (msg, False, 0)
#         return
#
#     last_msg, is_repeated, p = group_stat[group_id]
#     if last_msg == msg:     # 群友正在复读
#         if not is_repeated:     # 机器人尚未复读过，开始测试复读
#             if random.random() < p:    # 概率测试通过，复读并设flag
#                 try:
#                     group_stat[group_id] = (msg, True, 0)
#                     await bot.send(ev, msg)
#                 except CQHttpError as e:
#                     hoshino.logger.error(f'复读失败: {type(e)}')
#             else:                      # 概率测试失败，蓄力
#                 p = 1 - (1 - p) / PROB_A
#                 group_stat[group_id] = (msg, False, p)
#     else:   # 不是复读，重置
#         group_stat[group_id] = (msg, False, 0)

# @sv.on_prefix('前缀')
# async def random_repeater(bot, ev: CQEvent):
#     episode = ev.message.extract_plain_text()
#
#     msg = f'成功! 前缀后面的内容是{episode}'
#     await bot.send(ev, msg)

@sv.on_prefix('聊')
async def random_repeater(bot, ev: CQEvent):
    msg = ev.message.extract_plain_text()

    if ev.group_id == 582368081:    # 测试群
        respond_prob = 1.0
    elif ev.group_id == 863688150 and len(msg) > 5 and len(msg) < 15:
        respond_prob = 0.05
    else:
        respond_prob = 0
    

        return

    payload = {
        "msg": msg,
        "group": ev.group_id,   #群号
        "qq": ev.user_id    #qq号
    }
    sv.logger.debug(payload)
    # api = hoshino.config.deepchat.deepchat_api
    api = "http://127.0.0.1:7777/message"
    rsp = await aiorequests.post(api, data=payload, timeout=10)
    rsp = await rsp.json()
    sv.logger.debug(rsp)
    if rsp['msg'] and  random.random() < respond_prob:    # 满足概率:
        await bot.send(ev, rsp['msg'])



def _test_a(a):
    '''
    该函数打印prob_n用于选取调节a
    注意：由于依指数变化，a的轻微变化会对概率有很大影响
    '''
    p0 = 0
    for _ in range(10):
        p0 = (p0 - 1) / a + 1
        print(p0)



## 其他

`msg = str(ev.message)` : string格式的输入



发送消息:

```python
try:
    group_stat[group_id] = (msg, True, 0)
    await bot.send(ev, msg)
except CQHttpError as e:
    hoshino.logger.error(f'复读失败: {type(e)}')
```



全字匹配:

```python
@sv.on_fullmatch(('沙雕机器人', '沙雕機器人'))
async def say_sorry(bot, ev):
    await bot.send(ev, 'ごめんなさい！嘤嘤嘤(〒︿〒)')
```





# 数据类型

event (ev):
```
ev = {Event: 17} <Event, {'anonymous': None, 'font': 45606800, 'group_id': 495678411, 'message': [{'type': 'text', 'data': {'text': '.r'}}], 'message_id': 42, 'message_type': 'group', 'post_type': 'message', 'raw_message': '.r', 'self_id': 2432518641, 'sender': {'age': 16,
 detail_type = {str} 'group'
 name = {str} 'message.group.normal'
 sub_type = {str} 'normal'
 type = {str} 'message'
 'anonymous' = {NoneType} None
 'font' = {int} 45606800
 'group_id' = {int} 495678411
 'message' = {Message: 1} .r
 'message_id' = {int} 42
 'message_type' = {str} 'group'
 'post_type' = {str} 'message'
 'raw_message' = {str} '.r'
 'self_id' = {int} 2432518641
 'sender' = {dict: 9} {'age': 16, 'area': '澳门', 'card': '优衣', 'level': '冒泡', 'nickname': '冰糖', 'role': 'member', 'sex': 'female', 'title': '', 'user_id': 1773327701}
 'sub_type' = {str} 'normal'
 'time' = {int} 1595551673
 'user_id' = {int} 1773327701
 'to_me' = {bool} False
 'plain_text' = {str} '.r'
 'norm_text' = {str} '.r'
 'match' = {Match} <re.Match object; span=(0, 2), match='.r'>
 __len__ = {int} 17
```

# 装饰器

## on_*
`@sv.on_rex`: 匹配regex时的操作

`@sv.on_message()` 目前看是匹配所有群里消息

@sv.on_fullmatch(('沙雕机器人', '沙雕機器人')) 全字匹配




暂时还没搞清楚的

@sv.on_message('group')

@sv.on_prefix('.qj')


# debug: 生成结尾不同

```python
            top10_responses = [] # (内容, loss)
            for response in candidate_responses:
                mmi_input_id = [tokenizer.cls_token_id]  # 每个input以[CLS]为开头
                mmi_input_id.extend(response)
                mmi_input_id.append(tokenizer.sep_token_id)
                for history_utr in reversed(history[-args.max_history_len:]):
                    mmi_input_id.extend(history_utr)
                    mmi_input_id.append(tokenizer.sep_token_id)
                mmi_input_tensor = torch.tensor(mmi_input_id).long().to(device)
                out = mmi_model(input_ids=mmi_input_tensor, labels=mmi_input_tensor)
                loss = out[0].item()
                text = tokenizer.convert_ids_to_tokens(response)
                print("{} loss:{}".format("".join(text), loss))
                top10_responses.append((''.join(text), loss))

                samples_file.write("{} loss:{}\n".format("".join(text), loss))

            top10_responses.sort(key=lambda tup: tup[1])    # todo: 写的这部分会搞坏第二次输入

            if  (top10_responses[1][1] - top10_responses[0][1] > 0.2) and top10_responses[0][1] > 3:
                best_response = top10_responses[0][0]
            else:
                best_response = top10_responses[1][0]

            history.append(best_response)
            text = best_response
            print("chatbot:" + text)
            if args.save_samples_path:
                samples_file.write("chatbot:{}\n".format(text))

            return best_response    #第二小loss的meg部分
```





# debug: 发不出短文字

1. help可以发出来
2. help删的太短发不出来
3. 自定义的短文字发不出来
4. model1里的长文字可以发出来
5. 差不多长度的文字修改后可以发出来
6. 上面的文字改短了发不出来
7. 酷q里短消息应答发不出来, 长消息可以



发送成功的文本:

```ev
<Event, {'anonymous': None, 'font': 66996688, 'group_id': 582368081, 'message': [{'type': 'text', 'data': {'text': ''}}], 'message_id': 168, 'message_type': 'group', 'post_type': 'message', 'raw_message': 'help', 'self_id': 2432518641, 'sender': {'age': 30, 'area': '长沙', 'card': '', 'level': '潜水', 'nickname': 'null', 'role': 'owner', 'sex': 'male', 'title': '', 'user_id': 570879411}, 'sub_type': 'normal', 'time': 1595790063, 'user_id': 570879411, 'to_me': False, 'prefix': 'help'}>

```

发送失败的文本:
```ev
<Event, {'anonymous': None, 'font': 67865848, 'group_id': 582368081, 'message': [{'type': 'text', 'data': {'text': ''}}], 'message_id': 172, 'message_type': 'group', 'post_type': 'message', 'raw_message': '沙雕机器人', 'self_id': 2432518641, 'sender': {'age': 30, 'area': '长沙', 'card': '', 'level': '潜水', 'nickname': 'null', 'role': 'owner', 'sex': 'male', 'title': '', 'user_id': 570879411}, 'sub_type': 'normal', 'time': 1595790213, 'user_id': 570879411, 'to_me': False, 'prefix': '沙雕机器人'}>
```


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
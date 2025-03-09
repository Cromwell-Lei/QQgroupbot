#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import asyncio
import datetime
from nonebot import on_message, get_driver, on_time
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.config import Config

driver = get_driver()
config = Config(**driver.config.dict())

# 存储群聊消息
group_messages = []

# 监听群消息
@on_message().handle()
async def handle_group_message(bot: Bot, event: GroupMessageEvent):
    if event.group_id == config.group_id:
        group_messages.append(event.raw_message)

# 每天24点触发
@on_time("00:00", name="daily_summary")
async def daily_summary(bot: Bot):
    if not group_messages:
        return

    # 调用 DeepSeek API 进行总结
    import requests
    api_key = config.deepseek_api_key
    base_url = config.deepseek_base_url
    prompt = "请对以下群聊内容进行总结：\n" + "\n".join(group_messages)
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(f"{base_url}/chat/completions", json={"prompt": prompt}, headers=headers)
    summary = response.json()["choices"][0]["text"]

    # 发送总结到群聊
    await bot.send_group_msg(group_id=config.group_id, message=f"今日群聊总结：\n{summary}")

    # 清空消息列表
    group_messages.clear()




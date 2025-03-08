#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from nonebot import get_driver
from nonebot.config import Env

env = Env()
driver = get_driver()

driver.config.deepseek_api_key = "your_deepseek_api_key"  # 替换为你的 DeepSeek API Key
driver.config.deepseek_base_url = "https://api.deepseek.com/v1"  # DeepSeek API 地址
driver.config.group_id = "your_group_id"  # 替换为你的 QQ 群号





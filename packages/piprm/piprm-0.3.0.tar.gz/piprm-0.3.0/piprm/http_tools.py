#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


import requests
import time


def test_latency(url):
    start_time = time.time()
    requests.options(url, timeout=10)
    end_time = time.time()
    latency = end_time - start_time
    latency = int(latency * 1000)
    #  print(f"Latency for {url}: {latency} ms")
    return latency

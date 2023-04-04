import requests
import pandas as pd
import os

SCKEY = os.environ.get('SCKEY') # ServerChan Key
Authorization = os.environ.get('Authorization') # Authorization

url = "https://www.autodl.com/api/v1/user/machine/list"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Authorization": Authorization,
}

data = {
    "charge_type": "payg",
    "region_sign": "",
    "gpu_type_name": ["A100-SXM4-80GB"],
    "machine_tag_name": [],
    "gpu_idle_num": 1,
    "mount_net_disk": False,
    "instance_disk_size_order": "",
    "date_range": "",
    "date_from": "",
    "date_to": "",
    "page_index": 1,
    "page_size": 10,
    "pay_price_order": "",
    "gpu_idle_type": "",
    "default_order": True,
    "region_sign_list": ["beijing-C"],
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result_data = response.json()
else:
    print(f"请求失败，状态码：{response.status_code}")

print(result_data)
for i in range(pd.DataFrame(result_data['data']['list']).shape[0]):
        if pd.DataFrame(result_data['data']['list'])['gpu_order_num'][i] >= 4:
            data = {'text':'At Least 4-GPU A100-80G available now!',
                    'desp':'At Least 4-GPU A100-80G available in ' + pd.DataFrame(result_data['data']['list']).iloc[i]['region_name']}
            requests.post('https://sc.ftqq.com/%s.send'%(SCKEY), data=data)
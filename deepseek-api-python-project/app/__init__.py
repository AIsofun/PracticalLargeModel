# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

#client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com/v1")
client = OpenAI(api_key="sk-99bf12d8336a44b9aaf6be18b18628b8", base_url="https://api.deepseek.com/v1")
#这里的<DeepSeek API Key>，需要填写在官网申请的api key

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        #{"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)

#输出：openai.APIStatusError: Error code: 402 - {'error': {'message': 'Insufficient Balance', 'type': 'unknown_error', 'param': None, 'code': 'invalid_request_error'}}
#错误码402，意味着账号余额不足，充钱即可调用成功
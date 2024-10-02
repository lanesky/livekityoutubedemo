## 关于LLM的jailbreak

1. 方法论

- https://www.lesswrong.com/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction
- https://huggingface.co/blog/mlabonne/abliteration

2. 越狱原模和GGUF（Qwen2.5-7B-Instruct-abliterated-v2）
- https://huggingface.co/huihui-ai/Qwen2.5-7B-Instruct-abliterated-v2
- https://huggingface.co/mradermacher/Qwen2.5-7B-Instruct-abliterated-v2-GGUF


## 配置（main.py - 正常版本，即非越狱版本）
- llm: openai
- stt: openai
- tts: openai

## 配置（main_jb.py: QWEN2.5B越狱版本）
- llm: jail-broken qwen2.5B
- stt: openai (wisper-1)
- tts: cartesia.ai (参考：https://cartesia.ai/pricing）


## 视频
- 正常版本：https://youtu.be/7TQXMfCXTjI?si=jM0YoB_VHzaOaDhD
- QWEN2.5B越狱版本: https://youtu.be/V7kSsAoIWxQ?si=9Gc9I7jpdawtusaG

# Multilingual Meeting Benchmark

多语言会议智能助手评测框架。

## 目标

评估大语言模型在国际会议场景中的：

- 多语言理解能力
- 跨语言摘要能力
- 会议纪要生成能力
- 东南亚语言本土化表达能力

## 支持语言

- 中文 zh
- English en
- ไทย th
- Tiếng Việt vi
- Bahasa Indonesia id
- Bahasa Melayu ms

## Benchmark

- OPUS100：翻译能力
- XLSum：摘要能力
- CrossSum：跨语言摘要能力
- MeetingBank：会议理解能力
- SEA Meeting Benchmark：多语言会议纪要能力

## 推理方式

兼容 OpenAI API 格式，例如 vLLM：

```
http://localhost:8000/v1
```

## 使用

```bash
pip install -r requirements.txt
python benchmark/run_benchmark.py
```

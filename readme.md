### Часть 1 Подготовка инфраструктуры

- Скачать модель: https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF?spm=a2ty_o01.29997173.0.0.10ce55fbOF3J9l&file=Llama-3.2-3B-Instruct-GGUF

- Скачать Llama: https://github.com/ggml-org/llama.cpp/releases/tag/b8994

Строка запуска проекта: 

```bash
./llama-b8994/llama-server \
  -m ./Llama-3.2-3B-Instruct-Q4_K_M.gguf \
  -c 2048 \
  -t 4 \
  --port 8080 \
  --host 127.0.0.1
```

соответственно, llama.ccp будет доступен по адресу: http://127.0.0.1:8080/

### Часть 2. Подготовка структуры проекта: 

```
voice_assistant/
├── config.py              # Настройки: бэкенд, пути, параметры
├── llm_client.py          # Единый интерфейс к любой LLM (абстракция)
├── backends/
│   ├── __init__.py
│   ├── llama_server.py    # Реализация для llama-server
│   └── vllm.py           # Реализация для vLLM (добавите позже)
├── voice/
│   ├── __init__.py
│   ├── stt.py            # Speech-to-Text (микрофон → текст)
│   └── tts.py            # Text-to-Speech (текст → озвучка)
├── session.py            # Управление историей диалога
├── main.py               # Точка входа: связывает все модули
└── requirements.txt
```

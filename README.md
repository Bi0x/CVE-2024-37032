# CVE-2024-37032
Path traversal in Ollama with rogue registry server

- Learn from [Probllama: Ollama Remote Code Execution Vulnerability (CVE-2024-37032) – Overview and Mitigations](https://www.wiz.io/blog/probllama-ollama-vulnerability-cve-2024-37032#the-vulnerability-arbitrary-file-write-via-path-traversal-25)

# Vulnerability environment

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:0.1.33
```

# Rogue registry server

- Please modify `HOST` to your host **MUST WITHOUT PORT**
- Run with `python3 server.py`

# Run poc

- Please modify `HOST` to your rogue registry server host, and `target_url` to vulnerability host
- Run `python3 poc.py` and check rogue registry server log

![](screenshot.png)
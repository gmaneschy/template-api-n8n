# template-api-n8n

Template [Copier](https://copier.readthedocs.io/) para APIs FastAPI com Postgres, n8n e deploy em nuvem gratuita.

## Uso

```bash
uvx copier copy gh:SEU_USUARIO/template-api-n8n meu-projeto
cd meu-projeto
make env && make install && make test
```

Para trazer melhorias do template a projetos já criados: `copier update`.

## Estado

- [x] Passo 1: estrutura do template e perguntas do Copier
- [x] Passo 2: núcleo FastAPI (config validada, banco, logs JSON, chave de acesso, `/saude`, Alembic, testes)
- [x] Passo 3: Docker Compose com profiles (app, proxy, n8n, redis, llm), Dockerfile, Caddy, `make env`
- [x] Passo 4: n8n versionado (fluxo de exemplo em `n8n/workflows/`, `scripts/n8n.py` para exportar e importar, funciona sem `make`)
- [x] Passo 5: CI no GitHub Actions: nos projetos gerados (lint, testes com Postgres, Compose, imagem arm64) e no próprio template (gera variantes e testa)
- [ ] Passo 6: deploy na Oracle Cloud (arm64)

## Testando o próprio template

```bash
uvx copier copy --trust --defaults --data project_name="Teste" . /tmp/teste
cd /tmp/teste && make env && make install && make test && make lint
```

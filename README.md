# template-api-n8n

Template [Copier](https://copier.readthedocs.io/) para APIs FastAPI com Postgres, n8n e deploy em nuvem gratuita.

## Uso

```bash
uvx copier copy gh:SEU_USUARIO/template-api-n8n meu-projeto
cd meu-projeto
cp .env.example .env
make install && make test
```

Para trazer melhorias do template a projetos já criados: `copier update`.

## Estado

- [x] Passo 1: estrutura do template e perguntas do Copier
- [x] Passo 2: núcleo FastAPI (config validada, banco, logs JSON, chave de acesso, `/saude`, Alembic, testes)
- [ ] Passo 3: Docker Compose com profiles (api, db, n8n, redis, llm-local) e Caddy
- [ ] Passo 4: n8n versionado (fluxo de exemplo exportado)
- [ ] Passo 5: CI (ruff, pytest com Postgres, build da imagem)
- [ ] Passo 6: deploy na Oracle Cloud (arm64)

## Testando o próprio template

```bash
uvx copier copy --trust --defaults --data project_name="Teste" . /tmp/teste
cd /tmp/teste && make install && make test && make lint
```

"""Ambiente do Alembic: usa a configuração e a engine da própria aplicação."""

from alembic import context

from app.config import get_settings
from app.db import Base, get_engine

# Importe aqui os módulos de modelos para que o autogenerate os enxergue.
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=get_settings().database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    with get_engine().connect() as conexao:
        context.configure(connection=conexao, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

# Repository Guidelines

## Project Structure & Modules
```text
.
├── fundamentos.py      # fundamentos da linguagem (strings, variáveis)
├── colecoes.py         # listas, tuplas, dicts, sets
└── tests/              # testes (opcional)
    └── test_colecoes.py
```
- New modules: add `.py` files at root or `src/` as project grows (`src/utils.py`).
- Tests mirror modules under `tests/`.

## Build, Test, Develop
| Task | Command | Notes |
| --- | --- | --- |
| Run examples | `python3 fundamentos.py` | prints demo output |
| Run collections | `python3 colecoes.py` | manipulações de coleções |
| Create venv | `python3 -m venv .venv && source .venv/bin/activate` | isolated env |
| Lint | `ruff .` | `pip install ruff` |
| Format | `black .` | `pip install black` |
| Tests | `pytest -q` | `pip install pytest` |

## Coding Style & Naming
- PEP 8; 4 spaces; max line 88 (Black default).
- Names: modules `lowercase_with_underscores.py`; vars/funcs `snake_case`; constants `UPPER_CASE`.
- Prefer docstrings and type hints for clarity:
```python
def soma(a: int, b: int) -> int:
    """Retorna a soma de dois inteiros."""
    return a + b
```

## Testing Guidelines
- Framework: `pytest`; tests in `tests/test_<module>.py` with `test_<behavior>()`.
- Aim ≥80% coverage when tests exist; assert behaviors and edge cases.
```python
def test_uniao_sets():
    assert ({1, 2} | {2, 3}) == {1, 2, 3}
```

## Commits & Pull Requests
- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
  - Ex.: `feat: adicionar exemplos de conjuntos em colecoes.py`
- Keep commits small and scoped; language PT or EN consistently.
- PR checklist:
  - [ ] Descrição do que mudou e por quê
  - [ ] Passos de execução/verificação (comandos e saída esperada)
  - [ ] Issues vinculadas (se houver)

## Notes & Tips
> Use `.gitignore` para `.venv/` e `__pycache__/`. Evite segredos no repositório.
> Prefira exemplos pequenos e executáveis para facilitar revisão e aprendizado.

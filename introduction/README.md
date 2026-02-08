# PyTest

## Работа с .venv

```bash
# Создание venv
python3 -m venv .venv

# Активация venv
source .venv/bin/activate

# Выход 
deactivate
```

## Запуск тестов

```bash
uv run pytest -vv tests/test_*.py

uv run pytest 			# стандартный запуск
uv run pytest -q 			# тише
uv run pytest -vv 			# подробные имена кейсов
uv run pytest -k sum 		# фильтр по выражению/подстроке имени теста
uv run pytest -m "not slow" 	# запуск без помеченных slow
uv run pytest -x --maxfail=1 	# остановиться на первом падении
```
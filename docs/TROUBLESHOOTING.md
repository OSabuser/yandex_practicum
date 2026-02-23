# 🔧 Решение проблем с Pre-commit хуками

## Типичная проблема: "Your pre-commit configuration is unstaged"

### Что происходит?

При выполнении `git commit` вы видите ошибку:

```
[ERROR] Your pre-commit configuration is unstaged.
`git add .pre-commit-config.yaml` to fix this.
```

Или хуки сообщают:

```
Ruff: форматирование кода................................................Failed
- hook id: ruff-format
- files were modified by this hook

3 files reformatted, 19 files left unchanged
```

### Почему это происходит?

Pre-commit хуки **автоматически исправляют** ваши файлы:
- Удаляют лишние пробелы в конце строк
- Добавляют перенос строки в конец файла
- Форматируют код по правилам Ruff

Эти исправления происходят **после** того, как вы добавили файлы в staging (`git add`), но **до** коммита. Поэтому файлы оказываются изменёнными, но не застейдженными.

## ✅ Решение

### Вариант 1: Добавить исправленные файлы и повторить коммит

```bash
# 1. Попытка коммита (хуки исправляют файлы)
git commit -m "ваше сообщение"

# 2. Хуки сообщают что изменили файлы
# Добавляем исправленные файлы обратно в staging
git add .

# 3. Повторяем коммит (теперь всё ок)
git commit -m "ваше сообщение"
```

### Вариант 2: Запустить хуки заранее (рекомендуется!)

```bash
# 1. Сначала запускаем хуки вручную на всех файлах
uv run pre-commit run --all-files

# 2. Хуки автоматически исправят что нужно
# Добавляем ВСЕ изменения (включая исправления от хуков)
git add .

# 3. Теперь коммит пройдёт с первого раза
git commit -m "ваше сообщение"
```

## 📝 Рекомендуемый рабочий процесс

### Ежедневная работа

```bash
# 1. Работаете над кодом
vim sprint_1/task/solution.py

# 2. Сначала запускаете хуки (проверка + автоисправление)
uv run pre-commit run --all-files

# 3. Смотрите что изменилось
git status
git diff

# 4. Добавляете ВСЁ (ваши изменения + исправления хуков)
git add .

# 5. Коммитите (хуки уже ничего не изменят)
git commit -m "feat: решил задачу X"

# 6. Пушите
git push
```

### Быстрые коммиты (если уверены в коде)

```bash
# 1. Добавляете файлы
git add .

# 2. Коммитите (хуки запустятся автоматически)
git commit -m "ваше сообщение"

# 3. Если хуки что-то исправили - повторяете
git add .
git commit -m "ваше сообщение"
```

## 🚨 Частые ошибки и их решение

### Ошибка: `Failed to spawn: pytest`

**Проблема:** В `.pre-commit-config.yaml` неправильная команда для pytest

**Решение:** Используйте `uv run python -m pytest` вместо `uv run pytest`

```yaml
- id: pytest-check
  entry: bash -c 'uv run python -m pytest'  # ✅ Правильно
  # НЕ: entry: uv run pytest                # ❌ Не работает
```

### Ошибка: `no-commit-to-branch` блокирует коммит

**Проблема:** Хук не даёт коммитить напрямую в main/master

**Решение 1:** Работайте в отдельной ветке (правильно)
```bash
git checkout -b feature/my-task
git commit -m "..."
git push
```

**Решение 2:** Отключите хук для учебного проекта
```yaml
# В .pre-commit-config.yaml закомментируйте:
# - id: no-commit-to-branch
#   args: ['--branch', 'main', '--branch', 'master']
```

### Хуки слишком долго выполняются

**Проблема:** Тесты работают медленно

**Решение:** Временно пропустить хуки для WIP коммита
```bash
git commit -m "WIP: работаю над задачей" --no-verify
```

⚠️ **Важно:** Перед финальным push всё равно запустите проверку:
```bash
uv run pre-commit run --all-files
```

## 🔍 Отладка проблем

### Проверить что хуки установлены

```bash
ls -la .git/hooks/pre-commit
```

Должен существовать файл. Если нет:
```bash
uv run pre-commit install
```

### Запустить хуки с подробным выводом

```bash
uv run pre-commit run --all-files --verbose
```

### Запустить конкретный хук

```bash
# Только Ruff
uv run pre-commit run ruff --all-files

# Только Pytest
uv run pre-commit run pytest-check --all-files

# Только форматирование
uv run pre-commit run ruff-format --all-files
```

### Обновить версии хуков

```bash
uv run pre-commit autoupdate
```

### Полностью переустановить хуки

```bash
# Удалить
uv run pre-commit uninstall

# Установить заново
uv run pre-commit install

# Очистить кеш
uv run pre-commit clean
```

## 💡 Полезные команды

```bash
# Проверить только изменённые файлы
uv run pre-commit run

# Проверить все файлы
uv run pre-commit run --all-files

# Проверить конкретные файлы
uv run pre-commit run --files sprint_1/task/solution.py

# Пропустить хуки для одного коммита
git commit -m "сообщение" --no-verify

# Временно отключить хуки
uv run pre-commit uninstall

# Включить хуки обратно
uv run pre-commit install
```

## 📚 Дополнительная информация

Подробное руководство: [PRE_COMMIT_GUIDE.md](./PRE_COMMIT_GUIDE.md)

Официальная документация: https://pre-commit.com/

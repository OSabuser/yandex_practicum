# Justfile — commit & push с учётом pre-commit хуков
# Использование:
#   just cp "feat: добавил решение"
#   just cp "fix: исправил баг"  --no-verify

# Настройки
set shell := ["bash", "-euo", "pipefail", "-c"]

MAX_RETRIES := "2"
DEFAULT_BRANCH := "main"

# ─── Главная команда ────────────────────────────────────────────────────────

# Commit + push с автоматической обработкой исправлений хуков
# Использование: just cp "сообщение коммита"
[confirm("Запустить commit & push?")]
cp message:
    @bash {{ justfile_directory() }}/scripts/commit_push.sh {{ quote(message) }} ""

# Commit + push без pre-commit хуков (только для WIP!)
# Использование: just cp-wip "WIP: сообщение"
cp-wip message:
    @echo "⚠️  Хуки отключены! Используйте только для WIP коммитов."
    git add .
    git commit -m {{ quote(message) }} --no-verify
    git push

# ─── Утилиты ────────────────────────────────────────────────────────────────

# Запустить все хуки вручную (без коммита)
lint:
    @echo "🔍 Запуск pre-commit хуков на всех файлах..."
    uv run pre-commit run --all-files
    @echo "✅ Готово!"

# Показать статус репозитория
status:
    @echo "📋 Статус репозитория:"
    git status --short
    @echo ""
    @echo "📜 Последние 5 коммитов:"
    git log --oneline -5

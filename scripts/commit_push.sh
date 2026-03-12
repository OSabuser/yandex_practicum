#!/usr/bin/env bash
# scripts/commit_push.sh
# Надёжный commit + push с обработкой авто-исправлений pre-commit хуков

set -euo pipefail

# ─── Параметры ──────────────────────────────────────────────────────────────

MESSAGE="${1:?❌ Сообщение коммита не передано. Использование: just cp \"сообщение\"}"
MAX_RETRIES=2  # Хуки могут исправить файлы максимум N раз подряд

# ─── Цвета для вывода ───────────────────────────────────────────────────────

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

log_info()    { echo -e "${BLUE}ℹ️  $*${NC}"; }
log_success() { echo -e "${GREEN}✅ $*${NC}"; }
log_warning() { echo -e "${YELLOW}⚠️  $*${NC}"; }
log_error()   { echo -e "${RED}❌ $*${NC}"; }
log_step()    { echo -e "${BOLD}▶ $*${NC}"; }

# ─── Проверки перед стартом ─────────────────────────────────────────────────

# Проверяем что находимся в git репозитории
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    log_error "Не найден git репозиторий!"
    exit 1
fi

# Проверяем что есть staged или unstaged изменения
if git diff --quiet && git diff --cached --quiet && \
   [ -z "$(git ls-files --others --exclude-standard)" ]; then
    log_warning "Нечего коммитить — нет изменений."
    exit 0
fi

# ─── Stage всех изменений ───────────────────────────────────────────────────

log_step "Добавляем все изменения в staging..."
git add .

# ─── Цикл commit с обработкой авто-исправлений хуков ───────────────────────
#
# Некоторые хуки (ruff --fix, ruff-format, trailing-whitespace, end-of-file-fixer)
# модифицируют файлы и возвращают exit code 1, что прерывает коммит.
# Стратегия: если хуки изменили файлы — добавляем их и повторяем коммит.
# Если хуки упали по другой причине (тесты не прошли и т.д.) — выходим с ошибкой.

attempt=0

while [ $attempt -le $MAX_RETRIES ]; do

    if [ $attempt -gt 0 ]; then
        log_warning "Хуки исправили файлы. Повтор #${attempt}/${MAX_RETRIES}..."
        log_step "Добавляем авто-исправления хуков..."
        git add .
    fi

    log_step "Коммит: \"${MESSAGE}\"..."

    # Запускаем commit, перехватываем вывод и exit code
    commit_output=$(git commit -m "$MESSAGE" 2>&1) && commit_exit=0 || commit_exit=$?

    if [ $commit_exit -eq 0 ]; then
        # ✅ Коммит прошёл успешно
        echo "$commit_output"
        log_success "Коммит создан!"
        break
    fi

    # Коммит упал — разбираемся почему
    echo "$commit_output"

    # Проверяем: хуки изменили файлы? (характерное сообщение pre-commit)
    if echo "$commit_output" | grep -q "files were modified by this hook"; then
        if [ $attempt -lt $MAX_RETRIES ]; then
            # Хуки поправили файлы — попробуем ещё раз
            continue
        else
            log_error "Хуки продолжают изменять файлы после ${MAX_RETRIES} попыток."
            log_error "Запустите 'just lint' вручную и проверьте что происходит."
            exit 1
        fi
    fi

    # Хуки упали по другой причине (тесты, линтер с ошибками и т.д.)
    log_error "Pre-commit хуки завершились с ошибкой!"
    echo ""
    log_info "Что делать:"
    echo "  1. Исправьте ошибки выше"
    echo "  2. Запустите 'just lint' для проверки"
    echo "  3. Попробуйте 'just cp \"${MESSAGE}\"' снова"
    echo ""
    log_info "Для WIP коммита без проверок: just cp-wip \"${MESSAGE}\""
    exit 1

    attempt=$((attempt + 1))
done

# ─── Push ───────────────────────────────────────────────────────────────────

log_step "Отправляем изменения на remote..."

# Определяем текущую ветку
current_branch=$(git rev-parse --abbrev-ref HEAD)
log_info "Ветка: ${current_branch}"

# Push с отслеживанием upstream (для новых веток добавит --set-upstream)
if git push --set-upstream origin "$current_branch" 2>&1; then
    echo ""
    log_success "Готово! Коммит запушен в ветку '${current_branch}'."
    echo ""
    git log --oneline -1
else
    log_error "Push завершился с ошибкой!"
    log_info "Попробуйте 'git pull --rebase' если есть конфликты, затем повторите push."
    exit 1
fi
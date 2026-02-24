# Исключения в Python 3.13

## Содержание

1. [Что такое исключения](#что-такое-исключения)
2. [Иерархия исключений](#иерархия-исключений)
3. [Встроенные исключения](#встроенные-исключения)
4. [Обработка исключений](#обработка-исключений)
5. [Создание собственных исключений](#создание-собственных-исключений)
6. [Exception Groups и ExceptionGroup](#exception-groups-и-exceptiongroup)
7. [Новое в Python 3.11–3.13: улучшенные трассировки](#новое-в-python-3113-улучшенные-трассировки)
8. [Цепочки исключений](#цепочки-исключений)
9. [Контекстные менеджеры и исключения](#контекстные-менеджеры-и-исключения)
10. [Лучшие практики](#лучшие-практики)

---

## Что такое исключения

**Исключение** (exception) — это событие, возникающее во время выполнения программы и нарушающее нормальный ход её работы. В Python исключения являются объектами, унаследованными от базового класса `BaseException`.

В отличие от многих языков, Python активно использует принцип **EAFP** (Easier to Ask Forgiveness than Permission — «проще попросить прощения, чем разрешения»), предпочитая перехватывать исключения вместо предварительной проверки условий.

```python
# LBYL (Look Before You Leap) — менее Pythonic
if key in dictionary:
    value = dictionary[key]

# EAFP — более Pythonic
try:
    value = dictionary[key]
except KeyError:
    value = default
```

---

## Иерархия исключений

```
BaseException
 ├── BaseExceptionGroup          # Python 3.11+
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup           # Python 3.11+
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
```

---

## Встроенные исключения

### ArithmeticError и подклассы

| Исключение | Описание | Пример |
|---|---|---|
| `ZeroDivisionError` | Деление на ноль | `1 / 0` |
| `OverflowError` | Результат слишком велик для представления | `math.exp(1000)` |
| `FloatingPointError` | Ошибка операции с плавающей точкой | Редко встречается напрямую |

### LookupError и подклассы

| Исключение | Описание | Пример |
|---|---|---|
| `IndexError` | Индекс за пределами последовательности | `lst[100]` при `len(lst) == 3` |
| `KeyError` | Ключ отсутствует в словаре | `d["missing"]` |

### OSError и подклассы

`OSError` (он же `IOError`, `EnvironmentError`) — базовый класс для ошибок операционной системы. Содержит атрибуты:
- `errno` — код ошибки ОС
- `strerror` — строковое описание ошибки
- `filename` / `filename2` — имена файлов, связанных с ошибкой

```python
try:
    open("nonexistent.txt")
except FileNotFoundError as e:
    print(e.errno)      # 2
    print(e.strerror)   # No such file or directory
    print(e.filename)   # nonexistent.txt
```

### Прочие важные исключения

| Исключение | Описание |
|---|---|
| `TypeError` | Операция применена к объекту неподходящего типа |
| `ValueError` | Правильный тип, но недопустимое значение |
| `AttributeError` | Объект не имеет указанного атрибута |
| `NameError` | Имя переменной не найдено в области видимости |
| `RuntimeError` | Общая ошибка выполнения, не подходящая под другие категории |
| `NotImplementedError` | Абстрактный метод, который должен быть переопределён |
| `StopIteration` | Сигнал о завершении итерации |
| `AssertionError` | Провал оператора `assert` |
| `RecursionError` | Превышена максимальная глубина рекурсии |
| `MemoryError` | Недостаточно памяти |
| `SystemExit` | Вызов `sys.exit()` |
| `KeyboardInterrupt` | Прерывание с клавиатуры (Ctrl+C) |

---

## Обработка исключений

### Базовый синтаксис try/except/else/finally

```python
try:
    result = 10 / int(input("Введите делитель: "))
except ZeroDivisionError:
    print("Нельзя делить на ноль!")
except ValueError as e:
    print(f"Неверный ввод: {e}")
except (TypeError, OverflowError) as e:
    print(f"Ошибка типа или переполнение: {e}")
else:
    # Выполняется, если исключений не было
    print(f"Результат: {result}")
finally:
    # Выполняется всегда — с исключением или без
    print("Блок finally выполнен")
```

### Семантика блоков

- **`try`** — код, который может вызвать исключение.
- **`except`** — обработчик одного или нескольких типов исключений.
- **`else`** — выполняется только при отсутствии исключений в `try`; отделяет «нормальный» поток от логики восстановления.
- **`finally`** — выполняется **всегда**: при нормальном завершении, при исключении, при `return`, при `break` и `continue`.

### Перехват любого исключения

```python
# Перехватывает все Exception (но не BaseException!)
try:
    risky_operation()
except Exception as e:
    print(type(e).__name__, e)

# Перехватывает абсолютно всё, включая SystemExit, KeyboardInterrupt
try:
    risky_operation()
except BaseException as e:
    raise  # Обычно нужно повторно пробросить
```

> **Совет:** никогда не используйте голый `except:` без указания типа — это перехватывает даже `KeyboardInterrupt` и `SystemExit`, что может сделать программу неуправляемой.

### Повторное возбуждение исключения

```python
try:
    process()
except ValueError as e:
    log_error(e)
    raise           # Пробросить то же исключение дальше
    # или
    raise RuntimeError("Обёртка") from e  # Цепочка исключений
```

### Оператор raise

```python
# Возбудить новое исключение
raise ValueError("Некорректное значение")

# Возбудить с аргументами
raise TypeError(f"Ожидался int, получен {type(value).__name__}")

# Повторно возбудить текущее исключение
raise

# Подавить контекст исключения
raise NewError("сообщение") from None
```

---

## Создание собственных исключений

### Простое пользовательское исключение

```python
class AppError(Exception):
    """Базовое исключение приложения."""
    pass


class ValidationError(AppError):
    """Ошибка валидации данных."""

    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(f"Поле '{field}': {message}")


class NetworkError(AppError):
    """Сетевая ошибка."""

    def __init__(self, url: str, status_code: int):
        self.url = url
        self.status_code = status_code
        super().__init__(f"HTTP {status_code} при запросе {url}")
```

### Использование

```python
try:
    raise ValidationError("email", "неверный формат")
except ValidationError as e:
    print(e.field)    # email
    print(e.message)  # неверный формат
    print(e)          # Поле 'email': неверный формат
```

### Рекомендации по именованию

- Имя исключения должно заканчиваться на `Error` (для ошибок) или `Warning` (для предупреждений).
- Создавайте базовый класс исключений для каждого модуля/пакета — это позволяет пользователям перехватывать все ошибки модуля одним `except`.
- Добавляйте атрибуты, несущие контекст ошибки, вместо того чтобы всё кодировать в строку сообщения.

---

## Exception Groups и ExceptionGroup

Появились в **Python 3.11** и продолжают развиваться. Позволяют объединить несколько несвязанных исключений в одну группу — крайне полезно в асинхронном и параллельном коде.

### Создание ExceptionGroup

```python
eg = ExceptionGroup(
    "несколько ошибок",
    [
        ValueError("неверное значение"),
        TypeError("неверный тип"),
        KeyError("missing_key"),
    ]
)
raise eg
```

### Обработка с помощью except*

Синтаксис `except*` — специально для `ExceptionGroup`. Он **не** является заменой обычного `except`.

```python
try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(coro1())
        tg.create_task(coro2())
        tg.create_task(coro3())
except* ValueError as eg:
    print("Поймали ValueError:", eg.exceptions)
except* TypeError as eg:
    print("Поймали TypeError:", eg.exceptions)
```

Особенности `except*`:
- Один блок `except*` перехватывает **все** исключения указанного типа из группы.
- Несколько блоков `except*` могут сработать для одного `ExceptionGroup`.
- Необработанные исключения группы автоматически пробрасываются дальше.
- В одном `try` нельзя смешивать `except` и `except*`.

### Вложенные группы

```python
eg = ExceptionGroup("внешняя", [
    ValueError("v1"),
    ExceptionGroup("внутренняя", [
        KeyError("k1"),
        TypeError("t1"),
    ]),
])
```

### BaseExceptionGroup

`BaseExceptionGroup` — аналог для исключений, не унаследованных от `Exception` (например, `KeyboardInterrupt`). Если все исключения в группе наследуются от `Exception`, Python автоматически создаёт `ExceptionGroup`; иначе — `BaseExceptionGroup`.

---

## Новое в Python 3.11–3.13: улучшенные трассировки

### Точное указание на ошибку (Python 3.11+)

Начиная с Python 3.11, traceback указывает **точно на то выражение**, которое вызвало ошибку, а не только на строку.

```
Traceback (most recent call last):
  File "example.py", line 3, in <module>
    result = (a + b) * (c / d)
                        ~~^~~
ZeroDivisionError: division by zero
```

### Атрибуты исключений для точного указания (Python 3.11+)

Класс `BaseException` получил новые атрибуты:

| Атрибут | Тип | Описание |
|---|---|---|
| `__traceback__` | `TracebackType` | Объект трассировки (был и раньше) |
| `add_note(note)` | метод | Добавить заметку к исключению |
| `__notes__` | `list[str]` | Список заметок |

```python
try:
    raise ValueError("базовая ошибка")
except ValueError as e:
    e.add_note("Дополнительный контекст: произошло при обработке пользователя #42")
    e.add_note("Попробуйте проверить входные данные")
    raise
```

Вывод:

```
ValueError: базовая ошибка
  Дополнительный контекст: произошло при обработке пользователя #42
  Попробуйте проверить входные данные
```

### Изменения в Python 3.13

В Python 3.13 были улучшены:

- **Цветные трассировки** в интерактивном режиме (REPL) — ошибки и подсветка теперь цветные по умолчанию.
- **Улучшенный REPL** — многострочные блоки `try/except` стало удобнее писать в интерактивном режиме.
- **`sys.last_exc`** — теперь содержит последнее необработанное исключение как объект (ранее было три отдельных атрибута: `sys.last_type`, `sys.last_value`, `sys.last_traceback`).
- Улучшения в модуле `traceback` для более красивого форматирования групп исключений.

---

## Цепочки исключений

Python поддерживает явные и неявные цепочки исключений.

### Неявная цепочка (implicit chaining)

Возникает автоматически, когда исключение появляется внутри обработчика другого исключения.

```python
try:
    int("abc")
except ValueError:
    raise RuntimeError("Ошибка обработки данных")
# RuntimeError: Ошибка обработки данных
# During handling of the above exception, another exception occurred:
# ValueError: invalid literal for int() with base 10: 'abc'
```

Доступно через атрибут `__context__`.

### Явная цепочка (explicit chaining)

```python
try:
    connect_to_db()
except ConnectionError as e:
    raise ServiceUnavailableError("БД недоступна") from e
# ServiceUnavailableError: БД недоступна
# The above exception was the direct cause of the following exception:
# ConnectionError: ...
```

Доступно через атрибут `__cause__`. Флаг `__suppress_context__` устанавливается в `True`.

### Подавление контекста

```python
try:
    risky()
except SomeError:
    raise NewError("чистая ошибка") from None
# Контекст оригинального исключения скрыт
```

### Атрибуты цепочек

| Атрибут | Описание |
|---|---|
| `__cause__` | Явная причина (`raise X from Y`) |
| `__context__` | Неявный контекст (исключение внутри `except`) |
| `__suppress_context__` | `True`, если используется `from`, скрывает `__context__` |
| `__traceback__` | Объект трассировки |

---

## Контекстные менеджеры и исключения

### contextlib.suppress

Подавляет указанные типы исключений:

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("temp.txt")  # Не упадёт, если файла нет
```

### contextlib.contextmanager

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    resource = acquire()
    try:
        yield resource
    except SpecificError as e:
        handle_error(e)
    finally:
        release(resource)
```

### Обработка исключений в __exit__

Метод `__exit__` контекстного менеджера получает информацию об исключении и может его подавить, вернув `True`:

```python
class SuppressZeroDivision:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ZeroDivisionError:
            print("Подавлено ZeroDivisionError")
            return True  # Подавить исключение
        return False  # Пропустить исключение дальше
```

---

## Лучшие практики

### 1. Перехватывайте конкретные исключения

```python
# Плохо
try:
    process()
except:
    pass

# Хорошо
try:
    process()
except ValueError as e:
    logger.warning("Некорректное значение: %s", e)
```

### 2. Не молчите об исключениях

```python
# Плохо — ошибки исчезают незаметно
try:
    risky()
except Exception:
    pass

# Хорошо — хотя бы логируем
try:
    risky()
except Exception:
    logger.exception("Неожиданная ошибка в risky()")
```

### 3. Используйте finally для освобождения ресурсов

```python
# Лучше использовать with, но если нельзя:
conn = None
try:
    conn = open_connection()
    conn.execute(query)
finally:
    if conn:
        conn.close()
```

### 4. Добавляйте контекст через цепочки

```python
def load_config(path: str) -> dict:
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise ConfigurationError(f"Файл конфигурации не найден: {path}") from e
    except json.JSONDecodeError as e:
        raise ConfigurationError(f"Некорректный JSON в {path}") from e
```

### 5. Используйте add_note() для дополнительного контекста (Python 3.11+)

```python
def process_batch(items):
    for i, item in enumerate(items):
        try:
            process(item)
        except ValueError as e:
            e.add_note(f"Ошибка при обработке элемента #{i}: {item!r}")
            raise
```

### 6. Иерархия пользовательских исключений

```python
# Базовое исключение пакета
class MyLibError(Exception):
    """Все исключения mylib наследуются отсюда."""

class ParseError(MyLibError):
    """Ошибка парсинга."""

class NetworkError(MyLibError):
    """Сетевая ошибка."""

class AuthError(NetworkError):
    """Ошибка аутентификации."""
```

Это позволяет пользователям перехватывать либо конкретный тип, либо все ошибки библиотеки сразу:

```python
except MyLibError:   # Все ошибки библиотеки
except NetworkError: # Только сетевые
except AuthError:    # Только аутентификация
```

### 7. Предупреждения (warnings)

```python
import warnings

# Выдать предупреждение
warnings.warn("Функция устарела, используйте new_func()", DeprecationWarning, stacklevel=2)

# Настроить поведение предупреждений
warnings.filterwarnings("error", category=DeprecationWarning)  # Превратить в исключение
warnings.filterwarnings("ignore", category=ResourceWarning)    # Подавить
```

---

## Быстрая шпаргалка

```python
# Полная структура обработки исключений
try:
    pass                          # Код, который может упасть
except SpecificError as e:
    pass                          # Обработка конкретной ошибки
except (TypeError, ValueError):
    pass                          # Несколько типов сразу
except Exception as e:
    raise                         # Логируем и пробрасываем
else:
    pass                          # Если исключений не было
finally:
    pass                          # Всегда

# Exception Groups (Python 3.11+)
try:
    pass
except* ValueError as eg:
    pass
except* TypeError as eg:
    pass

# Полезные паттерны
raise ValueError("msg") from original_exc   # Явная цепочка
raise ValueError("msg") from None           # Скрыть контекст
exc.add_note("доп. контекст")               # Добавить заметку (3.11+)

from contextlib import suppress
with suppress(KeyError, IndexError):         # Подавить исключения
    pass
```

---

*Документ подготовлен для Python 3.13. Актуальная документация: [docs.python.org](https://docs.python.org/3.13/library/exceptions.html)*

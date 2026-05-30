<!-- language: ru -->
# LeetCode Daily

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Windows](https://img.shields.io/badge/OS-Windows-0078D6?logo=windows&logoColor=white)](#)

![Уведомление](assets/images/notification.png)

Проект для напоминания решить ежедневную задачу на LeetCode.

## 🛠️ Установка

1. Клонируйте репозиторий:
    ```bash
    git clone <url>
    cd leetcode-daily
    ```

2. Создайте виртуальное окружение (опционально):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    venv\Scripts\activate     # Для Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Команды

Запуск из корня проекта:
```bash
python src/main.py {open, check}
```

1. Открыть ежедневную задачу в браузере. Если путь к браузеру не указан (параметр `browser`), будет использован браузер по умолчанию.
   ```bash
   open [browser]
   ```

2. Проверить, решена ли ежедневная задача пользователя с никнеймом `username`. Результат будет выведен через системное уведомление.
   ```bash
   check <username>
   ```

## 🔨 Сборка в исполняемый файл 

1. Установите `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```

2. Запустите скрипт сборки `build.cmd`:
   ```bash
   .\build.cmd
   ```

В результате будет создан `leetcode-daily.exe`. 
Исполняемый файл используется для запуска без открытия консольного окна.

## ⏰ Настройка периодической проверки

Создайте задачу планировщика (Task Scheduler), которая будет, например, каждые 30 минут начиная с 18:00 запускать команду:

```bash
path/to/leetcode-daily.exe check <username>
```

# DemoQA UI Automation tests with PlayWright

[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=Playwright&logoColor=white)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)

Автоматические тесты для [demoqa.com](https://demoqa.com) — учебного сайта для отработки навыков тестирования веб-форм и элементов интерфейса.  
Проверяем работу полей ввода, чекбоксов, кнопок и других элементов.

### Возможности
- Page Object Model — чистая архитектура и переиспользование кода
- Параметризованные тесты — покрытие множества сценариев
- Pytest фикстуры — удобная настройка окружения для тестов

### Структура проекта
<pre>
DemoQA_PW/
├── pages/ # Page Object Model
│ ├── basepage.py # Базовая страница с общими методами
│ └── elements_page.py # Страницы раздела "Elements"
├── locators/ # Локаторы элементов
│ └── elements_locators.py # Локаторы для раздела Elements
├── tests/ # Тесты
│ └── test_elements.py # Тесты для раздела Elements
├── conftest.py # Фикстуры для pytest
├── other.py # Вспомогательные утилиты
└── .gitignore # Игнорируемые файлы
</pre>

## Установка

### Клонировать репозиторий:

git clone https://github.com/Wesley1012/DemoQA_PW.git  
cd DemoQA_PW


### Создать виртуальное окружение:

python -m venv .venv
source .venv/bin/activate  # Linux/Mac

.venv\Scripts\activate     # Windows

### Установить зависимости:

pip install -r requirements.txt
playwright install

sudo pacman -S jdk11-openjdk # Arch linux
sudo pacman -S allure 

brew install openjdk@11 # macOS
brew install allure 

winget install Microsoft.OpenJDK.11 # Windows (через winget)
scoop install allure # Windows (scoop)

### Запуск тестов

pytest

### Запуск с генерацией Allure отчёта(addopts уже прописан см. pytest.ini)

pytest --alluredir=allure-results
allure serve allure-results # или npx allure serve allure-results в моём случае

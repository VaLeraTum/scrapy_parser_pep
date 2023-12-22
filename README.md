### Опсисание

Асинхронный парсер PEP

### Стэк

* Python 3.9.10,
* Scrapy

### Как развернуть проект:

Клонировать репозиторий на удалённый сервер и перейти в него в командной строке:

```
git clone https://github.com/<ваш репозиторий>/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```
Создайте и активируйте виртуальное окружение 
```
python -m venv venv 

source venv/Scripts/activate
```

Установите зависимости

```
pip install -r requirements.txt 
```
Запустите парсер

```
scrapy crawl pep

```

В резултате вы получите два csv файла с результатами парсинга.

### Автор: Тумасов Валерий
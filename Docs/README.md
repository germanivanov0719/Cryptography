# Техническое задание
## Проект PyQt5 для Яндекс Лицея

### Описание
Простая в использовании программа с разными алгоритмами шифрования. Поможет разобраться в отличиях разных алгоритмов шифрования и случаях их применения тем, кто не знаком с криптографией, а также сделает генерацию/проверку хеш-сумм больших файлов куда более простой задачей, не требующей постоянного посещения терминала. Будет содержать описание каждого алгоритма и области его применения.

### Поддерживаемые алгоритмы
Планируется реализовать поддержку следующих алгоритмов:
* Fernet (реализация AES)
* SHA-1 и алгоритмы семейства SHA-2
* MD5

Возможна последующая реализация алгоритмов:
* RSA

### Интерфейс
Программа будет реализована в виде одного основного окна, которое будет состоять из нескольких вкладок, соответствующих шифрованию и дешиврованию (если возможно) каждого алгоритма. Алгоритмы SHA-1 и семейтсва SHA-2 будут представлены в виде 1 вкладки с возможностью выбора необходимого алгоритма.
Интерфейс соответствует оформлению оперционной системы, состоит из стандартных элементов PyQt5.
Элементы интерфейса выровнены с помощью различных Layout. 

### Функции
* Шифрование и дешифрование (где возможно) текста
* Шифрование и дешифрование (где возможно) файлов
* Подсказки для пользователей
* Описание каждого алгоритма с целями его применения
* Ссылки на описания каждого алгоритма
* Возможность проверки хеш-суммы файла (отдельная вкладка)
* Поддержка сохранения ключей
* Поддержка импорта и экспорта ключей в виде CSV файла
* Предупреждения и ошибки, выводимые в виде тектовых диалогов и не приводящие к экстренному завершеню работы 

Возможна последующая реализация:
* Поддержки русского и алийского языков
* Поддержки Drag-and-drop для файлов
* Растягиваемого интерфейса

### Системные требования
ОС: Windows 8.1 и выше (x64), macOS High Sierra (10.13) и выше (x64 и ARM через Rosseta). На других ОС можно запустить через интерпретатор Python, но будет неообходимо скачать все файлы из репозитория и выполнить установку библиотек, указанных в пункте "Используемые библиотеки".

### Используемые библиотеки
В данной программе используются следующие библиотеки:
* PyQt5 >= 5.14.2
* Cryptography >= 35.0.0
* Pyperclip >= 1.8.1
* Python >= 3.7.0
* Hashlib (встроен в Python)
* Locale (встроен в Python)


## Контакты:
germanivanov0719@gmail.com
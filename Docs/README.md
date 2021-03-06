# Техническое задание
## Cryptography

### Описание
Простая в использовании программа с разными алгоритмами шифрования. Поможет разобраться в отличиях разных алгоритмов шифрования и случаях их применения тем, кто не знаком с криптографией, а также сделает генерацию/проверку хеш-сумм больших файлов куда более простой задачей, не требующей постоянного посещения терминала. Будет содержать описание каждого алгоритма и области его применения.

### Поддерживаемые алгоритмы
Планируется реализовать поддержку следующих алгоритмов:
* Fernet (реализация AES)
* SHA-1 и алгоритмы семейств SHA-2 и SHA-3
* MD5

### Интерфейс
Программа будет реализована в виде одного основного окна, которое будет состоять из нескольких вкладок, соответствующих шифрованию и дешиврованию (если возможно) каждого алгоритма. Алгоритмы SHA-1 и семейтсва SHA-2 будут представлены в виде 1 вкладки с возможностью выбора необходимого алгоритма.
Интерфейс соответствует оформлению оперционной системы, состоит из стандартных элементов PyQt5.
Элементы интерфейса выровнены с помощью различных Layout. 

### Функции
* Шифрование и дешифрование (где возможно) текста
* Шифрование и дешифрование (где возможно) файлов
* Поддержка русского и английского языков
* Растягиваемый интерфейс
* Подсказки для пользователей
* Описание каждого алгоритма с целями его применения
* Ссылки на описания каждого алгоритма
* Возможность проверки хеш-суммы файла (отдельная вкладка)
* Поддержка сохранения ключей
* Поддержка импорта и экспорта ключей в виде CSV файла
* Предупреждения и ошибки, выводимые в виде тектовых диалогов и не приводящие к экстренному завершеню работы 

Возможна последующая реализация:
* Поддержки Drag-and-drop для файлов


### Системные требования
Наличие Python 3.7 или выше

### Используемые библиотеки
В данной программе используются следующие библиотеки (помимо встроенных в Python 3):
* PyQt5 >= 5.14.2
* Cryptography >= 35.0.0
* Pyperclip >= 1.8.1


## Контакты:
germanivanov0719@gmail.com

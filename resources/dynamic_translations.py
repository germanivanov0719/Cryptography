class dictionary:
    def dict_en(self):
        return {'Same': 'Same',
                'Different': 'Different',
                'Invalid Fernet title': 'The key you entered is not a valid Fernet key.',
                'Invalid Fernet body': 'You can generate a new valid key by pressing \"Generate\" button on the '
                                       'right.',
                'New Fernet title': 'You are about to generate a new Fernet key.',
                'New Fernet body': 'The new key is going to replace the old one. Are you sure you can safely '
                                   'proceed?',
                'Decryption error title': 'Unable to decrypt data.',
                'Decryption error body': 'Either the encrypted data was corrupted, or this key cannot be used for '
                                         'this data.',
                'Error': 'Error',
                'Warning': 'Warning',
                'Confirm': 'Confirm your action',
                'Select File': 'Select File',
                'File not found title': 'File not found.',
                'File not found body': 'You selected a file, which does not exist or not available.',
                'Big file title': 'The file you selected might take large time process.',
                'Big file body': 'File you selected would take longer than 1 second to proceed. During this operation, '
                                 'it might look like the program is unresponsive. Are you sure you want to continue?',
                'Show help': 'Show help',
                'Hide help': 'Hide help',
                # help messages
                'fe help': 'Fernet is a secure encryption algorithm based on AES. After you encrypt information with '
                           'your key, the only possible way to decrypt it is to use the same key. Without '
                           'the key, brute force would be required, taking up to 2^128 operations for this '
                           'algorithm. '
                           'For today no computer is able to perform that many calculations in adequate time. \n\nIn '
                           'order to encrypt data you need a unique Fernet key. You can generate a random one right '
                           'in this app, or just enter your own. When you generate a key, it is automatically copied '
                           'into Fernet decryption tab too. ',
                'fd help': 'In order to decrypt data, you need the same key it was '
                           'encrypted with. If data is corrupted or the wrong key is used, decryption will fail with '
                           'the corresponding message.\n\n'
                           'To see info about Fernet algorithm, go to help on \"Fernet decryption\" tab.',
                'sha help': 'SHA is a family of hashing algorithms developed by NIST. \"Hashing\" is a complicated'
                            'process which generates the same unique output (hash) for any input data. '
                            'It is important in today\'s world and used widely against cybercrime.\n\n'
                            'One of purposes of hashing is to check if the file you send on the Internet '
                            'was transferred correctly (file integrity verification). To do this, sender should '
                            'calculate hash for that file, send '
                            'it with the file, and receiver should also calculate hash for this file and then compare'
                            'it to the original hash. You can simplify this process by using this program.\n\n'
                            'As of today, only SHA-1 of all available here SHA algorithms is considered insecure. '
                            'SHA-256 is used in most cases, but for increased protection you should choose SHA-512.'
                            'SHA3 family is relatively new and is not recommended for now if you are planning to share'
                            'your hash with others, although it provides extra protection from some attacks.',
                'md5 help': 'MD5 is a popular hashing algorithm. It was developed a long time ago. \"Hashing\" is a '
                            'complicated process which generates the same unique output (hash) for any input data. '
                            'It is important in today\'s world and used widely against cybercrime.\n\n'
                            'MD5 should NOT be used , as collision was found in 1995. Instead, any modern '
                            'SHA should be preferred. However, it is fine to do file integrity verification using MD5.'
                            'To read about file integrity verifications, go to help on \"SHA\" tab.',
                'exit title': 'Do you want to remove the Fernet key database?',
                'exit body': 'We recommend removing it. If you tried to exit accidentally, '
                             'use \"Cancel\" to return to the program.'
                }

    def dict_ru(self):
        return {'Same': 'Одинаковые',
                'Different': 'Разные',
                'Invalid Fernet title': 'Введенный ключ не является правильным ключом Fernet.',
                'Invalid Fernet body': 'Вы можете сгенерировать новый правильный ключ нажав кнопку \"Генерировать\" '
                                       'справа.',
                'New Fernet title': 'Вы собираетесь сгенерировать новый ключ Fernet.',
                'New Fernet body': 'Новый ключ заменит старый. Вы уверены, что можете безопасно продолжить?',
                'Decryption error title': 'Невозможно расшифровать данные.',
                'Decryption error body': 'Либо зашифрованные данные были повреждены, либо этот ключ не может быть '
                                         'использован для этих данных.',
                'Error': 'Ошибка',
                'Warning': 'Предупреждение',
                'Confirm': 'Подтвердите действие',
                'Select File': 'Выбрать файл',
                'File not found title': 'Файл не найден.',
                'File not found body': 'Вы выбрали файл, который не существует или недоступен.',
                'Big file title': 'На обработку выбранного файла может потребоваться большое количество времени.',
                'Big file body': 'Обработка выбранного Вами файла может занять более 1 секунды. Во время этого '
                                 'процесса может показаться, что программа не отвечает. Вы уверены, '
                                 'что хотите продолжить?',
                'Show help': 'Показать помощь',
                'Hide help': 'Скрыть помощь',
                # help messages
                'fe help': 'Fernet — безопасный алгоритм шифрования, основанный на AES. После того, как данные '
                           'зашифрованны определенным ключом, единственный возможный метод расшифровать их — '
                           'использовать тот же ключ. В случае отсутствия ключа требуется перебор, который может '
                           'занять до '
                           '2^128 операций для данного алгоритма. На сегодняшний день нет ни одного компьютера, '
                           'который был бы способен провести столько вычислений за адекватное количество времени.\n\n'
                           'Чтобы зашифровать данные, Вам потребуется уникальный ключ Fernet. Вы можете '
                           'сгенерировать случайный ключ в приложении. Когда ключ сгенерирован, он автоматически '
                           'копируется во вкладку \"Расшифровка Fernet\".',
                'fd help': 'Чтобы расшифровать данные, Вам потребуется '
                           'тот же самый ключ, который был использован для шифрования. Если зашифрованные данные '
                           'были поврежденны или использован неправильный ключ, то расшифровка завершится '
                           'соответствующим сообщением.\n\n'
                           'Для информации об алгоритме шифрования Fernet, смотрите помощь в разделе '
                           '\"Расшифровка Fernet\"',
                'sha help': 'SHA - это семейство алгоритмов хеширования, разработанных NIST. \"Хеширование \" - '
                            'сложный '
                            'процесс, который генерирует одинаковый уникальный вывод (хеш) для любых входных данных. '
                            'Хеширование важно в современном мире и широко используется против киберпреступности. \n\n'
                            'Одно из применений хеширования - проверить, правильно ли был передан файл через Интернет '
                            '(проверка целостности файла). Для этого отправитель должен '
                            'вычислить хеш для этого файла, отправить '
                            'его с файлом, и получатель также должен вычислить хеш для этого файла, а затем сравнить'
                            'его с исходным хешем. Вы можете упростить этот процесс, используя эту программу. \n\n '
                            'На сегодняшний день только SHA-1 из всех доступных здесь алгоритмов SHA считается '
                            'небезопасным. '
                            'В большинстве случаев используется SHA-256, но для повышенной защиты следует выбрать '
                            'SHA-512. '
                            'Семейство SHA3 относительно новое и на данный момент не рекомендуется, если Вы '
                            'планируете поделиться '
                            'Ваш хеш с другими, хотя он обеспечивает дополнительную защиту от некоторых атак.',
                'md5 help': 'MD5 - популярный алгоритм хеширования. Он был разработан очень давно. \"Хеширование \" - '
                            'это '
                             'сложный процесс, который генерирует одинаковый уникальный вывод (хэш) для любых входных '
                            'данных. '
                             'Хеширование важно в современном мире и широко используется против киберпреступности. \n\n'
                             'Запрещенно использовать MD5, поскольку была обнаружена коллизия в 1995 году. Вместо него,' 
                             'используйте любой современный SHA. '
                             'Тем не менее, проверка целостности файлов с помощью MD5 может осуществляться.'
                             'Чтобы прочитать о проверках целостности файлов, перейдите в раздел справки на вкладке '
                            '\"SHA\". ',
                'exit title': 'Вы хотите удалить базу данных ключей Fernet?',
                'exit body': 'Мы рекомендуем удалить базы данных при выходе. Если вы попытались выйти случайно, '
                             'используйте \"Отменить\" чтобы вернуться в программу.'
                }

# Handouter

Тулза для автоматической вёрстки раздаток по простому текстовому описанию.

Пример описания можно посмотреть в `examples/handouts.txt`

Установка: `pip install handouter`. После установки доступна утилита `hndt`.

Пример запуска: `hndt --lang ru example/handouts.txt`. Вместо `hndt` можно писать `python -m handouter`.

Помимо утилиты `hndt`, устанавливается утилита `hndt-gen`. Она по chgksuite-файлу с расширением `.4s` генерирует txt-файл в формате handouter. Пример запуска: `hndt-gen packet.4s` → появится файл `packet_handouts.txt`.

~~Чтобы работало, надо, чтобы в `PATH` была тулза [tectonic](https://github.com/tectonic-typesetting/tectonic/releases/).~~ Upd.: уже не нужно, теперь тектоник ставится автоматически
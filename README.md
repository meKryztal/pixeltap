# Автофарм Pixel tap
![photo_2024-06-27_23-48-21](https://github.com/meKryztal/pixeltap/assets/47853767/bd470927-bf60-4375-b4f2-13acc5f46d0a)

-  Клеймит каждые 7 часов поинты, можно изменить, в коде есть комментарий
-  Забирает дейли ревард
-  Можно загрузить сотни акков
-  Работа по ключу, без авторизации
-  Сам улучшает питомцев
-  Сам покупает новых питомцев
-  Делает комбо



# Установка:
1. Установить python (Протестировано на 3.11)

2. Зайти в cmd и вписывать
   ```
   git clone https://github.com/meKryztal/pixeltap.git
   ```
   ```
   cd pixelverse
   ```
4. Установить модули
   
   ```
   pip install -r requirements.txt
   ```

   или

   ```
   python -m pip install -r requirements.txt
   ```
   
   или
   
   ```
   pip3 install -r requirements.txt
   ```

   или

   ```
   python3 -m pip install -r requirements.txt
   ```

6. Запуск
   Без рандомных комбо
   ```
   python NotRandomCombo.py
   ```

   или

   ```
   python3 NotRandomCombo.py
   ```
   С рандомными комбо
   
   ```
   python tre11t.py
   ```

   или

   ```
   python3 tre11t.py
   ```
Вставить в файл initdata ключи такого вида, каждый новый ключ с новой строки:
   ```
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   ```

# Как получить query_id:
Заходите в telegram web, открываете бота, жмете F12 и переходите в Network, жмете в боте Fight for supply и devtool ищете запрос с именем heath (Их будет два, вам нужен у которого Status Code: 200 OK), в правой колонке находите initdata: query_id=бла бла бла
![photo_2024-06-27_23-48-24](https://github.com/meKryztal/pixeltap/assets/47853767/9abd5c91-2acd-4991-b458-0b11c43f37fc)

# Рандомные комбо, то запускать tre11t.py
# Если не хотите рандомные комбо, то запускать NotRandomCombo.py

# Pet List
| Номер                               | Питомец                                                    |
| ---------------------------------- | ------------------------------------------------------------- |
| 1 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717749670570_1.png" width="100" height="100"> |
| 2 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717753602725_black_puma.png" width="100" height="100"> |
| 3 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717750211798_19.png" width="100" height="100"> |
| 4 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717750211795_16.png" width="100" height="100"> |
| 5 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717750072415_13.png" width="100" height="100"> |
| 6 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717750072416_15.png" width="100" height="100"> |
| 7 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717749670581_5.png" width="100" height="100"> |
| 8 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717749762365_8.png" width="100" height="100"> |
| 9 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717749670580_4.png" width="100" height="100"> |
| 10 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717750072415_14.png" width="100" height="100"> |
| 11 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717750072412_11.png" width="100" height="100"> |
| 12 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717750072414_12.png" width="100" height="100"> |
| 13 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717750211797_18.png" width="100" height="100"> |
| 14 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717749762363_6.png" width="100" height="100"> |
| 15 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717749762367_10.png" width="100" height="100"> |
| 16 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717750211796_17.png" width="100" height="100"> |
| 17 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717749670578_2.png" width="100" height="100"> |
| 18 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717749670579_3.png" width="100" height="100"> |
| 19 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717749762364_7.png" width="100" height="100"> |
| 20 | <img src="https://storage.googleapis.com/pixelverse-dev.appspot.com/1717749762366_9.png" width="100" height="100"> |

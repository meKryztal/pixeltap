# Автофарм Pixel tap
![photo_2024-06-27_23-48-21](https://github.com/meKryztal/pixeltap/assets/47853767/bd470927-bf60-4375-b4f2-13acc5f46d0a)

-  Клеймит каждые 7 часов поинты, можно изменить, в коде есть комментарий
-  Забирает дейли ревард
-  Можно загрузить сотни акков
-  Работа по ключу, без авторизации
-  Сам улучшает питомцев
-  Сам покупает новых питомцев
-  Выбирает рандомно 4 питомца в комбо



# Установка:
   ```
   pip install -r requirements.txt
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

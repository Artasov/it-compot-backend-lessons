# Static, post, request, условия.
На этом занятии мы реализуем игру с угадыванием числа.

1.  ## Создаем страничку для игры MagicNumber.
    Желательно чтобы ученики сделали сами.
    ```python
        # app_name/views.py
        def magic_number(request):
            return render(request, 'app_name/magic_number.html')
    ```
    ```python
        # project_name/urls.py
        from app_name.views import magic_number  # импортируем функцию
        
        urlpatterns = [
            path('magic_number/', magic_number),  # связываем маршрут и функцию
        ]
    ```
2.  ## Создаем формочку из одного input и кнопки.
    Тоже ученики должны сделать сами.<br>
    После добавляем `method="post"` `{% csrf_token %}` объясняем, что это.
    ```html
    <h1>Магическое число</h1>
    <form method="post"> {% csrf_token %} 
        <input type="number" placeholder="Угадай число" name="number">
        <button type="submit">Угадать</button>
    </form>
    ```
    Чтобы каждый раз не загружать `bootstrap` по ссылке давайте его скачаем.
    > На самом деле он кэшируется, но это пока не важно.
    
    Кто-нибудь спросит куда нужно сохранять этот файл.<br>
    Рассказываем про то, как устроено хранение статических файлов в django.<br>
     ┣-📂app1 `Приложение app1`<br>
     ┃    ┣-📂migrations `Файлы миграций`<br>
     ┃    ┣-📂static `Статические файлы`<br>
     ┃    ┃    ┣-📂app1 `Статические файлы app1 приложения`<br>
     ┃    ┃    ┃    ┣-📂css<br>
     ┃    ┃    ┃    ┃    ┗-📜bootstrap.min.css<br>
     ┃    ┃    ┃    ┣-📂img<br>
     ┃    ┃    ┃    ┗-📂js<br>
     ┃    ┣-📜__init__.py<br>
     ┃    ┣-📜apps.py<br>
     ┃    ┣-📜admin.py `Управление админкой`<br>
     ┃    ┣-📜models.py `Модели приложения app1`<br>
     ┃    ┣-📜urls.py `Маршруты приложения app1`<br>
     ┗    ┗-📜views.py `Функции приложения app1 для отображения страниц`<br>
    Подключаем .css файл в html.
    ```html
    {% load static %}
    <head>
        <link rel="stylesheet" href="{% static 'app1/css/bootstrap.min.css' %}"> 
    </head>
    ```
    Дальше пусть ученики сделают оформление формы (минуты 3-6).

3.  ## Получение данных во view
    ```python
    # app_name/views.py
    def magic_number(request):
        return render(request, 'app_name/magic_number.html', {'result': 'Победа'})
    ```
    ```html
    <h1 class="text-light text-center ">Магическое число</h1>
    <p>{{ result }}</p>
    <form method="post" class="d-flex flex-column gap-2 mx-auto"
          style="max-width: 150px;"> {% csrf_token %}
        <input class="form-control" type="number" placeholder="Угадай число" name="number">
        <button class="btn btn-primary mx-auto" type="submit">Угадать</button>
    </form>
    ```
    *   ### Обязательно рассказываем про render()
        Функция `render` в Django используется для формирования HTML-страницы по HTML-шаблону. 
        Она берет шаблон (второй аргумент функции `templates/some/some_more/some.html`) 
        и контекст (данные, которые нужно вставить в шаблон), комбинирует их вместе,
        заменяя например {{ result }} на значение переменной number
        и возвращает результат как HTTP-ответ с готовой HTML-страницей.<br><br>
        Попробуйте `распечатать render()`.
        ```python
        # app_name/views.py
        def magic_number(request):
            print(
                render(request, 'app_name/magic_number.html', {'result': number})
            )
            return render(request, 'app_name/magic_number.html', {'result': 'Победа'})
        ```
        Раздел про это есть в 
        **[шпаргалке](https://github.com/xlartas/it-compot-backend-methods/)**.
        
        
4.  ## Передача данных в шаблон.
    Показываем как получать данные из запроса и предложите самим попробовать вывести на страницу их число.<br>
    Объясняем, что такое request.
    ##### Учим использовать `print()`
       > С помощью print можно тестировать какие данные присутствуют на том или инном этапе выполнения кода.<br>
       > В дальнейшем всегда прибегайте к его использованию, если что-то не понятно или что-то не работает.
    ```python
    # app_name/views.py
    import random
    def magic_number(request):
        # Получаем данные из request
        number = request.POST['number']
        print(request.POST)
        print(number)
        # вместо [] правильнее использовать .get(), ошибка допущена специально.
        return render(request, 'app_name/magic_number.html', {'result': number})
    ```
    
     Генерируем число и сравниваем его со случайным. Отправляем результат в шаблон.
    ```python
    # app_name/views.py
    import random
    def magic_number(request):
        # Получаем данные из request
        number = request.POST['number']
        # Преобразуем строку в число
        number = int(number)
        # Генерируем случайное число от 1 до 5
        random_number = random.randint(1, 5)
        
        if user_guess == random_number:
            result = "Поздравляем, вы угадали число!"
        else:
            result = f"К сожалению, было загаданно число {random_number}. Попробуйте ещё раз."
            
        return render(request, 'app_name/magic_number.html', {'result': number})
    ```
    Теперь без `post` запроса мы не можем загрузить страницу из-за ошибки.<br>
    Знакомим немного с тем как отображаются ошибки django.<br>
    Когда мы просто загружаем страницу мы выполняем `GET`, <br>
    а обрабатываем корректно только `POST`.<br>
    Нужно отдельно обрабатывать эти запросы.
    Значит нужно сделать проверку `if request.method == 'POST':`<br>
    Даем время подумать куда ее вставить и как это все организовать.<br>
    ```python
    from django.shortcuts import render
    import random
    
    def magic_number(request):
        # Если POST
        if request.method == 'POST':
            number = int(request.POST['number'])
            random_number = random.randint(1, 5)
            if magic_number == random_number:
                result = "Поздравляем, вы угадали число!"
            else:
                result = f"К сожалению, загаданное число было {random_number}. Попробуйте ещё раз."
            
            return render(request, 'magic_number.html', {'result': result})
        
        # Если GET
        return render(request, 'magic_number.html')
    ```
    
Проверяем, радуемся.
># git push...
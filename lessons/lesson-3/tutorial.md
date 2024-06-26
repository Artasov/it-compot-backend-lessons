# Static, post, request, условия. Магическое число 1.
На этом занятии мы реализуем игру с угадыванием числа.

1.  ## Создаем страничку для игры MagicNumber.
    Желательно чтобы ученики сделали сами.
    ```python
        # Core/views.py
        def magic_number(request):
            return render(request, 'Core/magic_number.html')
    ```
    ```python
        # config/urls.py
        from Core.views import magic_number  # импортируем функцию
        
        urlpatterns = [
            path('magic_number/', magic_number),  # связываем маршрут и функцию
        ]
    ```
2.  ## Создаем формочку из одного input и кнопки.
    Тоже ученики должны сделать сами.<br>
    После добавляем `method="post"` `{% csrf_token %}` объясняем, что это.
    ```html
    <!-- Core/magic_number.html -->
    <h1>Магическое число</h1>
    <form method="post"> {% csrf_token %} 
        <input type="number" placeholder="Угадай число" name="number">
        <button type="submit">Угадать</button>
    </form>
    ```
3. ## Статические файлы What is dis?
    Чтобы каждый раз не загружать `bootstrap` по ссылке давайте его скачаем.
    > На самом деле он кэшируется, но это пока не важно.
   
    Рассказываем про статические файлы.
    Подробно в [разделе шпаргалки](https://github.com/xlartas/it-compot-backend-methods/blob/main/django-base.md#static-files).

    Подключаем `.css` файл.
    ```html
    <!-- Core/magic_number.html -->
    {% load static %}
    <head>
        <link rel="stylesheet" href="{% static 'core/css/bootstrap.min.css' %}"> 
    </head>
    ```
    Дальше пусть ученики сделают оформление формы (минуты 3-6).

3.  ## Получение данных во view
    ```python
    # Core/views.py
    def magic_number(request):
        return render(request, 'Core/magic_number.html', {'result': 'Победа'})
    ```
    ```html
    <!-- Core/magic_number.html -->
    <h1 class="text-light text-center ">Магическое число</h1>
    <p>{{ result }}</p>
    <form method="post" class="d-flex flex-column gap-2 mx-auto"
          style="max-width: 150px;"> {% csrf_token %}
        <input class="form-control" type="number" placeholder="Угадай число" name="number">
        <button class="btn btn-primary mx-auto" type="submit">Угадать</button>
    </form>
    ```
    *   ### Обязательно рассказываем про render()
        `render(request, template_path, context)`<br><br>
    
        `request`: переменная которая приходит вместе с запросом (`def magic_number(request)`)<br>
        содержит данные о ткущем пользователе и много другой нужной информации, которую пока нам знать не надо.<br>
        `template_path`: путь до шаблона начиная от папки **_templates_**<br>
        `context`: переменная типа `dict` для передачи переменных внутрь шаблона.<br><br>
    
        Функция `render` в Django используется для формирования HTML-страницы по HTML-шаблону. 
        Она берет шаблон *(template_path)* и `контекст`, комбинирует их вместе,
        заменяя в шаблоне `{{ ИМЯ ПЕРЕДАННОГО ПАРАМЕТРА }}` на значение этого параметра
        и возвращает результат как HTTP-ответ с готовой HTML-страницей.<br><br>
        Попробуйте `распечатать render()` ради интереса.
        ```python
        # Core/views.py
        def magic_number(request):
            print(
                render(request, 'Core/magic_number.html', {'result': number})
            )
            return render(request, 'Core/magic_number.html', {'result': 'Победа'})
        ```
        Раздел про это есть в 
        **[шпаргалке](https://github.com/xlartas/it-compot-backend-methods/blob/main/django-base.md#%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82%D1%83)**.

4.  ## Передача данных в шаблон.
    Показываем как получать данные из запроса и предложите самим попробовать вывести на страницу их число.<br>
    Объясняем, что такое request.
    ##### Учим использовать `print()`
       > С помощью print можно тестировать какие данные присутствуют на том или ином этапе выполнения кода.<br>
       В дальнейшем используйте, если что-то не понятно или что-то не работает.
    ```python
    # Core/views.py
    import random
    def magic_number(request):
        # Получаем данные из request
        number = request.POST['number']
        print(request.POST)
        print(number)
        # познакомьте учеников с полями обьекта request: WSGIRequest 
        # print(request.method) как пример, мы его будем использовать далее.
    
        # вместо [] правильнее использовать .get() и использовать дополнительные проверки, 'ошибка' допущена специально.
        return render(request, 'Core/magic_number.html', {'result': number})
    ```
    ### Не идете дальше если возникают трудности, не спешите, оставьте на следующий урок. Повторите пройденное целиком лучше.
        
    
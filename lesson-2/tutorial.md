# Статические файлы, тэг form, bootstrap, git
Работа с сервером почти во всех случаях сопровождается обменом данных между клиентом и сервером
и сегодня мы научимся создавать форму для ввода пользовательских данных и отправлять их на сервер.
Для примера будем делать форму регистрации новых пользователей. В дальнейшем используем её когда 
будем работать с User в django.

## Делаем форму на новой странице.
Желательно сразу задать адрес `magic_number/` или что-то типа того.
Рассказываем о разных видах input'ов и вообще о тэге form и его атрибутах.
```html
<body>
    <h1>Регистрация</h1>
    <form action="Если не писать, то отправка идёт на текущий адрес." method="get">
        <input type="text" placeholder="Имя" name="name">
        <input type="email" placeholder="Почта" name="email">
        <input type="password" placeholder="Пароль" name="password">
        <input type="password" placeholder="Повторите пароль" name="password_repeat">
        <button type="submit">Подтвердить</button>
    </form>
</body>
```

## На этом этапе ученики скорее всего захотят стилизировать форму.
Рассказываем и показываем что такое `bootstrap` и зачем он нужен.<br>
Скачиваем **[Bootstrap](https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css)**.<br>
Кто-то точно спросит где должен храниться этот файл.<br>

Рассказываем про то, как устроено хранение статических файлов в django.<br>
 ┣- 📂app1 `Приложение app1`<br>
 ┃  ┣- 📂migrations `Файлы миграций`<br>
 ┃  ┣- 📂static `Статические файлы`<br>
 ┃  ┃  ┣- 📂app1 `Статические файлы app1 приложения`<br>
 ┃  ┃  ┃  ┣- 📂css<br>
 ┃  ┃  ┃  ┃  ┗- 📜bootstrap.min.css<br>
 ┃  ┃  ┃  ┣- 📂img<br>
 ┃  ┃  ┃  ┗- 📂js<br>

Подключаем .css файл в html.
```html
{% load static %}
...
<head>
    <link rel="stylesheet" href="{% static 'app1/css/bootstrap.min.css' %}"> 
</head>
```
Проверяем и видим, что уже что-то изменилось.<br>
Начинаем стилизировать.
>Я бы не рассказывал про сетку
>на данном этапе, это не так просто для понимания даже для hard уровня, но если
>в учениках уверены можно и рассказать или если время останется в конце.

**Скидывает ученикам [это](https://github.com/Artasov/itcompot-methods/blob/main/bootstrap-base.md)**.
Обязательно рассказываем про часто используемые классы.
В готовые элементы идти пока рано.

Даем ученикам самим поприменять классы, подсказываем.<br>
По итогу должно получиться примерно это.
>Естественно, если изики убираем сложные поля. Это версия для Hard.


```html
<!-- Я знаю, что нужно использовать label, но им это не нужно сейчас. -->
<div class="mt-5">
    <h1 class="text-center text-light my-3">Регистрация</h1>
    <form class="d-flex flex-column gap-2 mx-auto"
          style="max-width: 300px;">
        <input class="form-control" type="text" 
               placeholder="Имя" name="name">
        <input class="form-control" type="email" 
               placeholder="Почта" name="email">
        <input class="form-control" type="password" 
               placeholder="Пароль" name="password">
        <input class="form-control" type="password" 
               placeholder="Повторите пароль" name="password_repeat">

        <div class="text-secondary d-flex gap-2 justify-content-center">
            <span>Мужчина</span>
            <input class="form-check-input" type="radio" name="gender" id="male" value="male">
            <input class="form-check-input" type="radio" name="gender" id="female" value="female">
            <span>Женщина</span>
        </div>

        <div class="mx-auto">
            <input class="form-check-input" type="checkbox" name="sub_email">
            <span class="fs-6 text-secondary">Хочу получать рассылку</span>
        </div>
        <button style="max-width: 90%; min-width: 200px;"
                class="btn btn-primary mx-auto my-2"
                type="submit">Подтвердить
        </button>
    </form>
</div>
```


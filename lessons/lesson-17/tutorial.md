# Начало работы с пользователями в Django
Сегодня мы начнем изучить как работает аутентификация и система пользователей в Django.
Сразу скажу, что целиком скорее всего не успеем.

1. ## Аутентификация и авторизация
   ### Это желательно проговорить в начале и вкратце в конце + в начале следующего урока 😅
   > Адаптируйте фразировку под учеников разных уровней. Этот текст больше для вас, преподавателей.
   
   &nbsp;&nbsp;&nbsp;&nbsp;Аутентификация и авторизация – ключевые концепции в веб-разработке.<br>
   Аутентификация – это процесс, посредством которого система определяет, кто вы, <br>
   обычно через имя пользователя и пароль. <br>
   &nbsp;&nbsp;&nbsp;&nbsp;После аутентификации идет авторизация, которая определяет, что пользователь может делать в системе – например, <br>
   какие страницы он может посещать или какие функции использовать.<br><br>
   
   &nbsp;&nbsp;&nbsp;&nbsp;В Django, управление пользователями и группами, а также аутентификация и авторизация, <br>
   обеспечивается с помощью приложения по умолчанию `django.contrib.auth`, 
   при старте проекта оно уже есть в `INSTALLED_APPS`. <br><br>
   
   &nbsp;&nbsp;&nbsp;&nbsp;Это приложение включает в себя модель `User`, которая содержит основную информацию о пользователях, <br>
   и механизмы для работы с паролями, сессиями и правами доступа.<br>
   То есть создавать отдельную модель нам не нужно. (Однако если мы захотим дополнить/изменить поля модели пользователя, то нужно...)<br><br>
   
   &nbsp;&nbsp;&nbsp;&nbsp;Покажите ученикам это приложение и модели по следующему пути:<br>
   `venv\Lib\site-packages\django\contrib\auth\models.py`<br>
   В этом файле есть модель `User`, которая наследуется от `AbstractUser`, а в ней <br>
   вы найдете существующие поля для пользователя стандартного пользователя.<br>
   Важно акцентировать внимание, что это такое же приложение, как и наши, но просто гораздо сложнее.<br><br>
   
   &nbsp;&nbsp;&nbsp;&nbsp;Сессии в контексте web разработки это механизм который 
   используются для сохранения информации о текущем пользователе между различными запросами. <br>
   &nbsp;&nbsp;&nbsp;&nbsp;Когда пользователь аутентифицируется, Django создает сессию, которая 
   представляет собой набор данных, хранящийся на сервере, с уникальным идентификатором, 
   отправляемым в браузер пользователя в виде cookie. <br>
   &nbsp;&nbsp;&nbsp;&nbsp;При последующих запросах `cookie` возвращается серверу, позволяя 
   Django идентифицировать пользователя и предоставить соответствующий доступ.<br>
   &nbsp;&nbsp;&nbsp;&nbsp;**А если более простым языком, то сессии позволяют один раз войти и ходить по страницам <br>
   уже авторизированным, а не входить каждый раз по новой при перезагрузке страницы (как пример).**
   
   ```python
   # settings.py
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',  <------------ 
       'django.contrib.contenttypes',
       'django.contrib.sessions',  <------------ 
       'django.contrib.messages',
       'django.contrib.staticfiles',
       ...
   ]
   ```
   >Мы уже использовали эти приложения, сами того не замечая, когда заходили в админку.
   
   Для регистрации и входа нам нужно создать соответствующие страницы с формами для входа, регистрации, <br>
   отрендерить их внутри функций внутри views.py, <br>
   а их связать с маршрутами в urls.py.
   > Мы намеренно не будем использовать Django Forms, как и раньше.
   
   Спросите учеников, где мы будем создавать эти страницы? <br>
   У нас есть приложение shop, но в нем нелогично создавать регистрацию, лучше декомпозировать эту логику.
   
   Поэтому создадим приложение `Core`.<br>
   `python manage.py startapp Core`
    > Не забываем добавить в `INSTALLED_APPS`


2. ## Сделаем базовые действия для создания страниц `SignUp` `SignIn` `SignOut` `Profile`
   Чтобы пользователь мог войти в систему, он сначала должен зарегистрироваться.<br>
   Регистрация обычно включает сбор необходимой информации, такой как имя пользователя и пароль..., <br>
   и создание нового объекта пользователя в базе данных по этим данным. Так же должна быть возможность выйти.<br>
   
   * ### Создайте `Core/urls.py`
      ```python
      # Core/urls.py
      from django.urls import path
      from .views import signup, signin, profile, signout
      
      urlpatterns = [
          path('signup/', signup, name='signup'),
          path('signin/', signin, name='signin'),
          path('signout/', signout, name='signout'),
          path('profile/', profile, name='profile'),
      ]
      ```
   * ### Подключите эти адреса к корневым.
      ```python
      # config/urls.py
      ...
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('shop/', include('shop.urls')),
          path('', include('Core.urls')), <--------------
      ]
      ```
   * ### Создайте шаблоны
      Для логичности создайте дополнительную папку auth.<br>
      `Core/templates/Core/auth/signup.html`<br>
      `Core/templates/Core/auth/signin.html`<br>
      `Core/templates/Core/auth/profile.html`<br>
      > Для `signout` страницы не будет.
   
   * ### Создайте контроллеры (функции обрабатывающие запросы)
      ```python
      # Core/views.py
      from django.shortcuts import render

      def signup(request):
          return render(request, 'Core/auth/signup.html')
      
      def signin(request):
          return render(request, 'Core/auth/signin.html')
     
      def signout(request):
          # Пока пусто
          pass 
      
      def profile(request):
          return render(request, 'Core/auth/profile.html')

      ```
   ### Проверьте, что все работает и страницы открываются.
  
3. ## Реализация шаблонов.
   В обоих шаблонах будут формы. <br>
   Ученики должны помнить как делаются формы, пусть попробуют справиться сами.
   > Внимательно проставляйте аттрибут `name` у `input`
   
   * ### Форма регистрации
      В форме будут 4 поля:<br>
      `username`, `email`, `password`, `repeat_password`
      ```html
      <!-- signup.html -->
      {% extends 'shop/base.html' %}
      {% load static %}
      {% block title %}Shop | SignUp{% endblock %}
      
      {% block content %}
          <h1 class="text-body text-center fw-bold mb-4">Sign Up</h1>
          <div class="d-flex gap-3 flex-wrap justify-content-center mx-auto">
              <form class="d-flex flex-column gap-2" method="post">
                  {% csrf_token %}
                  <input type="text" name="username"
                         placeholder="Username"
                         minlength="6" maxlength="50"
                         class="form-control text-center">
                  <input type="text" name="email"
                         placeholder="Email"
                         minlength="4" maxlength="100"
                         class="form-control text-center">
                  <input type="password" name="password"
                         placeholder="Password"
                         minlength="6" maxlength="100"
                         class="form-control text-center">
                  <input type="password" name="repeat_password"
                         placeholder="Repeat password"
                         minlength="6" maxlength="100"
                         class="form-control text-center">
                  <button class="btn btn-secondary">Confim</button>
              </form>
          </div>
      {% endblock %}
      ```
   * ### Форма входа
      2 поля: `username`, `password`
      ```html
      <!-- signin.html -->
      {% extends 'shop/base.html' %}
      {% load static %}
      {% block title %}Shop | SignIn{% endblock %}
      
      {% block content %}
          <h1 class="text-body text-center fw-bold mb-4">Sign In</h1>
          <div class="d-flex gap-3 flex-wrap justify-content-center mx-auto">
              <form class="d-flex flex-column gap-2" method="post">
                  {% csrf_token %}
                  <input type="text" name="username"
                         placeholder="Username"
                         minlength="3" maxlength="50"
                         class="form-control text-center">
                  <input type="password" name="password"
                         placeholder="Password"
                         minlength="3" maxlength="100"
                         class="form-control text-center">
                  <button class="btn btn-secondary">Login</button>
              </form>
          </div>
      {% endblock %}
      ```

3. ## Улучшим структуру проекта.
   *  Сейчас в приложении `shop` хранятся <br>
      `header.html` `footer.html` `base.html` `bootstrap.min.css`<br>
      Это не правильно, ведь эти файлы не относятся к магазину.<br>
      Они относятся к сайту в целом, а значит их лучше переместить в `Core`.<br><br>
       
      Перемещаем и корректируем пути.
      > Не забудьте исправить пути при наследовании `{% extends 'Core/base.html' %}`.<br>
      > Так же пути до header, footer, bootstrap.min.css, bootstrap.bundle.min.js
   
   *  В папке с конфигурацией проекта(там где `settings.py`) по-хорошему<br>
      должна быть только конфигурация, как ни странно.<br>
      Посмотрим, что там есть сейчас:<br>
      ┣---📂config `Конфигурация проекта`<br>
      ┃ ┣---📜__init__.py `Файл для распознавания текущей дериктории как python модуль`(Пока что не важно)<br>
      ┃ ┣---📜settings.py `Настройки проекта`<br>
      ┃ ┣---📜urls.py `Корневые маршруты`<br>
      ┃ ┣---📜wsgi.py `Настройки синхронного сервера` (Пока что не важно)<br>
      ┃ ┗---📜asgi.py `Настройки асинхронного сервера` (Пока что не важно)<br>
      Лишним тут является `urls.py`, давайте переместим из него маршруты
      и создание маршрутов для Media файлов в `Core/urls.py`, а `config/urls.py` удалим.
      
      ```python
      # Core/urls.py
      from django.conf import settings
      from django.conf.urls.static import static
      from django.contrib import admin
      from django.urls import path, include
      
      from .views import signup, signin, signout
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('signup/', signup, name='signup'),
          path('signin/', signin, name='signin'),
          path('signout/', signout, name='signout'),
      
          path('shop/', include('shop.urls')),
      ]
      if settings.DEBUG:
          urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      ```
      Теперь нужно указать новый файл для корневых маршрутов.<br>
      Найдите переменную <br>
      `ROOT_URLCONF = 'config.urls'`<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;замените на <br>
      `ROOT_URLCONF = 'Core.urls'`<br>
   
      ### Проверяем сервер на работоспособность.
      Теперь в папке `config` находятся только те файлы, которые<br>
      относятся к конфигурации проекта и сервера.

      
## Подведите итоги.
># git push...






  
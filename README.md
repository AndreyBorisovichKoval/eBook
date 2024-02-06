##### _____________________________________

## Приложение

# **eBook**

##### _____________________________________

*Примечание*:

* Настоящий проект был создан в процессе обучения командой учащихся **Alif Академии** в составе 4-х человек (преподаватель курса: **Рахимов Некруз**).
* В рамках своего обучения, участники команды сотрудничали и вкладывали свои усилия для разработки и реализации проекта. Они использовали полученные, в процессе обучения, знания и навыки, чтобы создать проект, отражающий их творческий подход и коллективную работу.

* Проект был разработан с учетом целей и задач, поставленных перед командой в процессе обучения. Это был программный проект, который требовал совместного участия и вклада каждого участника команды.

* Клонирование этого проекта с GitHub позволит сохранить и распространить результаты работы команды учащихся, а также даст возможность другим людям изучить детали проекта, внести свои вклады или использовать его в качестве основы для своих собственных проектов.

* Таким образом, клонирование проекта позволяет сохранить и распространить труд и достижения команды учащихся в процессе их обучения, давая возможность другим ученикам или пользователям воспользоваться и изучить этот проект, учитывая его контекст разработки в рамках обучения.

* Дата начала реализации проекта: **30**/**01**/20**24**. Окончание: **02**/**02**/20**24**.
* Проект не являлся коммерческим и был реализован "***на быструю руку***" :-)

##### _____________________________________

## Описание проекта

**eBook**  -  Помощник **Библиотекаря**, который предоставляет широкий спектр функций и возможностей для удобного управления Библиотекой с "***аналоговыми***" книгами.
1. Помогает вести учет бумажных книг в библиотеке. Вы можете добавлять новые книги в коллекцию, удалять книги, а также обновлять информацию о каждой книге, такую как название, автор, издательство и т.д.
2. ***Организация каталога***: Помощник позволяет создавать систематизированный каталог книг, используя различные категории, жанры или метки. Вы можете легко найти нужную книгу, используя поиск или просматривая различные категории.
3. ***Управление выдачей и возвратом***: помогает отслеживать выдачу книг читателям и контролировать их возврат. Вы можете отмечать, кому была выдана книга, записывать дату выдачи и устанавливать сроки возврата.
* Также реализованы всевозможные дополнительные функции.

##### _____________________________________

## Стек проекта

### HTTP - Flask

* **Flask** — это упрощенная платформа ***Python для веб-приложений***, которая обеспечивает
основные возможности маршрутизации <URL-адресов> и визуализации страниц. **Flask** называют "микро"-платформой, так как она не предоставляет напрямую такие функции, как проверка форм, абстракция базы данных, проверка подлинности и т. д. Эти функции предоставляются специальными пакетами Python, называемыми расширениями **Flask**.

### DataBase - SQLAlchemy

* **SQLAlchemy** — это набор инструментов ***Python SQL*** и реляционный преобразователь **объектов**,
который предоставляет разработчикам приложений всю мощь и гибкость **SQL**.

##### _____________________________________

_-=*=-_

- Это **бекендная часть приложения**, которая предоставляет API и обрабатывает бизнес-логику. Здесь нет **фронтендной** части, так как это отдельный компонент, который может быть (и возможно будет) разработан.
Приложение служит интерфейсом для обмена данными с другими приложениями или компонентами. Оно предоставляет набор эндпоинтов ***(URL-адресов)***, по которым другие приложения или клиенты **могут отправлять запросы** и **получать ответы**.

##### _____________________________________

## Выполняемые задачи проекта:

### 1. Управление книгами:

1. Добавление, редактирование и удаление информации о книгах.
2. Установка авторов, жанров и других атрибутов для каждой книги.
3. Возможность загрузки обложек книг.

### 2. Управление читателями:

1. Добавление и редактирование данных о читателях.
2. Просмотр списка читателей и их активности.
3. Отслеживание взятых книг и сроков возврата.

### 3. Управление заказами:
1. Регистрация новых заказов на книги.
2. Отметка заказов как выполненных или отклоненных.
3. Отображение деталей заказа, включая книги, статус и сроки.

### 4. Управление персоналом:

1. Добавление и удаление библиотекарей и администраторов.
2. Установка различных ролей и прав доступа для персонала.

##### _____________________________________

## Структура проекта

**Books**
* id: Целочисленное поле, являющееся первичным ключом для таблицы. Каждая книга в библиотеке имеет уникальный идентификатор.
* title: Строковое поле с ограничением длины до 255 символов, содержащее название книги.
* publication: Строковое поле с ограничением длины до 50 символов, содержащее информацию о издательстве книги.
* publication_date: Поле типа DateTime, содержащее дату публикации книги.
* cover_image: Строковое поле, содержащее путь к обложке книги.
* book_location: Строковое поле с ограничением длины до 8 символов, представляющее информацию о местонахождении книги в библиотеке, например, этаж, ряд, стеллаж и полка.
* description: Строковое поле с ограничением длины до 120 символов, содержащее описание книги.
* price: Поле типа Float, содержащее цену книги.
* available_copies: Целочисленное поле, содержащее количество доступных копий книги.

Это таблица, которая содержит информацию о книгах в библиотеке. У каждой книги есть уникальный идентификатор (id), название (title), издательство (publication), дата публикации (publication_date), обложка (cover_image), местонахождение (book_location), описание (description), цена (price) и количество доступных копий (available_copies).

**BooksAuthors**
* id: Целочисленное поле, являющееся первичным ключом для таблицы. Каждая запись в таблице связывает книгу с автором.
* book_id: Целочисленное поле, внешний ключ, связанное с полем id в таблице Books, указывающее на книгу.
* author_id: Целочисленное поле, внешний ключ, связанное с полем id в таблице Authors, указывающее на автора.

В этой таблице хранится информация о связи между книгами и авторами. Каждая запись содержит уникальный идентификатор (id), идентификатор книги (book_id), связанный с таблицей Books, и идентификатор автора (author_id), связанный с таблицей Authors.

**Authors**
* id: Целочисленное поле, являющееся первичным ключом для таблицы. Каждый автор имеет уникальный идентификатор.
* author_name: Строковое поле с ограничением длины до 70 символов, содержащее имя автора.
* description: Строковое поле, содержащее описание автора.

Это таблица, которая содержит информацию об авторах книг. У каждого автора есть уникальный идентификатор (id), имя (author_name) и описание (description).

**BooksGenres**
* id: Целочисленное поле, являющееся первичным ключом для таблицы. Каждая запись в таблице связывает книгу с жанром.
* book_id: Целочисленное поле, внешний ключ, связанное с полем id в таблице Books, указывающее на книгу.
* genre_id: Целочисленное поле, внешний ключ, связанное с полем id в таблице Genres, указывающее на жанр.

В данной таблице хранится информация о связи между книгами и жанрами. Каждая запись содержит уникальный идентификатор (id), идентификатор книги (book_id), связанный с таблицей Books, и идентификатор жанра (genre_id), связанный с таблицей Genres.

**Genres**
* id: Целочисленное поле, являющееся первичным ключом для таблицы. Каждый жанр имеет уникальный идентификатор.
* title_genre: Строковое поле с ограничением длины до 70 символов, содержащее название жанра.

Это таблица, которая содержит информацию о жанрах книг. У каждого жанра есть уникальный идентификатор (id) и название (title_genre).

**Readers**
* id: Целочисленное поле, являющееся первичным ключом для таблицы. Каждый читатель имеет уникальный идентификатор.
* reader_name: Строковое поле с ограничением длины до 70 символов, содержащее имя читателя.
* year_birth: Год рождения читателя.

Интерпретация данной структуры:
В данной таблице хранится информация о читателях библиотеки. У каждого читателя есть уникальный идентификатор (id), имя (reader_name), год рождения (year_birth), адрес (reader_address) и электронная почта (email).

**BorrowedBooks**
* Это таблица, которая содержит информацию о выданных книгах. Каждая запись содержит уникальный идентификатор (id), идентификатор книги (book_id), связанный с таблицей Books, и идентификатор читателя (reader_id), связанный с таблицей Readers. Также есть поля, отражающие дату выдачи (date_borrowed), дату возврата (date_return), дату фактического возврата (date_returned) и информацию о статусе возврата (is_returned). Также есть поле, указывающее местонахождение книги (location).

**Orders**
* Это таблица, которая содержит информацию о заказах. У каждого заказа есть уникальный идентификатор (id), дата заказа (order_date) и статус (status). Также есть связь с таблицей OrderItems через поле order_items.

**OrderItems**
* В данной таблице хранится информация о товарах в заказе. Каждая запись содержит уникальный идентификатор (id), идентификатор заказа (order_id), связанный с таблицей Orders, и идентификатор книги (new_book_id), связанный с таблицей Books. Также есть поля, отражающие цену товара (new_book_price), количество (quantity) и связь с таблицей Books через поле new_book.

**Staff**

Таблица "Staff" содержит информацию о сотрудниках и их характеристиках.

Каждая запись в таблице представляет отдельного сотрудника и содержит следующие поля:

* id: Уникальный идентификатор сотрудника.
* name: Имя сотрудника.
* role: Роль, которую занимает сотрудник в организации.
* access_level: Уровень доступа сотрудника.
* is_deleted: Флаг, указывающий, удален ли сотрудник (soft-delete).

Поле **id** используется для однозначной идентификации сотрудника в таблице. **name** содержит имя сотрудника, **role** определяет роль, которую он занимает в организации (например, "***Библиотекарь***", "***Администратор***", "***Менеджер***" и т.д.). **access_level** указывает на уровень доступа сотрудника, который может использоваться для определения прав доступа в системе. Поле **is_deleted** является флагом, который указывает, удален ли сотрудник.

Функции выполняют операции добавления, получения, обновления и удаления сотрудников в таблице "**Staff**" с использованием ***ORM*** для взаимодействия с базой данных.

##### _____________________________________

## Структура проекта по файлам (модулям):

### main

* Данный код представляет собой простое приложение **Flask**, которое запускает веб-сервер и определяет маршруты для обработки HTTP-запросов.

* Первым шагом импортируется класс Flask из модуля flask. Затем импортируется переменная **app** из модуля **routes** (это модуль, содержащий определения маршрутов для приложения).

* Далее создается **экземпляр класса** Flask и присваивается переменной **app**. В качестве аргумента конструктору передается __name__, что указывает Flask на то, что это основной модуль или пакет.

* Затем вызывается метод register_blueprint() на объекте **app**, чтобы зарегистрировать маршруты из модуля routes. Регистрация маршрутов позволяет приложению знать, каким образом обрабатывать входящие HTTP-запросы.

* Наконец, проверяется, является ли текущий модуль **основным** модулем, вызывая **__name__ == '__main__'**. Если это так, то приложение запускается с помощью метода run() объекта **app**. В данном случае, включен режим отладки (debug=True) и сервер будет слушать порт 7000.

*   Таким образом, этот код создает ***Flask-приложение***, регистрирует маршруты и запускает сервер для обработки ***HTTP-запросов***.

### connection

* Данный код относится к работе с базой данных в приложении, используя ***SQLAlchemy***.

* Сначала импортируются всё необходимые: dbname_app, user_app, password_app, host_app, port_app из модуля **security**, а также **sessionmaker** и **create_engine** из модуля ***sqlalchemy***.

* Далее определяется строка подключения к базе данных **DATABASE_URL** с использованием значений, полученных из user_app, password_app, host_app, port_app и dbname_app. Эта строка будет содержать информацию, необходимую для установления соединения с базой данных **PostgreSQL**.

* Затем создается экземпляр класса **Engine** из модуля **create_engine** и передается ему **DATABASE_URL** в качестве аргумента. Этот объект (**engine**) представляет собой основной интерфейс к базе данных и будет использоваться для выполнения ***SQL-запросов***.

* Наконец, создается класс **Session** с использованием **sessionmaker**, который связывается с **engine**. Этот класс будет использоваться для создания отдельных сессий (экземпляров) для каждого подключения к базе данных. Сессии позволяют выполнять ***операции чтения и записи данных*** в базу данных.

* Таким образом, данный код устанавливает соединение с базой данных ***PostgreSQL*** с помощью ***SQLAlchemy*** и создает класс **Session**, который будет использоваться для управления подключениями к базе данных в приложении.

### models

Содержит архитетктуру базы данных со всеми ей таблицами и атрибутами таблиц.

**Классы** отражают ***структуру таблиц*** базы данных и связи между ними с использованием ***SQLAlchemy***.
Они предоставляют объектно-реляционное отображение **(ORM)**, которое позволяет взаимодействовать с данными в базе данных с помощью объектов и методов классов.

Таким образом эти таблицы хранят всю необходимую информацию.

### roules

Данный модуль представляет собой набор маршрутов (routes) для веб-приложения, созданного с использованием **Flask**, фреймворка для разработки веб-приложений на языке Python.
В данном модуле используется модуль ***repository***, содержащим функции для работы с базой данных и хранения данных. Код определяет различные маршруты (эндпоинты) для обработки ***HTTP-запросов*** и вызывает соответствующие функции из модуля ***repository*** для обработки запросов и возврата данных в формате JSON.

Общая структура кода соответствует парадигме **RESTful API**, где каждому ***URL-адресу*** соответствует определенный **HTTP-метод (GET, POST и т.д.)** и функция для обработки запроса и возврата данных. **Flask** облегчает создание и настройку веб-приложения, предоставляя удобные инструменты для определения маршрутов и обработки запросов.

### repository

Данный модуль представляет собой набор функций для взаимодействия с базой данных с использованием ***SQLAlchemy***.
В коде импортируются необходимые модули и классы, а также создается соединение с базой данных.

Каждая **функция** использует контекстные менеджеры ***Session*** и ***with*** для обеспечения **корректного управления сессией** и **соединением с базой данных**, выполняет необходимые запросы и сохраняет изменения с помощью метода **commit()**. Это позволяет обеспечить целостность данных и корректное управление сессией и соединением с базой данных.

##### _____________________________________

### readme

* Файл __README.md__ - это текущий файл, который может быть изменен по мере необходимости, включая сам **"код"**. В процессе разработки и обновления проекта, **README.md** может подвергаться изменениям, чтобы отражать ***актуальную информацию о проекте***, его ***функциональности***, ***инструкции по установке*** и ***использованию***, а также другую полезную информацию для **разработчиков** и **пользователей**. Это важный компонент документации, который помогает улучшить понимание проекта и содействует его успешному использованию.

##### _____________________________________


### Структура базы данных:
![Screenshot 2024-02-02 154610.png](image%2FScreenshot%202024-02-02%20154610.png)


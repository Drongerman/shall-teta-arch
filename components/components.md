# Компонентная архитектура
<!-- Состав и взаимосвязи компонентов системы между собой и внешними системами с указанием протоколов, ключевые технологии, используемые для реализации компонентов.
Диаграмма контейнеров C4 и текстовое описание. 
Подробнее: https://confluence.mts.ru/pages/viewpage.action?pageId=375783368
-->
## Контейнерная диаграмма

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="microservice")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")


Person(guest, "Посетитель", "Сторонний посетитель - слушатель/докладчи")
Person(employee, "Сотрудник МТС", "Сотрудник МТС - слушатель/докладчик/\nведущий/модератор")
Person(support, "Сотрудник Поддержки", "Сотрудник поддержки МТС")



System_Boundary(hello, "Hello Conf Platform") {
   Container(app, "Клиентское веб-приложение", "html, JavaScript, React", "Портал Hello Conf")
   Container(user_mgmt_srv, "User Profile Management", "Java, Spring Boot", "Управление профилями и контактами пользователей", $tags = "microService")
   ContainerDb(user_db, "User Profile DB", "PostgreSQL", "Хранение данных пользователей, котактов", $tags = "storage")
   Container(user_stream, "User Profile Data Stream", "Debezium", "Чтение WAL, передача в Kafka")
   Container(event_mgmt_srv, "Event Management", "Java, Spring Boot", "Управление конференциями, регистрациями на конференции", $tags = "microService")
   ContainerDb(event_db, "Event DB", "PostgreSQL", "Хранение информации о событиях", $tags = "storage")
   Container(event_stream, "Event Data Stream", "Debezium", "Чтение WAL, передача в Kafka")
   Container(lecture_mgmt_srv, "Lecture Management", "Java, Spring Boot", "Управление докладами, рецензирование, избранным, подпиской на доклады, статистикой", $tags = "microService")
   ContainerDb(lecture_db, "Lecture DB", "PostgreSQL", "Хранение информации о докладах, рецензиях", $tags = "storage")
   Container(lecture_stream, "Lecture Data Stream", "Debezium", "Чтение WAL, передача в Kafka")
   Container(advert_mgmt_srv, "Advert Management", "Java, Spring Boot", "Управление рекламными баннерами, ссылками, статистикой", $tags = "microService")
   ContainerDb(advert_db, "Advert DB", "PostgreSQL", "Хранение информации о рекламе", $tags = "storage")
   Container(advert_stream, "Advert Data Stream", "Debezium", "Чтение WAL, передача в Kafka")
   Container(schedule_mgmt_srv, "Schedule Management", "Java, Spring Boot", "Компилятор расписания докладов, управление персональным расписанием, генерация уведомлений", $tags = "microService")
   ContainerDb(schedule_db, "Schedule DB", "PostgreSQL", "Хранение информации о расписании", $tags = "storage")
   Container(schedule_stream, "Schedule Data Stream", "Debezium", "Чтение WAL, передача в Kafka")
   Container(notify_message_bus, "Message Bus", "Kafka", "Транспорт для доставки уведомлений")
   Container(tg_notify_srv, "Telegram Notification Service", "Java, Spring Boot", "Отправка уведомлений пользователям в Telegram", $tags = "microService")
   ContainerDb(tg_notify_srv_db, "Telegram Notification DB", "PostgreSQL", "Хранение данных уведомлений в Telegram", $tags = "storage")
   Container(tg_notify_stream, "Tg Notify Data Stream", "Debezium", "Чтение WAL, передача в Kafka")
   Container(email_notify_srv, "Email Notification Service", "Java, Spring Boot", "Отправка уведомлений пользователям по Email", $tags = "microService")
   ContainerDb(email_notify_srv_db, "Email Notification DB", "PostgreSQL", "Хранение данных уведомлений по Email", $tags = "storage")
   Container(email_notify_stream, "Email Notify Data Stream", "Debezium", "Чтение WAL, передача в Kafka")
   Container(stream_mgmt_srv, "Stream Management", "Golang, nginx", "Управление информацией о трансляции (индекс файлами)", $tags = "microService")
   ContainerDb(stream_db, "Stream DB", "Cassandra", "Хранение информацией о трансляции (индекс файлами, сегментами)", $tags = "storage")
   Container(stream_data_stream, "Stream Data Stream", "Debezium", "Чтение WAL, передача в Kafka")
   Container(streaming_service, "Streaming Service", "C#/.NET", "Получение сегментов видео/аудио потока", $tags = "microService")
   Container(interaction_srv, "Interaction Service", "Java, Spring Boot", "Обеспечение взаимодействия пользователей (Чаты, Реакции, Отзывы)", $tags = "microService")
   ContainerDb(interaction_db, "Interaction DB", "MongoDB", "Хранение информации о чатах, сообщениях", $tags = "storage")
   Container(interaction_stream, "Interaction Data Stream", "Debezium", "Чтение WAL, передача в Kafka")
   Container(billing_mgmt_srv, "Billing Management", "Java, Spring Boot", "Управление бонусами", $tags = "microService")
   ContainerDb(billing_db, "Billing DB", "PostgreSQL", "Хранение информации по бонусным транзакциям", $tags = "storage")
   Container(billing_stream, "Billing Data Stream", "Debezium", "Чтение WAL, передача в Kafka")
   Container(support_mgmt_srv, "Support Management", "Java, Spring Boot", "Управление поддержкой пользователей", $tags = "microService")
   Container(event_message_bus, "Message Bus", "Kafka", "Транспорт для броадкаста данных в аналитику")
   Container(analytics, "Web App Analytics", "Click House, Apache Superset", "Сбор данных, формирование и просмотр аналитических отчетов")
   Container(superset, "Apache Superset", "Аналитика и метрики")
}
 
System(int_sso, "Integnal Web SSO", "Внутреннее SSO для сотрудников")
System(ext_sso, "External Web SSO", "Внешнее SSO для клиентов МТС")
System_Ext(tg, "Telegram Бот", "Телеграм бот МТС")
System_Ext(partner, "Портал партнера", "Внешний адрес площадки партнера")
System(stream_src, "Источник видео потока", "Источник видео потока")
System(email, "Email Server", "SMTP Сервер МТС")
Container(s3, "S3 хранилище", "Хранилище файлов")
Container(obs, "Monitoring & Observability", "Kibana, Elasticsearch, Graphana", "Просмотр логов и мониторинг системы")   


Lay_D(hello, obs)

Lay_R(guest, employee)
Lay_R(employee, support)

Lay_U(ext_sso, guest)
Lay_U(ext_sso, employee)
Lay_U(ext_sso, support)
Lay_U(int_sso, guest)
Lay_U(int_sso, employee)
Lay_U(int_sso, support)
Lay_U(app, ext_sso)
Lay_U(app, int_sso)
Lay_U(user_mgmt_srv, app)
Lay_U(event_mgmt_srv, app)
Lay_U(lecture_mgmt_srv, app)
Lay_U(advert_mgmt_srv, app)
Lay_U(interaction_srv, app)
Lay_U(billing_mgmt_srv, app)
Lay_U(support_mgmt_srv, app)
Lay_U(streaming_service, app)

Lay_D(app, tg)
Lay_D(app, email)


Rel(app, ext_sso, "Проверяет доступ")
Rel(app, int_sso, "Проверяет доступ")
Rel(guest, ext_sso, "Аутентифицируется")
Rel(employee, int_sso, "Аутентифицируется")
Rel(support, int_sso, "Аутентифицируется")
Rel(guest, app, "HTTP/WebSocket")
Rel(employee, app, "HTTP/WebSocket")
Rel(support, app, "HTTP/WebSocket")


Rel(app, user_mgmt_srv, "CRUD", "HTTP/REST")
Rel(app, event_mgmt_srv, "CRUD", "HTTP/REST")
Rel(app, lecture_mgmt_srv, "CRUD", "HTTP/REST")
Rel(app, advert_mgmt_srv, "CRUD", "HTTP/REST")
Rel(app, schedule_mgmt_srv, "CRUD", "HTTP/REST")
Rel(app, interaction_srv, "CRUD", "WebSocket")
Rel(app, support_mgmt_srv, "CRUD", "HTTP/REST")
Rel(app, stream_mgmt_srv, "CRUD", "HTTP/REST")
Rel(app, streaming_service, "CRUD", "WebSocket")

Rel(advert_mgmt_srv, partner, "HTTP/REST")

Rel(analytics, superset, "Получение данных")
Rel(event_message_bus, superset, "Передача данных")

Rel(streaming_service, s3, "HTTP/REST")
Rel(stream_src, s3, "HTTP/REST")

Rel(user_mgmt_srv, user_db, "Read/Write", "Spring Data, SQL")
Rel(event_mgmt_srv, event_db, "Read/Write", "Spring Data, SQL")
Rel(lecture_mgmt_srv, lecture_db, "Read/Write", "Spring Data, SQL")
Rel(advert_mgmt_srv, advert_db, "Read/Write", "Spring Data, SQL")
Rel(billing_mgmt_srv, billing_db, "Read/Write", "Spring Data, SQL")
Rel(stream_mgmt_srv, stream_db, "Read/Write", "Spring Data, SQL")
Rel(interaction_srv, interaction_db, "Read/Write", "Spring Data, NOSQL")
Rel(schedule_mgmt_srv, schedule_db, "Read/Write", "Spring Data, SQL")

Rel(schedule_mgmt_srv, notify_message_bus, "Передача уведомления", "Kafka")
Rel(notify_message_bus, tg_notify_srv, "Передача уведомления", "Kafka")
Rel(notify_message_bus, email_notify_srv, "Передача уведомления", "Kafka")

Rel(tg_notify_srv, tg_notify_srv_db, "Read/Write", "Spring Data, SQL")
Rel(email_notify_srv, email_notify_srv_db, "Read/Write", "Spring Data, SQL")

Rel(tg_notify_srv, tg, "Send", "HTTP")
Rel(email_notify_srv, email, "Send", "SMTP")
Rel(support_mgmt_srv, email, "Send", "SMTP")


Rel(user_stream, user_db, "PostgresConnector")
Rel(event_stream, event_db, "PostgresConnector")
Rel(lecture_stream, lecture_db, "PostgresConnector")
Rel(advert_stream, advert_db,"PostgresConnector")
Rel(schedule_stream, schedule_db,"PostgresConnector")
Rel(interaction_stream, interaction_db, "MongoDbConnector")
Rel(stream_data_stream, stream_db, "PostgresConnector")
Rel(billing_stream, billing_db, "PostgresConnector")
Rel(tg_notify_stream, tg_notify_srv_db, "PostgresConnector")
Rel(email_notify_stream, email_notify_srv_db, "PostgresConnector")

Rel(user_stream, event_message_bus,"Kafka")
Rel(event_stream, event_message_bus,"Kafka")
Rel(lecture_stream, event_message_bus,"Kafka")
Rel(advert_stream, event_message_bus,"Kafka")
Rel(schedule_stream, event_message_bus,"Kafka")
Rel(interaction_stream, event_message_bus,"Kafka")
Rel(stream_data_stream, event_message_bus,"Kafka")
Rel(billing_stream, event_message_bus,"Kafka")
Rel(tg_notify_stream, event_message_bus,"Kafka")
Rel(email_notify_stream, event_message_bus,"Kafka")

Lay_U(user_db, user_mgmt_srv)
Lay_U(event_db, event_mgmt_srv)
Lay_U(lecture_db, lecture_mgmt_srv)
Lay_U(advert_db, advert_mgmt_srv)
Lay_U(schedule_db, schedule_mgmt_srv)
Lay_U(billing_db, billing_mgmt_srv)
Lay_U(interaction_db, interaction_srv)
Lay_U(stream_db, stream_mgmt_srv)
Lay_U(tg_notify_srv_db, tg_notify_srv)
Lay_U(email_notify_srv_db, email_notify_stream)

Lay_U(user_stream, user_db)
Lay_U(event_stream, event_db)
Lay_U(lecture_stream, lecture_db)
Lay_U(advert_stream, advert_db)
Lay_U(schedule_stream, schedule_db)
Lay_U(billing_stream, billing_db)
Lay_U(interaction_stream, interaction_db)
Lay_U(stream_data_stream, stream_db)
Lay_U(tg_notify_stream, tg_notify_srv_db)
Lay_U(email_notify_stream, email_notify_srv_db)

@enduml
```


## Список компонентов платформы Hello Conf
| Компонент             | Роль/назначение                  |
|:----------------------|:---------------------------------|
|Web App|Web Портал для доступа к онлайн конференции|
|Identity & Access Management|Управление доступом и ролями|
|User Profile Management|Управление профилями и контактами пользователей|
|Event Management|Управление конференциями, регистрациями на конференции|
|Lecture Management|Управление докладами, рецензирование, избранным, подпиской на доклады, статистикой|
|Advert Management|Управление рекламными баннерами, ссылками, статистикой|
|Schedule Management|Компилятор расписания докладов, управление персональным расписанием, генерация уведомлений|
|Telegram Notification Service|Отправка уведомлений пользователям в Telegram|
|Email Notification Service|Отправка уведомлений пользователям по Email|
|Stream Management|Управление информацией о трансляции (индекс файлами)|
|Streaming Service|Получение сегментов видео/аудио потока|
|Interaction Service|Обеспечение взаимодействия пользователей (Чаты, Реакции, Отзывы)|
|Billing Management|Управление бонусами|
|Support Management|Управление поддержкой пользователей|
|Analytics|Сбор данных, формирование и просмотр аналитических отчетов|
|Monitoring & Observability|Просмотр логов и мониторинг системы|

## Список компонентов обработчика трансляции
| Компонент             | Роль/назначение                  |
|:----------------------|:---------------------------------|
|Stream Management|Управление информацией о трансляции|
|Input Media Encoder|Приёмщик видео/аудио потока от источников|
|Stream Segmenter|Разделение видео/аудио потока на сегменты|
|Data Distributor|Распределение сегментов по CDN, индексация сегментов|
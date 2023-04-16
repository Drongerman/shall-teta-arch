# Контекст решения
```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_WITH_LEGEND()

Person(guest, "Посетитель", "Сторонний посетитель - слушатель/докладчи")
Person(employee, "Сотрудник МТС", "Сотрудник МТС - слушатель/докладчик/\nведущий/модератор")
Person(support, "Сотрудник Поддержки", "Сотрудник поддержки МТС")


System(hello, "Hello Conf Platform", "Платформа проведения онлайн конференции")

System_Ext(ext_sso, "Integnal Web SSO", "Внутреннее SSO для сотрудников")
System_Ext(int_sso, "External Web SSO", "Внешнее SSO для клиентов МТС")
System_Ext(tg, "Telegram Бот", "Телеграм бот МТС")
System_Ext(rutube, "Rutube Сервер", "Rutube сервер для повтора трансляции")
System_Ext(partner, "Портал партнера", "Внешний адрес площадки партнера")
Container(email, "Email Server", "SMTP Сервер МТС")
Container(superset, "Apache Superset", "Аналитика и метрики")
Container(s3, "S3 хранилище", "Хранилище файлов")


Rel(guest, ext_sso, "Аутентифицируется")
Rel(employee, int_sso, "Аутентифицируется")
Rel(support, int_sso, "Аутентифицируется")
Rel(guest, hello, "Uses")
Rel(employee, hello, "Uses")
Rel(support, hello, "Uses")
Rel(hello, email, "Отправляет уведомления", "SMTP")
Rel(hello, tg, "Отправляет уведомления", "Telegram")
Rel(hello, superset, "Пересылает данные в", "Kafka")
Rel(hello, rutube, "Передает трансляцию в")
Rel(hello, partner, "Перенаправляет в")
Rel(hello, s3, "Хранит файлы", "S3")

@enduml
```


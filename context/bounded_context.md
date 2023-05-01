# Контекст решения
```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_WITH_LEGEND()

Person(guest, "Посетитель", "Сторонний посетитель - слушатель/докладчи")
Person(employee, "Сотрудник МТС", "Сотрудник МТС - слушатель/докладчик/\nведущий/модератор")
Person(support, "Сотрудник Поддержки", "Сотрудник поддержки МТС")


Boundary(hello, "Hello Conf Platform", "Платформа проведения онлайн конференции"){
    System(access_ctx, "Доступ", "Управление доступом и ролями")
    System(user_ctx, "Пользователи", "Управление профилями и контактами пользователей") 
    System(event_ctx, "Конференции", "Управление конференциями, регистрациями на конференции") 
    System(lecture_ctx, "Доклады", "Управление докладами, рецензирование, избранным, подпиской на доклады, статистикой")
    System(advert_ctx, "Реклама", "Управление рекламными баннерами, ссылками, статистикой") 
    System(schedule_ctx, "Расписание", "Компиляция расписания докладов, управление персональным расписанием, генерация уведомлений")
    System(notification_ctx, "Уведомления", "Формирование, Отправка, Контроль уведомлений пользователям") 
    System(bonuses_ctx, "Бонусы", "Управление бонусами") 
    System(translation_ctx, "Трансляция", "Управление информацией о трансляции. Получение сегментов видео/аудио потока.")
    System(interaction_ctx, "Интерактив", "Взаимодействие пользователей (Чаты, Реакции, Отзывы)")
    System(support_ctx, "Поддержка","Управление поддержкой пользователей")
    System(analytics_ctx, "Аналитика","Сбор данных, формирование и просмотр аналитических отчетов")
}

System_Ext(ext_sso, "Integnal Web SSO", "Внутреннее SSO для сотрудников")
System_Ext(int_sso, "External Web SSO", "Внешнее SSO для клиентов МТС")
System_Ext(tg, "Telegram Бот", "Телеграм бот МТС")
System_Ext(rutube, "Rutube Сервер", "Rutube сервер для повтора трансляции")
System_Ext(partner, "Портал партнера", "Внешний адрес площадки партнера")
System(stream_src, "Источник видео потока", "Источник видео потока")
Container(email, "Email Server", "SMTP Сервер МТС")
Container(superset, "Apache Superset", "Аналитика и метрики")
Container(s3, "S3 хранилище", "Хранилище файлов")


Rel(user_ctx, lecture_ctx, "")
Rel(schedule_ctx, lecture_ctx, "")
Rel(user_ctx, event_ctx, "")
Rel(lecture_ctx, event_ctx, "")
Rel(advert_ctx, lecture_ctx, "")
Rel(translation_ctx, lecture_ctx, "")
Rel(schedule_ctx, notification_ctx, "")
Rel(bonuses_ctx, user_ctx, "")
Rel(interaction_ctx, user_ctx, "")
Rel(interaction_ctx, translation_ctx, "")
Rel(support_ctx, user_ctx, "")
Rel(access_ctx, analytics_ctx, "")
Rel(user_ctx, analytics_ctx, "")
Rel(event_ctx, analytics_ctx, "")
Rel(lecture_ctx, analytics_ctx, "")
Rel(bonuses_ctx, analytics_ctx, "")
Rel(notification_ctx, analytics_ctx, "")
Rel(interaction_ctx, analytics_ctx, "")

Rel(guest, ext_sso, "Аутентифицируется")
Rel(employee, int_sso, "Аутентифицируется")
Rel(support, int_sso, "Аутентифицируется")
Rel(guest, access_ctx, "Uses")
Rel(employee, access_ctx, "Uses")
Rel(support, support_ctx, "Uses")
Rel(stream_src, translation_ctx, "Передает трансляцию в")
Rel(notification_ctx, email, "Отправляет уведомления", "SMTP")
Rel(notification_ctx, tg, "Отправляет уведомления", "Telegram")
Rel(analytics_ctx, superset, "Пересылает данные в", "Kafka")
Rel(translation_ctx, rutube, "Передает трансляцию в")
Rel(advert_ctx, partner, "Перенаправляет в")
Rel(lecture_ctx, s3, "Хранит файлы", "S3")
Rel(translation_ctx, s3, "Хранит файлы", "S3")

@enduml
```



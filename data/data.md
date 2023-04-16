# Модель предметной области
| Бизнес Сущность | Подтипы |Данные     |
|-------------------------|-------------------------|-------------------------|
|Посетитель|Случайный/Рефферальный|Рефферальная ссылка, Дата/Время посещения |
|Пользователь | Слушатель/Докладчик/Редактор/Ведущий/Модератор/Техподдержка | ФИО, аватар, Статус, Уведомления вкл/выкл, Дата/Время регистрации, Дата/Время посещения, Возможность использовать чат, Количество бонусов|
|Транзакция бонусов | Начисление/Списание | Id Пользователя, Количество бонусов, Дата/Время транзакции|
|Контакты | email/телефон/телеграм | Id пользователя, Значение, Уведомления вкл/выкл|
|Мероприятие | | Наименование, Описание, Дата, Статус|
|Доклад |Несогласованный/Согласованный, Подтвержденный/Отмененный| Id пользователя, Id Мероприятия, Тема, Описание, Дата/Время проведения, Id секции, Статус согласования, Статус подтверждения, Ссылка на запись|
|Секция докладов | Dev/QA/DevOps/Management/Scrum/Support | Наименование, Цвет |
|Рецензия|Ответ редактора/Ответ докладчика| Id доклада, Id пользователя, Текст комментария, Дата/Время рецензии |
|Файл доклада | Презентация/Подстрочник/План выступления/Запись| Наименование файла, Ссылка в хранилище, Дата/Время создания |
|Посещение доклада | | Id доклада, Id пользователя, Дата/Время посещения|
|Избранные доклады | | Id Доклада, Id пользователя |
|Уведомляемые доклады | | Id Доклада, Id пользователя |
|Отзыв о докладе | | Id Доклада, Id пользователя, Текст, Дата/Время |
|Чат комната| | Id доклада |
|Чат сообщение |Сообщение/Вопрос/Ответ| Id чат комнаты, Id пользователя, Дата/время, Текст|
|Отзыв о мероприятии | |Id пользователя, Id мероприятия, Текст отзыва, Оценка, Дата/Время |
|Заявка в техподдержку |Жалоба/Технические неполадки/Отзыв о мероприятии|Id пользователя, Текст обращения, Дата/Время |
|Ответ на заявку | |Id заявки, Текст ответа, Дата/Время |

```plantuml
@startuml
' Логическая модель данных в варианте UML Class Diagram (альтернатива ER-диаграмме).
namespace Users {

 class Guest
 {
 }

 enum GuestType
 {
  refferal
  random
 }

 Guest -- GuestType

 class User
 {
 }

 enum UserType
 {
  speaker
  editor
  listener
  support  
 }


 User -- UserType

 class Contact
 {
 }

 
 User *-- "*" Contact

 enum ContactType
 {
 }

 Contact -- ContactType

}

namespace Billing {

 class Transation
 {
    
 }
 
 enum TransationType
 {
 }

 
 Transation -- TransationType

}

namespace Events {
 class Event
 {
 }
 class EventUserRegistration
 {
 }
 
 Event *-- "*" EventUserRegistration

}

namespace Lectures {

 class Lecture
 {
 }

 class Section
 {
 }

 enum SectionType
 {
 }
 
 Section -- SectionType
 Lecture *-- "1" Section

 class Review
 {
 }

 class File
 {
 }


 Lecture *--"*" File

 class Visit
 {
 }

 Lecture *--"*" Visit

 class Feedback
 {
 }

 Lecture *--"*" Feedback

 class Favorite
 {
 }

 Lecture *--"*" Favorite

 class Notifiable
 {
 }
 
 Lecture *--"*" Notifiable

}

namespace Interaction {

 class ChatRoom
 {
 }

 class Message
 {
 }
 
 ChatRoom *--"*" Message

 enum MessageType
 {
 }
 
 Message -- MessageType

 class Feedback
 {
 }

}

namespace Support {

 class Request
 {
 } 

 enum RequestType
 {
    request
    comlain
    feedback
 } 

 Request -- RequestType
 
 class Response
 {
 }

}
 
 
namespace CX {
 Users.User ..> Guest : ref
 Events.EventUserRegistration ..> User : ref
 Billing.Transation ..> User : ref
 Interaction.Message ..> User : ref
 Interaction.Feedback ..> Event : ref
 Lectures.Lecture ..> User : ref
 Lectures.Lecture ..> Event : ref
 Lectures.Review ..> User : ref
 Lectures.Visit ..> User : ref
 Lectures.Favorite ..> User : ref
 Lectures.Notifiable ..> User : ref
 Support.Request ..> User : ref
 Support.Response ..> User : ref
}

@enduml
```

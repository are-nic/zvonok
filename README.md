### 1 - Задача на подумать. Ответ:
Считаю, что в данной ситуации можно использовать технологии очередей сообщений, например RabbitMQ или Amazon SQS.
Данные инструменты позволят настроить очередь так, чтобы часть сообщений можно было временно оставить в буфере и отдавать их когда Сервис Б будет свободен.
Еще вариант - масштабировать Сервис Б, добавляя больше рабочих экземпляров для параллельной обработки запросов.

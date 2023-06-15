Инструкции для 29.05.2023:

## Задача с чтением моделей из файла:
Лучше оформить это в отдельной функции, в аргументы, которой будет подаваться класс
модели, которую мы хотим прочитать и имя файла.

        # def load_from_file(class, filename):
        #     res = list()
        #     try:
        #         with open(filename, 'r', encoding='UTF8') as f:
        #             for line in f:
        #                 for c_data, c in zip(line.split(','), self.__table__.columns):
        #                     new = self.__init__()
        #                     setattr(new, c.name, c_data) 
        #                 res.append(new)
        #         return res
        #     except Exception as e:
        #         logger.error('Fail load from file')
        #         print('Fail load from file', e, sep='\n')  
возвращает эта функция список прочитанных объектов.   
То есть у класса всё время будет вызываться конструктор. **С этим могут быть проблемы.**

## Задача с версткой формы регистрации.  
По образу и подобию формы с лоогином воссоздать форму регистрации. Это не сложно  
можно просто классы подобные привязать и всё. Тут возникает такая задача.  

## Подумать над тем, зачем использовать WTF-Forms  
Если весь функционал этого дополнения можно реализовать на JS



Server-Sent Events (SSE) – это стандарт, который позволяет серверу инициировать передачу данных на клиент. Это особенно полезно для случаев, когда необходимо обновлять данные на веб-странице в реальном времени.

Пример реализации на стороне сервера на Flask:

```python
from flask import Flask, Response
import time

app = Flask(__name__)

@app.route('/stream')
def stream():
    def event_stream():
        while True:
            yield "data: Current server time: {}\n\n".format(time.time())
            time.sleep(1)

    return Response(event_stream(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
```

Клиентская сторона, которая использует JavaScript для подключения к SSE и обновления данных на странице, может выглядеть следующим образом:

```html
<!DOCTYPE html>
<html>
<body>
    <script>
        var source = new EventSource("/stream");

        source.onmessage = function(event) {
            document.body.innerHTML += event.data + "<br>";
        };
    </script>
</body>
</html>
```

По поводу твоего вопроса о передаче более чем одного поля данных, ты можешь передавать только одно поле `data`, но это не означает, что ты ограничен одним значением. Обычный подход заключается в использовании формата JSON для передачи структурированных данных. Ты можешь кодировать свои данные в JSON на стороне сервера, а затем декодировать их на стороне клиента. Вот пример:

```python
import json
# ...

@app.route('/stream')
def stream():
    def event_stream():
        while True:
            data = {
                'time': time.time(),
                'message': 'Hello, World!'
            }
            yield 'data: {}\n\n'.format(json.dumps(data))
            time.sleep(1)

    return Response(event_stream(), mimetype='text/event-stream')
```

На стороне клиента:

```html
<!DOCTYPE html>
<html>
<body>
    <script>
        var source = new EventSource("/stream");

        source.onmessage = function(event) {
            var data = JSON.parse(event.data);
            document.body.innerHTML += data.message + " at " + data.time + "<br>";
        };
    </script>
</body>
</html>
```

Так ты можешь передавать любое количество данных через SSE, структурируя их в JSON.
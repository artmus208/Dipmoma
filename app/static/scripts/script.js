document.getElementById('mainForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию
  
    // Получаем значения полей
    var numberValue = document.getElementById('tf-pow').value;
    var selectValue = document.getElementById('methods').value;
  
    // Создаем JSON-объект
    var data = {
        degree: numberValue,
        method_id: selectValue
    };
  
    // Отправляем данные на сервер
    fetch('/ident/handler', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(function(response) {
      if (response.ok) {
        console.log('Данные успешно отправлены на сервер');
      } else {
        console.log('Ошибка отправки данных на сервер');
      }
    })
    .catch(function(error) {
      console.log('Произошла ошибка:', error);
    });
  });
  
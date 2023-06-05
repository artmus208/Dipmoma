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
    .then(response => response.json())
    .then(data => {
        var trace1 = {
            x: data.x1,
            y: data.y1,
            mode: 'lines',
            name: 'First Trace'
        };

        var trace2 = {
            x: data.x2,
            y: data.y2,
            mode: 'lines',
            name: 'Second Trace'
        };

        var layout = {
            title: 'Two Traces Plot',
            xaxis: {
                title: 'x-axis',
            },
            yaxis: {
                title: 'y-axis',
            },
        };

        var plotData = [trace1, trace2];
        Plotly.newPlot('plot', plotData, layout);
    })
    .catch(error => console.log(error));
});

  
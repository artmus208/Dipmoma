MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true
  },
  svg: {
    fontCache: 'global'
  }
};

document.getElementById('mainForm').addEventListener('submit', function (event) {
  event.preventDefault(); // Предотвращаем отправку формы по умолчанию
  
  var layout = { title: "Real-time Data" };
  var data = [{ x: [], y: [], mode: "lines", line: { color: "#00FF00" } }];
  Plotly.newPlot('plot', data, layout);
  // Получаем значения полей
  var numberValue = document.getElementById('tf-pow').value;
  var selectValue = document.getElementById('methods').value;

  // Создаем JSON-объект
  var data = {
    degree: numberValue,
    method_id: selectValue
  };

  if (selectValue == "3") {
    // Если выбран градиентный метод
    var buff = 0;
    var init_num = [];
    var init_den = [];

    for (var i = 1; i <= numberValue; i++) {
      buff = document.getElementById('b' + i);
      init_num.push(buff.value);
    }

    for (var i = 0; i <= numberValue; i++) {
      buff = document.getElementById('a' + i);
      init_den.push(buff.value);
    }
    console.log(init_num);
    console.log(init_den);
    data.init_num = init_num;
    data.init_den = init_den;
    // Отправляем данные на сервер
    fetch('/ident/grad-handler', {
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
          name: 'Исходная П.Х.'
        };

        var trace2 = {
          x: data.x2,
          y: data.y2,
          mode: 'lines',
          name: 'П.Х. модели'
        };

        var layout = {
          title: `Результат идентификации. Ошибка: ${data.error} `,
          xaxis: {
            title: 't, c',
          },
        };

        var plotData = [trace1, trace2];
        Plotly.newPlot('plot', plotData, layout);

        let latex_form = document.getElementById('tf_formula');
        latex_form.innerHTML = data.tf_formula
        MathJax.typesetPromise([latex_form]);

      });
  } else {
    // Отправляем данные на сервер
    fetch('/ident/handler', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(data => { // получаем данные с серврера
        var trace1 = {
          x: data.x1,
          y: data.y1,
          mode: 'lines',
          name: 'Исходная П.Х.'
        };

        var trace2 = {
          x: data.x2,
          y: data.y2,
          mode: 'lines',
          name: 'П.Х. модели'
        };

        var layout = {
          title: `Результат идентификации. Ошибка: ${data.error} `,
          xaxis: {
            title: 't, c',
          },
        };

        var plotData = [trace1, trace2];
        Plotly.newPlot('plot', plotData, layout);

        let latex_form = document.getElementById('tf_formula');
        latex_form.innerHTML = data.tf_formula
        MathJax.typesetPromise([latex_form]);
      })
      .catch(error => {
        console.log(error);
        let latex_form = document.getElementById('plot');
        latex_form.innerHTML = 'Ошибка на сервере'
      });
  }
});




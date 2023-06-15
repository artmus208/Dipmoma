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

  // Получаем значения полей
  var numberValue = document.getElementById('tf-pow').value;
  var selectValue = document.getElementById('methods').value;

  // Создаем JSON-объект
  var data = {
    degree: numberValue,
    method_id: selectValue
  };

  if (selectValue == "3") {
    var buff = 0;
    var num_arr = [];
    var den_arr = [];

    for (var i = 1; i <= numberValue; i++) {
      buff = document.getElementById('b' + i);
      num_arr.push(buff.value);
    }

    for (var i = 0; i <= numberValue; i++) {
      buff = document.getElementById('a' + i);
      den_arr.push(buff.value);
    }
    console.log(num_arr);
    console.log(den_arr);
    data.init_num = num_arr;
    data.init_den = den_arr;
  }

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
});




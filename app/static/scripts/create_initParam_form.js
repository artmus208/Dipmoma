// document.getElementsByClassName('flex-container-tf-init').addEventListener('submit', function(event) {

// });

var selectElement = document.getElementById('methods');
var degreeElement = document.getElementById('tf-pow');
var formPlacer = document.getElementById("tf_formula");
var ident_btn = document.getElementById("ident-btn");

function createInitInput(i, placeholder) {
    var numInput = document.createElement('input');
    numInput.placeholder = placeholder + i;
    numInput.id = placeholder + i;
    numInput.type = "number";
    numInput.min = "0";
    numInput.step = "1e-3";
    numInput.required = true; 
    numInput.style.padding = "2px";
    return numInput;
}

function createIterCount() {
    var iter_count = document.createElement('input');
    iter_count.placeholder = 'Кол-во итераций';
    iter_count.type = "number";
    iter_count.min = "0";
    iter_count.max = "1000";
    iter_count.required = true;
    iter_count.id = "iter_count";
    iter_count.style.padding = "2px";
    iter_count.style.marginTop = "5px";
    iter_count.style.maxWidth = "140px";
    return iter_count;
}

function createInitParamform(degree) {
    var form = document.createElement('form');
    form.className = "flex-container-tf-init";

    var numerator = document.createElement('div');
    numerator.className = "numerator";

    var hr = document.createElement('hr');

    var denumerator = document.createElement('div');
    denumerator.className = "denumerator";

    var submit_btn = document.createElement('input');
    submit_btn.type = "submit";
    submit_btn.className = "submit-btn-tf-init";
    submit_btn.value = "Сохранить";

    for (var i=1; i <= degree; i++){
        var numInput = createInitInput(i, "b");
        if (i == degree) {
            numInput.placeholder = 'hуст';
        }else {
            numInput.style.marginRight = "5px";
        }
        numerator.appendChild(numInput);
    }

    for (var i = 0; i <= degree; i++) {        
        var denumInput = createInitInput(i, "a");
        if (i != degree) {
            denumInput.style.marginRight = "5px";
        }
        denumerator.appendChild(denumInput);
    }
    var iter_count = createIterCount();

    var label = document.createElement('p');
    label.innerHTML = "Начальные параметры:"
    label.style.marginBottom = "5px";
    form.appendChild(label);
    form.appendChild(numerator);
    form.appendChild(hr);
    form.appendChild(denumerator);
    var iter_count_btn_container = document.createElement('div');
    iter_count_btn_container.style.display = 'flex';
    iter_count_btn_container.style.justifyContent = 'space-between';
    iter_count_btn_container.appendChild(iter_count);
    iter_count_btn_container.appendChild(submit_btn);
    form.appendChild(iter_count_btn_container);


////// Обработчик подтверждения формы ///////////////
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        ident_btn.toggleAttribute('disabled');
        var buff = 0;
        var num_arr = [];
        var den_arr = [];

        for (var i = 1; i <= degree; i++){
            buff = document.getElementById('b'+ i);
            buff.disabled = true;
            num_arr.push(buff.value);
        }

        for (var i = 0; i <= degree; i++){
            buff = document.getElementById('a'+ i);
            buff.disabled = true;
            den_arr.push(buff.value);
        }
        console.log(num_arr);
        console.log(den_arr);

    });
    return form;
}

// Добавляем обработчик события
degreeElement.addEventListener('change', function (event) {
    var selectedOption = selectElement.value;
    if (selectedOption == "3") {
        // Если выбран градиентный метод, надо сгенерировать форму
        formPlacer.innerHTML = '';
        var initForm = createInitParamform(degreeElement.value);
        formPlacer.appendChild(initForm);
        ident_btn.toggleAttribute('disabled');

    }; 
});

// TIPS Если захочешь сделать так, чтоб ПФ не стиралась после
// выбоора другого метода из списка. Сделай так, чтоб была какая-то
// глоабальная переменная-флаг, отражающая факт существования ПФ
selectElement.addEventListener('change', function (event) {
    var selectedOption = event.target.value;
    if (selectedOption != "3") {
        // Если не выбран градиентный метод, надо убрать форму

        formPlacer.innerHTML = "";
        ident_btn.disabled = false;
    };
});
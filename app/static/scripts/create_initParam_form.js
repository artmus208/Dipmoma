// document.getElementsByClassName('flex-container-tf-init').addEventListener('submit', function(event) {

// });

function createInitInput(i, placeholder) {
    var numInput = document.createElement('input');
    numInput.placeholder = placeholder + i;
    numInput.type = "number";
    numInput.min = "0";
    numInput.step = "1e-3";
    return numInput;
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


    for (var i = 0; i <= degree; i++) {
        var numInput = createInitInput(i, "b");

        var denumInput = createInitInput(i, "a");



        if (i == degree) {
            numInput.placeholder = 'hуст';
        } else {
            numInput.style.marginRight = "5px";
            denumInput.style.marginRight = "5px";

        }
        numerator.appendChild(numInput);
        denumerator.appendChild(denumInput);
    }

    form.appendChild(numerator);
    form.appendChild(hr);
    form.appendChild(denumerator);
    form.appendChild(submit_btn);

    return form;
}


var selectElement = document.getElementById('methods');
var degreeElement = document.getElementById('tf-pow');
var formPlacer = document.getElementById("tf_formula");
// Добавляем обработчик события
degreeElement.addEventListener('change', function (event) {
    var selectedOption = selectElement.value;
    
    if (selectedOption == "3") {
        // Если выбран градиентный метод, надо сгенерировать форму
        initForm = createInitParamform(degreeElement.value);
        formPlacer.innerHTML = initForm.outerHTML;
    }; 
});

selectElement.addEventListener('change', function (event) {
    var selectedOption = event.target.value;
    var saveInner = formPlacer.innerHTML;
    if (selectedOption != "3") {
        // Если не выбран градиентный метод, надо убрать форму
        formPlacer.innerHTML = "";
    }else{
        formPlacer.innerHTML = saveInner;
    }
});
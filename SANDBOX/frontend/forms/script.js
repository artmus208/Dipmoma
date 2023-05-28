function handleFormSubmit(event) {
    // Просим форму не отправлять данные самостоятельно
    event.preventDefault()
    console.log('Отправка!')
}

const applicantForm = document.getElementById('mars-once')
console.log(applicantForm)
applicantForm.addEventListener('submit', handleFormSubmit)
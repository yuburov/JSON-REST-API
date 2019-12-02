
let add = $('#add');
let substract = $('#substract');
let multiply = $('#multiply');
let divide = $('#divide');
let A = $('#my-input_1');
let B = $('#my-input_2');
let answer = $('#answer');

add.on('click', function () {
    $.ajax({
        url: "http://localhost:8000/api/v1/add/",
        method: 'post',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({A: A.val(), B: B.val()}),
        success: function (response) {
            answer.addClass('alert-success');
            result = response.answer;
            answer.text('Ответ: ' + result)
        },
        error: function (response) {
           if (status === 'error') {
               answer.addClass('alert-danger');
               answer.text(response.responseJSON.error)
           }
        }
    });
});

substract.on('click', function () {
    $.ajax({
        url: "http://localhost:8000/api/v1/substract/",
        method: 'post',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({A: A.val(), B: B.val()}),
        success: function (response) {
            answer.addClass('alert-success');
            result = response.answer;
            answer.text('Ответ: ' + result)
        },
        error: function (response) {
           if (status === 'error') {
               answer.addClass('alert-danger');
               answer.text(response.responseJSON.error)
           }
        }
    });
});

multiply.on('click', function () {
    $.ajax({
        url: "http://localhost:8000/api/v1/multiply/",
        method: 'post',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({A: A.val(), B: B.val()}),
        success: function (response) {
            answer.addClass('alert-success');
            result = response.answer;
            answer.text('Ответ: ' + result)
        },
        error: function (response) {
            if (status === 'error') {
                answer.addClass('alert-danger');
                answer.text(response.responseJSON.error)
                }
        }
    });
});

divide.on('click', function () {
    $.ajax({
        url: "http://localhost:8000/api/v1/divide/",
        method: 'post',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({A: A.val(), B: B.val()}),
        success: function (response) {
            answer.addClass('alert-success');
            result = response.answer;
            answer.text('Ответ: ' + result)
        },
        error: function (response, status) {
            if (status === 'error') {
                answer.addClass('alert-danger');
                answer.text(response.responseJSON.error)
            }
        }
    });
});

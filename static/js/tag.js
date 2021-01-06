// /* JavaScript markdown editor SimpleMDE */
// var simplemde = new SimpleMDE({ element: document.getElementById("MyID") });

// input type hidden 줘야 함
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

/* add Tag by click or press enter, comma, space */
var elements = document.getElementById('element');
var taskSubmit = document.getElementById('btn_add_task');
var taskBox = document.querySelector('#text_task');
var taskList = document.getElementById('list_tasks');
var taskLi = document.querySelectorAll('ul li');

/* Prevent input other than Korean, English and numbers */
taskBox.addEventListener('keyup',  removeSpecial);
function removeSpecial (e) {
   e.target.value = e.target.value.replace(/[^ㄱ-힣a-zA-Z0-9+#]/gi,"");
}

/* Prevent duplicate tags */
var checkSame = [];
/* click */
$("#text_task").keyup(function(e){
    var keyCode = e.keyCode;
    if (e.keyCode == 13 || e.keyCode == 188 || e.keyCode == 32){
        var task = taskBox.value.trim().toLowerCase();
        var newLi = document.createElement('li');
        var input = document.createElement('input')
        input.value = task
        input.name = "tagList"
        input.type = "hidden"
        var removeBtn = document.createElement('button');
        var element = newLi.appendChild(document.createTextNode(task));
        if((taskBox.value != "")  && checkSame.includes(task)===false){
            $.ajax({
                url: '/terms/tag',
                data: {
                    'csrfmiddlewaretoken': csrftoken,
                },
                type: "POST",
                dataType: "json",

                success: function(response){
                    checkSame.push(task);
                    taskList.appendChild(newLi);
                    newLi.appendChild(removeBtn);
                    newLi.appendChild(input);
                    const test = newLi
                    removeBtn.innerHTML = "X";
                    taskBox.value = '';
                    removeBtn.addEventListener('click', function() {
                        removeBtn.parentNode.removeChild(removeBtn);
                        newLi.parentNode.removeChild(newLi);
                        checkSame.splice(checkSame.indexOf(task), 1);
                    });
                },
                error: function(request, status, error){
                    taskBox.value='';
                    alert('중복된 태그입니다.');
                }
            });
        }
    }
}),

taskSubmit.addEventListener('click', clickFunction, false);
function clickFunction(e) {
    var task = taskBox.value.trim().toLowerCase();
    var newLi = document.createElement('li');
    var removeBtn = document.createElement('button');
    var input = document.createElement('input');
    var test = document.getElementsByClassName
    input.value = task
    input.name = "tagList"
    input.type = "hidden"
    var element = newLi.appendChild(document.createTextNode(task));
    if (taskBox.value != "" && checkSame.includes(task) == false) {
        $.ajax({
            url: '/terms/tag',
            data: { 
                'csrfmiddlewaretoken': csrftoken,
            },
            type: "POST",
            dataType: "json",

            success: function(response){
                checkSame.push(task);
                e.preventDefault();
                taskList.appendChild(newLi);
                newLi.appendChild(input);
                newLi.appendChild(removeBtn);
                removeBtn.innerHTML = "X";
                taskBox.value = '';
                removeBtn.addEventListener('click', function() {
                    removeBtn.parentNode.removeChild(removeBtn);
                    newLi.parentNode.removeChild(newLi);
                    checkSame.splice(checkSame.indexOf(task), 1);
                });
            },

            error: function(request, status, error){
                taskBox.value='';
                alert("중복된 태그입니다.");
            }
        });
    }
}

// CSRF TOKEN 함수
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// var elements = document.getElementById("element");
// var taskSubmit = document.getElementById("btn_add_task");
// var taskBox = document.querySelector("#text_task");
// var taskList = document.getElementById("list_tasks");
// var taskLi = document.querySelectorAll("ul li");

// taskBox.addEventListener("keyup", removeSpecial);
// taskSubmit.addEventListener("click", removeSpecial);

// function removeSpecial(e) {
//     e.target.value = e.target.value.replace(/[^ㄱ-힣a-zA-Z0-9+#]/gi, "");
// }

// let checkSame = [];
// taskBox.addEventListener("keyup", function (e) {
//     const keyCode = e.keyCode;
//     if (e.keyCode == 188 || e.keyCode == 32 || e.keyCode == 13) {
//         addTag();
//     }
// });
// taskSubmit.addEventListener("click", addTag, false);

// function addTag() {
//     const task = taskBox.value.trim().toLowerCase();
//     const newLi = document.createElement("li");
//     const input = document.createElement("input");
//     input.type = "hidden";
//     input.value = task;
//     input.name = "tagList";
//     const removeBtn = document.createElement("button");
//     const element = newLi.appendChild(document.createTextNode(task));
//     if (taskBox.value != "" && checkSame.includes(task) === false) {
//         checkSame.push(task);
//         taskList.appendChild(newLi);
//         newLi.appendChild(input);
//         newLi.appendChild(removeBtn);
//         removeBtn.innerHTML = "X";
//         taskBox.value = "";
//         removeBtn.addEventListener("click", function () {
//             removeBtn.parentNode.removeChild(removeBtn);
//             newLi.parentNode.removeChild(newLi);
//             checkSame.splice(checkSame.indexOf(task), 1);
//         });
//     } else if (checkSame.includes(task) === true) {
//         taskBox.value = "";
//         alert("중복된 연관어입니다.");
//     }
// }

// var elements = document.getElementById("element");
// var taskSubmit = document.getElementById("btn_add_task");
// var taskBox = document.querySelector("#text_task");
// var taskList = document.getElementById("list_tasks");
// var taskLi = document.querySelectorAll("ul li");
const termSubmit = document.getElementById("btn_add_task");
const termList = document.getElementById("list_tasks");
const termBox = document.getElementById("text_task");
const termLi = document.querySelectorAll("ul li");

termSubmit.addEventListener("click", () => {
  addRelatedTerm(termBox.value);
}, false);

termBox.addEventListener("keyup", (e) => {
  const keyCode = e.keyCode;
  if (e.keyCode == 188 || e.keyCode == 32 || e.keyCode == 13) {
    addRelatedTerm(termBox.value);
  }
});

function addRelatedTerm(name) {
  const newTerm = name.replace(/[^ㄱ-힣a-zA-Z0-9+#]/gi, "");
  if (!newTerm) {
    return;
  }
  const trimmedTerm = newTerm.trim();

  const liElem = document.createElement("li");
  const input = document.createElement("input");
  input.type = "hidden";
  input.value = trimmedTerm;
  input.name = "tagList";

  liElem.innerText = trimmedTerm;

  const removeBtn = document.createElement("button");
  removeBtn.innerText = 'X';
  removeBtn.addEventListener('click', () => {
    removeBtn.parentNode.removeChild(removeBtn);
    liElem.parentNode.removeChild(liElem);
  })

  const items = document.querySelectorAll("#list_terms > li");
  for (let i = 0; i < items.length; i++) {
    if (items[i].innerHTML.split('<')[0] === newTerm) {
      alert('중복 단어');
      termBox.value = '';
      return;
    }
  };
  termList.appendChild(liElem).appendChild(removeBtn);
  liElem.appendChild(input);
  termBox.value = '';
  return;
}
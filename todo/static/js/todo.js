// function addItem(btnId){
//     let inputAddItem = document.getElementById('todo-text').value;
//     const todoList = document.getElementById('todo-list');
//     const msg = document.querySelector('#msg');
//     console.log(todoList);

//     const xhttp = new XMLHttpRequest();
//     xhttp.open('POST', '/todo/add', true );
//     xhttp.setRequestHeader("Content-Type", "application/json");

//     if(inputAddItem === '')
//     {
//         // msg.classList.add(error);
//         msg.innerHTML = 'Please enter todo value';

//         setTimeout(() => msg.remove(), 3000);
//     }
//     else{
//         xhttp.onreadystatechange = function() {
//             if(this.readyState== 4 && this.status == 200){
//                 const div = document.createElement('div');
//                 const divCss = " display: flex; justify-content:space-between; background-color: #eee; list-style: none; margin-bottom: 5px; padding: 5px;"
//                 div.style.cssText = divCss;
//                 const li = document.createElement('li');
//                 const chkBx = document.createElement('input');
//                 chkBx.type = 'checkbox';
//                 const delBtn = document.createElement('input');
//                 delBtn.type = 'button';
//                 delBtn.value = 'delete';
               
//                 li.style.listStyle = 'None';
//                 li.appendChild(document.createTextNode(`${inputAddItem}`));
//                 div.appendChild(li);
//                 div.appendChild(chkBx);
//                 div.appendChild(delBtn);
                
//                 todoList.appendChild(div);
                
//                 inputAddItem = '';
//             }
//         };
//         console.log(JSON.stringify({'todo_item':inputAddItem}));
//         xhttp.send(JSON.stringify({'todo_item':inputAddItem}))
//     }
// }


function taskDone(chkId){
    const todoId = chkId.split('-')[1];
    const completedChkBOx = document.getElementById(chkId);
    const parent = document.getElementById(chkId).parentElement;
    console.log(parent);
    // console.log(todoId);

    const xhttp = new XMLHttpRequest();
    xhttp.open('POST', '/todo/completed', true );
    xhttp.setRequestHeader("Content-Type", "application/json")
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(xhttp.responseText);

            const jsonreturn = JSON.parse(xhttp.responseText);
            console.log(jsonreturn['is_completed']);
            if( jsonreturn['is_completed'] === true){
                parent.style.backgroundColor= "#a6eda7"
            }
            else{
                parent.style.backgroundColor= "rgb(240, 240, 85)"
            }
        }
      };
    
    let data = {'is_completed': completedChkBOx.checked,
                'todo_id': Number(todoId)}
    // console.log(JSON.stringify(data));
    xhttp.send(JSON.stringify(data));
}



function deleteItem(delId) {
    const todoId = delId.split('-')[1];
    // console.log(delId.split('-')[1]);
    const toDeleteItem = document.getElementById(delId).parentElement;
    const xhttp = new XMLHttpRequest();
    xhttp.open("POST", '/todo/delete', true);
    xhttp.setRequestHeader("Content-Type", "application/json")
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    };
   
    // console.log(toDeleteItem);
    xhttp.send(JSON.stringify({'todo_post_id':Number(todoId)}));
    toDeleteItem.remove();

}



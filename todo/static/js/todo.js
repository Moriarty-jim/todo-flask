function addItem(btnId){
    const inputAddItem = document.getElementById('todo-text').value;
    console.log(inputAddItem);

    const xhttp = new XMLHttpRequest();
    xhttp.open('POST', '/todo/add', true );
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onreadystatechange = function() {
        if(this.readyState== 4 && this.status == 200){
            document.getElementById('demo').innerHTML=this.responseText;

        }
    };
    console.log(JSON.stringify({'todo_item':inputAddItem}));
    xhttp.send(JSON.stringify({'todo_item':inputAddItem}))
}


function taskDone(chkId){
    const parent = document.getElementById(chkId).parentElement;
    const completedItemText = parent.children[0];
    const completedChkBOx = document.getElementById(chkId);

    const xhttp = new XMLHttpRequest();
    xhttp.open('POST', '/todo/completed', true );
    xhttp.setRequestHeader("Content-Type", "application/json")
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const jsonreturn = JSON.parse(xhttp.responseText)
            console.log(jsonreturn['is_completed']);
            if( jsonreturn['is_completed'] == true){
                parent.style.backgroundColor= "#a6eda7"
            }
            else{
                parent.style.backgroundColor= "#eee"
            }
        }
      };
    
    let data = {'is_completed': completedChkBOx.checked,
                'todo_item': completedItemText.textContent}
    // console.log(JSON.stringify(data))
    xhttp.send(JSON.stringify(data));
}



function deleteItem(btnId) {
    const toDeleteItem = document.querySelector('#'+btnId).parentElement;
    const toDeleteText = toDeleteItem.children[0].textContent;
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML = this.responseText;
        }
    };
    xhttp.open("POST", '/todo/delete', true);
    xhttp.send(toDeleteText)
    toDeleteItem.remove();

}


// function someFunction(){
//     const text = document.getElementById('message').value;
//     console.log(JSON.stringify({'text': text}));
//     const xhttp = new XMLHttpRequest();
//     xhttp.open("PosT", '/register/somefunction', true);
//     xhttp.setRequestHeader("Content-Type", "application/json")
//     xhttp.onreadystatechange = function(){
//       if (this.readyState == 4 && this.status == 200){
//         const jsonreturn = JSON.parse(xhttp.responseText)
//       document.getElementById('demo').innerHTML = jsonreturn['text'];
//       }
//     };
    
//     xhttp.send(JSON.stringify({'text': text}));
//   }
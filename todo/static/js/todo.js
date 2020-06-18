function taskDone(chkId){
    let completeditem = document.querySelector('#'+chkId).parentElement.children[0];
    let completedChkBOx = document.getElementById(chkId);
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            completeditem.innerHTML = this.responseText;
        }
      };
    
    let data = {'completed': completedChkBOx.checked}
    xhttp.open('POST', '/todo/completed', true );
    xhttp.send(JSON.stringify(data));


    // if(completedChkBOx.checked == true){
    //     // completeditem.style.color = "#467a47"
    //     completeditem.parentElement.style.backgroundColor= "#a6eda7"
    // }else{
    //     completeditem.style.color = "black"
    //     completeditem.parentElement.style.backgroundColor= "#eee"
    // }
}

function deleteItem(btnId) {
    let toDeleteItem = document.querySelector('#'+btnId).parentElement;
    let toDeleteText = toDeleteItem.children[0].textContent;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML = this.responseText;
        }
    };
    xhttp.open("POST", '/todo/delete', true);
    xhttp.send(toDeleteText)
    toDeleteItem.remove();

}
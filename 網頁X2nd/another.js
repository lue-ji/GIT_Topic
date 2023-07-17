let title = document.getElementById("title");
let content = document.getElementById("content");
let btn = document.getElementById("btn");
let list = document.getElementById("list");

btn.addEventListener("click", function(){
    list.innerHtml = list.innerHTML + `
    <div class="articale">
        <h2>${title.value}</h2>
        <p>${content.value}</p>
    </div>
    `;
    title.value = "";
    content.value = "";
    

})
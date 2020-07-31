
function menu(user,email,pk){
    var menu = document.getElementById("menu");
    var main = document.getElementById("text-main");
    var image_div =document.getElementById("main-image");
    var button_image = document.getElementById("button-project");
    
    menu.hidden = false;
    main.hidden = true;
    image_div.hidden = true;
    button_image.hidden = true


}

function close_menu(){
    
    var image_div =document.getElementById("main-image");
    var menu = document.getElementById("menu");
    var main = document.getElementById("text-main");
    
    main.hidden = false;
    menu.hidden = true;
    image_div.hidden = false;
   
    
    
    
}

function delete_alert(){
    var element = document.getElementById("alert-message");
    element.remove();
    
}



window.onload = function(){
    let timer = setTimeout(this.delete_alert,3000);
}


function show_add_project(){
    var main = document.getElementById("text-main");
    var page = document.getElementById("add-project-page");
    var startbutton = document.getElementById("add-button");
    if(page.hidden == true){
        startbutton.hidden = true;
        main.hidden = true;
        page.hidden = false;
    }else{
        startbutton.hidden = false;
        main.hidden = false;
        page.hidden = true;
    }
}
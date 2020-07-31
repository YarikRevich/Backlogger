function ChangeClass(){
    
    var element = document.getElementById("main-text");
    
    
    if(element.className == "main-changed"){  
        element.setAttribute("class","main-text");
        element.innerHTML = "";
        var image = new Image();
        image.src = "https://icons.iconarchive.com/icons/icons8/ios7/128/Arrows-Up-3-icon.png";
        element.appendChild(image);

    }else if (element.className == "main-text"){
        element.innerHTML = "@yaroslav<br/>This site was made by a simple coder<br/>To write someting use⬇️<br/>yariksvitlitskiy2@gmail.com";
        element.setAttribute("class","main-changed");
        
    }
    
}


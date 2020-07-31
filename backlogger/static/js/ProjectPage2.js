function show_add_page(){
    var page = document.getElementById("entry-page");
    var back_ground = document.getElementById("wrapper");
    var broker = document.getElementById("broker");
    var paginator = document.getElementById("paginator");
    var back_image = document.getElementById("back-image");
    var back_image_home = document.getElementById("back-image-project");
    if(page.hidden == false){
        back_image_home.hidden = false;
        back_image.hidden = true;
        page.hidden = true;
        back_ground.className = "";
        broker.hidden = false;
        paginator.hidden = false;
        
    }else{
        back_image_home.hidden = true;
        back_image.hidden = false;
        page.hidden = false;
        broker.hidden = true;
        paginator.hidden = true;
        back_ground.className = "wrapper";
        
    }

    
}
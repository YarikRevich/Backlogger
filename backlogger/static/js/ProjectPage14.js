function show_add_page(){

    /* This func shows page for the adding of entry*/

    var page = document.getElementById("entry-page");
    var back_ground = document.getElementById("wrapper");
    var broker = document.getElementById("broker");
    var paginator = document.getElementById("paginator");
    var back_image = document.getElementById("back-image");
    var back_image_home = document.getElementById("back-image-project");
    document.getElementById("plan_page").hidden = true;

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


function show_plan_page(){

    /*This func shows page where there is shown a plan*/ 
    

    var plan = document.getElementById("plan_page");
    var broker = document.getElementById("broker")
    var plan_t = document.getElementById("plan_form");
    
    if(document.getElementById("emptyy") != null){
        
        var empty = document.getElementById("emptyy");
        empty.setAttribute("hidden",true);
        var plan = document.getElementById("plan_page");
        var broker = document.getElementById("broker")
        var plan_t = document.getElementById("plan_form");
    }else{
        
        document.getElementById("entry-page").hidden = true;
        var plan = document.getElementById("plan_page");
        var broker = document.getElementById("broker")
        var plan_t = document.getElementById("plan_form");
    }

    
    if(document.getElementById("plan_page").hidden == true){
        
        plan.removeAttribute("hidden",false);
        broker.setAttribute("hidden",true);
        
         
    }else{
        
        plan.hidden = true;
        if(document.getElementById("emptyy") != null){
            document.getElementById("emptyy").hidden = false;
        }
        broker.hidden = false;
    }
}


function edit_plan(){
    
    /* 
    This func show 'Confirm' button for plan-page and makes
    textarea editable   
    */

    document.getElementById("edit_button").hidden = true;
    document.getElementById("confirm_button").hidden = false;
    document.getElementById("plan_form").removeAttribute("readonly");
}

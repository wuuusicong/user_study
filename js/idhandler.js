var userid;

function idHandler(id){
    
    if(id = "*"){
        return userid;
    }
    else{
        userid = id;
        return 0;
    }
}
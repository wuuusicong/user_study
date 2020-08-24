function FunctionHub(){
    var _this = this;

    this._init = function(){
        this._age = ""
        this._gender = ""
        this._studyinterest = ""
        this._academiclevel = ""
        this._experience = ""
    }

   

    this.saveUserInfo = function(){
        var self = this;
        var formData = new FormData();
        formData.append("age", this._age)
        formData.append("gender", this._gender)
        formData.append("studyinterest", this._studyinterest)
        formData.append("academiclevel", this._academiclevel)
        formData.append("experience", this._experience);
        var url = "http://localhost:22030/saveUserInfo";
        console.log("userInfo的消息")
        lSendUrl("POST", url, formData, self.successSave)
    }

    this.successSave = function(response, self){
        // console.log("response", response)
        // userid = response;
        console.log("save ok")
    }

    this.loadQuestion = function(){
        var self = this;
        var formData = new FormData();
        formData.append('name', "loadQuestion")
        var url = "http://localhost:2000/transferpage";
        lSendUrl("POST", url, formData, self.successLoad)
    }

    this.successLoad = function(response, self){
        console.log("Load OK!")
    }

    this.submit = function(){
        this._age = $('input[name="age"]').val();
        this._gender = $('input:radio[name="gender"]:checked').val();
        this._studyinterest = $('input:radio[name="studyinterest"]:checked').val();
        this._academiclevel = $('input:radio[name="academiclevel"]:checked').val();
        this._experience = $('input:radio[name="experience"]:checked').val();
        if(this._age == ""){
            window.alert("empty age")
        }
        else{
            this.saveUserInfo()
            // this.loadQuestion()
        }
        console.log("age", this._age)
        console.log("age", this._gender)
        console.log("age", this._studyinterest)
        console.log("age", this._academiclevel)
        console.log("experience", this._experience)

    }

    this.loadimgpage = function(){
        var self = this;
        var formData = new FormData();
        formData.append("name", "loadimgpage")
        var url = "http://localhost:2000/loadQuestion";
        lSendUrl("POST", url, formData, self.successLoad)
    }

    this._init()
}
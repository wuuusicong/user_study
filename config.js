function ConfigProcess(dataroot){
    this._init = function(){
        this._totalConfig = []
        this._userinfoConfig = []
        this._questionConfig = []
        this._questionandoptionConfig = []
    }

    this.getTotalConfig = function(){
        var totalconfig1 = []
        $(document).ready(function(){
            $.ajax({
                url: dataroot,
                async: false,
                success: function(data){
                    console.log("data",data)
                    this._totalConfig = data
                    totalconfig1 = this._totalConfig
                }
            })
        })
        console.log("totalconfig2", totalconfig1)
        return totalconfig1
    }

    this.getQuestionContent = function(){
        var questionContent = []
        $(document).ready(function(){
            $.ajax({
                url: dataroot,
                async: false,
                success: function(data){
                    this._questionConfig = data["singleproblem"]
                    questionContent = this._questionConfig
                }
            })
        })
        return questionContent
    }

    this.getQuestionandOption = function(){
    }

    this.getUserContent = function(slideIndex){
        var htmlcontent = ""
        console.log("sss")
        $(document).ready(function(){
            $.ajax({
                url: dataroot,
                // url: './config.json',
                async: false,
                success: function(data){
                    this._userinfoConfig = data[slideIndex]
                    console.log("config", this._userinfoConfig)
                    var divstyle = this._userinfoConfig["divstyle"]
                    var tablestyledict = this._userinfoConfig["tablestyle"]
                    var tablecaption = this._userinfoConfig["tablecaption"]
                    var trandtd = this._userinfoConfig["trandtd"]
                    
                    var tablecss = "<table "
                    var styleList = Object.keys(tablestyledict)
                    for(var k = 0; k < styleList.length; k++){
                        var stylekey = styleList[k]
                        var stylecss = stylekey +'=' + '"' + tablestyledict[stylekey] + '"'
                        if(k == styleList.length -1){
                            var stylecssstr = stylecss + ">"
                        }
                        else{
                            var stylecssstr = stylecss 
                        }
                        tablecss = tablecss.concat(stylecssstr)
                        console.log("stylecss",stylecssstr)
                        console.log("tablecss", tablecss)
                    }


                    var divcsshead = '<div style="'+ divstyle+'">'
                    htmlcontent = htmlcontent.concat(divcsshead)
                    var formhead = '<form method="post" action="">'
                    htmlcontent = htmlcontent.concat(formhead)
                    htmlcontent = htmlcontent.concat(tablecss)
                    var captioncssandtbody = '<caption>' + tablecaption + '</caption> <tbody>' 
                    htmlcontent = htmlcontent.concat(captioncssandtbody)
                    var tail = '</tbody></table></form></div>'


                    

                    for(var i = 0; i < trandtd.length; i++){
                        trconfig = trandtd[i]
                        if(trconfig["tdtype"] == "text"){
                            var trcontent = '<tr>'+
                                        '<td>' + trconfig['display'] +'</td>'+
                                        '<td><input type = ' + '"'+trconfig['type'] +'"'+ ' name = ' + '"'+trconfig['name'] +'"'+'></input></td>'+
                                        '</tr>'
                            htmlcontent = htmlcontent.concat(trcontent)
                        }
                        else if (trconfig['tdtype'] == "radio"){
                            trdisplay = '<tr><td>' + trconfig['display'] +': </td><td>'
                            htmlcontent = htmlcontent.concat(trdisplay)
                            tdconfig = trconfig['option']
                            console.log("tdconfig",tdconfig)
                            for(var j = 0; j < tdconfig.length; j++){
                                var tdContent = '<input type = '+'"'+ tdconfig[j]['type'] +'"' +' name = '+ '"'+tdconfig[j]['name'] +'"'+' value='+ '"'+tdconfig[j]['value'] +'"'+' checked='+ '"'+tdconfig[j]['checked'] +'"'+'>' + tdconfig[j]['display']
                                htmlcontent = htmlcontent.concat(tdContent)
                                if(j == tdconfig.length -1){
                                    htmlcontent = htmlcontent.concat('</td></tr>')
                                } 
                            }
                        }
                        console.log("aaa", trconfig)
                    }

                    
                    console.log("ddd", this._userinfoConfig)
                }
            })
        })
        return htmlcontent
    }

    this._init()
}

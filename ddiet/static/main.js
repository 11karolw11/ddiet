function update_single_item(name, amount, callback) {
    console.log("update single item")
    console.log(name)
    console.log(amount)

    $.ajax({
        url : "/ajax/update_single_item/",
        type : "POST",
        data : { name: name, amount: amount },

        success : function(json) {
            console.log(json)
            console.log("successful response from update_single_item")
            callback(json)
        },

        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }

    })
};

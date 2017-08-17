function newTextInput(key){
    output = "";
    output += '<div class="formItem text">';
    output += '<p>text</p>';
    output += '<label for="' + key + '_out"> ' + key + ': </label>';
    output += '<textarea name="' + key + '_out" id="' + key + '_out"></textarea>';
    output += '<input type="hidden" name="' + key + '_type" value="text">';
    output += '</div>';
    return output;
}

function newLinkImageInput(key){
    output = "";
    output += '<div class="formItem link_image">';
    output += '<p>link image</p>';
    output += '<label for="' + key + '_out">' + key + ': </label>';
    output += '<textarea name="' + key + '_out" id="' + key + '_out"></textarea>';
    output += '<input type="hidden" name="' + key + '_type" value="link_image">';
    output += '</div>';
    return output;
}

function newFileImageInput(key){
    output = "";
    output += '<div class="formItem fileImage">';
    output += '<p>file image</p>';
    output += '<label for="' + key + '_out">' + key + ': </label>';
    output += '<textarea name="' + key + '_out" id="' + key + '_out"></textarea>';
    output += '<label for="' + key + '_file">' + key + ' file: </label>';
    output += '<input type="file" name="' + key + '_file" id="' + key + '_file">';
    output += '<input type="hidden" name="' + key + '_type" value="file_image">';
    output += '</div>';
    return output
}

function addFormInput(){
    formSize = parseInt($(".uploadFormSize").val());
    inputType = $(".newInputType").val()
    if(inputType == "text"){
        newInput = newTextInput(formSize);
    }else if(inputType == "linkImage"){
        newInput = newLinkImageInput(formSize);
    }else if(inputType == "fileImage"){
        newInput = newFileImageInput(formSize);
    }
    $(newInput).insertBefore(".uploadFormSubmit");
    $(".uploadFormSize").val(formSize + 1);
}
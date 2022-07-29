const variable = document.getElementsById(id).value;

function getValue(e){
    variable = e.value;
}

function doc() {
    document.write(variable)
}
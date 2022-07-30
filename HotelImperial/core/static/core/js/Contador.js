var empId;
function getEmpId(element){
    empId = element.dataset.employeeId;
    sessionStorage.setItem('var', empId);
}

function doc() {
    return(sessionStorage.getItem('var'));
}

function esconde_div(){
    element.parentNode.removeChild(element);
}

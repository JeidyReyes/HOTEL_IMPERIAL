var empId;
var cont;
function getEmpId(element)
{
    empId = element.dataset.employeeId;
    alert(empId);
    sessionStorage.setItem('var', empId);
}


function doc() {
    document.write(sessionStorage.getItem('var'));
}
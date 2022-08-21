let temp = $("#btn1").clone();
$("#btn1").click(function(){
    $("#btn1").after(temp);
});

$(document).ready(function(){
    var table = $('#example').DataTable({
       orderCellsTop: true,
       fixedHeader: false 
    });

    //Creamos una fila en el head de la tabla y lo clonamos para cada columna
    $('#example thead tr').clone(true).appendTo( '#example thead' );

    $('#example thead tr:eq(1) th').each( function (i) {
        var title = $(this).text(); //es el nombre de la columna
        $(this).html( '<input type="text" placeholder="Search...'+title+'" />' );
 
        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );   
});

function ocultar(){
    var box = document.querySelector(".navegacion")
    var estado = box.style.display;
    if (estado == "none") {
        box.style.display = "flex";
    }else{
        box.style.display = "none";
    }
    
}
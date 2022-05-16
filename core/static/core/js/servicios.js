$(document).ready(function(){
    //$('#api1').click(initiate_ghibliapi);
    initiate_servicios();
});

function crearCard(id, titulo, descripcion){
    var card = "<div class = 'card'>"+
    "<img id= '" + id + titulo +"' ><div class ='card-body'>" +
    "<h5 class= 'card-title'>" + titulo + "</h5>" + 
    "<p class='card-text'>" + descripcion + "</p></div></div>"

    return card
}

function initiate_servicios(){
        $.get({
            url: 'http://localhost/webservicephp/controller/producto.php', //DIRECCIÓN SERVER
            success: function(listado) {  
            console.log(listado);
            
                var contenedor = $('#listado')
                    contenedor.empty();

            var imagen;

            $.each(listado, function (index, producto){

                var prod = "<b>Nombre: </b>" + producto.nombre
                    prod += "<br/><b>Descripcion: </b>" + producto.descripcion
                    prod += "<br/><b>TPrecio: </b>" + producto.precio
                    prod += "<br/><b>Disponibilidad: </b>" + producto.disponible

                    contenedor.append(
                        crearCard(producto.id_producto, producto.nombre, prod)              
                       );
                       
                })
            

            },
            error: function(e) {
                console.error(e)

            }
        
        });
    }

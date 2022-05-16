$(document).ready(initiate_ws)
console.log("DOM cargado")

function crearCard(id, img, descripcion) {
  var card =
    "<div class = 'card'>" +
    "<img id= '" +
    id +
    "'src='" +
    img +
    "'class = 'card-img-top' alt='" +
    descripcion +
    "</p></div></div>";

  return card;
}

function initiate_ws() {
  $.get({
    url: "http://localhost/webservicephp/controller/producto.php", //DIRECCIÓN SERVER

    success: function (listado) {
      console.log(listado);

      var contenedor = $("#listado");
      contenedor.empty();

      var imagen;

      $.each(listado.data, function (index, producto) {
        switch (producto.descripcion) {
          case "XAOXOAXOAXOAOXAOA":
            imagen = "https://falabella.scene7.com/is/image/Falabella/14903367_1?wid=800&hei=800&qlt=70";
            break;
        }

        var movie = "<b>Id producto: </b>" + producto.descripcion;
/*         movie += "<br/><b>Descripción: </b>" + producto.descripcion; */
        movie += "<br/><b>Precio: </b>" + producto.precio;
        movie += "<br/><b>Disponibilidad: </b>" + producto.disponible;

        contenedor.append(
          crearCard(producto.id, imagen, pelicula.descripcion, movie)
        );
      });
    },
    error: function (e) {
      console.error(e);
    },
  });
}

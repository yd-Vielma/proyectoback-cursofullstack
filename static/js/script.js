$(document).ready(function() {
    // Cargar datos de platillos
    function cargarPlatillos() {
        $.ajax({
            url: '/api-restaurante/platillo',
            method: 'GET',
            success: function(data) {
                $('#tabla-platillos tbody').empty();
                data.forEach(function(platillo) {
                    $('#tabla-platillos tbody').append(`
                        <tr>
                            <td>${platillo.platillo_id}</td>
                            <td>${platillo.plato}</td>
                            <td>${platillo.descripcion}</td>
                            <td>${platillo.precio}</td>
                            <td>
                                <button class="editar-platillo" data-id="${platillo.platillo_id}">Editar</button>
                                <button class="btn-accion btn-eliminar" data-id="${platillo.platillo_id}">Eliminar</button>
                            </td>
                        </tr>
                    `);
                });
            }
        });
    }

    // Cargar datos de comentarios
    function cargarComentarios() {
        $.ajax({
            url: '/api-restaurante/comentario',
            method: 'GET',
            success: function(data) {
                $('#tabla-comentarios tbody').empty();
                data.forEach(function(comentario) {
                    $('#tabla-comentarios tbody').append(`
                        <tr>
                            <td>${comentario.id_comentario}</td>
                            <td>${comentario.nombre}</td>
                            <td>${comentario.apellido}</td>
                            <td>${comentario.correo_electronico}</td>
                            <td>${comentario.comentario}</td>
                        </tr>
                    `);
                });
            }
        });
    }

    // Cargar datos de valoraciones
    function cargarValoraciones() {
        $.ajax({
            url: '/api-restaurante/valoracion',
            method: 'GET',
            success: function(data) {
                $('#tabla-valoraciones tbody').empty();
                data.forEach(function(valoracion) {
                    $('#tabla-valoraciones tbody').append(`
                        <tr>
                            <td>${valoracion.id_valoracion}</td>
                            <td>${valoracion.platillo}</td>
                            <td>${valoracion.puntos}</td>
                        </tr>
                    `);
                });
            }
        });
    }

    // Inicializar carga de datos
    cargarPlatillos();
    cargarComentarios();
    cargarValoraciones();

    // Manejar envío de formulario de platillo
    $('#form-platillo').on('submit', function(e) {
        e.preventDefault();
        const datos = {
            plato: $(this).find('input[name="plato"]').val(),
            descripcion: $(this).find('input[name="descripcion"]').val(),
            precio: $(this).find('input[name="precio"]').val()
        };

        $.ajax({
            url: '/api-restaurante/platillo',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ datos }),
            success: function(respuesta) {
                alert(respuesta.mensaje);
                cargarPlatillos();
            }
        });
    });

    // Manejar eliminación de platillo
    $(document).on('click', '.eliminar-platillo', function() {
        const id = $(this).data('id');

        $.ajax({
            url: `/api-restaurante/platillo/${id}`,
            method: 'DELETE',
            success: function(respuesta) {
                alert(respuesta.mensaje);
                cargarPlatillos();
            }
        });
    });

    // Manejar edición de platillo (puedes expandir este código para manejar la edición)
    $(document).on('click', '.editar-platillo', function() {
        const id = $(this).data('id');
        // Lógica para editar platillo
    });
});

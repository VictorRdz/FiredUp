$(document).foundation();

$(document).ready(function() {

    // registro/vacante.html ----------------------------------
 
    $('.time-input').timepicker({ 'timeFormat': 'H:i:s' });

    $("#add-habilidad-vacante").click(function() {
        cloneMore('.habilidad-container:last', 'form');
    });

    $("#add-competencia-vacante").click(function() {
        cloneMore('.competencia-container:last', 'form');
    });

    $("#add-idioma-vacante").click(function() {
        cloneMore('.idioma-container:last', 'form');
    });

    $("#add-educacion-vacante").click(function() {
        cloneMore('.educacion-container:last', 'form');
    });

    $("#add-prestacion-vacante").click(function() {
        cloneMore('.prestacion-container:last', 'form');
    });

    $("#add-funcion-vacante").click(function() {
        cloneMore('.funcion-container:last', 'form');
    });

    // --------------------------------------------------------
    function cloneMore(selector, prefix) {
        var newElement = $(selector).clone(true);
        var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
        newElement.find(':input').each(function() {
            var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        });
        total++;
        $('#id_' + prefix + '-TOTAL_FORMS').val(total);
        $(selector).after(newElement);
        return false;
    }
});

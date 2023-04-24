var $ = jQuery.noConflict();

$(document).ready(function() {
    $('select.select2').select2({
        theme:'bootstrap',
        //style: 'background-color:#1e1e2f;'
    });
});

core = {
    showModal: (url,id)=>{
        $(id).load(url,function (){
            $(id).modal();
            //core.onUpdate()
        });
    },

    showNotification: function( message, color='info', icon="tim-icons icon-bell-55", position={from:'top',align:'right'}) {
        $.notify({
        icon: icon,
        message: message
        }, {
        type: color,
        timer: 2500,
        placement: {
            from: position.from,
            align: position.align
        }
        });
    },

    onUpdate: function(e){
        btnUpdateProduct = document.getElementById('modalUpdatebtn')
        formProduct = document.getElementById('modalForm')

        btnUpdateProduct.onclick = e=>{
            e.preventDefault()
            urlUpdate = formProduct.getAttribute('action-update')
            formProduct.action = urlUpdate

            formProduct.submit()
        }
    }
    
}
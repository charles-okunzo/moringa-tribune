$(document).ready(()=>{
    $('form.newsletter').submit((e)=>{
        e.preventDefault()
        form = $('form.newsletter')

        $.ajax({
            'url':'/ajax/newsletter/',
            'type': 'POST',
            'data': form.serialize(),
            'dataType':'json',
            'success': function(data){
                alert(data['success'])
            },
        })

        $('#id_your_name').val('')
        $('#id_email').val('')
    })
})
$(document).ready(()=>{
    $('form').submit((e)=>{
        e.preventDefault()
        form = $('form')

        $.ajax({
            'url':'/ajax/newsletter/',
            'type': 'POST',
            'data': form.serialize(),
            'dataType':'json',
            'success': function(data){
                alert('You have been sucessfully added to our mailing list')
            },
        })

        $('#id_your_name').val('')
        $('#id_email').val('')
    })
})
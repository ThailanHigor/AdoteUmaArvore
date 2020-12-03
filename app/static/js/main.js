
$(".cadastrar").click(function(){
    let email = $("#NewsInputEmail").val();
      
    Swal.fire({
        title: 'Aguarde',
        text: "Estamos salvando seu envio..",
        showCancelButton: false,
        showConfirmButton: false,
        showCloseButton: false,
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    $.ajax({
        url: '/news/cadastrar',
        data: {email: email},
        type: 'POST',
        success: function (data) {
            if(data.status){
                Swal.fire({
                    title: 'Obrigado',
                    text: "Seu email foi cadastrado com sucesso",
                    icon: 'success',
                    confirmButtonColor: '#1c6856',
                    confirmButtonText: 'Ok'
                })
                $("#NewsInputEmail").val("");
            }else{
                Swal.fire({
                    title: 'Erro',
                    text: "Email inválido ou vazio",
                    icon: 'warning',
                    confirmButtonColor: '#1c6856',
                    confirmButtonText: 'Ok'
                })
            }
        },
    });

})



$(".cadastrar-contato").click(function(){
    let nome = $(".Nome-Contato").val();
    let email = $(".Email-Contato").val();
    let assunto = $(".Assunto-Contato").val();
    let mensagem = $(".Mensagem-Contato").val();
      
    Swal.fire({
        title: 'Aguarde',
        text: "Estamos salvando seu envio..",
        showCancelButton: false,
        showConfirmButton: false,
        showCloseButton: false,
        allowOutsideClick: false,
        allowEscapeKey: false
    })
    $.ajax({
        url: '/contato/cadastrar',
        data: {
            nome: nome,
            email: email,
            assunto: assunto,
            mensagem: mensagem
        },
        type: 'POST',
        success: function (data) {
            if(data.status){
                Swal.fire({
                    title: 'Obrigado',
                    text: "Seu cadastrado foi realizado com sucesso",
                    icon: 'success',
                    confirmButtonColor: '#1c6856',
                    confirmButtonText: 'Ok'
                })
                $("#NewsInputEmail").val("");
            }else{
                Swal.fire({
                    title: 'Erro',
                    text: "Campos vazios ou inválidos",
                    icon: 'warning',
                    confirmButtonColor: '#1c6856',
                    confirmButtonText: 'Ok'
                })
            }
        },
    });

})

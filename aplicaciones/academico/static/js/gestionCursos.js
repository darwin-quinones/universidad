(function () { // se ejecuta al cargar la pagina
    
    const btnEliminar = document.querySelectorAll('.btnEliminar')

    btnEliminar.forEach(btn =>{
        btn.addEventListener('click', (e) =>{
            const confirmacion = confirm('¿ Seguro de eliminar el curso ?')
            // si cancela, no se elimina
            if(!confirmacion){
                e.preventDefault()
            }
        })
    })

})()
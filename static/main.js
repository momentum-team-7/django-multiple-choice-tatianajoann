copyButtons = document.querySelectorAll('.save-button')
deleteButtons = document.querySelectorAll('.delete-button')

for (let button of copyButtons){
    button.addEventListener('click', event => {
        const snippetElement = event.target.parentElement
        const copyUrl = event.target.dataset.url
        fetch (copyUrl, {
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
        .then(response => response.json())
        .then(data => {
            console.log(data['code'])
        })
    })
}


for (let button of deleteButtons){
    button.addEventListener('click', event => {
        const snippetElement = event.target.parentElement
        const deleteUrl = event.target.dataset.url
        fetch (deleteUrl, {
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            snippetElement.remove()
        })
    })
}
copyButtons = document.querySelectorAll('.save-button')
deleteButtons = document.querySelectorAll('.delete-button')


function saveReload(){
    console.log('saveReload()')
    copyButtons = document.querySelectorAll('.save-button')
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
                renderSnippet(data)
            })
        })
    }
}


function deleteReload(){
    console.log('deleteReload')
    deleteButtons = document.querySelectorAll('.delete-button')
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
}

function renderSnippet(data) {

    let snippetContainer = document.querySelector('.snippet-box')

    let snippetDiv = document.createElement('div')

    let preCode = document.createElement('pre')

    let code = document.createElement('code')
    code.className = `language-${data['language']}`
    code.innerHTML = `${data['code']}`
    console.log(code)

    let author = document.createElement('p')
    author.innerHTML = 'author: '

    let userLink = document.createElement('a')
    userLink.href = `/user/${data['user_pk']}` 
    userLink.innerHTML = `${data['user']}`
    console.log(userLink)


    let editButton = document.createElement('button')

    let editLink = document.createElement('a')
    editLink.href = `/snippet/${data['code_pk']}/edit`
    editLink.innerHTML = 'Edit Snippet'


    let deleteButton = document.createElement('button')
    deleteButton.className = 'delete-button'
    deleteButton.id = `${data['code_pk']}`
    deleteButton.dataset.url = `/snippet/${data['code_pk']}/delete`
    deleteButton.innerHTML = 'Destroy Snippet'
    console.log(deleteButton)


    let saveButton = document.createElement('button')
    saveButton.className = 'save-button'
    saveButton.id = `${data['code_pk']}`
    saveButton.dataset.url = `/snippet/${data['code_pk']}/save`
    saveButton.innerHTML = 'Save Snippet'
    console.log(saveButton)


    let copyButton = document.createElement('button')

    let copyLink = document.createElement('a')
    copyLink.href = `/snippet/${data['code_pk']}/copy`
    copyLink.innerHTML = 'Copy Snippet'


    Prism.highlightElement(preCode)
    Prism.highlightElement(code)

    preCode.appendChild(code)
    author.appendChild(userLink)
    editButton.appendChild(editLink)
    copyButton.appendChild(copyLink)

    snippetDiv.appendChild(preCode)
    snippetDiv.appendChild(author)
    snippetDiv.appendChild(editButton)
    snippetDiv.appendChild(deleteButton)
    snippetDiv.appendChild(saveButton)
    snippetDiv.appendChild(copyButton)

    
    snippetContainer.appendChild(snippetDiv)

    saveReload()
    deleteReload()

}
saveReload()
deleteReload()
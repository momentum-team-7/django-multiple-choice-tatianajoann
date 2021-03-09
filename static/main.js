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
            renderSnippet(data)
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
    userLink.href = "{% url 'user' pk=snippet.user.pk %}"  
    userLink.innerHTML = `${data['user']}`
    console.log(userLink)


    let editButton = document.createElement('button')

    let editLink = document.createElement('a')
    editLink.href = "{% url 'edit-snippet' pk=snippet.pk %}"
    editLink.innerHTML = 'Edit Snippet'


    let deleteButton = document.createElement('button')
    deleteButton.className = 'delete-button'
    deleteButton.id = `${data['pk']}`
    deleteButton.dataset.url = "{% url 'delete-snippet' pk=snippet.pk %}"
    deleteButton.innerHTML = 'Destroy Snippet'
    console.log(deleteButton)


    let saveButton = document.createElement('button')
    saveButton.className = 'save-button'
    saveButton.id = `${data['pk']}`
    saveButton.dataset.url = "{% url 'save-snippet' pk=snippet.pk %}" 
    saveButton.innerHTML = 'Save Snippet'
    console.log(saveButton)


    let copyButton = document.createElement('button')

    let copyLink = document.createElement('a')
    copyLink.href = "{% url 'copy-snippet' pk=snippet.pk %}"
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

}


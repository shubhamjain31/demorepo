new Autocomplete('#autocomplete', {

    search: input => {
        console.log(input)
        const url = `/search/?address=${(input)}`
        return new Promise(resolve => {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    resolve(data.data)
                })
        })
    },


    renderResult: (result, props) => {
        console.log(props)

        let group = ''
        if (result.index % 3 === 0) {
            group = `<li class="group">Group</li>`
        }
        return `
${group}
<li ${props}>
<div class="wiki-title">
  ${result}
</div>

</li>
`
    },

    getResultValue: result => result,
    onSubmit: result => {
        window.open(`/places/?=${(result)}`)
    }
})
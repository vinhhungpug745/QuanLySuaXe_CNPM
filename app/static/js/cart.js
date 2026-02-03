function toggleCart() {
    const cart = document.getElementById("mini-cart");
    cart.classList.toggle("active");
}


function addToCart(id, name, price, image) {
    event.preventDefault()

    fetch('/api/add-cart', {
        method: 'post',
        body: JSON.stringify({
            'id': id,
            'name': name,
            'price': price,
            'image': image
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (res) {
        console.info(res)
        return res.json()
    }).then(function (data) {
        console.info(data)
        let counter = document.getElementsByClassName('number_cart')
        for (let i=0 ; i<counter.length; i++)
            counter[i].innerText = data.total_quantity
    }).catch(function (err) {
        console.error(err)
    })
}

document.addEventListener("DOMContentLoaded", () => {
    const products = [
        {id: "product1", name:"Apple AirPods Max", price: 110.99 },
        {id: "product2", name:"Gaming keyboard", price: 68.90 },
        {id: "product3", name:"iPad Pro 13", price: 223.99 },
        {id: "product4", name:"Sony Headphones", price: 89.99 }
    ];
    
    let cart = JSON.parse(localStorage.getItem("cart")) || []
    
    function saveCart(){
        localStorage.setItem("cart", JSON.stringify(cart));
    }
    
    function addToCart(){
        cart.push(product);
        saveCart();
        alert(`${product.name} added to cart`);
    }
    
    function remove(){
        cart = cart.filter(p => p.id !== productId);
        saveCart()
        alert("Product removed from the cart")
    }
    
    document.querySelectorAll(".add-to-cart-btn").forEach((btn, index) => {
        btn.addEventListener("click", () =>
        addToCart(products[index]));
    });
    
    document.querySelectorAll(".remove-btn").forEach((btn,index) => {
        btn.addEventListener("click", () =>
        remove(products[index],id))
    });
    
})




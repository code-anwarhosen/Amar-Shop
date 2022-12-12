// toggle menu button
let menu_items = document.getElementById('menu-items');
let menu_btn = document.getElementById('menu-btn');

menu_items.style.maxHeight = "0px";
menu_btn.addEventListener('click', function(){
    if(menu_items.style.maxHeight == "0px"){
        menu_items.style.maxHeight = "200px"
    }
    else{
        menu_items.style.maxHeight = "0px"
    }
})


// toggle image--product details page
let product_img = document.getElementById('product-img');
let small_img = document.getElementsByClassName('small-img');
small_img[0].addEventListener('click', function(){
    product_img.src = small_img[0].src;
})
small_img[1].addEventListener('click', function(){
    product_img.src = small_img[1].src;
})
small_img[2].addEventListener('click', function(){
    product_img.src = small_img[2].src;
})
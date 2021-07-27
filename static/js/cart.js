var upatedBtns = document.getElementsByClassName('장바구니업데이트')

for(var i =0 ; i <upatedBtns.length; i++ ){
    upatedBtns[i].addEventListener('click', function(){
        var productID = this.dataset.product
        var action = this.dataset.action
        console.log('productID:',productID , 'action:',action  )
        
        console.log('사용자:',user) 
        if(user == 'AnonymousUser'){
            addCookieItem(productID,action)
            
        }else{
            updateUserOrder(productID,action)
        }
    })
}

function addCookieItem(productID,action){
    console.log('로그인 안됨!!')
    if (action == 'add'){
        if (cart[productID] == undefined){
            cart[productID] = {'quantity':1}
        }else {
            cart[productID]['quantity'] += 1
        }

    }
    if (action == 'remove'){
        cart[productID]['quantity'] -= 1
        if (cart[productID]['quantity'] <= 0){
            console.log('제품이 삭제되었습니다')
            delete cart[productID];
        }        
    }
    console.log('Cart:', cart)
    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()

}

function updateUserOrder(productID,action){
    console.log('로그인 되었으니 정보를 보냅니다')

    var url ='/update_item/'
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken

        },
        body:JSON.stringify({'productID': productID,'action' : action})

    })

    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()

    })

}
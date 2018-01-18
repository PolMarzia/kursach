var doc = document,
    elem = doc.getElementsByClassName("jsallert")[0];
elem.addEventListener("click", function(){
    alertify.alert("Спасибо за заказ! Перенаправляем на главную...");
}, true);
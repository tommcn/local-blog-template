document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM content fully loaded.");

    
    var navs = document.getElementsByClassName("nav-item");
    for (var i = 0; i < navs.length; i++)
    {
        if (navs[i].href == window.location.protocol + "//" + window.location.host + window.location.pathname)
        {
            navs[i].classList.add("nav-bar-active")
        } else {
            navs[i].classList.remove("nav-bar-active")
        }
    }


    coll = document.getElementsByClassName("collapsible");

    for (var i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling.nextElementSibling;
            if (content.style.maxHeight){
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            } 
        });
    }   

    window.onscroll = function() {stickyNav()};
    var navbar = document.getElementById("navbar");
    var sticky = navbar.offsetTop;
    function stickyNav() {
        if (window.pageYOffset >= sticky) {
            navbar.classList.add("sticky")
        } else {
            navbar.classList.remove("sticky");
        }
    }

    startTime();
});

function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('clock').innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}

function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}


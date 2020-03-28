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

    var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    mm = months[today.getMonth()]
    d = today.getDate()
    y = today.getFullYear()
    document.getElementById("date").innerHTML = 
    mm + " " + d + ", " + y;
}

function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

function validateForm() {
    valid = true;
    if( document.contact.name.value == "" ) {   // check empty name
        document.contact.name.classList.add("invalid");
        document.contact.name.classList.remove("valid");
        valid = false;
    } else {
        document.contact.name.classList.add("valid");
        document.contact.name.classList.remove("invalid");
    }
    if( document.contact.primaryEmail.value == "" ) {   // chack empty email
        document.contact.primaryEmail.classList.add("invalid");
        document.contact.primaryEmail.classList.remove("valid");
        valid = false;
    } else {
        document.contact.primaryEmail.classList.add("valid");
        document.contact.primaryEmail.classList.remove("invalid");
    }
    if (document.contact.phone.value != "") {
        if(! ValidatePhone(document.contact.phone.value) ) {  // chack invalid email
            document.contact.phone.classList.add("invalid");
            document.contact.phone.classList.remove("valid");
            valid = false;
        } else {
            document.contact.phone.classList.add("valid");
            document.contact.phone.classList.remove("invalid");
        }
    } else {
        document.contact.phone.classList.add("valid");
        document.contact.phone.classList.remove("invalid");
    }

    document.contact.address.classList.add("valid");
    document.contact.address.classList.remove("invalid");
    document.contact.secondaryEmail.classList.add("valid");
    document.contact.secondaryEmail.classList.remove("invalid");

    return( valid );
}

function ValidatePhone(inputText)
{
    var mailformat = "/(1-)?([0-9]{3}-?){2}[0-9]{4}/";
    if(inputText.match(mailformat) != "")
    {
        return true;
    }
    else
    {
        return false;
    }
}

  
function validateform(){
    var first_name=document.registration_form.first_name.value;  
    var last_name=document.registration_form.last_name.value; 
    var email=document.registration_form.email.value; 
    var password=document.registration_form.password.value;  
    var confirm_password=document.registration_form.confirm_password.value; 
    var filter = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if (first_name < 2  || last_name > 2){  
      alert("First Name and Last Name must be at least 2 characters");  
      return false;  
    }
    else if(password.length < 8){  
      alert("Password must be at least 8 characters long.");  
      return false;  
      }  
    else if(password != confirm_password){  
        alert("Password must be be at match.");  
        return false; }

    else if(!filter.test(email)) {
        alert('Please provide a valid email address');
        return false;  
    }

}



    

    
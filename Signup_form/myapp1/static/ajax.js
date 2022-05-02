$("#login-btn").click(function(){
    console.log("Log in button clicked");
    let Email=$("#email").val()
    let Password=$("#password").val()
    let csrf = "{{ csrf_token }}"

    console.log(Email);
    console.log(Password);
    LoginData={Email:Email, Password:Password, csrfmiddlewaretoken:csrf}
    console.log(LoginData);

    $.ajax({
        url:"{% url 'getlogindata' %}",
        method:"POST",
        data:LoginData,
        success:function(data){
            console.log(data);
            if(data.status=="LoggedIn"){
                alert("Log In Successfully")
            }
        }
    })

    
})



$("#signup_btn").click(function(){
    console.log("SIGN UP BUTTON CLICKED");
    let Name=$("#name").val()
    let Email=$("#email").val()
    let Password=$("#password").val()
    let csrf = "{% csrf_token %}"

    console.log(Name);
    console.log(Email);
    console.log(Password);
    console.log(csrf)
    SignupData={Name:Name, Email:Email, Password:Password, csrfmiddlewaretoken:csrf}
    console.log(SignupData);

    $.ajax({
        url:"{% url 'getdata' %}",
        method:"POST",
        data:SignupData,
        success:function(data){
            console.log(data);
            if(data.status=="Submitted"){
                alert("Sign Up Successfully")
            }
        }
    })
})
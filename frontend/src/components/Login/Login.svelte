<script>
    import { Link } from "svelte-navigator";
    import { auth } from "../../firebase";
    import { signInWithEmailAndPassword } from "firebase/auth";
    import { useNavigate } from "svelte-navigator";
    
    const navigate = useNavigate();
    export let title = "login";


    let credentials = {
      email: "",
      password: "",
    };
    const changeUser = (e) => {
      credentials = {
        ...credentials,
        [e.target.name]: e.target.value,
      };
    };
    function loginUser(){
      if(title =="login"){  
        signInWithEmailAndPassword(auth,credentials.email, credentials.password).then((userCredential) => 
        {
          const user = userCredential.user;
          if(credentials.email == "admin@gmail.com"){
            localStorage.setItem("admin", user.uid);
            navigate("/");
          }
          if(credentials.email != "admin@gmail.com"){
            localStorage.setItem("uid", user.uid);
            navigate("/");
          }  
        })
        .catch((error) =>{
          console.log(error)
        });
    }
  }

  </script>
  
  <div>
    <br /><br /><br />
    <div class="form-signin">
      <h1 class="text-center text-login">Login</h1>
      <div class="center">
        <input
          name="email"
          type="email"
          id = "email"
          class="input-form"
          placeholder="Email"
          required
          on:input={(e) => changeUser(e)}
        />
      </div>
      <div class="center">
        <input
          name="password"
          type="password"
          class="input-form"
          placeholder="Password"
          on:input={(e) => changeUser(e)}
        />
      </div>
      <br />
      <div class="center">
        <button class="button-signup fondo-color-signup" on:click={loginUser} > Login </button>
      </div>
      <p class="text-center">
        ¿You do not have an account? <Link to="/register">Register</Link>
      </p>
    </div>
  </div>
  
  <style>
    .text-login {
      font-size: 26px;
    }
    .center {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .form-signin {
      width: 100%;
      max-width: 520px;
      height: 300px;
      padding: 15px;
      margin: auto;
      background-color: white;
      box-shadow: 0 4px 14px 0 rgb(0 0 0 / 10%);
    }
    .text-center {
      text-align: center;
    }
    /* INPUTS */
    .input-form {
      background-color: transparent;
      border: 1.5px solid rgb(0 0 0 / 10%);
      border-radius: 5px;
      padding: 10px;
      outline: none;
      width: 90%;
      font-size: 16px;
      -webkit-box-shadow: none;
      box-shadow: none;
      -webkit-box-sizing: content-box;
      box-sizing: content-box;
      margin: 5px;
    }
    /* BUTTON SIGNUP */
    .button-signup {
      display: inline-block;
      font-weight: 400;
      color: #ffffff;
      height: 45px;
      width: 90%;
      text-align: center;
      border: 1px solid transparent;
      padding: 0.375rem 0.75rem;
      font-size: 1rem;
      line-height: 1.5;
      cursor: pointer;
      transition: 0.2s;
    }
    .fondo-color-signup {
      background: #FF0000;
    }
  </style>


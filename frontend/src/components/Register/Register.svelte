<script>
  import { Link } from "svelte-navigator";
  import { auth } from "../../firebase";
  import { createUserWithEmailAndPassword } from "firebase/auth";
  import { useNavigate } from "svelte-navigator";

  const navigate = useNavigate();
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
  const registerUser = async () => {
    try {
      await createUserWithEmailAndPassword(
        auth,
        credentials.email,
        credentials.password
      );
      navigate("/");
    } catch (error) {
      console.log(error);
    }
  };

  


  var Fn = {
	// Valida el rut con su cadena completa "XXXXXXXX-X"
	validaRut : function (rutCompleto) {
		if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
			return false;
		var tmp 	= rutCompleto.split('-');
		var digv	= tmp[1]; 
		var rut 	= tmp[0];
		if ( digv == 'K' ) digv = 'k' ;
		return (Fn.dv(rut) == digv );
	},
	dv : function(T){
		var M=0,S=1;
		for(;T;T=Math.floor(T/10))
			S=(S+T%10*(9-M++%6))%11;
		return S?S-1:'k';
	}
}


  function formHandler(event) {
    event.preventDefault()

    var RUT= credentials.rut;
    if(Fn.validaRut(RUT)== true){
    fetch('http://localhost:8000/users/',{
      method:  'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name:credentials.name,
        email:credentials.email,
        rut:credentials.rut,
        password:credentials.password,
        number:credentials.number,
        adress:credentials.adress,
      })
    })
      .then(response => response.json())
      .then(result => console.log(result))

      createUserWithEmailAndPassword(
        auth,
        credentials.email,
        credentials.password
      );
      navigate("/");
    }

    else{ 
      swal('The Rut is invalid, remember that the Rut must exist and also use - at the end. Thank you');
    }

 
  }






</script>

<div>
  <br /><br /><br />
  <div class="form-signin">
    <h1 class="text-center text-login">Register</h1>
     <div class="center">
      <input
        name="name"
        type="name"
        class="input-form"
        placeholder="Fist name"
        on:input={(e) => changeUser(e)}
      />
    </div>
    <div class="center">
      <input
        name="rut"
        type="rut"
        class="input-form"
        placeholder="Rut, Ej: 20211694-9"
        required
        on:input={(e) => changeUser(e)}
      />
    </div>
    <div class="center">
      <input
        name="email"
        type="email"
        class="input-form"
        placeholder="Email"
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
    <div class="center">
      <input
        name="number"
        type="number"
        class="input-form"
        placeholder="Phone"
        on:input={(e) => changeUser(e)}
      />
    </div>
    <div class="center">
      <input
        name="adress"
        type="adress"
        class="input-form"
        placeholder="Shipping info"
        on:input={(e) => changeUser(e)}
      />
    </div>
    <br />
    <div class="center">
      <button class="button-signup fondo-color-signup" on:click={formHandler}> Register </button>
    </div>
    <p class="text-center">
      ¿you already have an account? <Link to="/login">Login</Link>
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
    height: 500px;
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
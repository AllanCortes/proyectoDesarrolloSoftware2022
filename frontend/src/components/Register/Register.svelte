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
  const loginUser = async () => {
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
</script>

<div>
  <br /><br /><br />
  <div class="form-signin">
    <h1 class="text-center text-login">Register</h1>
     <div class="center">
      <input
        name="Name"
        type="Name"
        class="input-form"
        placeholder="Fist name"
        on:input={(e) => changeUser(e)}
      />
    </div>
    <div class="center">
      <input
        name="Rut"
        type="Rut"
        class="input-form"
        placeholder="Rut"
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
        placeholder="ShippingInfo"
        on:input={(e) => changeUser(e)}
      />
    </div>
    <br />
    <div class="center">
      <button class="button-signup fondo-color-signup" on:click={loginUser}> Register </button>
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
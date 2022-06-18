<script>
	import { Router, Route, Link } from "svelte-navigator";
	import Login from "./components/Login/Login.svelte";
	import Register from "./components/Register/Register.svelte";
	import Navbar from "./components/Navbar/Navbar.svelte";
  </script>
  
  <div>
	<Router>
	  <div>
		<Navbar />
		<Route path="/">
		  <h1>Esta es la home</h1>
		</Route>
		<Route path="/login" component={Login} />
		<Route path="/register" component={Register} />
	  </div>
	</Router>
  </div>
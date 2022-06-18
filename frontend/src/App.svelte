<script>
	import { Router, Route, Link } from "svelte-navigator";
	import Login from "./components/Login/Login.svelte";
	import Register from "./components/Register/Register.svelte";
	import Navbar from "./components/Navbar/Navbar.svelte";
	import { Styles, Button } from 'sveltestrap';
    
    export let title = "Petshop";
  </script>
  <Styles/>

  <div>
	<Router>
	  <div>
	  	<div>
			<div>
				<Navbar />
				<Route path="/">

				<div> 	
				
					<div>
						<div class ="row">
							<div class ="col-md-4">
		  					 </div>
							   <div align="center">
							   <img src="https://i.ibb.co/5kQbrtc/Pet-Lovers.png" alt="" />
							   		  <h1> {title} </h1>
							   <h1> La plataforma online de la mejor tienda de mascotas </h1>
							   </div>

		 				</div>
	 				</div>
					 
				</div>
			
			<div>


				</Route>
				<Route path="/login" component={Login} />
				<Route path="/register" component={Register} />
			  </div>
			  
		</Router>
		
	  </div>


<script>
	import { Router, Route, Link } from "svelte-navigator";
	import Login from "./components/Login/Login.svelte";
	import Register from "./components/Register/Register.svelte";
	import Navbar from "./components/Navbar/Navbar.svelte";
	import { Styles, Button } from 'sveltestrap';
import Catalogo from "./components/Catalogo.svelte";
    
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
						 <div aling="center">
							<h5> PetLovers was born in 2020, in the city of Antofagasta. We opened our store with the desire and illusion of becoming a relevant actor in the lives of pets and their owners.
								Our team, our way of working and our actions are distinguished by the following attributes:</h5>
							<h6> We are committed.</h6>
							<h6>We like to make things easy and simple for you.</h6>
							<h6>We are close.</h6>
							<h6>We aim to deliver a service of excellence.</h6>
						</div>
	 				</div>
					 
				</div>
			
			<div>


				</Route>
				<Route path="/login" component={Login} />
				<Route path="/register" component={Register} />
				<Route path="/catalogo" component={Catalogo} />
			  </div>
			  
		</Router>
		
	  </div>


<script>
	import { Router, Route, navigate } from "svelte-navigator";
	import Login from "./components/Login/Login.svelte";
	import Register from "./components/Register/Register.svelte";
	import Navbar from "./components/Navbar/Navbar.svelte";
	import { Styles} from 'sveltestrap';
	import Catalogo from "./components/Catalogo.svelte";
	import AddProduct from "./components/admin/addProduct.svelte";
	import EditProduct from "./components/admin/editProduct.svelte";
    import Cart from "./components/client/cart.svelte";
	import Buy from "./components/client/buy.svelte"
	import Products from "./components/admin/ListProduct.svelte";
	import { getAuth,onAuthStateChanged } from "firebase/auth";
	import { onMount } from "svelte";

    export let title = "Petshop";
	let email;
	let url='';
	//users routes
	let buy= "http://localhost:8080/buy";
	let cart ="http://localhost:8080/cart";
	//admin
	let addProduct= "http://localhost:8080/addProduct";
	let editProduct= "http://localhost:8080/editProduct";
	let emailAdmin = "admin@gmail.com";
	onMount(() => url = window.location.href);

	onMount(() => {
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
		if(user !==null){
			email = user.email;
			if(emailAdmin==email && (url ==buy || url == cart)){
				navigate("/");
			}
			if(emailAdmin!=email && (url ==addProduct || url == editProduct)){
				navigate("/");
			}
			console.log(url);
			console.log(email);
		}

    });
  });

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
				{#if email!= null && email=="admin@gmail.com"}
				<Route path="/addProduct" component={AddProduct} />
				<Route path="/editProduct" component={EditProduct} />
				<Route path="/ListProduct" component={Products} />
				{/if}
				{#if email!= null && email!="admin@gmail.com"}
				<Route path="/buy" component={Buy} />
				<Route path="/cart" component={Cart} />
				{/if}
			  </div>  
		</Router>
	  </div>
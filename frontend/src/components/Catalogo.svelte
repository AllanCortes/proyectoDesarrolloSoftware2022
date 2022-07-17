
<script>
	const tableHeading = ["Order by price highest to lowest","Order by price lowest to highest","Order by stock highest to lowest",
	"Order by stock lowest to highest","Order by old added","Order by recent added"];
	
	
	import { onMount } from 'svelte';
	import {Table} from 'sveltestrap';
	import { Styles, Button } from 'sveltestrap';
	import {navigate } from "svelte-navigator";
	
	
	
	let cart=[];
	
    let types = []; 
	let selectedOption = "";
	let selectedType = "";
	
	let products = [];
	let selectedHeader = "stock";
	let ascendingOrder = true;
	
	
	onMount(async () => {
	  const res = await fetch("http://127.0.0.1:8000/products/");
	  products = await res.json();

		
		for (let proObj of products) {
			if (!types.includes(proObj.type_product)) {
				types = [...types, proObj.type_product]
			}
		}
		types = types.sort();
		console.log(types);
	 

	  
    })
	

	const sortByNumber = () => {
		  
		  products = products.sort((obj1, obj2) => {
			  return ascendingOrder ? Number(obj1['price']) - Number(obj2['price'])
			  : Number(obj2['price']) - Number(obj1['price'])
		
		  });
		 
	}
	const sortByNumbers = () => {
		  
		  products = products.sort((obj1, obj2) => {
			  return ascendingOrder ? Number(obj1['stock']) - Number(obj2['stock'])
			  : Number(obj2['stock']) - Number(obj1['stock'])
		
		  });
		 
	}
	const sortByNumberl = () => {
		  
		  products = products.sort((obj1, obj2) => {
			  return !ascendingOrder ? Number(obj1['price']) - Number(obj2['price'])
			  : Number(obj2['price']) - Number(obj1['price'])
		
		  });
		 
	}
	const sortByNumbersls = () => {
		  
		  products = products.sort((obj1, obj2) => {
			  return !ascendingOrder ? Number(obj1['stock']) - Number(obj2['stock'])
			  : Number(obj2['stock']) - Number(obj1['stock'])
		
		  });
		 
	}
	const sortByNumberdate = () => {
		  
		  products = products.sort((obj1, obj2) => {
			  return ascendingOrder ? Number(obj1['dateAdded']) - Number(obj2['dateAdded'])
			  : Number(obj2['dateAdded']) - Number(obj1['dateAdded'])
		
		  });
		 
	}
	const sortByNumberdatel = () => {
		  
		  products = products.sort((obj1, obj2) => {
			  return !ascendingOrder ? Number(obj1['dateAdded']) - Number(obj2['dateAdded'])
			  : Number(obj2['dateAdded']) - Number(obj1['dateAdded'])
		
		  });
		 
	}
	const sortByStringA = () => {
		  products = products.sort((obj1, obj2) => {
			  if (obj1['dateAdded'] < obj2['dateAdded']) {
					  return -1;
			  } else if (obj1['dateAdded'] > obj2['dateAdded']) {
				  return 1;
			  }
			  return 0; //string code values are equal		
		  });
		
		  
	}
	const sortByString = (colHeader) => {
		  products = products.sort((obj1, obj2) => {
			  if (obj1[colHeader] < obj2[colHeader]) {
					  return -1;
			  } else if (obj1[colHeader] > obj2[colHeader]) {
				  return 1;
			  }
			  return 0; //string code values are equal		
		  });
		 
		  products = products.reverse()
		  
		 
	}

	function buyNoLogged(){
    	navigate("/login");
	}


	$: if (selectedOption==="Order by price lowest to highest") sortByNumber();
	$: if (selectedOption==="Order by price highest to lowest") sortByNumberl();

	$: if (selectedOption==="Order by stock lowest to highest") sortByNumbers();
	$: if (selectedOption==="Order by stock highest to lowest") sortByNumbersls();
	
	$: if (selectedOption==="Order by recent added") sortByStringA();
	$: if (selectedOption==="Order by old added") sortByString ();
	

	
	
	// Query results
	let filteredProducts = [];
	
	// For Select Menu
	$: if (selectedType) getProductsByTypes();

	
	const getProductsByTypes = () => {
		// resets search input if menu is being used
		
		
		if (selectedType === "all") {
			return filteredProducts = [];
		} 
		return filteredProducts = products.filter(product => product.type_product === selectedType);

	}	

</script>

	






<section class="menu-cont">

	<select class="menu" 
					name="menu" 
					id="menu" 
					bind:value={selectedOption}>
		<option disabled selected value="">Select a type of filter</option>
		<option value="none">None</option>
		{#each tableHeading as option}
			<option value={option}>{option}</option>
			
		{/each}

	</select>
		<select class="menu" 
					name="menu" 
					id="menu" 
					bind:value={selectedType}>
		<option disabled selected value="">Select a type of product</option>
		<option value="all">All types</option>
		{#each types as type}
			<option value={type}>{type}</option>
			
		{/each}

	</select>

	<div>
   

</div>

</section>




<main id="bookshelf">
	
	
	{#if filteredProducts.length > 0}
	<div class="product-list">
	{#each filteredProducts as product}
	<div>
		<div class="image" style="background-image: url({product.image})"></div>
	<h4>{product.product_name}</h4>
	<p>Price: ${product.price} </p>
	{#if product.stock > 0}
	<p>Stock disponible </p>
		
	{:else}
	<p>Stock no disponible </p>
	{/if}
	<td><Button on:click={buyNoLogged} color="primary"> Add to cart </Button></td>
	</div>
	
	{/each}
</div>
	
{:else}
<div class="product-list">
	{#each products as product}
	<div>
		<div class="image" style="background-image: url({product.image})"></div>
	<h4>{product.product_name}</h4>
	<p>Price: ${product.price} </p>
	{#if product.stock > 0}
	<p>Stock disponible </p>
		
	{:else}
	<p>Stock no disponible </p>
	{/if}
	<td><Button on:click={buyNoLogged} color="primary"> Add to cart </Button></td>
	</div>
	
	{/each}
</div>
	
{/if}
	
</main>	




<style>
	.product-list {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
	}
	
	.image {
		height: 150px;
		width: 150px;
		background-size: contain;
		background-position: center;
		background-repeat: no-repeat;
	}
	
</style>


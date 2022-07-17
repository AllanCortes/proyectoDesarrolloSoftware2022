
<script>
	const tableHeading = ["Order by price highest to lowest","Order by price lowest to highest","Order by stock highest to lowest",
	"Order by stock lowest to highest","Order by old added","Order by recent added"];
	
	
	import { onMount } from 'svelte';
	import {Table} from 'sveltestrap';
	import { Styles, Button } from 'sveltestrap';
	import {navigate } from "svelte-navigator";
	
	
	
	
	
    let types = []; 
	let selected_Option = "";
	let selected_Type = "";
	
	let products = [];
	
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


	$: if (selected_Option==="Order by price lowest to highest") sortByNumber();
	$: if (selected_Option==="Order by price highest to lowest") sortByNumberl();

	$: if (selected_Option==="Order by stock lowest to highest") sortByNumbers();
	$: if (selected_Option==="Order by stock highest to lowest") sortByNumbersls();
	
	$: if (selected_Option==="Order by recent added") sortByStringA();
	$: if (selected_Option==="Order by old added") sortByString ();
	

	
	
	// Query results
	let filteredProducts = [];
	
	// For Select Menu
	$: if (selected_Type) getProductsByTypes();

	
	const getProductsByTypes = () => {
		// resets search input if menu is being used
		
		
		if (selected_Type === "all") {
			return filteredProducts = [];
		} 
		return filteredProducts = products.filter(product => product.type_product === selected_Type);

	}	

</script>

	


<section class="menu-cont">

	<select class="menu" 
					name="menu" 
					id="menu" 
					bind:value={selected_Option}>
		<option disabled selected value="">Select a type of filter</option>
		<option value="none">None</option>
		{#each tableHeading as option}
			<option value={option}>{option}</option>
			
		{/each}

	</select>
		<select class="menu" 
					name="menu" 
					id="menu" 
					bind:value={selected_Type}>
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


=======

<script>
	const tableHeading = ["product Name", "type Product", "price", "stock", "description","action"];
	const tableHeading2 = ["product Name", "type Product", "price", "stock", "description","action"];
	
	import { onMount } from 'svelte';
	import {Table} from 'sveltestrap';
	import { Styles, Button } from 'sveltestrap';

	import {navigate } from "svelte-navigator";
	
	
	
  
	
	
	let types = []; 
	let selectedType = ""; 
	let products = [];
	let selectedHeader = "stock";
	let ascendingOrder = true;
	
	function buyNoLogged(){
    navigate("/login");
	}	

	
	
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
	const sortByNumber = (colHeader) => {
		  products = products.sort((obj1, obj2) => {
			  return ascendingOrder ? Number(obj1[colHeader]) - Number(obj2[colHeader])
			  : Number(obj2[colHeader]) - Number(obj1[colHeader])
		
		  });
		  selectedHeader = colHeader;
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
		  if (!ascendingOrder) {
			  products = products.reverse()
		  }
		  selectedHeader = colHeader;
	}
	
	


	
	
	
	
	
	
	
	// Query results
	let filteredProducts = [];
	
	// For Select Menu
	$: if (selectedType) getBooksByLang();
	$: console.log(filteredProducts, selectedType);
	
	const getBooksByLang = () => {
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
					bind:value={selectedType}>
		<option disabled selected value="">Select a type of product</option>
		<option value="all">All types</option>
		{#each types as type}
			<option value={type}>{type}</option>
		{/each}
	</select>
</section>



<main id="bookshelf">
	
	
	{#if filteredProducts.length > 0}
	<Table style="background-color: #cfcfcf">
		<thead>
			<tr>
				{#each tableHeading as heading}
					<th>{heading}</th>
		  		
				{/each}
			
			
			
			</tr>
			
	
		</thead>
		<tbody>
  
	  
	
			{#each filteredProducts as f}
				<tr>
					<td>{f.product_name}</td>
					<td>{f.type_product}</td>
					<td>{f.price}</td>
					<td>{f.stock}</td>
					<td>{f.description}</td>
					<td><Button on:click={buyNoLogged} color="primary"> Add to cart </Button></td>
				</tr>		
			{/each}
		</tbody>	
	
	
	</Table>
	{:else}
	<Table style="background-color: #cfcfcf">
		<thead>
			<tr>
				{#each tableHeading2 as heading}
				<th class:highlighted={selectedHeader === heading}
					on:click={() => (heading === "stock" || heading === "price"  ) ? sortByNumber(heading) : sortByString(heading)}>
				{heading.replace("_", " ")}
		
  
				{#if heading === selectedHeader && (selectedHeader=== "stock" || selectedHeader=== "price" )}	
				<span class="order-icon" on:click={() => ascendingOrder = !ascendingOrder}>
					{@html ascendingOrder ? "&#9661;" : "&#9651;"}
				</span>		
				{/if}	
		  		</th>	
				{/each}
			
			
			
			</tr>
			
	
		</thead>
		<tbody>
  
	  
	
			{#each products as product}
				<tr>
					<td>{product.product_name}</td>
					<td>{product.type_product}</td>
					<td>{product.price}</td>
					<td>{product.stock}</td>
					<td>{product.description}</td>
					<td><Button on:click={buyNoLogged} color="primary"> Add to cart </Button></td>

				</tr>		
			{/each}
		</tbody>	
	
	
	</Table>
	{/if}
	
</main>	


<style>



    th {
        text-transform: uppercase;
        cursor: pointer;
        background-color: #f3f3f0
    }

    th, td {
        text-align: left;
        padding: 16px;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2
    }
</style>

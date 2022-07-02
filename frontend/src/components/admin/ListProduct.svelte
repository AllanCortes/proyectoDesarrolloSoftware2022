
<script>
	const tableHeading = ["id","product Name", "type Product", "price", "stock", "description","date added"];
	const tableHeading2 = ["id","product Name", "type Product", "price", "stock", "description","date added"];
	
	import { onMount } from 'svelte';
	import {Table} from 'sveltestrap';
	import { Styles, Button } from 'sveltestrap';
	
	
	
	let types = []; 
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
                    <td>{f.id}</td>
					<td>{f.product_name}</td>
					<td>{f.type_product}</td>
					<td>{f.price}</td>
					<td>{f.stock}</td>
					<td>{f.description}</td>
					<td>{f.dateAdded}</td>
					
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
					on:click={() => (heading === "stock" || heading === "price" || heading === "id"  ) ? sortByNumber(heading) : sortByString(heading)}>
				{heading.replace("_", " ")}
		
  
				{#if heading === selectedHeader && (selectedHeader=== "stock" || selectedHeader=== "date added" || selectedHeader=== "price" || selectedHeader=== "id" )}	
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
                    <td>{product.id}</td>
					<td>{product.product_name}</td>
					<td>{product.type_product}</td>
					<td>{product.price}</td>
					<td>{product.stock}</td>
					<td>{product.description}</td>
					<td>{product.dateAdded}</td>
			
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
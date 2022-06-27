<script lang="ts">
  import { Table } from 'sveltestrap';
  import {onMount} from "svelte";
  
  let selectedHeader = "id";
	let ascendingOrder = true;

  let products = [];
  const tableHeading = ["id", "productName", "price", "stock", "typeProduct", "description","dateAdded"];

  onMount(async () => {
    const res = await fetch("http://127.0.0.1:8000/products/");
    products = await res.json();
    
})

	
	
	// SORT BY NUMBER
	const sortByNumber = (colHeader) => {
		products = products.sort((obj1, obj2) => {
			return ascendingOrder ? Number(obj1[colHeader]) - Number(obj2[colHeader])
			: Number(obj2[colHeader]) - Number(obj1[colHeader])
      
		});
		selectedHeader = colHeader;
	}
 
	// SORT BY STRINGs
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
  ;
</script>


<Table style="background-color: #cfcfcf">
	
  <thead>
    <tr>
      {#each tableHeading as heading}
      <th class:highlighted={selectedHeader === heading}
					on:click={() => (heading === "id" || heading === "price"  ) ? sortByNumber(heading) : sortByString(heading)}>
				{heading.replace("_", " ")}

			{#if heading === selectedHeader}	
				<span class="order-icon" on:click={() => ascendingOrder = !ascendingOrder}>
					{@html ascendingOrder ? "&#9661;" : "&#9651;"}
				</span>		
			{/if}	
		</th>	
      {/each}
    </tr>
  </thead>
  <tbody>

    {#each products as product }
      <tr>
          <td>{product.id}</td>
          <td>{product.product_name}</td>
          <td>{product.price}</td>
		  <td>{product.stock}</td>
          <td>{product.type_product}</td>
          <td>{product.description}</td>
          <td>{product.dateAdded}</td>
      </tr>
    {/each}
  </tbody>
  
  
</Table>


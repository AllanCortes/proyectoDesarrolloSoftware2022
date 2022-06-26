<script lang="ts">
    import { Table } from 'sveltestrap';

    import {onMount} from "svelte";

    let products = [];
    onMount(async () => {
      const res = await fetch("http://127.0.0.1:8000/products/");
      products = await res.json();
  });
  </script>


  
  <Table style="background-color: #cfcfcf">
    <thead>
      <tr>
        <th>Name product</th>
        <th>Price</th>
        <th>Type</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
        {#each products as product }
            <tr>
                <td>{product.productName}</td>
                <td>{product.price}</td>
                <td>{product.typeProduct}</td>
                <td>{product.description}</td>
            </tr>
        {/each}
    </tbody>
  </Table>
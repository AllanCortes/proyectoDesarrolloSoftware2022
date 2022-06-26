<script lang="ts">
    import { Table } from 'sveltestrap';
    import {onMount} from "svelte";

    import { Form, FormGroup, FormText, Input, Label } from 'sveltestrap';

    let products = [];
    onMount(async () => {
      const res = await fetch("http://127.0.0.1:8000/products/");
      products = await res.json();
  });
  </script>


<Form>
    <h1 class="text-center">Catalogue</h1>
    <FormGroup>
      <Label for="exampleSelect">Sort by</Label>
      <Input type="select" name="select" id="exampleSelect">
        <option>Name product</option>
        <option>Vegetable</option>
        <option>Dairy</option>
        <option>4</option>
        <option>5</option>
      </Input>
    </FormGroup>
  </Form>
  
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
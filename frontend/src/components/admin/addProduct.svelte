<script lang="ts">
  import { Form, FormGroup, FormText, Input, Label } from 'sveltestrap';
  import { Styles, Button } from 'sveltestrap';
  import { onMount } from 'svelte';
  import { navigate } from "svelte-navigator";

  let selected;
  let name_product;
  let description_product;
  let price_product;
  let type_product;
  let stock_product;
  let types = []; 
  let products = []; 
  let image_product;



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
  function viewProducts(){
      navigate("/ListProduct")
  }
  

  function formHandler(event) {
    event.preventDefault()

    fetch('http://localhost:8000/products/',{
      method:  'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        product_name:name_product,
        type_product:selected,
        price:price_product,
        stock:stock_product,
        description:description_product,
        image:image_product
      })
    })
      .then(response => response.json())
      .then(result => console.log(result))
      .then(viewProducts)
  }
  console.log(type_product)
</script>


<Form >
  <h1 class="text-center text-product">Add product</h1>
  <FormGroup>
    <Label for="examplePassword">Product Name</Label>
    <Input
      type="text"
      name="nameproduct"
      id="nameproduct"
      placeholder="Example: Onion"
      bind:value={name_product}
    />
  </FormGroup>
  <FormGroup>
      <Label for="examplePassword">Price</Label>
      <Input
        type="text"
        name="price"
        id="price"
        placeholder="Example: 1000"
        bind:value={price_product}
      />
  </FormGroup>
  <FormGroup>
    <Label for="examplePassword">stock</Label>
    <Input
      type="text"
      name="price"
      id="price"
      placeholder="Example: 1000"
      bind:value={stock_product}
    />
</FormGroup>
  <FormGroup>
    <Label for="exampleSelect">Type</Label>
    <Input type="select" name="select" id="type_product" bind:value={selected}>
      {#each types as typee}
			  <option value={typee}>{typee}</option>
		  {/each}
     
    </Input>
  </FormGroup>
  <FormGroup>
    <Label for="exampleText">Other Type</Label>
    <Input type="text" name="text" id="type_product" bind:value={selected}/>
  </FormGroup>
  
  <FormGroup>
    <Label for="exampleText">Description</Label>
    <Input type="text" name="text" id="description" bind:value={description_product}/>
  </FormGroup>

  <FormGroup>
    <Label for="exampleText">Image</Label>
    <Input type="text" name="text" id="image" bind:value={image_product}/>
  </FormGroup>
  <FormGroup>
  <Button on:click={formHandler} on:click={viewProducts} color="primary"> Add</Button>
  </FormGroup>
</Form>
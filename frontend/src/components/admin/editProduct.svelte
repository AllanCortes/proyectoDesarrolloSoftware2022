<script lang="ts">
	
  import { Form, FormGroup, FormText, Input, Label } from 'sveltestrap';
  import { Styles, Button } from 'sveltestrap';
  import { onMount } from 'svelte';
  import { navigate } from "svelte-navigator";

 
  let selected_product;
  let product_name;
  let description_product;
  let price_product;
  
  let stock_product;
  
  let product_names =[];
  let products = []; 
  



    onMount(async () => {
      const res = await fetch("http://127.0.0.1:8000/products/");
      products = await res.json();
        

        for (let proObj of products) {
            if (!product_names.includes(proObj.product_name)) {
              product_names = [...product_names, proObj.product_name]
            }
        }
        product_names = product_names.sort();
        console.log(product_names);
     
     
        
        
      
      
    })

  function viewProducts(){
    navigate("/ListProduct")
  }

  function formHandler(event) {
    event.preventDefault()
    let i=selected_product;
      
    fetch('http://localhost:8000/products/?id='+i,{
      method:  'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        product_name:product_name,
        price:price_product,
        stock:stock_product,
        description:description_product
        
      })
    })
      .then(response => response.json())
      .then(result => console.log(result))
      .then(viewProducts)
  }
  
</script>




<Form >
  <h1 class="text-center text-product">Mod product</h1>
  <FormGroup>
      <Label for="exampleSelect">Product Name</Label>
      <Input type="select" name="select1" id="product_name" bind:value={selected_product}>
        {#each products as product}
                <option value={product.id}>{product.product_name}</option>
                
          
        {/each}
        
              
              
      
       
      </Input>
  </FormGroup>
   <FormGroup>
      <Label for="examplePassword">New Name Product</Label>
      <Input
        type="text"
        name="name"
        id="name"
        placeholder="Example: 1000"
        bind:value={product_name}
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
    <Label for="examplePassword">Stock</Label>
    <Input
      type="text"
      name="stock"
      id="stock"
      placeholder="Example: 1000"
      bind:value={stock_product}
    />
  </FormGroup>

  <FormGroup>
    <Label for="exampleText">Description</Label>
    <Input type="text" name="text" id="description" bind:value={description_product}/>
  </FormGroup>
  <FormGroup>
  <Button on:click={formHandler} color="primary"> Apply changes</Button>
  </FormGroup>
</Form>

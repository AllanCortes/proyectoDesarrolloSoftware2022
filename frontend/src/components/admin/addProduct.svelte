<script lang="ts">
  import { Form, FormGroup, FormText, Input, Label } from 'sveltestrap';
  import { Styles, Button } from 'sveltestrap';

  let selected;
  let name_product;
  let description_product;
  let price_product;
  let type_product;
  let stock_product;

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
        description:description_product
      })
    })
      .then(response => response.json())
      .then(result => console.log(result))
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
      <option {selected}>Fruit</option>
      <option {selected}>Vegetable</option>
      <option {selected}>Dairy </option>
    </Input>
  </FormGroup>
  <FormGroup>
    <Label for="exampleText">Description</Label>
    <Input type="text" name="text" id="description" bind:value={description_product}/>
  </FormGroup>
  <FormGroup>
  <Button on:click={formHandler} color="primary"> Create new Product</Button>
  </FormGroup>
</Form>
<script>
import { cart } from "../../store/store.js";
import {onMount} from "svelte";
import { Styles, Button } from 'sveltestrap';
import { jsPDF  } from "jspdf";
import autoTable from 'jspdf-autotable';
import { getAuth,signOut,onAuthStateChanged } from "firebase/auth";
import { navigate } from "svelte-navigator";

const tableHeading = ["Product Name", "Type Product", "Quantity", "Price by unit","Price total by product"];


let gotohome="False";
let products=[];

let email;
let namess;
function viewProducts(){
      navigate("/")
	  
	  
	  
}
onMount(async () => {
        const res = await fetch("http://127.0.0.1:8000/products/");
        products = await res.json();
          

         
       
          
          
				
        
      })



onMount(() => {
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
		if(user !==null){
			email = user.email;
			namess = user.name;
		}

    });
  });
const PDFREAD= () => {
	

		var doc = new jsPDF();
        console.log($cart.length)
    
		var logo="https://i.ibb.co/1nZpY9H/Pet-Lovers-1-removebg-preview.png"
		doc.addImage(logo,140,10,60,30);

		doc.text("                                                                               Total price: "+total, 10, 90);


		autoTable(doc, {html: '#basic-tablee'})


		autoTable(doc, {html: '#basic-table'})

		


		

		doc.text("Here is the receipt of your purchase, thank you for choosing us!", 10, 10);
		

		
        
        
        doc.save("Ticket.pdf");

		setTimeout( function() { window.location.href = "http://localhost:8080"; }, 5000 );
		gotohome="True";
		console.log(gotohome)
		
		

};





const minusItem = (product) => {
		for(let item of $cart) {
				if(item.id === product.id) {
					if(product.quantity > 1 ) {
							product.quantity -= 1
							$cart = $cart
							console.log($cart)
					} else {
							$cart = $cart.filter((cartItem) => cartItem != product)
							console.log($cart)
					}
					return;
				}
		}
	}
	
const plusItem = (product) => {
		for(let item of $cart) {
			if(item.id === product.id) {
				if (product.stock>product.quantity){
				item.quantity += 1
				$cart = $cart;
				console.log($cart)
				return;
				}
			}
		}
	}

$: total = $cart.reduce((sum, item) => sum + item.price * item.quantity, 0)




function formHandler(event) {
      event.preventDefault()
      let i=1;
	  let stockn=0;
	  let namen="";
	  let descriptionn="";
	  let pricen=0;
      for (let item of $cart) {
	    i=item.id
		stockn=((item.stock)-(item.quantity))
		namen=item.product_name
		pricen=item.price
		descriptionn=item.description
		console.log(stockn)
		console.log(i)

		fetch('http://localhost:8000/products/?id='+i,{
        method:  'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
		  product_name:namen,
          price:pricen,
          stock:stockn,
          description:descriptionn
					
        })
      	})
        .then(response => response.json())
        .then(result => console.log(result))
        
              
        } 
      
}




</script>




<div class="cart-list">
	<h4>Shoping cart</h4>
	
	{#each $cart as item }
		{#if item.quantity > 0}
		<div class="cart-item">
			<img width="50" src={item.image} alt={item.product_name}/>
			<div>{item.quantity}
				<button on:click={() => plusItem(item)}>+</button>
				<button on:click={() => minusItem(item)}>-</button>
				
			</div>
			<p>${item.price * item.quantity}</p>
		</div>
		{/if}
	
   
	{/each}
	
	<div class="total">
		
		<h4>Total:${total}</h4>
		
	</div>
	<button on:click={()=>PDFREAD()}
     on:click={formHandler}>Checkout</button>
</div>



<table id="basic-tablee" style="display: none;">
	<thead>
		<tr>
			{#each tableHeading as heading}
				<th>{heading}</th>
			  
			{/each}
		
		
		
		</tr>
		

	</thead>
	<tbody>

  

		{#each $cart as f}
			<tr>
				
				<td>{f.product_name}</td>
				<td>{f.type_product}</td>
				<td>{f.quantity}</td>
				<td>{f.price}</td>
				<td>{f.price * f.quantity}</td>
				
				
				
				
				
			</tr>		
		{/each}
	</tbody>	


</table>
<table id="basic-table" style="display: none;">
	<thead>
		<tr>
			
			
			<th>Email</th>
			
			
		
		
		</tr>
		

	</thead>
	<tbody>

  

		
			<tr>
				
			
				<td>{email}</td>
			
				
				
				
			</tr>		
		
	</tbody>	


</table>

<table id="basic-table" style="display: none;">
	<thead>
		<tr>
			
			<th>Total</th>
			
			
			
		
		
		</tr>
		

	</thead>
	<tbody>

  

		
			<tr>
				
				<td>{total}</td>
				
			
				
				
				
			</tr>		
		
	</tbody>	


</table>








<style>
	
    .cart-item {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
    }
  
   

      .total {
      text-align: right;
    }
  
    .cart-list {
      border: 2px solid;
      padding: 10px;
    }

  
  
</style>

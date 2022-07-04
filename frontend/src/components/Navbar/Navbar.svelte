<script lang="ts">
  import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
  } from 'sveltestrap';
  import { onMount } from "svelte";
  import { Button } from 'sveltestrap';
  import { auth } from "../../firebase";
  import { islogged} from "../../store/store";
  //import { userApi } from "../../Api/userApi";
  import { navigate } from "svelte-routing";
  import { useNavigate } from "svelte-navigator";
  import { getAuth,signOut,onAuthStateChanged } from "firebase/auth";
  import { prevent_default } from 'svelte/internal';



  let isOpen = false;
  let email ;

  onMount(() => {
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
      if (user) {
        email = user.email;
        islogged.update(() => true);
      } else {
        islogged.update(() => false);
      }
    });
  });

  function handleUpdate(event) {
    isOpen = event.detail.isOpen;
  }

 function logout(){
    signOut(auth)
    .then(() => {
      localStorage.removeItem("admin");
      localStorage.removeItem("uid");
      navigate("/home");
    })
    .catch((error) => {
      console.log(error);
    })
 }

</script>

<Navbar style="background-color: #f7bd53" light expand="md" alt="">
  <!-- svelte-ignore a11y-missing-attribute -->
  <img src="https://i.ibb.co/1nZpY9H/Pet-Lovers-1-removebg-preview.png" width="270" height="120" alt="" />
  <NavbarToggler on:click={() => (isOpen = !isOpen)} />
  <Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
    <Nav class="ms-auto" navbar>
      {#if !$islogged}
      <NavItem>
        <NavLink href="/">Home</NavLink>
      </NavItem>
      <NavItem>
        <NavLink href="/catalogo">Cataloge</NavLink>
      </NavItem>
      <NavItem>
        <NavLink href="/login">Login</NavLink>
      </NavItem>
      <NavItem>
        <NavLink href="/register">Register</NavLink>
      </NavItem>
      {/if}
      {#if $islogged && email=="admin@gmail.com"}
      <NavItem>
        <NavLink href="/">Home</NavLink>
      </NavItem>
        <NavItem>
          <NavLink href="/addProduct">Add Product</NavLink>
        </NavItem> 
        <NavItem>
          <NavLink href="/editProduct">Edit Product</NavLink>
        </NavItem> 
        <NavItem>
          <NavLink href="/ListProduct">Products</NavLink>
        </NavItem> 
        <NavItem>
          <a class ="nav-link" on:click={logout} href="/login">Sign out</a>
        </NavItem>
      {/if}
      {#if $islogged && email!="admin@gmail.com"}
      <NavItem>
        <NavLink href="/">Home</NavLink>
      </NavItem>
      <NavItem>
        <NavLink href='/buy'>Cataloge</NavLink>
      </NavItem>
      <NavItem>
        <NavLink href="/cart">Shopping Cart</NavLink>
      </NavItem>
      <NavItem>
        <a class ="nav-link" on:click={logout} href="/login">Sign out</a>
      </NavItem>
      {/if}
    </Nav>
      
  </Collapse>
</Navbar>
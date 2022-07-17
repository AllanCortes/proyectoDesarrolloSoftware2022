
<script lang="ts">
  import {
    Collapse,
    Navbar,
    NavbarToggler,
    Nav,
    NavItem,
  } from 'sveltestrap';
  import { onMount } from "svelte";
  import { auth } from "../../firebase";
  import { islogged} from "../../store/store";
  import { navigate } from "svelte-routing";
  import { Link } from "svelte-navigator";
  import { getAuth,signOut,onAuthStateChanged } from "firebase/auth";
 
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
        <Link class ="nav-link" to="/">Home</Link>
      </NavItem>
      <NavItem>
        <Link class ="nav-link" to="/catalogo">Cataloge</Link>
      </NavItem>
      <NavItem>
        <Link class ="nav-link" to="/login">Login</Link>
      </NavItem>
      <NavItem>
        <Link class ="nav-link" to="/register">Register</Link>
      </NavItem>
      {/if}
      {#if $islogged && email=="admin@gmail.com"}
      <NavItem>
        <Link class ="nav-link" to="/">Home</Link>
      </NavItem>
        <NavItem>
          <Link class ="nav-link" to="/addProduct">Add Product</Link>
        </NavItem> 
        <NavItem>
          <Link class ="nav-link" to="/editProduct">Edit Product</Link>
        </NavItem> 
        <NavItem>
          <Link class ="nav-link" to="/ListProduct">Products</Link>
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
        <Link class ="nav-link" to="/">Home</Link>
      </NavItem>
      <NavItem>
        <Link class ="nav-link" to='/buy'>Cataloge</Link>
      </NavItem>
      <NavItem>
        <Link class ="nav-link" to="/cart">Shopping Cart</Link>
      </NavItem>
      <NavItem>
        <a class ="nav-link" on:click={logout} href="/login">Sign out</a>
      </NavItem>
      {/if}
    </Nav>
      
  </Collapse>
</Navbar>
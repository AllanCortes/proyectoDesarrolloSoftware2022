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
  import { Button } from 'sveltestrap';
  import { auth } from "../../firebase";
  import { islogged } from "../../store/store";
  import { userApi } from "../../Api/userApi";
  import { navigate } from "svelte-routing";
  import { useNavigate } from "svelte-navigator";
  const navigates = useNavigate();

  
  let isloggedUser =false;
  islogged.subscribe((data)=>{
    isloggedUser =data;
  })

  let isOpen = false;

  function handleUpdate(event) {
    isOpen = event.detail.isOpen;
  }

  function handleLogout(){
    auth.signOut().then(()=>{
      console.log("user singned out")
      console.log(isloggedUser)
    })
    localStorage.clear();
    navigates("/login");
  };


</script>

<Navbar style="background-color: #f7bd53" light expand="md" alt="">
  <img src="https://i.ibb.co/1nZpY9H/Pet-Lovers-1-removebg-preview.png" width="270" height="120" />
  <NavbarToggler on:click={() => (isOpen = !isOpen)} />
  <Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
    <Nav class="ms-auto" navbar>
      <NavItem>
        <NavLink href="/">Home</NavLink>
      </NavItem>
      {#if isloggedUser =false}
        <NavItem>
          <NavLink href="/login">Login</NavLink>
        </NavItem>
        <NavItem>
          <NavLink href="/register">Register</NavLink>
        </NavItem>
      {/if}
      <NavItem>
        <NavLink href="/catalogo">Catalogo</NavLink>
      </NavItem>
      <NavItem>
        <NavLink href="/addProduct">AddProduct</NavLink>
      </NavItem>
      {#if isloggedUser =true}
        <NavItem>
          <Button size="sm" on:click={handleLogout}>Sign Out</Button>
        </NavItem>
      {/if}
    </Nav>
  </Collapse>
</Navbar>
<script lang="ts">
  import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
    Dropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem
  } from 'sveltestrap';

  import { islogged } from "../../store/store";

  let isloggedUser =false;
  islogged.subscribe((data)=>{
    isloggedUser =data;
  })

  let isOpen = false;

  function handleUpdate(event) {
    isOpen = event.detail.isOpen;
  }
</script>

<Navbar style="background-color: #f7bd53" light expand="md" alt="">
  <img src="https://i.ibb.co/1nZpY9H/Pet-Lovers-1-removebg-preview.png" width="270" height="120" />
  <NavbarToggler on:click={() => (isOpen = !isOpen)} />
  <Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
    <Nav class="ms-auto" navbar>
      <NavItem>
        <NavLink href="/">Home</NavLink>
      </NavItem>
      {#if isloggedUser}
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
    </Nav>
  </Collapse>
</Navbar>
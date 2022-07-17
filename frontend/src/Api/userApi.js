import { onMount } from "svelte";
import {getAuth, onAuthStateChanged} from "firebase/auth";
import {auth} from "../firebase";
import {useNavigate, useLocation} from "svelte-navigator"
import {islogged,isAdmin} from "../store/store"


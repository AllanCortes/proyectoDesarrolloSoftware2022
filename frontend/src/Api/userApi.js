import { onMount } from "svelte";
import {onAuthStateChanged} from "firebase/auth";
import {auth} from "../firebase";
import {useNavigate, useLocation} from "svelte-navigator"
import {islogged} from "../store/store"

export const userApi =()=>{
    const navigate = useNavigate();
    const {subcribe} =useLocation()
    let pathname = "/"
    subcribe((info)=>{
        pathname = info.pathname
    })

    onMount(()=>{
        onAuthStateChanged(auth,(user) =>{
            let userlogged =user ==null ? false:true;

            if (!userlogged){
                navigate("/login");
                islogged.set(false);
            }else{
                islogged.set(true);
                if (pathname ==="/login"|| "/register"){
                    navigate("/")
                }
            }
        });
    });
}
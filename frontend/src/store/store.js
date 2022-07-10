import { writable } from "svelte/store";
 
export const islogged =writable(false);
export const cart = writable([]);
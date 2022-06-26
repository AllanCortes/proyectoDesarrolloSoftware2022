import { writable, derived } from 'svelte/store';

export const current_product = writable([]);
export const current_user = writable([]);

export const productNames = derived(current_product, ($current_product) => {
    if ($current_product.products){
      return $current_product.products.map(product=> product.strProduct);
    }
    return [];
  });
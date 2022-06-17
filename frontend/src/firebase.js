// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDGIxABq4I_bF44e0NdF4wE4tvp7t-2dWY",
  authDomain: "proyectopsoftware.firebaseapp.com",
  projectId: "proyectopsoftware",
  storageBucket: "proyectopsoftware.appspot.com",
  messagingSenderId: "433594787287",
  appId: "1:433594787287:web:b5349a463ba53bfa725792"
};

// Initialize Firebase
//const app = initializeApp(firebaseConfig);

let app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export {
    auth,
}
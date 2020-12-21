import firebase from 'firebase'


const firebaseConfig = {
    // apiKey: "AIzaSyCGYV_gX30Ubk9FkWspNCCacmGZv25p2pQ",
    // authDomain: "bird-identification-960ce.firebaseapp.com",
    databaseURL: "https://krishi-unnati-d8565-default-rtdb.firebaseio.com",
    // projectId: "bird-identification-960ce",
    // storageBucket: "bird-identification-960ce.appspot.com",
    // messagingSenderId: "874837997797",
    // appId: "1:874837997797:web:b6c6521374cfc956d17c0c",
    apiKey: "AIzaSyAcB9U1QYUcZ8_WIeIcdOJQmzwngkJvsDg",
    authDomain: "krishi-unnati-d8565.firebaseapp.com",
    projectId: "krishi-unnati-d8565",
    storageBucket: "krishi-unnati-d8565.appspot.com",
    messagingSenderId: "933323104391",
    appId: "1:933323104391:web:a9d6ca4ba085da4eb59822"
}


let Firebase = firebase.initializeApp(firebaseConfig)

export default Firebase
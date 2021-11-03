let username = "JackOfAllTrades";
let userCheck = /^[A-Za-z]+([A-Za-z]{1,}|(\d+\d))\d*$/g; // Change this line
let result = userCheck.test(username);
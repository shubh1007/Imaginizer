// jshint esversion:6
const express = require("express");

const app = express();
app.get("/", function(req, res){
  res.sendFile(__dirname + "/main.py");
})




app.listen(3000, function(req, res){
  console.log("Server Running at Port: 3000");
})

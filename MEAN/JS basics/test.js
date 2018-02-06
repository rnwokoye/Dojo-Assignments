let magic_multiply = function(x,y){
    if(typeof(x) == "number" || typeof(x) == "Array" || typeof(x) == "String" || typeof(y) == "number" || typeof(y) == "Array" || typeof(y) == "String"){
        return x*y;
    }
}
console.log(magic_multiply(5,20)); 
console.log(magic_multiply(5,"hello"));
console.log(magic_multiply("head",4));
console.log(magic_multiply(0,0));
console.log(magic_multiply([1,2,3],4));
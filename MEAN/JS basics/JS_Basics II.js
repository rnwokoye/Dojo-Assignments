function magic_multiply(x, y){
    if(x.constructor === Array){
        for(let i = 0; i < x.length; i ++){
            x[i]*= y;
        } 
        return x; 
    }
    if(y.constructor === String){
        console.log("Error: Can not multiply by string");

    }
    if(x.constructor === String){
        let temp =x; 
        for(let i = 0; i < y-1; i ++){
            x += temp;
        }
        return x; 
    }
    if(x === 0 && y === 0){
        return "All inputs 0";
    }
    x = x*y;

    return x; 
}
// console.log(magic_multiply(5,2));
// console.log(magic_multiply(0,0));
// console.log(magic_multiply([1,2,3],2));
console.log(magic_multiply(7,"three"));
// console.log(magic_multiply("Brendo",4));

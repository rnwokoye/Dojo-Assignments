let x = [];
console.log(x);
x.push('coding', 'dojo', 'rocks');
console.log(x);
x.pop();
console.log(x);

//BAsic 2.
const y = [];
console.log(y);
y.push(88);
console.log(y);
y.push(10);
console.log(y);

// basic 3:
let z = [9,10,6,5,-1,20,13,2];
for (let i = 0; i < z.length; i ++){
    // console.log(z[i]);
    if(z[i] == 2){ continue};
    console.log(z[i]);  
}

// basic 4
let names = ['kadie', 'Joe', 'Firtze', 'Piere', 'Alphonse'];
for (let i = 0; i < names.length; i ++){
    if (names[i].length == 5){
        console.log(names[i]);
    }
}

//basic 5

function yell(string){
    return string.toUpperCase();
}
console.log(yell("richard"));
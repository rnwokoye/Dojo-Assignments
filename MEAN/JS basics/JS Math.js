function zero_negativity(arr){
    for(let i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            return true;
        }
   }
   return false;
}
// Math 2
function is_Even(num){
        return num%2 == 0;
    }
//Math 3:
function how_many_even(arr){
    let total = 0;
    for(let i=0;i<arr.length;i++){
        if(is_Even(arr[i])){
            total++;
        }
    }
    return total;
}
console.log(how_many_even([2,4,8,5,9]));

function dummyArr(n){
    let arr = [];
    for(let i=0;i<n;i++){
        arr[i] = Math.floor(Math.random()*10);   
    }return arr;
}
console.log(dummyArr(4));

function rand_choice(arr){
    let arr = []; 
    return arr[Math.floor(Math.random() * arr.length) + 0] 
}
console.log(rand_choice[2,4,1]);





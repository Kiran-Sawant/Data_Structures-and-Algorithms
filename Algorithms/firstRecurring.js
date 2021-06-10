// Find the first recurring number from the array

function firstRecurringCharacter(array){

    for(i=0; i < array.length; i++){
        var cache = [];
        cache.push(array[i]);
        for(j=i+1; j < array.length; j++){
            if(cache.includes(array[j])){
                return `element ${array[j]} at index ${j}`;
            }
            else{
                cache.push(array[j]);
                continue;
            }
        }
    }
    return undefined;
}

const array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
const array2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]

console.log(firstRecurringCharacter(array2))
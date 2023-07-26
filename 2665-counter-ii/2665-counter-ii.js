/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let curr=init
    let cu=init
    return {
        increment: (init) => {
        cu+=1
        return cu
    },
        decrement :(init) =>{
        cu-=1
        return cu
    },
        reset: (init)=>{
        cu=curr
        return cu
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
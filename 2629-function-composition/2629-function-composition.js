/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {
        let val=0
        if(functions.length===0) return x
        for(i=functions.length-1;i>=0;i--) {
            if (i===functions.length-1) val=functions[i](x)
            else val=functions[i](val)
           }
        return val
        }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
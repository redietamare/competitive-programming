/**
 * @return {number}
 */
var argumentsLength = function(...args) {
    array=[]
    array.push(...args)
    return array.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
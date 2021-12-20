// partial apply

const add = (a, b) => a + b;

const add10 = (x) => x + 10;

const partial = (fn, ...argsToApply) => {
  return (...restArgsToApply) => {
    return fn(...argsToApply, ...restArgsToApply);
  };
};

const add10 = partial(add, 10);

const get15 = partial(add10, 5);

const get15 = partial(add, 10, 5);

const add10 = add.bind(null, 10);

const get15 = add.bind(null, 10, 5);

// currying

const add = (a) => (b) => a + b;

// lodash fp

// https://github.com/getify/functional-light-js

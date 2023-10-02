function add(...numbers) {
  if (numbers.length > 1) {
    let result = 0;
    for (let i = 0; i < numbers.length; i++) {
      if (typeof numbers[i] === "number") {
        result += numbers[i];
      } else {
        throw Error("something went wrong");
      }
    }
    return result;
  } else {
    throw `Please enter at least two numbers to sum.`;
  }
}
function mul(...numbers) {
  if (numbers.length > 1) {
    let result = 1;
    for (let i = 0; i < numbers.length; i++) {
      if (typeof numbers[i] === "number") {
        result *= numbers[i];
      } else {
        throw Error("something went wrong");
      }
    }
    return result;
  } else {
    throw `Please enter at least two numbers to multiply.`;
  }
}
function sub(...numbers) {
  if (numbers.length > 1) {
    let result = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
      if (typeof numbers[i] === "number") {
        result -= numbers[i];
      } else {
        throw Error("something went wrong");
      }
    }
    return result;
  } else {
    throw `Please enter at least two numbers to subtract.`;
  }
}
function div(...numbers) {
  if (numbers.length > 1) {
    let result = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
      if (typeof numbers[i] === "number") {
        result /= numbers[i];
      } else {
        throw Error("something went wrong");
      }
    }
    return result;
  } else {
    throw `Please enter at least two numbers to divide.`;
  }
}
function sums(start, end, func) {
  let Start = typeof start === "number" && !Number.isNaN(start) ? start : null;
  let End = typeof end === "number" && !Number.isNaN(end) ? end : null;
  let Func = typeof func === "function" ? func : null;
  if (Start !== null && End !== null && Func !== null) {
    try {
      r = func(start);
      if (r === undefined) throw Error("something went wrong");
      else if (typeof r !== "number") throw Error("something went wrong");
    } catch (err) {
      throw err;
    }
    if (Start <= End) {
      let result = 0;
      for (let i = start; i <= end; i++) {
        result += func(i);
      }
      return result;
    } else {
      throw Error("something went wrong");
    }
  } else {
    if (Start === null) throw Error("something went wrong");
    if (End === null) throw Error("something went wrong");
    if (Func === null) throw Error("something went wrong");
  }
}

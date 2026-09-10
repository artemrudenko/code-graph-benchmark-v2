const { encode } = require('gpt-tokenizer');
const fs = require('fs');
const file = process.argv[2];
const text = fs.readFileSync(file, 'utf8');
console.log(encode(text).length);

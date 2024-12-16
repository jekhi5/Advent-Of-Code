var fs = require("fs");
console.log("Going to write into existing file");
// Open a new file with name input.txt and write Simply Easy Learning! to it.

var total = 0
var index = 0;

fs.readFile('Input-File.txt', function (err, data) {
    if (err) {
        return console.error(err);
    }
    var temp = data.toString();
    total += temp.length + 2;
});

console.log(total);

console.log('hello'.length);
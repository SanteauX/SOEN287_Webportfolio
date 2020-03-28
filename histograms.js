const fs = require("fs");
const parse = require("csv-parse");

const csvData = [];

fs.createReadStream(__dirname + "/data/connections.csv")
  .pipe(parse({ delimiter: "," }))
  .on("data", function(dataRow) {
    csvData.push(dataRow);
  })
  .on("end", function() {
    console.log(csvData);
  });

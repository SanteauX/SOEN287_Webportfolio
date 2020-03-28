const fs = require("fs");
const parse = require("csv-parse");

const csvData = [];

fs.createReadStream("./data/connections.csv")
  .pipe(parse({ delimiter: "," }))
  .on("data", function(dataRow) {
    csvData.push(dataRow);
  })
  .on("end", function() {
    console.log(csvData);
  });

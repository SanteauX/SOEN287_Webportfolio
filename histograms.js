const fs = require("fs");
const parse = require("csv-parse");

const csvData = [];

fs.createReadStream(__dirname + "data/connections.csv")
  .pipe(
    parse({
      delimiter: ","
    })
  )
  .on("data", function(datarow) {
    csvData.Data.push(dataRow);
  })
  .on("end", function() {
    console.log(csvData);
  });

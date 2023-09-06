const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter year-end date (dd/mm/yyyy): ", function (date_input) {
  // Split the input string to extract day, month, and year
  const [day, month, year] = date_input.split('/').map(Number);

  // Define the start and end dates for the comparison with a fixed year
  const start_date_m_code = new Date(year, 0, 1);
  const end_date_m_code = new Date(year, 2, 31);
  const start_date_d_code = new Date(year, 11, 1);
  const end_date_d_code = new Date(year, 11, 31);

  // Create a Date object using the input year, month, and day
  const input_date = new Date(year, month - 1, day);

  // Perform the date comparison
  if (start_date_m_code <= input_date && input_date <= end_date_m_code) {
    console.log("");
    console.log(`Result: 'M Code', the standard deadline should be 15 Nov ${year}`);
    console.log(`Adjusted loss could be extended to 31 Jan ${year}`);
    console.log("");
  } else if (start_date_d_code <= input_date && input_date <= end_date_d_code) {
    console.log("");
    console.log(`Result: 'D Code', the standard deadline should be 15 Aug ${year + 1}`);
    console.log("Loss extension not available");
    console.log("");
  } else {
    console.log("");
    console.log(`Result: 'N Code', the standard deadline should be 30 Apr ${year + 1}`);
    console.log("Loss extension not available");
    console.log("");
  }

  rl.close();
});

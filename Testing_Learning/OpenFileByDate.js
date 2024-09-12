/**
 * @author Neamen
 * @description
 *      Loads file saved as currenct date
 */


/**
 * @param {}
 * @return {string}
 * 
 */


let DateAsString = function(){
    let currenct_date = new Date();
    let date_components = [];

    let year = currenct_date.getFullYear();
    // Month is zero indexed, runs 0-11
    let month = currenct_date.getMonth() + 1;
    // Day is 1 indexded, runs 1-31
    let day = currenct_date.getDate();

    // Adding components to the array as strings padded if needed
    date_components.push(year.toString());
    // padstart() pads the string with a given string to reach the given length. so if 1, pad with 0 to make 01.
    date_components.push(month < 10 ? month.toString().padStart(2,'0') : month.toString());
    date_components.push(day < 10 ? day.toString().padStart(2, '0') : day.toString());

    // Apply typecast function using map
    // date_components = date_components.map( x => String(x));
    // Two ways to do this
    // 1. 
    // let file_name = '';
    // return file_name.concat(date_components.join('-'), '.json');

    // or
    // 2.

    // Needs relative path so adding that
    const path = require('path');
    file_path = path.join(__dirname, date_components.join('-'));
    return `${file_path}.json`;
    
    // console.log(file_name);
    // console.log(date_components.map(x => String(x)));
    // console.log(currenct_date.getFullYear());

}
console.log(DateAsString());
/**
 * 
 * @param {string} filename
 * @return {}
 */
let OpenFile = function (DateAsString){

    // Create an object of a filesystem accessor
    const fs = require('fs');

    /* So when opening a file in javascript, you can do it
        1. Synchronously
            Sequential code where the program waits for the file to be opened before it carries on
        2. Asynchronously
            The file opening is handed of to node.js and the rest of the program is worked on until the file reading completes
    */
    
    // Asynchronous
    // The readFile function takes three arguments here. 
    //  patht to file, read mode (utf or buffer), and a callback function in arrow function form
    //      Arrow function has parameters err and data in a tuple
    fs.readFile('Testing_Learning/2024-09-02.json', 'utf-8', (err, data) => {

        if (err){
            console.log(err);
            return;
        }

        // Do whatever with the dara
        console.log(data);

    });
}
// console.log(DateAsString());

// OpenFile(DateAsString);
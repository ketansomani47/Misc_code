module.exports = function date_format(input_date, format){
    let [day, month, year] = input_date.split("/");
    console.log('day : ', day, 'month : ', month, 'year : ', year);
    if (month <= 9) {
      month = `0${month}`
    }
    if (day <= 9) {
      day = `0${day}`
    }
    let output_date;
    if (format === undefined){
        output_date = `${day}/${month}/${year}`;
    }
    else{
        output_date = `${year}/${month}/${day}`;
    }
    return output_date;
}
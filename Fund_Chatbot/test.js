// const date_regex = new RegExp('^(0[1-9]|[12][0-9]|3[01])[/-](0[1-9]|1[012])[/-]((19|20)[0-9][0-9])$');
// const date_regex = new RegExp('^((((0[1-9]|1[0-9]|2[0-8])[/-](0[1-9]|1[012]))|((29|30|31)[/-](0[13578]|1[02]))|((29|30)[/-](0[4,6,9]|11)))[/-](19|[2-9][0-9])\d\d$)|(^29[/-]02[/-](19|[2-9][0-9])(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96))$');
// const date_regex = new RegExp('^(?:0[1-9]|[12]\d|3[01])/(?:0[1-9]|1[012])/(?:19\d\d|20\d\d)$');
// final
// const date_regex = new RegExp('^((((0[13578]|1[02])[/-](0[1-9]|1[0-9]|2[0-9]|3[01]))|((0[469]|11)[/-](0[1-9]|1[0-9]|2[0-9]|3[0]))|((02)([/-](0[1-9]|1[0-9]|2[0-8]))))[/-](19([6-9][0-9])|20([0-9][0-9])))|((02)[/-](29)[/-](19(6[048]|7[26]|8[048]|9[26])|20(0[048]|1[26]|2[048])))')
// const start_date = "02/22/2023";
// console.log("matching : ", date_regex.test(start_date));
// if (!date_regex.test(start_date)) {
//     console.log('regex failed');
// }


// ^
// (
//     (
//         (
//             (0[13578]|1[02])[/-](0[1-9]|1[0-9]|2[0-9]|3[01])
//         )|
//         (
//             (0[469]|11)[/-](0[1-9]|1[0-9]|2[0-9]|3[0])
//         )|
//         (
//             (02)([/-](0[1-9]|1[0-9]|2[0-8]))
//         )
//     )
//     [/-]
//     (19([6-9][0-9])|20([0-9][0-9])
//     )
// )
// |
// ((02)[/-](29)[/-](19(6[048]|7[26]|8[048]|9[26])|20(0[048]|1[26]|2[048])))




// const str1 = "23/02/2023"
// const str2 = "23/01/2023"
// if (str2 <= str1){
//     console.log(typeof str1, typeof str2);
//     console.log('working');
// }
// else{
//     console.log('not working');
// }

// const moment = require('moment');
// const start = moment();
// console.log(start, typeof start);
// const end = new Date('2023-02-23')
// console.log(end, typeof end);


// let [day1, month1, year1] = [30, 06, 2020];
// let start_date = new Date(year1,month1-1,day1).toLocaleDateString();
// console.log(start_date, typeof start_date);
// const date_format = require('./date.js');
// const date = [ '30/6/2020', '30/6/2022' ];
// let start_date = date_format(date[0]);
// // let start_date = date[0];
// console.log("start date : ", start_date, typeof start_date);
// let end_date = date_format(date[1]);
// // let end_date = date[1];
// console.log('end date : ', end_date, typeof end_date);
// const trasaction_data = [
// { transaction_date: "12/08/2021", opening_balance: 0, amount_invested: 1000, closing_balance: 1000, fund: 'ABC overnight fund' },
// { transaction_date: "10/11/2021", opening_balance: 1000, amount_invested: 500, closing_balance: 1500, fund: 'ABC liquid fund' },
// { transaction_date: "20/12/2021", opening_balance: 1500, amount_invested: 500, closing_balance: 2000, fund: 'ABC savings fund' },
// { transaction_date: "04/01/2022", opening_balance: 2000, amount_invested: 1000, closing_balance: 3000, fund: 'ABC savings fund' },
// { transaction_date: "12/05/2022", opening_balance: 3000, amount_invested: 1000, closing_balance: 4000, fund: 'ABC overnight fund' },
// { transaction_date: "23/08/2022", opening_balance: 4000, amount_invested: 500, closing_balance: 4500, fund: 'ABC liquid fund' },
// { transaction_date: "06/01/2023", opening_balance: 4500, amount_invested: 1500, closing_balance: 6000, fund: 'ABC overnight fund' },
// { transaction_date: "29/03/2023", opening_balance: 6000, amount_invested: 600, closing_balance: 6600, fund: 'ABC savings fund' },
// { transaction_date: "12/07/2023", opening_balance: 6600, amount_invested: 1000, closing_balance: 7600, fund: 'ABC liquid fund' },
// { transaction_date: "04/10/2023", opening_balance: 7600, amount_invested: 500, closing_balance: 8100, fund: 'ABC overnight fund' },
// { transaction_date: "01/01/2024", opening_balance: 8100, amount_invested: 900, closing_balance: 9000, fund: 'ABC savings fund' },
// { transaction_date: "15/02/2024", opening_balance: 9000, amount_invested: 1000, closing_balance: 10000, fund: 'ABC liquid fund' }
// ]
// // res = trasaction_data.filter(t => t.transaction_date >= start_date && t.transaction_date <= end_date)
// // let res = [];
// // for (let i=0; i < trasaction_data.length; i++){
// //     console.log("td",trasaction_data[i].transaction_date, typeof trasaction_data[i].transaction_date);
// //     console.log('start : ', trasaction_data[i].transaction_date >= start_date);
// //     if (trasaction_data[i].transaction_date >= start_date && trasaction_data[i].transaction_date <= end_date){
// //         console.log('filtered data');
// //         res.concat(trasaction_data[i]);
// //     }
// // }
// // console.log(res);
// const cmp1 = '2023/10/20'
// const start_date1 = '2020/06/30'
// // const d1 = Date.parse(start_date1);
// // const d2 = Date.parse(cmp1);
// // console.log(d1, d2, typeof d1, typeof d2);
// // if (d1 <= d2) {
// if (start_date <= cmp1) {
//   console.log("date greater than strat date");
// }
// // console.log(cmp1 >= start_date);

const str1 = '25/05/2020';
// let [year, month, day] = str1.split('/');
console.log(new Date(str1));
// console.log(new Date(year, month, day));
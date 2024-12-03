const { Suggestion } = require('dialogflow-fulfillment')
const date_format = require('./date.js');

function show_transaction(agent) {
  console.log('show transaction intent called');
  let date = agent.context.get('transactionhistory')['parameters']['date'];
  console.log(date);
  let start_date = date_format(date[0], 1);
  console.log("start date : ", start_date, typeof start_date);
  let end_date = date_format(date[1], 1);
  console.log('end date : ', end_date, typeof end_date);
  agent.add(`Transaction list from ${start_date} to ${end_date}`);
  
  trasaction_data = [
    { transaction_date: "2021/08/12", opening_balance: 0, amount_invested: 1000, closing_balance: 1000, fund: 'ABC overnight fund' },
    { transaction_date: "2021/11/10", opening_balance: 1000, amount_invested: 500, closing_balance: 1500, fund: 'ABC liquid fund' },
    { transaction_date: "2021/12/20", opening_balance: 1500, amount_invested: 500, closing_balance: 2000, fund: 'ABC savings fund' },
    { transaction_date: "2022/01/04", opening_balance: 2000, amount_invested: 1000, closing_balance: 3000, fund: 'ABC savings fund' },
    { transaction_date: "2022/05/12", opening_balance: 3000, amount_invested: 1000, closing_balance: 4000, fund: 'ABC overnight fund' },
    { transaction_date: "2022/08/23", opening_balance: 4000, amount_invested: 500, closing_balance: 4500, fund: 'ABC liquid fund' },
    { transaction_date: "2023/01/06", opening_balance: 4500, amount_invested: 1500, closing_balance: 6000, fund: 'ABC overnight fund' },
    { transaction_date: "2023/03/29", opening_balance: 6000, amount_invested: 600, closing_balance: 6600, fund: 'ABC savings fund' },
    { transaction_date: "2023/07/12", opening_balance: 6600, amount_invested: 1000, closing_balance: 7600, fund: 'ABC liquid fund' },
    { transaction_date: "2023/10/04", opening_balance: 7600, amount_invested: 500, closing_balance: 8100, fund: 'ABC overnight fund' },
    { transaction_date: "2024/01/01", opening_balance: 8100, amount_invested: 900, closing_balance: 9000, fund: 'ABC savings fund' },
    { transaction_date: "2024/02/15", opening_balance: 9000, amount_invested: 1000, closing_balance: 10000, fund: 'ABC liquid fund' }
    ]
  
  res = trasaction_data.filter(t => Date.parse(t.transaction_date) >= Date.parse(start_date) && Date.parse(t.transaction_date) <= Date.parse(end_date))
  console.log(" transaction data : ",res);
  if (res === undefined || res.length === 0) {
    agent.add('No Data Found');
  }
  else {
    let transaction_data = '';
    for (i = 0; i < res.length; i++) {
      transaction_data += 'Opening Balance : ' + res[i].opening_balance + '\n' + res[i].amount_invested + ' invested in ' + res[i].fund + ' on ' + res[i].transaction_date + '\n' + 'Closing Balance : ' + res[i].closing_balance + '\n\n'
    }
    agent.add(transaction_data);
  }
  agent.add('Do you want to invest more?');
  agent.add(new Suggestion('Yes'));
  agent.add(new Suggestion('No'));
}

function show_transaction_yes(agent) {
  console.log('show transaction yes intent called');
  agent.add('moving to fund explorer intent');
  agent.setFollowupEvent('fundexplorer');
}

function show_transaction_no(agent) {
  console.log('show transaction no intent called');
  agent.add('moving to thankyou intent');
  agent.setFollowupEvent('thankyou');
}

module.exports = { show_transaction, show_transaction_yes, show_transaction_no };

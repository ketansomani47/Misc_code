const { Suggestion } = require('dialogflow-fulfillment')
const date_format = require('./date.js');

function transaction_history(agent) {
  service_context_params = agent.context.get('services')['parameters'];
  service_context_params['use_case'] = 'Transaction History';
  agent.context.set('services', 20, service_context_params);
  console.log(agent.parameters.date);
  if (agent.parameters.date === undefined || agent.parameters.date.length === 0) {
    agent.add('Please provide a time period');
    agent.add(new Suggestion('Current Financial Year'));
    agent.add(new Suggestion('Last Financial Year'));
    agent.add(new Suggestion('Enter Custom Dates'));
  }
  else {
    console.log("both date got : ", agent.parameters.date);
    let start_date = new Date(agent.parameters.date[0]);
    let end_date = new Date(agent.parameters.date[1]);
    let current_date = new Date();
    console.log(start_date, end_date, current_date);
    if (start_date <= end_date && start_date <= current_date && end_date <= current_date) {
      var date = [start_date.toLocaleDateString(), end_date.toLocaleDateString()];
      console.log(`showing list of transactions from ${start_date} to ${end_date}`);
      agent.add('showing list of transactions');
      transaction_context_params = agent.context.get('transactionhistory')['parameters'];
      transaction_context_params['date'] = date;
      agent.context.set('transactionhistory', 20, transaction_context_params);
      agent.setFollowupEvent('showtransaction');
    }
    else {
      console.log('invalid date provided');
      agent.add('invalid date provided');
      agent.setFollowupEvent('transaction');
    }
  }
}

function transaction_history_inputdate(agent) {
  console.log('input date intent called');
  console.log(agent.parameters);
  if (agent.parameters.timePeriod == '') {
    agent.add('Please provide a time period');
    agent.add(new Suggestion('Current Financial Year'));
    agent.add(new Suggestion('Last Financial Year'));
    agent.add(new Suggestion('Enter Custom Dates'));
  }
  else if (agent.parameters.timePeriod.toLowerCase() == 'current financial year') {
    var current_year = new Date().getFullYear();
    if (new Date().getMonth() <= 3) {
      var start_date = new Date(current_year - 1, 3, 1).toLocaleDateString();
    }
    else {
      var start_date = new Date(current_year, 3, 1).toLocaleDateString();
    }
    var end_date = new Date().toLocaleDateString();
    var date = [start_date, end_date];
    console.log(date);
    agent.add('show list of transactions');
    transaction_context_params = agent.context.get('transactionhistory')['parameters'];
    transaction_context_params['date'] = date;
    agent.context.set('transactionhistory', 20, transaction_context_params);
    agent.setFollowupEvent('showtransaction');
  }
  else if (agent.parameters.timePeriod.toLowerCase() == 'last financial year') {
    var last_year = new Date().getFullYear() - 1;
    if (new Date().getMonth() <= 3) {
      console.log("lte 3");
      var start_date = new Date(last_year - 1, 3, 1).toLocaleDateString();
      var end_date = new Date(last_year, 2, 31).toLocaleDateString();
    }
    else {
      console.log("else lte 3");
      var start_date = new Date(last_year, 3, 1).toLocaleDateString();
      var end_date = new Date(last_year + 1, 2, 31).toLocaleDateString();
    }
    var date = [start_date, end_date];
    console.log("date : ", date);
    agent.add('show list of transactions');
    transaction_context_params = agent.context.get('transactionhistory')['parameters'];
    transaction_context_params['date'] = date;
    agent.context.set('transactionhistory', 20, transaction_context_params);
    agent.setFollowupEvent('showtransaction');
  }
  else {
    agent.add('moving to transaction history intent');
    agent.setFollowupEvent('customdate');
  }
}

function transaction_history_customdate(agent) {
  console.log("custom date intent called")
  if (agent.parameters.start_date == '') {
    agent.add('Please enter start date ');
  }
  else {
    const date_regex = new RegExp('^((((0[1-9]|1[0-9]|2[0-9]|3[01]))[/-](0[13578]|1[02])|((0[1-9]|1[0-9]|2[0-9]|3[0])[/-](0[469]|11))|((0[1-9]|1[0-9]|2[0-8])([/-])(02)))[/-](19([6-9][0-9])|20([0-9][0-9])))|((29)[/-](02)[/-](19(6[048]|7[26]|8[048]|9[26])|20(0[048]|1[26]|2[048])))');
    console.log("start date : ", agent.parameters.start_date);
    const start_date_str = new Date(agent.parameters.start_date).toLocaleDateString();
    console.log('start date str : ', start_date_str);
    const start_date = date_format(start_date_str);
    console.log("converted start date : ", start_date);
    console.log("matching : ", date_regex.test(start_date))
    if (!date_regex.test(start_date)) {
      console.log('regex failed');
      agent.add('start date provided in invalid format');
      agent.setFollowupEvent('transaction');
    }
    if (agent.parameters.end_date == '') {
      agent.add('Please enter end date ');
    }
    else {
      console.log("end date : ", agent.parameters.end_date);
      const end_date_str = new Date(agent.parameters.end_date).toLocaleDateString();
      console.log('end date str : ', end_date_str);
      const end_date = date_format(end_date_str);
      console.log("converted end date : ", end_date);
      if (!date_regex.test(end_date)) {
        agent.add('end date provided in invalid format');
        agent.setFollowupEvent('transaction');
      }
      let date = [date_format(start_date_str,1), date_format(end_date_str,1)]
      console.log(date);
      agent.add('moving to transaction history intent');
      agent.setFollowupEvent({ "name": "transaction", "parameters": { "date": date } });
    }
  }
}

module.exports = { transaction_history, transaction_history_customdate, transaction_history_inputdate };

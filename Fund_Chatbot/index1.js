const express = require('express')
const { WebhookClient, Suggestion } = require('dialogflow-fulfillment')
const app = express()

app.get('/', (req, res) => res.send('online'))
app.post('/dialogflow', express.json(), (req, res) => {
  const agent = new WebhookClient({ request: req, response: res })

  function welcome (agent) {
    console.log('********welcome*********');
    if (agent.parameters.service_name==''){
    agent.add('Hi Welcome to ABC mutual fund services. you can ask about');
    agent.add(new Suggestion('Portfolio Valuation'));
    agent.add(new Suggestion(`Fund Explorer`));
    agent.add(new Suggestion(`Transaction History`));
    }
    else{
      let service_name = agent.parameters.service_name;
      console.log('******'+service_name+'*********');
      context_params = agent.context.get('services')['parameters'];
      context_params['service_name'] = service_name;
      agent.context.set('services',20,context_params);
      if (['Portfolio Valuation','Transaction History'].includes(service_name)){
        agent.add('redirecting to phone number');
        agent.setFollowupEvent('phonenumber');
      }
      else{
        agent.add('redirecting to fund explorer');
        agent.setFollowupEvent('fundexplorer');
      }
    }
  }

  function phone_number(agent){
    const mobile_regex = new RegExp('^([0|\+[0-9]{1,5})?([7-9][0-9]{9})$');
    console.log(agent.parameters);
    if (!mobile_regex.test(agent.parameters.mobile_number)){
        agent.add('Please enter your registered mobile number');
        agent.setFollowupEvent({"name":'phonenumber'});
    }
    else{
      console.log(agent.parameters);
      service_context = agent.context.get('services');
      if (service_context['parameters']['service_name']=='Portfolio Valuation'){
        agent.add('redirect to portfolio intent');
        agent.setFollowupEvent('portfolio');
      }
      else if (service_context['parameters']['service_name']=='Transaction History'){
        agent.add('redirect to transaction history intent');
        agent.setFollowupEvent('transaction');
      }
      else if (service_context['parameters']['service_name']=='Fund Explorer'){
        agent.add('redirect to thankyou intent');
        agent.setFollowupEvent('thankyou');
      }
      else{
        agent.add('redirect to fallback intent');
        agent.setFollowupEvent('fallback');
      }
    }
  }

  function portfolio_valuation(agent) {
    service_context_params = agent.context.get('services')['parameters'];
    service_context_params['service_name'] = 'Portfolio Valuation';
    agent.context.set('services',20,service_context_params);
    console.log(agent.parameters);
    console.log('*********portfolio intent**************');
    const folio = ['PAN_123','PAN_234'];
    if (!(folio.includes(agent.parameters.folio_name))){
      console.log(agent.parameters.folio_name);
      agent.add('Please select your folio');
      agent.add(new Suggestion(folio[0]));
      agent.add(new Suggestion(folio[1]));
    }
    else{
      console.log(agent.parameters.folio_name);
      agent.add('Your folio ' + agent.parameters.folio_name + ' , Valuation 130000 on ' + new Date().toDateString());
    }
  }
    function transaction_history(agent) {
      service_context_params = agent.context.get('services')['parameters'];
      service_context_params['service_name'] = 'Transaction History';
      agent.context.set('services',20,service_context_params);
      console.log(agent.parameters.date);
      if (agent.parameters.date===undefined || agent.parameters.date.length===0){
        agent.add('Please provide a time period');
        agent.add(new Suggestion('Current Financial Year'));
        agent.add(new Suggestion('Last Financial Year'));
        agent.add(new Suggestion('enter dates'));
      }
      else{
        let start_date = new Date(agent.parameters.date[0]);
        let end_date = new Date(agent.parameters.date[1]);
        let current_date = new Date();
        if (start_date<=end_date && start_date<=current_date && end_date<=current_date){
          var date = [start_date.toLocaleDateString(), end_date.toLocaleDateString()];
          console.log(`show list of transactions from ${start_date} to ${end_date}`);
          agent.add('show list of transactions');
          transaction_context_params = agent.context.get('transactionhistory')['parameters'];
          transaction_context_params['date'] = date;
          agent.context.set('transactionhistory',20,transaction_context_params);
          agent.setFollowupEvent('showtransaction');
        }
        else{
          console.log('invalid date provided');
          agent.add('invalid date provided');
          agent.setFollowupEvent('transaction');
        }
      }
 }

 function transaction_history_inputdate(agent){
  console.log('**********input date intent************');
  console.log(agent.parameters);
  if (agent.parameters.timePeriod==''){
    agent.add('Please provide a time period');
    agent.add(new Suggestion('Current Financial Year'));
    agent.add(new Suggestion('Last Financial Year'));
    agent.add(new Suggestion('enter dates'));
  }
  else if (agent.parameters.timePeriod.toLowerCase()=='current financial year'){
    var current_year = new Date().getFullYear();
    if (new Date().getMonth()<=3){
      var start_date = new Date(current_year-1,3,1).toLocaleDateString();
    }
    else{
      var start_date = new Date(current_year,3,1).toLocaleDateString();
    }
    var end_date = new Date().toLocaleDateString();
    var date = [start_date, end_date];
    console.log(date);
    agent.add('show list of transactions');
    transaction_context_params = agent.context.get('transactionhistory')['parameters'];
    transaction_context_params['date'] = date;
    agent.context.set('transactionhistory',20,transaction_context_params);
    agent.setFollowupEvent('showtransaction');
  }
  else if (agent.parameters.timePeriod.toLowerCase()=='last financial year'){
    var last_year = new Date().getFullYear()-1;
    if (new Date().getMonth()<=3){
      var start_date = new Date(last_year-1,3,1).toLocaleDateString();
      var end_date = new Date(last_year,2,31).toLocaleDateString();
    }
    else{
      var start_date = new Date(last_year,3,1).toLocaleDateString();
      var end_date = new Date(last_year+1,2,31).toLocaleDateString();
    }
    var date = [start_date, end_date];
    agent.add('show list of transactions');
    transaction_context_params = agent.context.get('transactionhistory')['parameters'];
    transaction_context_params['date'] = date;
    agent.context.set('transactionhistory',20,transaction_context_params);
    agent.setFollowupEvent('showtransaction');
  }
  else{
    agent.add('redirecting to transaction history intent');
    agent.setFollowupEvent('customdate');
  }
 }

 function transaction_history_customdate(agent){
  console.log("********custom date intent*********")
  if (agent.parameters.start_date==''){
    agent.add('Please enter start date');
 }
 else{
  if (agent.parameters.end_date==''){
    agent.add('Please enter end date');
  }
  else{
    let date = [agent.parameters.start_date, agent.parameters.end_date]
    console.log(date);
    agent.add('redirecting to transaction history intent');
    agent.setFollowupEvent({"name":"transaction","parameters":{"date":date}});
  }
 }
}

 function show_transaction(agent){
  console.log('********show transaction***********');
  let date = agent.context.get('transactionhistory')['parameters']['date'];
  console.log(date);
  let [day, month, year] = date[0].split("/");
  if (month<=9){
    month = `0${month}`
  }
  if (day<=9){
    day = `0${day}`
  }
  let start_date = `${year}/${month}/${day}`;
  [day, month, year] = date[1].split("/");
  if (month<=9){
    month = `0${month}`
  }
  if (day<=9){
    day = `0${day}`
  }
  let end_date = `${year}/${month}/${day}`;
  agent.add(`Transaction list from ${start_date} to ${end_date}`);
  trasaction_data=[{transaction_date:"2021/10/25",opening_balance:10000,amount_invested:1000,closing_balance:11000,fund:'ABC overnight fund'},
  {transaction_date:"2021/12/23",opening_balance:11000,amount_invested:500,closing_balance:11500,fund:'ABC liquid fund'},
  {transaction_date:"2022/04/16",opening_balance:11500,amount_invested:1000,closing_balance:12500,fund:'ABC savings fund'},
  {transaction_date:"2022/07/10",opening_balance:12500,amount_invested:1000,closing_balance:13500,fund:'ABC overnight fund'},
  {transaction_date:"2022/08/15",opening_balance:13500,amount_invested:500,closing_balance:14000,fund:'ABC savings fund'},
  {transaction_date:"2023/05/20",opening_balance:14000,amount_invested:700,closing_balance:14700,fund:'ABC overnight fund'},
  {transaction_date:"2023/09/17",opening_balance:14700,amount_invested:800,closing_balance:15500,fund:'ABC savings fund'},
  {transaction_date:"2023/11/18",opening_balance:15500,amount_invested:1000,closing_balance:16500,fund:'ABC liquid fund'},
  {transaction_date:"2023/12/05",opening_balance:16500,amount_invested:1000,closing_balance:17500,fund:'ABC savings fund'},
  {transaction_date:"2024/01/23",opening_balance:17500,amount_invested:500,closing_balance:18000,fund:'ABC overnight fund'},
  {transaction_date:"2024/02/12",opening_balance:18000,amount_invested:1000,closing_balance:19000,fund:'ABC liquid fund'}
  ]
  res=trasaction_data.filter(t => t.transaction_date >= start_date && t.transaction_date <= end_date)
  console.log(res);
  if (res===undefined || res.length===0){
    agent.add('No Data Found');
  }
  else{
    let response_data = '';
    for (i=0; i<res.length; i++){
      response_data += 'Invested '+res[i].amount_invested+' in '+res[i].fund+' on '+res[i].transaction_date+'\n'+'Opening Balance:'+res[i].opening_balance+' Closing Balance:'+res[i].closing_balance+'\n\n'
    }
    agent.add(response_data);
  }
  agent.add('Do you want to invest more?');
  agent.add(new Suggestion('Yes'));
  agent.add(new Suggestion('No'));
 }

 function show_transaction_yes(agent){
  console.log('*******show transaction yes*********');
  agent.add('redirect to fund explorer intent');
  agent.setFollowupEvent('fundexplorer');
 }

 function show_transaction_no(agent){
  console.log('*********show transaction no*********');
  agent.add('redirect to thankyou intent');
  agent.setFollowupEvent('thankyou');
 }

 function fund_explorer(agent){
  console.log("fund explorer intent");
  service_context_params = agent.context.get('services')['parameters'];
  service_context_params['service_name'] = 'Fund Explorer';
  agent.context.set('services',20,service_context_params);
  if (agent.parameters.fund_category==''){
    agent.add('Here are fund categories, you can select to view.')
    agent.add(new Suggestion('Equity'));
    agent.add(new Suggestion('Debt'));
    agent.add(new Suggestion('Hybrid'));
  }
  else{
    console.log('parameters:'+agent.parameters);
    if (agent.parameters.option_number==''){
      agent.add(`To select from the below option(s),\n Enter option number:\n Enter 1 - ABC overnight fund\n Enter 2 - ABC liquid fund \n Enter 3 - ABC savings fund`);
    }
    else{
    console.log('option number:'+agent.parameters.option_number);
    agent.add(agent.parameters.option_number+' details:\nThe investment objective of the scheme is to provide returns that closely correspond to the total returns of the securities as represented by the underlying index, subject to tracking error. More details: https://www.investopedia.com/terms/m/mutualfund.asp');
    agent.add(new Suggestion('Invest'));
    agent.add(new Suggestion('Main Menu'));
    }
  }
 }

 function fund_explorer_invest(agent){ 
  console.log("*******invest*******");
  servicescontext = agent.context.get('services');
  if (!('mobile_number' in servicescontext['parameters']) || servicescontext['parameters']['mobile_number']==''){
    agent.add('redirecting to portfolio intent');
    console.log('phone number not provided');
    agent.setFollowupEvent('phonenumber');
  }
  else{
    agent.add('redirecting to thankyou intent');
    console.log('phone number already provided');
    agent.setFollowupEvent('thankyou');
  }
 }

 function fund_explorer_mainmenu(agent){ 
  console.log("*******main menu*******");
  agent.add('redirecting to welcome intent');
  agent.setFollowupEvent('welcome');
 }

 function thankyou(agent){
  console.log('**************thankyou intent*************');
  agent.add('Thank you for using our services');
  agent.contexts = [];
 }

  let intentMap = new Map()
  intentMap.set('Default Welcome Intent', welcome);
  intentMap.set('PortfolioValuation', portfolio_valuation);
  intentMap.set('TransactionHistory', transaction_history);
  intentMap.set('FundExplorer', fund_explorer);
  intentMap.set('FundExplorer - invest', fund_explorer_invest);
  intentMap.set('FundExplorer - mainmenu', fund_explorer_mainmenu);
  intentMap.set('Thankyou', thankyou);
  intentMap.set('PhoneNumber', phone_number);
  intentMap.set('TransactionHistory - inputdate', transaction_history_inputdate);
  intentMap.set('ShowTransaction', show_transaction);
  intentMap.set('ShowTransaction - yes', show_transaction_yes);
  intentMap.set('ShowTransaction - no', show_transaction_no);
  intentMap.set('TransactionHistory - customdate', transaction_history_customdate);
  agent.handleRequest(intentMap)
})

app.listen(process.env.PORT || 8080)
const express = require('express')
const { WebhookClient } = require('dialogflow-fulfillment')
const welcome = require('./welcome.js')
const fund = require('./fund_explorer.js')
const phone_number = require('./phone_number.js')
const portfolio = require('./portfolio.js')
const thank_you = require('./thank_you.js')
const transaction = require('./transaction_history.js')
const details = require('./show_transaction.js')
const app = express()

app.get('/', (req, res) => res.send('server running on port 8080'))
app.post('/dialogflow', express.json(), (req, res) => {
  const agent = new WebhookClient({ request: req, response: res })

  let intentMap = new Map();
  intentMap.set('Default Welcome Intent', welcome);
  intentMap.set('fund_explorer', fund.fund_explorer);
  intentMap.set('fund_explorer - invest', fund.invest);
  intentMap.set('fund_explorer - main_menu', fund.main_menu);
  intentMap.set('phone_number', phone_number);
  intentMap.set('portfolio', portfolio);
  intentMap.set('show_transaction', details.show_transaction);
  intentMap.set('show_transaction - yes', details.show_transaction_yes);
  intentMap.set('show_transaction - no', details.show_transaction_no);
  intentMap.set('transaction_history', transaction.transaction_history);
  intentMap.set('transaction_history - custom_date', transaction.transaction_history_customdate);
  intentMap.set('transaction_history - input_date', transaction.transaction_history_inputdate);
  intentMap.set('thank_you', thank_you);
  agent.handleRequest(intentMap)
})

app.listen(process.env.PORT || 8080)
const { Suggestion } = require('dialogflow-fulfillment')

module.exports = function welcome(agent) {
  console.log('welcome intent called');
  if (agent.parameters.use_case == '') {
    agent.add('hi, Welcome to ABC mutual fund services. you can ask about :');
    agent.add(new Suggestion('Portfolio Valuation'));
    agent.add(new Suggestion('Fund Explorer'));
    agent.add(new Suggestion('Transaction History'));
  }
  else {
    let use_case = agent.parameters.use_case;
    console.log('$$$$$$$$$$$$$$' + use_case + '$$$$$$$$$$');
    context_params = agent.context.get('services')['parameters'];
    console.log(context_params);
    context_params['use_case'] = use_case;
    console.log(context_params);
    agent.context.set('services', 20, context_params);
    if (['Portfolio Valuation', 'Transaction History'].includes(use_case)) {
      agent.add('moving to phone number');
      agent.setFollowupEvent('phonenumber');
    }
    else {
      console.log("fund explorer case");
      agent.add('moving to fund explorer');
      agent.setFollowupEvent('fundexplorer');
    }
  }
} 
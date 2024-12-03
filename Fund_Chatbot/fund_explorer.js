const { Suggestion } = require('dialogflow-fulfillment')

function fund_explorer(agent) {
  console.log("fund explorer intent");
  service_context_params = agent.context.get('services')['parameters'];
  console.log(service_context_params);
  service_context_params['use_case'] = 'Fund Explorer';
  console.log(service_context_params);
  agent.context.set('services', 20, service_context_params);
  if (agent.parameters.fund_category == '') {
    agent.add('Here are fund categories, you can select to view.')
    agent.add(new Suggestion('Equity'));
    agent.add(new Suggestion('Debt'));
    agent.add(new Suggestion('Hybrid'));
  }
  else {
    console.log('parameters:' + agent.parameters);
    if (agent.parameters.option_number == '') {
      agent.add(`To select from the below option(s),\n Enter option number:\n Enter 1 - ABC overnight fund\n Enter 2 - ABC liquid fund \n Enter 3 - ABC savings fund`);
    }
    else {
      console.log('option number:' + agent.parameters.option_number);
      agent.add(agent.parameters.option_number + ' details :\nThe investment objective of the scheme is to provide returns that closely correspond to the total returns of the securities as represented by the underlying index, subject to tracking error. More details: https://www.amfiindia.com/investor-corner/knowledge-center/what-are-mutual-funds-new.html');
      agent.add(new Suggestion('Invest'));
      agent.add(new Suggestion('Main Menu'));
    }
  }
}

function invest(agent) {
  console.log("invest intent called");
  servicescontext = agent.context.get('services');
  if (!('mobile_number' in servicescontext['parameters']) || servicescontext['parameters']['mobile_number'] == '') {
    agent.add('moving to portfolio intent');
    console.log('phone number not provided');
    agent.setFollowupEvent('phonenumber');
  }
  else {
    agent.add('moving to thankyou intent');
    console.log('phone number already provided');
    agent.setFollowupEvent('thankyou');
  }
}

function main_menu(agent) {
  console.log("main menu intent called");
  agent.add('moving to welcome intent');
  agent.setFollowupEvent('welcome');
}

module.exports = { fund_explorer, invest, main_menu };

const { Suggestion } = require('dialogflow-fulfillment')

module.exports = function portfolio_valuation(agent) {
  service_context_params = agent.context.get('services')['parameters'];
  service_context_params['use_case'] = 'Portfolio Valuation';
  agent.context.set('services', 20, service_context_params);
  console.log('portfolio intent called');
  const folio_list = ['PAN_123', 'PAN_234'];
  if (!(folio_list.includes(agent.parameters.folio_name))) {
    console.log(agent.parameters.folio_name);
    agent.add('Please select your folio');
    agent.add(new Suggestion(folio_list[0]));
    agent.add(new Suggestion(folio_list[1]));
  }
  else {
    console.log(agent.parameters.folio_name);
    agent.add('Your folio ' + agent.parameters.folio_name + ' , Valuation 130000 on ' + new Date().toDateString());
    agent.contexts = [];
    console.log(agent.contexts);
  }
}
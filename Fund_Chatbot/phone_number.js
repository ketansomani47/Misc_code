module.exports = function phone_number(agent) {
  const mobile_regex = new RegExp('^([0|\+[0-9]{1,5})?([7-9][0-9]{9})$');
  console.log(agent.parameters);
  if (!mobile_regex.test(agent.parameters.mobile_number)) {
    agent.add('Please enter your registered mobile number');
    agent.setFollowupEvent('phonenumber');
  }
  else {
    console.log(agent.parameters);
    service_context = agent.context.get('services');
    if (service_context['parameters']['use_case'] == 'Portfolio Valuation') {
      agent.add('moving to portfolio intent');
      agent.setFollowupEvent('portfolio');
    }
    else if (service_context['parameters']['use_case'] == 'Transaction History') {
      agent.add('moving to transaction history intent');
      agent.setFollowupEvent('transaction');
    }
    else if (service_context['parameters']['use_case'] == 'Fund Explorer') {
      agent.add('moving to thankyou intent');
      agent.setFollowupEvent('thankyou');
    }
    else {
      agent.add('moving to fallback intent');
      agent.setFollowupEvent('fallback');
    }
  }
}
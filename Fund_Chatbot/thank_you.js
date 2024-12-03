module.exports = function thank_you(agent) {
    console.log('thankyou intent called');
    agent.add('Thank you for using our services.');
    agent.contexts = [];
}

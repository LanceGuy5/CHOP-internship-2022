// Exports is a class to store confidential data
const EXPORTS = require('./exports.js');
const { Configuration, OpenAIApi } = require("openai");
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

const configuration = new Configuration({
    apiKey: EXPORTS.OPENAI_SECRET_KEY,
});
const openai = new OpenAIApi(configuration);

// while(true){
    readline.question(`eng2cyph-cfdikg:>`, async search => {
        // if(search.toLowerCase() === 'exit') readline.close(); break;
        let prompt = search + '\n';
        const response = await openai.createCompletion({
            model: "davinci:ft-personal:eng-2-cyph-proto1-2022-09-04-12-25-03",
            prompt: prompt,
            temperature: 0.2,
            max_tokens: 200,
            top_p: 1,
            frequency_penalty: 0.5,
            presence_penalty: 0,
            best_of: 1,
            stop: ["###"],
        });
        console.log(response.data.choices[0].text);
    });
// }
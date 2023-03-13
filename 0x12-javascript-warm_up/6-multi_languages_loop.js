#!/usr/bin/node
const language1 = 'C is fun';
const language2 = 'Python is cool';
const language3 = 'JavaScript is amazing';
const languages = [language1, language2, language3];
for (language in languages) {
  console.log(languages[language]);
}

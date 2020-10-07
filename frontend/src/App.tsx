import React from 'react';
import './App.css';
import HomePage from "./components/HomePage"


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Welcome to the Anagram Checker!
        </h1>
        <h4>
          Created for the Arctic Wolf Take Home Test
        </h4>
      </header>
      <div className="Definition">
        <p><b>Definition:</b> Two words are anagrams if you can rearange the letters of one word to get the second word. 
        For example "wolf" and "flow". Anagrams ignore all spaces, punctuation and capitalization, so "Dormitory" and 
        "dirty Room!" are also anagrams.</p>
      </div>
      <HomePage></HomePage>
    </div>
  );
}

export default App;

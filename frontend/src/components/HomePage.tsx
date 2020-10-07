import React, { useState } from 'react';
import axios from 'axios'

import {IFormPair, ITablePair} from '../types/interfaces'
import Checker from './Checker'
import TopSearched from './TopSearched'

const URL = "http://localhost:5000/anagram"

const HomePage = () => {
    const [isLoading, setLoading] = useState(false);
    const [isSubmitted, setSubmitted] = useState(false);
    const [isAnagram, setAnagram] = useState(false);
    const [anagramList, setAnagramList] = useState<ITablePair[]>([]);
    
    const onSubmit = (data: IFormPair) => {
        setLoading(true)
        var bodyFormData = new FormData();
        bodyFormData.append("word1", data.word1);
        bodyFormData.append("word2", data.word2);
        axios.post(URL, bodyFormData, {headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }})
        .then(response => {
            setAnagram(response.data.isAnagram);
            setLoading(false);
            setSubmitted(true);
            getData()
        });
      };

      const getData = async () => {
        const response = await axios.get(URL);
        setAnagramList(response.data);
    }

    const formProp = {
        isLoading: isLoading,
        isSubmitted: isSubmitted,
        isAnagram: isAnagram,
        onSubmit: onSubmit,
    }

    const topSearchedProp = {
        anagramList: anagramList
    }

    return (
        <div>
            <Checker {...formProp}></Checker>
            <br></br>
            <TopSearched {...topSearchedProp}></TopSearched>
        </div>
        
    );
}

export default HomePage;
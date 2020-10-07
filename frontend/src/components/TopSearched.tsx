import React from 'react'

import Table from 'react-bootstrap/Table'

import "./TopSearched.css"
import {ITablePair, ITableProp} from '../types/interfaces'

const TopSearched = (prop: ITableProp) => {

    const renderTableData = () => {
        if(prop.anagramList.length > 0){
            return prop.anagramList.map((anagram: ITablePair, index: number) => {
                const {words, frequency} = anagram
                return (
                    <tr key={index} data-testid="table-row">
                        <td>{index+1}</td>
                        <td>{words[0]}</td>
                        <td>{words[1]}</td>
                        <td>{frequency}</td>
                    </tr>
                )
            });
        }else{
            return (
                <tr data-testid="table-row">
                    <td className="NoAnagrams" colSpan={4}>No anagrams have been submitted.</td>
                </tr>
            )
        }
        
    }
    
    return (
        <Table striped bordered hover className='table-padding'>
            <thead>
                <tr>
                    <th></th>
                    <th colSpan={2}>
                    Most Popular Anagram Requests
                    </th>
                    <th>Frequency</th>
                </tr>
            </thead>
            <tbody>
                {renderTableData()}
            </tbody>
        </Table>
    )

}

export default TopSearched
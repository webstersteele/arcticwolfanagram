import React from 'react'
import { useForm } from "react-hook-form";

import Card from 'react-bootstrap/Card'
import Form from 'react-bootstrap/Form'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button'

import "./Checker.css"
import {IFormPair, IFormProp} from '../types/interfaces'

const Checker = (prop: IFormProp) => {

    const { register, handleSubmit, errors } = useForm<IFormPair>();

    return (
        <div>
        <Card className='text-center card-padding'>
          <Card.Body>
            <Form onSubmit={handleSubmit(prop.onSubmit)}>
                <Row>
                    <Form.Group as={Col} controlId="formGridText">
                        <Form.Label>Word 1</Form.Label>
                        <Form.Control 
                        type="text" 
                        name="word1" 
                        ref={register({required: true})} 
                        placeholder="wolf" 
                        disabled={prop.isLoading}
                        data-testid="formInput1"/>

                        {errors.word1 && errors.word1.type === "required" && (
                        <div className="error">Your must enter a word.</div>
                        )}

                    </Form.Group>

                    <Form.Group as={Col} controlId="formGridText">
                        <Form.Label>Word 2</Form.Label>
                        <Form.Control 
                        type="text" 
                        name="word2" 
                        ref={register({required: true})} 
                        placeholder="flow" 
                        disabled={prop.isLoading}
                        data-testid="formInput2"/>

                        {errors.word2 && errors.word2.type === "required" && (
                        <div className="error">Your must enter a word.</div>
                        )}

                    </Form.Group>
                </Row>

                <Row>
                    <Button 
                    className="submit-center" 
                    variant="primary" 
                    type="submit" 
                    disabled={prop.isLoading} 
                    >
                         {prop.isLoading ? 'Loading…' : 'Submit'}
                    </Button>
                </Row>

                {prop.isSubmitted && prop.isAnagram && !prop.isLoading && 
                    <div className="Yes">
                        <h1>YES</h1>
                        <h5>Word1 and Word2 are anagrams</h5>
                    </div>
                }
                
                {prop.isSubmitted && !prop.isAnagram && !prop.isLoading && 
                    <div className="No">
                        <h1>NO</h1>
                        <h5>Word1 and Word2 are not anagrams</h5>
                    </div>
                }

            </Form>
          </Card.Body>
        </Card>
      </div>);
}

export default Checker
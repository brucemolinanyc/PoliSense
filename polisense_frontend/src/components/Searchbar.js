import React from 'react';
import { InputGroup, Input } from 'reactstrap';
import Card from './Card'

export default class SearchBar extends React.Component{
    state = {
       articles: [],
       author: '',
       base:'',
       headline:'',
       sentiment: [],
       result: []
    }

    onChange = (e) => {
        this.setState({
            author: '',
        })

        const text = e.target.value
        let results = Object.values(this.state.articles)
        
        let result = results.find((obj) => obj.keywords.includes(text))

        if (result){
            this.setState({
                author: result.author,
                base:result.base,
                headline:result.headline,
                sentiment: result.sentiment,
                result: result,
                text_test: ''
            })
        }
    }

    componentDidMount = () => {
        fetch('/breitbart.json')
          .then(response => response.json())
          .then(json => this.setState({articles: json}))
    }

    fetchData = () => {
        fetch('http://localhost:5000/pull_txt/test.txt', {mode: 'cors'})
        .then(result => result.text())
        .then(data => this.setState({text_test: data}))
    }

    render(){
      
        return(
            <div>
                <InputGroup  xs="6" className="input">
                    <Input  onChange={this.onChange} placeholder="Enter your search" />
                </InputGroup>
                <div>  
                    {this.state.author && <Card data={this.state.result} sentiment={this.state.sentiment}/> }
                </div>

            </div>
        )
    }

}




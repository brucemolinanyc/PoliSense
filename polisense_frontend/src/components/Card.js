import React from 'react'

const Card = (props) => (
    <div className="card">
        <h3>{props.data.author}</h3>
        <a href={`http://${props.data.base}`} target="_blank" >{props.data.base}</a>
        <br></br>
        <p>{props.data.headline}</p>
        <p className="neg">Negative sentiment score: {props.sentiment.neg}</p>
        <p className="neu">Neutral sentiment score: {props.sentiment.neu}</p>
        <p className="pos">Postive sentiment score: {props.sentiment.pos}</p>
        <p className="comp">Compound sentiment score: {props.sentiment.compound}</p>

    </div>
)

export default Card;

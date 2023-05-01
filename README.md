# Xsolla Assessment Book ChatGPT3 / Langchain Summarizer Python Flask Server

### Explanation of the assessment

https://docs.google.com/document/d/1fEBbYPMTkM7mtw22CLjE0cZBTGoDo3bA0sqQp3bW5Y8/edit?usp=sharing

### Live Version

http://exilzety.pythonanywhere.com/

### Usage

To call the endpoints, you can use postman export included in the repository

#### Dev

##### xsolla.postman_collection.json 

#### Production

##### xsolla-prod.postman_collection.json 

### Installation
1. Navigate to the root directory and run  ```pip install -r requirements.txt```

2. Create .env file to set the OPENAI_API_KEY environment variabke in the root folder and modify it as such to use your own api key

```cmd
OPENAI_API_KEY=<PUT YOUR API KEY HERE>
```
![image](https://user-images.githubusercontent.com/48543482/235380019-09ab0d93-2f80-43cd-a15f-dd00902f4575.png)

3. In the root directory, run ```python app.py```

4. The server should then be up

### Available endpoints

#### Create a book record 

**POST** /api/books

Request
```json
{
    "title": "the-little-mermaid",
    "content": "The Little Mermaid becomes melancholy and asks her grandmother if humans can live forever. Her grandmother explains that humans have a much shorter lifespan than mermaids (300 years), but that they have an eternal soul that lives on in heaven, while mermaids turn to sea foam at death and cease to exist.The Little Mermaid, longing for the prince and an eternal soul, visits the Sea Witch who lives in a dangerous part of the ocean. The witch willingly helps her by selling her a potion that gives her legs in exchange for her voice (her tongue), as the Little Mermaid has the most enchanting voice in the entire world. The witch warns the Little Mermaid that once she becomes a human, she will never be able to return to the sea. Consuming the potion will make her feel as if a sword is being passed through her body. When she recovers, she will have two human legs and will be able to dance like no human has ever danced before; however, she will constantly feel as if she is walking on sharp knives. Moreover, she will obtain a soul only if she wins the love of the prince and marries him, for then a part of his soul will flow into her. Otherwise, at dawn on the first day after he marries someone else, the Little Mermaid will die with a broken heart and dissolve into sea foam upon the waves.After she agrees to the arrangement, the Little Mermaid swims up to the surface near the prince's castle and drinks the potion. The liquid feels like a sword piercing her body and she passes out on the shore, naked. She is found by the prince, who is mesmerized by her beauty and grace, even though he discovers that she is mute. Most of all, he likes to see her dance, and she dances for him despite suffering excruciating pain with every step. Soon, the Little Mermaid becomes the prince's favorite companion and accompanies him on many of his outings—but he does not fall in love with her at all. "
}
```

Response
```json
{
    "id": 1,
    "message": "Book is created",
    "title": "the-little-mermaid"
}
```


#### Upload pdf book to create a book record

**POST** /api/books/upload

Request

form-data
```json
{
    "file": "alice-in-wonderland.pdf"
}
```

Response
```json
{
    "id": 2,
    "message": "Book is uploaded",
    "title": "alice-in-wonderland"
}
```


#### Get all book records

**GET** /api/books

Request

Response
```json
{
    "books": [
        {
            "content": "The Little Mermaid becomes melancholy and asks her grandmother if humans can live forever. Her grandmother explains that humans have a much shorter lifespan than mermaids (300 years), but that they have an eternal soul that lives on in heaven, while mermaids turn to sea foam at death and cease to exist.The Little Mermaid, longing for the prince and an eternal soul, visits the Sea Witch who lives in a dangerous part of the ocean. The witch willingly helps her by selling her a potion that gives her legs in exchange for her voice (her tongue), as the Little Mermaid has the most enchanting voice in the entire world. The witch warns the Little Mermaid that once she becomes a human, she will never be able to return to the sea. Consuming the potion will make her feel as if a sword is being passed through her body. When she recovers, she will have two human legs and will be able to dance like no human has ever danced before; however, she will constantly feel as if she is walking on sharp knives. Moreover, she will obtain a soul only if she wins the love of the prince and marries him, for then a part of his soul will flow into her. Otherwise, at dawn on the first day after he marries someone else, the Little Mermaid will die with a broken heart and dissolve into sea foam upon the waves.After she agrees to the arrangement, the Little Mermaid swims up to the surface near the prince's castle and drinks the potion. The liquid feels like a sword piercing her body and she passes out on the shore, naked. She is found by the prince, who is mesmerized by her beauty and grace, even though he discovers that she is mute. Most of all, he likes to see her dance, and she dances for him despite suffering excruciating pain with every step. Soon, the Little Mermaid becomes the prince's favorite companion and accompanies him on many of his outings—but he does not fall in love with her at all. ",
            "id": 1,
            "summary": null,
            "title": "the-little-mermaid",
            "type": "json"
        },
        {
            "content": null,
            "id": 2,
            "summary": null,
            "title": "alice-in-wonderland",
            "type": "pdf"
        }
    ]
}
```


#### Get specific book record

**GET** /api/books?title=the-little-mermaid

Response
```json
{
    "content": "The Little Mermaid becomes melancholy and asks her grandmother if humans can live forever. Her grandmother explains that humans have a much shorter lifespan than mermaids (300 years), but that they have an eternal soul that lives on in heaven, while mermaids turn to sea foam at death and cease to exist.The Little Mermaid, longing for the prince and an eternal soul, visits the Sea Witch who lives in a dangerous part of the ocean. The witch willingly helps her by selling her a potion that gives her legs in exchange for her voice (her tongue), as the Little Mermaid has the most enchanting voice in the entire world. The witch warns the Little Mermaid that once she becomes a human, she will never be able to return to the sea. Consuming the potion will make her feel as if a sword is being passed through her body. When she recovers, she will have two human legs and will be able to dance like no human has ever danced before; however, she will constantly feel as if she is walking on sharp knives. Moreover, she will obtain a soul only if she wins the love of the prince and marries him, for then a part of his soul will flow into her. Otherwise, at dawn on the first day after he marries someone else, the Little Mermaid will die with a broken heart and dissolve into sea foam upon the waves.After she agrees to the arrangement, the Little Mermaid swims up to the surface near the prince's castle and drinks the potion. The liquid feels like a sword piercing her body and she passes out on the shore, naked. She is found by the prince, who is mesmerized by her beauty and grace, even though he discovers that she is mute. Most of all, he likes to see her dance, and she dances for him despite suffering excruciating pain with every step. Soon, the Little Mermaid becomes the prince's favorite companion and accompanies him on many of his outings—but he does not fall in love with her at all. ",
    "id": 1,
    "summary": "\"The Little Mermaid\" is the story of a mermaid who longs for an eternal soul and falls in love with a human prince. She visits a sea witch who gives her legs in exchange for her voice and warns her that she will feel like walking on knives, but she will have a chance for a soul if she wins the love of the prince and marries him. The Little Mermaid agrees to the deal and becomes human, catching the eye of the prince with her beauty and dance. Despite becoming his companion, the prince does not fall in love with her, and the Little Mermaid faces the threat of dissolving into sea foam if the prince marries another.",
    "title": "the-little-mermaid",
    "type": "json"
}
```


#### Generate summary for a specific book record based on the content or pdf file content

**POST** /api/books/summary

Generate book summary when content type is json type using ChatGPT3 model

Request
```json
{
    "title": "the-little-mermaid"
}
```

Response
```json
{
    "summary": "\"The Little Mermaid\" is the story of a mermaid who longs for an eternal soul and falls in love with a human prince. She visits a sea witch who gives her legs in exchange for her voice and warns her that she will feel like walking on knives, but she will have a chance for a soul if she wins the love of the prince and marries him. The Little Mermaid agrees to the deal and becomes human, catching the eye of the prince with her beauty and dance. Despite becoming his companion, the prince does not fall in love with her, and the Little Mermaid faces the threat of dissolving into sea foam if the prince marries another."
}
```

Generate book summary when content type is pdf using Langchain

Request
```json
{
    "title": "alice-in-wonderland"
}
```

Response
```json
{
    "summary": " Alice follows a White Rabbit down a deep well and finds herself in a hall with locked doors. She finds a tiny golden key that fits a small door leading to a beautiful garden, but she is too big to fit through. After drinking a bottle labeled \"DRINK ME\" and eating a cake labeled \"EAT ME\", Alice grows to nine feet tall and is unable to get into the garden. She meets a Mouse, the March Hare, and the Hatter, and they all swim to the shore together. Alice finds a door leading to a tree and unlocks it with a golden key, shrinking to a foot high and entering a beautiful garden."
}
```


#### Get all book summaries

**GET** /api/books/summary

Response
```json
{
    "books": [
        {
            "summary": "\"The Little Mermaid\" is the story of a mermaid who longs for an eternal soul and falls in love with a human prince. She visits a sea witch who gives her legs in exchange for her voice and warns her that she will feel like walking on knives, but she will have a chance for a soul if she wins the love of the prince and marries him. The Little Mermaid agrees to the deal and becomes human, catching the eye of the prince with her beauty and dance. Despite becoming his companion, the prince does not fall in love with her, and the Little Mermaid faces the threat of dissolving into sea foam if the prince marries another.",
            "title": "the-little-mermaid"
        },
        {
            "summary": " Alice follows a White Rabbit down a deep well and finds herself in a hall with locked doors. She finds a tiny golden key that fits a small door leading to a beautiful garden, but she is too big to fit through. After drinking a bottle labeled \"DRINK ME\" and eating a cake labeled \"EAT ME\", Alice grows to nine feet tall and is unable to get into the garden. She meets a Mouse, the March Hare, and the Hatter, and they all swim to the shore together. Alice finds a door leading to a tree and unlocks it with a golden key, shrinking to a foot high and entering a beautiful garden.",
            "title": "alice-in-wonderland"
        }
    ]
}
```


#### Get specific book summary

**GET** /api/books/summary?title=the-little-mermaid

Response
```json
{
    "summary": "\"The Little Mermaid\" is the story of a mermaid who longs for an eternal soul and falls in love with a human prince. She visits a sea witch who gives her legs in exchange for her voice and warns her that she will feel like walking on knives, but she will have a chance for a soul if she wins the love of the prince and marries him. The Little Mermaid agrees to the deal and becomes human, catching the eye of the prince with her beauty and dance. Despite becoming his companion, the prince does not fall in love with her, and the Little Mermaid faces the threat of dissolving into sea foam if the prince marries another.",
    "title": "the-little-mermaid"
}
```




















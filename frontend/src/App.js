import React from 'react'
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate} from 'react-router-dom'
import AuthorList from './components/AuthorList.js'
import BookList from './components/BookList.js'
import AuthorBooks from './components/AuthorBooks.js'
import axios from 'axios'


const NotFound = () => {
    return (
        <div>Page not found</div>
    )
}

class App extends React.Component {
    constructor(prop) {
        super(prop)
        this.state = {
            'authors': [],
            'books': []
        }
    }

    componentDidMount() {
        axios
        .get('http://127.0.0.1:8000/api/authors/')
        .then(response => {
            const authors = response.data
            this.setState({
                'authors': authors
            })
        })
        .catch(error => console.log(error))

        axios
        .get('http://127.0.0.1:8000/api/books/')
        .then(response => {
            const books = response.data
            this.setState({
                'books': books
            })
        })
        .catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link to="/">Authors</Link> </li>
                            <li><Link to="/books">Books</Link> </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<AuthorList authors={this.state.authors} /> } />
                        <Route exact path='/books' element={<BookList books={this.state.books} /> } />
                        <Route path="/authors" element={<Navigate to="/"/>} />
                        <Route path='/author/:id' element={<AuthorBooks books={this.state.books} /> } />
                        <Route path="*" element={<NotFound /> } />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;


// https://docs.djangoproject.com/en/4.0/ref/models/fields/#null
// http://localhost:3000/#/books
// http://localhost:3000/books
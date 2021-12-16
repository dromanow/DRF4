import {useParams} from 'react-router-dom'


const BookItem = ({book}) => {
    return(
        <tr>
            <td>{book.text}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const AuthorBooks = ({books}) => {
    let { id } = useParams();
    let filteredBooks = books.filter((book) => book.authors.includes(parseInt(id)))

    return (
        <table>
            <th>
                Title
            </th>
            <th>
                Author
            </th>
            {filteredBooks.map((book) => <BookItem book={book} />)}
        </table>
    )
}

export default AuthorBooks;

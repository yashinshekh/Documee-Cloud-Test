import {useEffect, useState} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
    const [count, setCount] = useState(0)
    const [message, setMessage] = useState('')

    useEffect(() => {
        const getmessage = async () => {
            const res = await fetch(`http://localhost:5000/api/data`, {
                method: 'GET',
            })

            const data = await res.json()
            console.log(data)
            setMessage(data.message)
        }
        getmessage()
    },[])

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>

        {message && (
            <h1>{message}</h1>
        )}
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
            Message : {message}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App

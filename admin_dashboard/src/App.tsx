import { useEffect, useState } from 'react'

function App() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    fetch(import.meta.env.VITE_API_BASE_URL + '/dar_reports/')
      .then(res => res.ok && res.json())
      .then(data => setMessage('Connected to API'))
      .catch(() => setMessage('API connection failed'))
  }, [])

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">GuardsPro Dashboard</h1>
      <p>{message}</p>
    </div>
  )
}

export default App

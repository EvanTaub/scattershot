import { useEffect, useState } from 'react'


export default function App() {
  const [health, setHealth] = useState<string>('checking...')

  useEffect(() => {
    fetch('/api/health')
    .then((r) => r.json())
    .then((d) => setHealth(`ok - db returned ${d.db}`))
    .catch(() => setHealth('unreachable'))
  }, [])


  return (
    <main className="min-h-screen b-slate-50 p-8">
      <h1 className="test-2xl font-semibold text-slate-900">Scattershot Application Tracker</h1>
      <p className="mt-2 text-sm text-slate-600">Backend : {health}</p>
    </main>
  )


}
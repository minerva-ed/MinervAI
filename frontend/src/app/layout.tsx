import './globals.css'
import type { Metadata } from 'next'


export const metadata: Metadata = {
  title: 'MinervAI',
  description: 'MinervAI',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>
        <main className='flex flex-col gap-12 min-h-screen mx-auto bg-white p-2'>
          <header className="flex justify-between items-center py-8">
            <a href="/" className="text-5xl font-bold font-mono">Minerv<span className="text-indigo-700 font-bold">AI</span></a>
            <div className="text-lg font-mono flex gap-4">
              <a href="#" className="hover:underline underline-offset-2 decoration-dotted">About</a>
              <a href="#" className="hover:underline underline-offset-2 decoration-dotted">Mission</a>
              <a href="#" className="hover:underline underline-offset-2 decoration-dotted">Join</a>
            </div>
          </header>
          {children}
        </main>
        <footer className="text-center p-4 font-mono text-neutral-600">© 2023 MinervAI</footer>
      </body>
    </html>
  );
}

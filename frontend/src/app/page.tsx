import FileUploader from './FileUploader'

export default function Home() {
  return (
    <div className="flex flex-col items-center gap-16">
      <h2 className="text-center font-mono font-bold text-2xl">Upload your lecture notes and select the number of virtual students to begin.</h2>
      <FileUploader />
    </div>
  )
}
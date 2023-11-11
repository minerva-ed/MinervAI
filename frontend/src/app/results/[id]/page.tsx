export default function Results({ params }: { params: { id: string } }) {
  return (
    <div className="flex flex-col items-center gap-16">
      <h2 className="text-center font-mono font-bold text-2xl">The results are in!</h2>
      <p className="font-mono font-bold text-xl">Task ID: {params.id}</p>

      <p>
        So, here's what's going on. You upload a file and select a student count. You press the Submit button. This takes the raw file data and student count and wraps it up into an object. This object is POSTed to the API. This returns a result, which will contain a session ID. The user is then redirected to the results page and the session ID is passed as a paramater to the page. This means we can display the session ID on the results page and connect back to the API to get updates. These updates will be displayed on this page. The SVG images may also be added to this page.
      </p>
    </div>
  )
}


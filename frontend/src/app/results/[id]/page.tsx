import ResultsView from "@/app/ResultsView"


export default function Results({ params }: { params: { id: string } }) {
  return (
    <div className="flex flex-col items-center">
      {/* <script type="text/javascript" id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
      </script> */}
      {/* <p className="font-mono font-bold text-xl">Task ID: {params.id}</p> */}
      <ResultsView task_id={params.id} />
      {/* <p>
        So, here's what's going on. You upload a file and select a student count. You press the Submit button. This takes the raw file data and student count and wraps it up into an object. This object is POSTed to the API. This returns a result, which will contain a session ID. The user is then redirected to the results page and the session ID is passed as a paramater to the page. This means we can display the session ID on the results page and connect back to the API to get updates. These updates will be displayed on this page. The SVG images may also be added to this page.
      </p> */}
    </div>
  )
}

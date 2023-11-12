'use client';
import { useEffect, useState } from 'react';
import Image from 'next/image';
interface ClassroomProps {
    taskResult: any;
}

export default function ClassroomView({ taskResult }: ClassroomProps) {
    const [indexState, setIndex] = useState(0);
    const [lectureIndex, setLectureIndex] = useState(0);
    const [done, setDone] = useState(false);

    const handleNextClick = () => {
        console.log(indexState, lectureIndex)
        if (indexState < taskResult.lectures[lectureIndex].QnA.length - 1) {
            setIndex(indexState + 1);
        } else if(lectureIndex < taskResult.lectures.length - 1) {
            setLectureIndex(lectureIndex + 1);
            setIndex(0);
        } else {
            setDone(true)
        }
        console.log(indexState, lectureIndex)
        console.log("handled")
    };

    const imageSrc = (index) => {
        if (!taskResult.lectures[lectureIndex].QnA[indexState]) {
            return "/images/s" + (index + 1) + ".png"
        }
        if (taskResult.lectures[lectureIndex].QnA[indexState].associated_students_list.includes(index)) {
            return "/images/s" + (index + 1) + ".png"
        }else{
            return "/images/s" + (index + 1) + "_active.png"
        }
    }

    if (!taskResult) {
        // Render a message or return null to render nothing
        return(<div role="status">
            <svg aria-hidden="true" className="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor" />
                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill" />
            </svg>
            <span className="sr-only">Loading...</span>
        </div>)
    }
    if (done) {
        return (
            <div>
                <h1>Detailed Summary</h1>
                {taskResult.lectures.map((lecture, index) => (
                    <div key={index} className="bg-white p-8 shadow-md my-8 rounded-lg">
                        <h1 className="text-3xl font-bold">{"Section " + (index + 1)}</h1>
                        {/* Display lecture notes */}
                        < div className="bg-white p-6 rounded-lg mb-6" >
                            <h2 className="text-xl font-bold mb-2">Lecture Notes</h2>
                            <p>{lecture.lecture}</p>
                        </div>

                        {/* Display questions and answers */}
                        <div className="bg-white p-6 rounded-lg mb-6">
                            <h2 className="text-xl font-bold mb-2">Questions and Answers</h2>
                            {lecture.QnA.map((item, index) => (
                                <div key={index} className="mb-4">
                                    <h3 className="font-semibold">Question {index + 1}: {item.question}</h3>
                                    <p className="text-gray-700">Answer: {item.answer}</p>
                                    <p className="text-sm text-gray-600">Associated Students: {item.associated_students_list.join(', ')}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                ))
                }
                {/* Display summary */}
                <div className="bg-white p-6 rounded-lg shadow-md">
                    <h2 className="text-xl font-bold mb-2">Summary</h2>
                    <p>{taskResult.summary}</p>
                </div>
            </div>
        )
    }
    return (
        <div className="max-w-4xl mx-auto p-4 whitespace-pre-wrap" >
            <div id="classroom" className="flex flex-col place-content-between bg-contain bg-no-repeat bg-top" style={{backgroundImage: `url(https://raw.githubusercontent.com/dmavani25/MinervAI/0849f885d846f0bee34e6de8bccfb7939481d6a5/frontend/src/app/results/%5Bid%5D/images/Background_wout_student.png)` }}>
                <div id="whiteboard" className="text-3xl flex-left overflow-y-scroll m-10">
                    Abstract Algebra
                    <div className="text-xl">{"Lecture 1, section " + (lectureIndex + 1)}</div>
                    <div className="text-sm line-clamp-5 w-72">{"Answer: " + taskResult.lectures[lectureIndex].QnA[indexState].answer}</div>
                </div>
                
                <div className="speech-bubble bg-white p-2 rounded shadow-md h-24 m-5 relative">
                    <div className="line-clamp-3 text-sm">{taskResult.lectures[lectureIndex].QnA[indexState].associated_students_list.length + " student(s) asked: " + taskResult.lectures[lectureIndex].QnA[indexState].question}</div>
                    <button className="bottom-0 right-5 absolute text-white bg-blue-700 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2" onClick={handleNextClick}>Next</button>
                </div>
                <div id="students" className="flex flex-row justify-center items-center w-full bottom-0">
                    {taskResult.students.map((studentInfo, index) => (
                        <div key={index} className="student mx-2 relative w-36 h-56 flex flex-col">
                            <p className="text-sm">{studentInfo}</p>
                            <Image src={imageSrc(index)} alt={"Student" + (index + 1)} className="" layout='fill' objectFit='contain' />
                        </div>
                       
                    ))}
                </div>
                {/* Display summary */}
                {/* <div className="bg-white p-6 rounded-lg shadow-md">
                    <h2 className="text-xl font-bold mb-2">Summary</h2>
                    <p>{taskResult.summary}</p>
                </div> */}
        </div>
    </div>
    );
}

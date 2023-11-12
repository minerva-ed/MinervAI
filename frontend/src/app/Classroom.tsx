'use client';
import { useEffect, useState } from 'react';
import { MathJax, MathJaxContext } from "better-react-mathjax";

interface ClassroomProps {
    task_id: string;
}

export default function Classroom({ task_id }: ClassroomProps) {
    const [taskResult, setTaskResult] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const ws = new WebSocket(`ws://127.0.0.1:8000/ws/${task_id}`);

        ws.onopen = () => console.log('WebSocket Connected');

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.error) {
                setError(data.error);
            } else {
                setTaskResult(data);
            }
        };

        ws.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        ws.onclose = () => console.log('WebSocket Disconnected');

        return () => ws.close();
    }, [task_id]);

    if (!taskResult) {
        // Render a message or return null to render nothing
        return <p className="text-center text-gray-700">No data available.</p>;
    }

    return (
        <div className="max-w-4xl mx-auto p-4 whitespace-pre-wrap">
            <MathJaxContext><MathJax>
            {/* Display lecture notes */}
            <div className="bg-white p-6 rounded-lg shadow-md mb-6">
                <h2 className="text-xl font-bold mb-2">Lecture Notes</h2>
                <p>{taskResult.lecture}</p>
            </div>

            {/* Display questions and answers */}
            <div className="bg-white p-6 rounded-lg shadow-md mb-6">
                <h2 className="text-xl font-bold mb-2">Questions and Answers</h2>
                {taskResult.questions.map((item, index) => (
                    <div key={index} className="mb-4">
                        <h3 className="font-semibold">Question {index + 1}: {item.question}</h3>
                        <p className="text-gray-700">Answer: {item.answer}</p>
                        <p className="text-sm text-gray-600">Associated Students: {item.associated_students_list.join(', ')}</p>
                    </div>
                ))}
            </div>

            {/* Display summary */}
            <div className="bg-white p-6 rounded-lg shadow-md">
                <h2 className="text-xl font-bold mb-2">Summary</h2>
                <p>{taskResult.summary}</p>
            </div>
            </MathJax></MathJaxContext>
        </div>

    );
}

'use client';
import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';

export default function Classroom({ task_id }) {
    const router = useRouter();
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
                router.push(`/results/${task_id}`);
            }
        };

        ws.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        ws.onclose = () => console.log('WebSocket Disconnected');

        return () => ws.close();
    }, [task_id, router]);

    return (
        <div className="flex flex-col items-center justify-center p-4">
            {error && <p className="text-red-500 text-xl">{error}</p>}
            {taskResult ? (
                <div className="text-indigo-700 text-lg">
                    <p>Task Result:</p>
                    <pre className="bg-indigo-100 p-2 rounded">{JSON.stringify(taskResult, null, 2)}</pre>
                </div>
            ) : (
                <p className="text-indigo-700 text-lg">Waiting for task result...</p>
            )}
        </div>
    );
}

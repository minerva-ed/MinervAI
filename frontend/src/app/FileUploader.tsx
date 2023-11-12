'use client';
import { useRouter } from 'next/navigation'
import { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';



export default function FileUploader() {
    const router = useRouter();

    const [file, setFile] = useState<File | undefined>();
    const [studentCount, setStudentCount] = useState<number>(6);

    function handleSliderChange(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();

        setStudentCount(parseInt(e.target.value));
    }

    async function handleSubmit(e: React.SyntheticEvent) {
        e.preventDefault();

        if (typeof file === 'undefined') return;

        const formData = new FormData();


        formData.append('file', file);
        formData.append('student_count', studentCount.toString());

        const res = await fetch('http://127.0.0.1:8000/upload', {
            method: 'POST',
            body: formData
        });

        const data = await res.json();

        console.log(data['task_id']);
        router.push(`/results/${data['task_id']}`);
    }

    const onDrop = useCallback((acceptedFiles: Array<File>) => {
        setFile(acceptedFiles[0]);
    }, []);

    const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

    return (
        <form onSubmit={handleSubmit} className="flex flex-col items-center gap-12">
            <div className="flex flex-col items-center gap-4">
                <p className="text-indigo-700 text-3xl"><span className="font-bold">{studentCount}</span> {studentCount == 1 ? 'Student' : 'Students'}</p>
                <input onChange={handleSliderChange} value={studentCount} className="w-48 accent-indigo-700 hover:cursor-pointer" type="range" min="1" max="12" step="1" />
            </div>

            <div className="flex items-center justify-center p-8 w-64 h-64 bg-indigo-100 hover:bg-indigo-200 border-2 text-indigo-700 border-indigo-700 rounded-2xl hover:cursor-pointer scale-90 hover:scale-100 transition overflow-hidden" {...getRootProps()}>
                <input {...getInputProps()} />
                <div className="text-center text-xl">
                    {file && <p className="break-all"><span className="font-bold">{file.name}</span> uploaded!</p>}
                    {
                        !file && (isDragActive ?
                            <p className="font-bold">Drop files here ...</p> :
                            <p><span className="font-bold">Click here</span> or drag files to upload ...</p>)
                    }
                </div>
            </div>

            <button className={`font-bold transition text-2xl border-2 border-indigo-700 rounded-xl px-6 py-4 scale-90 ${file ? 'bg-indigo-700 text-white hover:cursor-pointer hover:scale-100' : 'text-indigo-700 hover:cursor-default'}`} type="submit">Submit</button>
        </form>
    )
}

from fastapi import FastAPI
app=FastAPI()

#Path Parameters
@app.get("/jobs/{job_id}")
def get_job(job_id:int):
    return{
        "job_id":job_id,
    }

#Query Parameters
@app.get("/jobs")
def get_jobs(job_id:int=0, job_name:str=None):
    return{
        "job_id":job_id,
        "job_name":job_name,
    }

@app.post("/create-job")
def create_job(job_id:int=0, job_name:str=None):
    return{
        "job_id":job_id,
        "job_name":job_name,
    }

#handling request body using Dictionary 
@app.post("/newjobs")
def new_jobs(jobs:dict):
    return{
        "Message":"Job created successfully",
        "Hiring":jobs
    }
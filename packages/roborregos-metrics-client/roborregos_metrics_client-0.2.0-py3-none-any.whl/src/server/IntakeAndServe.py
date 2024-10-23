from robometrics.worker.worker import ProcessInfo, MachineInfo, StaticMachine
import os
from typing import List, Dict, Union
from pydantic import BaseModel
from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId


app = FastAPI()
app.mongo_db_client = MongoClient(
    "mongodb://root:root@localhost:27017/")
app.db = app.mongo_db_client["metrics"]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/intake/process/{machine_id}")
def intake_process(machine_id: str, process_info: ProcessInfo):
    t = process_info.model_dump()
    t["machine_id"] = machine_id
    app.db.processes.insert_one(process_info)


@app.post("/intake/processes/{machine_id}")
def intake_processes(machine_id: str, processes: List[ProcessInfo]):
    p = []
    for process in processes:
        t = process.model_dump()
        t["machine_id"] = machine_id
        p.append(t)
    if len(p) > 0:
        app.db.processes.insert_many(p)


@app.post("/intake/many/machine/{machine_id}")
def intake_many_machine(machine_id: str, machines: List[Dict[str, Union[str, float]]]):
    p = []
    for machine in machines:
        t = machine
        t["machine_id"] = machine_id
        p.append(t)
    if len(p) > 0:
        app.db.machines.insert_many(p)


@app.post("/intake/machine/{machine_id}")
def intake_machine(machine_id: str, machine_info: MachineInfo):
    t = machine_info.model_dump()
    t["machine_id"] = machine_id
    app.db.machines.insert_one(t)


@app.post("/intake/static_machine/{machine_id}")
def intake_static_machine(machine_id: str, static_machine: StaticMachine):
    t = static_machine.model_dump()
    t["machine_id"] = machine_id
    app.db.static_machines.insert_one(t)


@app.get("/intake/static/{machine_id}")
def get_machine(machine_id: str):
    return app.db.static_machines.find_one({"machine_id": machine_id})


@app.get("/intake/machine/{machine_id}")
def get_machine(machine_id: str):
    return app.db.machines.find_many({"machine_id": machine_id})


@app.get("/intake/process/{machine_id}")
def get_machine(machine_id: str):
    return app.db.processes.find_many({"machine_id": machine_id})


def serialize_doc(doc):
    if isinstance(doc, ObjectId):
        return str(doc)
    if isinstance(doc, dict):
        return {k: serialize_doc(v) for k, v in doc.items()}
    if isinstance(doc, list):
        return [serialize_doc(i) for i in doc]
    return doc


@app.get("/serve/static")
def serve_static():
    return [serialize_doc(x) for x in app.db.static_machines.find()]


@app.get("/serve/machine")
def serve_machine():
    return [serialize_doc(x) for x in app.db.machines.find()]


@app.get("/serve/process")
def serve_process():
    return [serialize_doc(x) for x in app.db.processes.find()]

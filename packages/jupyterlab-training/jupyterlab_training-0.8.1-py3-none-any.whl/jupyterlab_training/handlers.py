import getpass
import json
import os
import sqlalchemy
import tornado

import nbformat
from nbconvert import PDFExporter
from jupyter_server.utils import url_path_join
from jupyter_server.base.handlers import APIHandler

from jupyterlab_training.db import (
    create_db_session,
    reset_db,
    Student,
)


_initialized = False


if not _initialized and os.geteuid() != 0:
    session = create_db_session()
    _initialized = True


def setup_handlers(web_app):
    host_pattern = ".*$"
    web_app.add_handlers(
        host_pattern,
        [
            # askHelp
            (
                url_path_join(
                    web_app.settings["base_url"], "/jupyterlab-training/progress"
                ),
                ProgressAPIHandler,
            ),
            # nbconvert to pdf
            (
                url_path_join(
                    web_app.settings["base_url"], "/jupyterlab-training/topdf"
                ),
                FormatAPIHandler,
            ),
            # read student info in database
            (
                url_path_join(
                    web_app.settings["base_url"], "/jupyterlab-training/coll"
                ),
                CollectAPIHandler,
            ),
            # reset student database
            (
                url_path_join(
                    web_app.settings["base_url"], "/jupyterlab-training/resetDatabase"
                ),
                ResetDatabaseAPIHandler,
            ),
            # get exercice state (needHelp, success)
            (
                url_path_join(
                    web_app.settings["base_url"], "/jupyterlab-training/state/([^/]+)"
                ),
                StateAPIHandler,
            ),
        ],
    )


def to_pdf(nb_filename):
    pdf_exporter = PDFExporter()
    with open(nb_filename) as f:
        nb_content = nbformat.read(f, as_version=4)
    # handle date error
    if nb_content["metadata"].get("date"):
        nb_content["metadata"].pop("date")
    try:
        pdf_data, _ = pdf_exporter.from_notebook_node(nb_content)
        pdf_filename = nb_filename.replace(".ipynb", ".pdf")
        with open(pdf_filename, "wb") as f:
            f.write(pdf_data)
    except Exception:
        print(f"Convertion error: {nb_filename}")


def handle_progress(data):
    global session
    user_name = os.environ.get("JUPYTERHUB_USER", getpass.getuser())
    query = session.query(Student).filter_by(username=user_name)
    try:
        student_info = query.one_or_none()
    except sqlalchemy.exc.OperationalError:
        session = create_db_session()
        student_info = None
    if not student_info:
        student_info = Student(
            username=user_name,
            done_exercises=[],
            need_help_exercises=[],
        )
        session.add(student_info)
        try:
            session.commit()
        except Exception:
            print("Warning: DataBase error")
    state = data["state"]
    need_help_exercises = [json.loads(e) for e in student_info.need_help_exercises]
    done_exercises = [json.loads(e) for e in student_info.done_exercises]
    exo_name = data["path"].split("/")[-2]
    exercise = {"state": state, "name": exo_name, "url": data["url"]}
    if exercise in need_help_exercises:
        need_help_exercises = [
            exo for exo in need_help_exercises if exo["name"] != exo_name
        ]
    elif exercise in done_exercises:
        done_exercises = [exo for exo in done_exercises if exo["name"] != exo_name]
    else:
        if state == "needHelp":
            need_help_exercises.append(exercise)
        elif state == "done":
            done_exercises.append(exercise)
    student_info.need_help_exercises = [json.dumps(e) for e in need_help_exercises]
    student_info.done_exercises = [json.dumps(e) for e in done_exercises]
    try:
        session.commit()
    except Exception:
        print("Warning: DataBase error")


def read_student_info():
    students_info = []
    try:
        infos = session.query(Student).all()
    except sqlalchemy.exc.OperationalError as e:
        print("Warning; Database error: " + e)
        return students_info
    for info in infos:
        done_exercises = []
        if info.done_exercises:
            done_exercises = [json.loads(e) for e in info.done_exercises]
        need_help_exercises = []
        if info.need_help_exercises:
            need_help_exercises = [json.loads(e) for e in info.need_help_exercises]
        done_exercises_len = len(done_exercises)
        need_help_exercises_len = len(need_help_exercises)
        update_date = info.up_date.isoformat()
        students_info.append(
            [
                info.username,
                done_exercises_len,
                need_help_exercises_len,
                done_exercises,
                need_help_exercises,
                update_date,
            ]
        )
    return students_info


def read_state_info(exo_name, user_name):
    query = session.query(Student).filter_by(username=user_name)
    try:
        student_info = query.one_or_none()
    except sqlalchemy.exc.OperationalError as e:
        print("Warning: Database Error: " + e)
        student_info = None
    if not student_info:
        return {"done": False, "needHelp": False}
    done_exercises = [json.loads(e) for e in student_info.done_exercises]
    need_help_exercises = [json.loads(e) for e in student_info.need_help_exercises]
    succeed = False
    if [exo for exo in done_exercises if exo_name == exo["name"]]:
        succeed = True
    need_help = False
    if [exo for exo in need_help_exercises if exo_name == exo["name"]]:
        need_help = True
    return {"done": succeed, "needHelp": need_help}


class ProgressAPIHandler(APIHandler):

    @tornado.web.authenticated
    def post(self) -> None:
        data = json.loads(self.request.body.decode("utf-8"))
        handle_progress(data)


class FormatAPIHandler(APIHandler):

    @tornado.web.authenticated
    def post(self) -> None:
        data = json.loads(self.request.body.decode("utf-8"))
        if "filename" in data:
            to_pdf(data["filename"])
            self.finish(json.dumps({}))


class CollectAPIHandler(APIHandler):

    @tornado.web.authenticated
    def get(self) -> None:
        user = os.environ.get("JUPYTERHUB_USER", getpass.getuser())
        self.finish(json.dumps({"info": read_student_info(), "user": user}))


class ResetDatabaseAPIHandler(APIHandler):

    @tornado.web.authenticated
    def get(self) -> None:
        reset_db()
        self.finish(json.dumps({}))


class StateAPIHandler(APIHandler):

    @tornado.web.authenticated
    def get(self, exo_name) -> None:
        user = os.environ.get("JUPYTERHUB_USER", getpass.getuser())
        self.finish(json.dumps(read_state_info(exo_name, user)))

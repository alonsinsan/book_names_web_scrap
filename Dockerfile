FROM jupyter/pyspark-notebook
WORKDIR /home/jovyan/work
RUN pip install requirements.txt
COPY web_s.py ./

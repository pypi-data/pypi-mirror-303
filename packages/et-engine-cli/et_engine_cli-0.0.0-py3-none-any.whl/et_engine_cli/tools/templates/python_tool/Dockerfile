FROM public.ecr.aws/docker/library/python:3.11.9-bullseye

WORKDIR /app

# install et_engine
RUN pip install et-engine

# install <<{{TOOL_NAME}}>> dependencies

 
# important files
COPY <<{{TOOL_NAME}}>>.py /app/<<{{TOOL_NAME}}>>.py
COPY tool.py /app/tool.py

CMD ["python", "tool.py"]

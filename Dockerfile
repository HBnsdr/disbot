FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -U discord-py
RUN pip install discord-py-interactions
#RUN pip install frozenlist
#RUN pip install -r requirements.txt

CMD ["python", "disbot.py"]

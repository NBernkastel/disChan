FROM python

COPY . /app

RUN cd backend

RUN pip install -r requirements.txt

CMD python main.py